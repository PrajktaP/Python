import pandas as pd
from sklearn.model_selection import train_test_split

def create_dataframe():
    line = "*"*100

    data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}

    print(line)

    # create Dataframe
    df = pd.DataFrame(data)

    print(f"Created DataFrame: \n{line}\n{df}\n")

    return df

def main():
    line = "*"*100

    df = create_dataframe()

    x = df[['Age']]
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
Q5: Create a DataFrame with 'Age' and 'Purchased' columns and split into train/test sets. 
data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]} 
"""