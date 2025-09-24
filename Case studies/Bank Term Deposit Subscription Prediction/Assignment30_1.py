import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

def main():
    line = "#" * 80
    fobj = open("output.txt", "w")

    # 1. Load and Explore the Dataset
    df = pd.read_csv("bank-full.csv", sep=';')
    fobj.write("First 5 rows: \n" + str(df.head()) + "\n")
    fobj.write("\n Info: \n" + str(df.info()) + "\n")
    fobj.write("\n Missing values: \n" + str(df.isnull().sum()) + "\n")
    fobj.write("\n Basic stats: \n" + str(df.describe(include='all')) + "\n")
    fobj.write("\n Class distribution: \n" + str(df['y'].value_counts()) + "\n")

    # 2. Preprocess the Data
    df['y'] = df['y'].map({'yes': 1, 'no': 0})

    # Handle 'unknown' values in categorical columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].replace('unknown', np.nan)
    print("\nMissing after replacing 'unknown':\n", df.isnull().sum())
    df = df.fillna(df.mode().iloc[0])  # Fill with mode for categorical

    X = df.drop(columns=['y'])
    y = df['y']

    # Label Encoding for all categorical columns
    fobj.write("X before label encoding: \n" + str(X.head()) + "\n")
    cat_cols = X.select_dtypes(include='object').columns # Finds all columns in X that have data type object (i.e., categorical/string columns)
    le = LabelEncoder()
    for col in cat_cols:
        X[col] = le.fit_transform(X[col])
    fobj.write("X after label encoding: \n" + str(X.head()) + "\n")

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 3. Split the Data
    x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

    # 4. Train Classification Models
    models = {
        "Logistic Regression": LogisticRegression(max_iter=200),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    plt.figure(figsize=(8,6))   # prepare ROC figure before loop

    for name, model in models.items():
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        y_proba = model.predict_proba(x_test)[:,1] if hasattr(model, "predict_proba") else None

        fobj.write(f"\n{line}")
        fobj.write(f"\n{name} Results:")
        fobj.write(f"\n{line}\n")
        fobj.write(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}\n")
        fobj.write("Confusion Matrix:\n" + str(confusion_matrix(y_test, y_pred)) + "\n")
        fobj.write("Classification Report:\n" + str(classification_report(y_test, y_pred)) + "\n")

        if y_proba is not None:
            roc_auc = roc_auc_score(y_test, y_proba)
            fobj.write(f"ROC-AUC Score: {roc_auc:.3f}\n")
            fpr, tpr, _ = roc_curve(y_test, y_proba)
            plt.plot(fpr, tpr, label=f"{name} (AUC={roc_auc:.2f})")  # <- label added here

        # Plot confusion matrix separately
        plt.figure()
        sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
        plt.title(f"{name} Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.show()

    # 6. Plot ROC Curves (finalize ROC figure)
    plt.plot([0,1], [0,1], 'k--', label="Random Classifier")  # add label for baseline
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curves")
    plt.legend()   # now legend has models + baseline
    plt.show()

    fobj.close()

if __name__ == "__main__":
    main()