import pandas as pd
import numpy as np

def create_dataframe():
    line = "*"*100

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
    }

    print(line)

    # create Dataframe
    df = pd.DataFrame(data)
    print(f"Created DataFrame with missing data: \n{line}\n{df}\n")

    return df

def fill_missing_values(df):
    line = "*"*100

    df['Math'] = df['Math'].fillna(df['Math'].mean())
    df['Science'] = df['Science'].fillna(df['Science'].mean())
    
    print(f"DataFrame after filling the missing data: \n{line}\n{df}\n")

def main():
    df = create_dataframe()
    fill_missing_values(df)


if __name__ == "__main__":
    main()


"""
Create a DataFrame with missing values and fill them with column mean.
data 2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}
"""