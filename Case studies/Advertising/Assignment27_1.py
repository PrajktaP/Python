import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt

def advertising_regression(datafilepath):
    line = "*"*100

    # Step 1: load Data
    df = pd.read_csv(datafilepath)
    print(f"Advertising Dataset:\n{df.head()}\n{line}\n")
    print(f"Dimensions of Dataset: {df.shape}\n{line}\n")

    # Step 2: Clean, Prepare and Manipulate data
    # (Checked the csv and there are no missing values and all columns are numeric)
    print("Data is clean and ready for analysis.\n")

    # Features and target
    X = df.drop(columns=['sales'])
    y = df['sales']

    # Step 3: Train Data (split into half)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Step 4: Test the data
    y_pred = model.predict(X_test)

    # Step 5: Display predicted and expected values
    results = pd.DataFrame({'Expected': y_test, 'Predicted': y_pred})
    print("Expected vs Predicted values:\n")
    print(results.head(10))  # Show first 10 rows

    # Visualize with seaborn
    # Did just for better understanding of the model performance
    # The red slanting line in our scatter plot is a reference line (also called the identity line or diagonal). 
    # It represents the ideal case where the predicted values exactly match the expected (actual) values.
    # If a point lies on this line: The prediction is perfect for that sample.
    # If points are close to this line: The model is performing well.
    # If points are far from this line: The predictions deviate from the actual values.
    # This line helps you visually assess the accuracy of your regression model.
    sns.scatterplot(x='Expected', y='Predicted', data=results)
    plt.plot([results['Expected'].min(), results['Expected'].max()],
             [results['Expected'].min(), results['Expected'].max()],
             color='red', linestyle='--')  # Diagonal line for reference
    plt.xlabel('Actual Sales')
    plt.ylabel('Predicted Sales')
    plt.title('Actual vs Predicted Sales')
    plt.show()
    

def main():
    advertising_regression("Advertising.csv")

if __name__ == "__main__":
    main()