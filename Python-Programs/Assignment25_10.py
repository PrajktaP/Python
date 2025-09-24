import pandas as pd
from sklearn.model_selection import train_test_split

def create_dataframe():
    line = "*"*100

    data = { 
        'Age': [25, 30, 45, 35, 22], 
        'Salary': [50000, 60000, 80000, 65000, 45000], 
        'Purchased': [1, 0, 1, 0, 1] 
    }

    print(line)

    # create Dataframe
    df = pd.DataFrame(data)

    print(f"Created DataFrame: \n{line}\n{df}\n")

    return df

def main():
    line = "*"*100

    df = create_dataframe()

    x = df[['Age', 'Salary']]
    y = df['Purchased']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    print(line)
    print(f"X Train: \n{x_train}")
    print(f"X Test: \n{x_test}")
    print(f"Y Train: \n{y_train}")
    print(f"Y Test: \n{y_test}")

if __name__ == "__main__":
    main()


"""
Q10: Split a DataFrame with multiple features into train-test for supervised learning. 
data = { 'Age': [25, 30, 45, 35, 22], 'Salary': [50000, 60000, 80000, 65000, 45000], 'Purchased': [1, 0, 1, 0, 1] }
"""