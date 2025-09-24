import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def findBestK(x_train, y_train, x_test, y_test):
    best_k = 1
    best_accuracy = 0.0

    for k in range(1, 21):  # Testing k from 1 to 20
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k

    print(f"Best value of k: {best_k} with accuracy: {best_accuracy * 100}\n")

    return best_k, best_accuracy

def wine_classification():
    line = "*"*100

    # Step 1: Load Data from sklearn
    # wine = load_wine()
    # X = pd.DataFrame(wine.data, columns=wine.feature_names)
    # y = pd.Series(wine.target)  # 0, 1, 2 for Class 1, 2, 3
    df = pd.read_csv("WinePredictor.csv")
    x = df.drop(columns=['Class'])
    y = df['Class']

    print(f"Wine Dataset Sample:\n{x.head()}\n{line}\n")
    print(f"Dimensions of Dataset: {x.shape}\n{line}\n")

    # Step 2: Clean, Prepare and Manipulate data
    # The dataset is already clean and numeric.. No missing or null values.. 
    # So, the data is ready for training.
    print("Data is clean and ready for training.\n")

    # Step 3: Train Data (split into train/test)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Step 4: Train Model
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x_train, y_train)
    print("Model trained using KNN.\n")

    # Step 5: Test Data & Calculate Accuracy
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy of KNN classifier with k=5: {accuracy * 100}\n{line}\n")

    # Show some predictions
    results = pd.DataFrame({'Expected': y_test, 'Predicted': y_pred})
    print("Expected vs Predicted classes:\n")
    print(results.head(10))

    ###########################################################
    print("\n\n" + line + "\n\n")
    # self practice to find best value of n_neighbors
    best_k, best_accuracy = findBestK(x_train, y_train, x_test, y_test)

    # Now again train the model with the best k
    print(f"Using Best k to train the model again.\n")
    model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(x_train, y_train)

    # Step 5: Test Data & Calculate Accuracy
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy of KNN classifier with best K value {best_k}: {accuracy * 100}\n{line}\n")

    # Show some predictions
    results = pd.DataFrame({'Expected': y_test, 'Predicted': y_pred})
    print("Expected vs Predicted classes:\n")
    print(results.head(10))

def main():
    print("Wine Classification using KNN\n")
    wine_classification()

if __name__ == "__main__":
    main()