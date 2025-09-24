import pandas as pd
import numpy as np

def create_dataframe():
    line = "*"*100

    data = {'Marks': [85, np.nan, 90, np.nan, 95]} 

    print(line)

    # create Dataframe
    df = pd.DataFrame(data)
    print(f"Created DataFrame with missing data: \n{line}\n{df}\n")

    return df

def fill_missing_values(df):
    line = "*"*100

    df['Marks'] = df['Marks'].fillna(df['Marks'].interpolate())
    
    print(f"DataFrame after filling the missing data: \n{line}\n{df}\n")

def main():
    df = create_dataframe()
    fill_missing_values(df)


if __name__ == "__main__":
    main()


"""
Q8: Fill missing values in a numeric column using interpolation. data = {'Marks': [85, np.nan, 90, np.nan, 95]} 
"""