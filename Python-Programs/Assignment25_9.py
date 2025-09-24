import pandas as pd
import numpy as np

def create_dataframe():
    line = "*"*100

    data = {'Marks': [45, 67, 88, 32, 76]} 

    print(line)

    # create Dataframe
    df = pd.DataFrame(data)
    print(f"Created DataFrame with missing data: \n{line}\n{df}\n")

    return df

def replace_values(df):
    line = "*"*100

    df['Marks'] = df['Marks'].where(df['Marks'] >= 50, 'Fail')
    
    print(f"DataFrame after filling the missing data: \n{line}\n{df}\n")

def main():
    df = create_dataframe()
    replace_values(df)


if __name__ == "__main__":
    main()


"""
Q9: Replace values in 'Marks' less than 50 with 'Fail' using where(). data = {'Marks': [45, 67, 88, 32, 76]} 
"""