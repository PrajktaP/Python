########################################################
# Required Python Packages
########################################################
from pathlib import Path
import joblib # used for preserving model on HD
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# homo - single models
from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt

# Configuration details
# ARTIFACTS.mkdir(exist_ok=True)
########################################################
# File Paths
########################################################
ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(exist_ok=True)
MODEL_PATH = ARTIFACTS / "diabetes_pipeline.joblib"
DATA_CSV_PATH = "diabetes.csv"

########################################################
# Global variables
########################################################
RANDOM_STATE = 42
TEST_SIZE = 0.2
MAX_DEPTH = 10
N_ESTIMATORS = 100

########################################################
# Function name : check_feature_importance
# Description : check which features are important in a case study
# Input : X, model
# Output : Plots bar graph
# Author : Prajkta
# Date : 04/08/2025
########################################################
# def check_feature_importance(X, model):
#     # use following code to check which features are important in a case study
#     importance = pd.Series(model.feature_importances_, index=X.columns) # series is array
#     importance = importance.sort_values(ascending=False)

#     importance.plot(kind='bar', figsize=(10,6), title="Feature Importance")
#     plt.grid(True)
#     plt.show()

def check_feature_importance(X, pipe):
    # Get the RandomForestClassifier step from the pipeline
    rf_model = pipe.named_steps['rf']   # use whatever name you gave in Pipeline

    # Extract feature importances
    importance = pd.Series(rf_model.feature_importances_, index=X.columns)
    importance = importance.sort_values(ascending=False)

    # Plot
    importance.plot(kind='bar', figsize=(10, 6), title="Feature Importance")
    plt.grid(True)
    plt.show()


########################################################
# Function name : display_confusion_matrix
# Description : Display Confusion Matrix
# Input : Y_test, Y_pred
# Output : displays confusion matrix
# Author : Prajkta
# Date : 04/08/2025
########################################################
def display_confusion_matrix(Y_test, Y_pred):
    conf_matrix = confusion_matrix(Y_test, Y_pred)
    print(f"\n Confusion Matrix \n {conf_matrix}")
    # score = (tp + tn) / (tp + fp + tn + fn)

########################################################
# Function name : display_classification_report
# Description : Display classification report
# Input : Y_test, Y_pred
# Output : displays classification report
# Author : Prajkta
# Date : 04/08/2025
########################################################
def display_classification_report(Y_test, Y_pred):
    report = classification_report(Y_test, Y_pred)
    print(f"\n Classification report: \n {report}")


########################################################
# Function name : split_dataset
# Description : Split the dataset
# Input : X and Y
# Output : Dataset after splitting
# Author : Prajkta
# Date : 04/08/2025
########################################################
def split_dataset(X, Y):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = TEST_SIZE, random_state = RANDOM_STATE)
    return x_train, x_test, y_train, y_test

########################################################
# Function name : get_best_accuracy
# Description : Calculate accuracies with N_estimators in range from 50 to 200 and loop on it and find best value of N_estimator
# Input : X_train, X_test, Y_train, Y_test
# Output : pipe and Y_pred
# Author : Prajkta
# Date : 04/08/2025
########################################################
def get_best_accuracy(X_train, X_test, Y_train, Y_test):
    best_n_estimator = 0
    best_accuracy = 0

    for i in range(50, 210, 10):
        # Train the pipe
        pipe = Pipeline([
            ("scalar", StandardScaler()),
            ("rf", RandomForestClassifier(n_estimators = i, max_depth = MAX_DEPTH, random_state = RANDOM_STATE))
            #n_estimators by default is 100, max_depth=none by default
        ])

        pipe.fit(X_train, Y_train)

        # Test model - Predictions
        Y_pred = pipe.predict(X_test)

        # Calculate accuracy of the model
        print(f"Train Accuracy for n_estimator={i} ", accuracy_score(Y_train, pipe.predict(X_train)) * 100)
        test_accuracy = accuracy_score(Y_test, Y_pred) * 100
        print(f"Test Accuracy for n_estimator={i} ", test_accuracy)

        if best_accuracy < test_accuracy:
            best_accuracy = test_accuracy
            best_n_estimator = i
    
    print(f"Best Accuracy is {best_accuracy}, with Best N_Estimator value {best_n_estimator}")

    return pipe, Y_pred

########################################################
# Function name : main function
# Description : Main function from where execution starts
# Author : Prajkta
# Date : 04/08/2025
########################################################
# this is (homogenious) bagging - 1 bag goes to each 
def main():
    # Load CSV
    df = pd.read_csv(DATA_CSV_PATH)

    # Set X and Y
    X = df.drop(columns=['Outcome'])
    Y = df['Outcome']

    # Split data into 4 parts
    X_train, X_test, Y_train, Y_test = split_dataset(X, Y)
    # X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = TEST_SIZE,  random_state = RANDOM_STATE)

    pipe, Y_pred = get_best_accuracy(X_train, X_test, Y_train, Y_test)

    # Visualizations
    check_feature_importance(X, pipe)
    display_confusion_matrix(Y_test, Y_pred)
    display_classification_report(Y_test, Y_pred)

    joblib.dump(pipe, MODEL_PATH)

if __name__ == "__main__":
    main()
