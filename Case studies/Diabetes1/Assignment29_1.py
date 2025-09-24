import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.tree import DecisionTreeClassifier

def main():
    # 1. EDA
    diabetes = pd.read_csv("diabetes.csv")
    print("First 5 rows:\n", diabetes.head())
    print("\nInfo:\n")
    print(diabetes.columns)
    print("\nNull values:\n", diabetes.isnull().sum())
    print("\nStatistics:\n", diabetes.describe())

    # Plot target variable distribution
    plt.figure(figsize=(6,4))
    sns.countplot(x='Outcome', data=diabetes)
    plt.title("Distribution of Outcome")
    plt.xticks([0, 1], ['0 (No Diabetes)', '1 (Diabetes)'])
    plt.show()

    # # Histograms for features
    # diabetes.hist(figsize=(12,10))
    # plt.tight_layout()
    # plt.show()

    # Boxplots for outlier detection
    plt.figure(figsize=(15, 8))
    sns.boxplot(data=diabetes.drop(columns=['Outcome']))
    plt.xticks(rotation=45)
    plt.title("Boxplot for All Features (Before Cleaning)")
    plt.show()

    # 2. Data Preprocessing:
    # Check and handle missing or zero values in columns like Glucose, BloodPressure, etc.
    # Apply feature scaling using StandardScaler or MinMaxScaler.
    # Split the dataset into features (X) and target (y)
    cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    diabetes[cols_with_zero] = diabetes[cols_with_zero].replace(0, np.nan)
    diabetes[cols_with_zero] = diabetes[cols_with_zero].fillna(diabetes[cols_with_zero].median())

    # Apply feature scaling using StandardScaler or MinMaxScaler
    X = diabetes.drop(columns=['Outcome'])
    y = diabetes['Outcome']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split the dataset into features (X) and target (y).
    x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 3. Model Building: Train at least 2 different algorithms on the dataset
    models = {
        "Logistic Regression": LogisticRegression(max_iter=200),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(n_estimators=100)
    }
    results = {}

    for name, model in models.items():
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        results[name] = y_pred

        # Model Evaluation:
        # Print accuracy score, confusion matrix, precision, recall, and F1 score.
        # Use matplotlib or seaborn to visualize confusion matrix
        print(f"\n{name} Results:")
        print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
        print(f"Precision: {precision_score(y_test, y_pred):.2f}")
        print(f"Recall: {recall_score(y_test, y_pred):.2f}")
        print(f"F1 Score: {f1_score(y_test, y_pred):.2f}")

        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(4,3))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['No Diabetes','Diabetes'],
            yticklabels=['No Diabetes','Diabetes'])
        plt.title(f"{name} Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.show()

    # 5. Final Output:
    # Predict whether a patient is diabetic based on test data.
    # Display predictions on screen and save them in a CSV file
    final_df = pd.DataFrame({
        'Actual': y_test,
        'LogisticRegression_Pred': results["Logistic Regression"],
        'KNN_Pred': results["KNN"],
        'DecisionTree_Pred': results["Decision Tree"],
        'RandomForest_Pred': results["Random Forest"]
    })

    print("\nSome predictions:\n", final_df.head())
    final_df.to_csv("diabetes_predictions.csv", index=False)

if __name__ == "__main__":
    main()