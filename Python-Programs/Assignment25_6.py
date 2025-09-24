import pandas as pd
import numpy as np

def create_dataframe():
    line = "*"*100

    data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']} 

    print(line)

    # create Dataframe
    df = pd.DataFrame(data)

    print(f"Created DataFrame: \n{line}\n{df}\n")

    return df

def replace_values(df):
    line = "*"*100

    replace_values_dict = {
        'A+': 'Excellent',
        'A': 'Very Good',
        'B+': 'Good',
        'B': 'Average',
        'C': 'Poor'
    }

    df['Grade'] = df['Grade'].replace(replace_values_dict)

    print(line)
    print(f"Dataframe after replacing values': \n{line}\n{df}\n")

def main():
    df = create_dataframe()

    replace_values(df)

if __name__ == "__main__":
    main()

"""
Q6: Replace multiple values in a column using a dictionary. 
data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']} 
Replace as 'A+': ‘Excellent' 'A': 'Very Good’ 'B+': ‘Good' 'B': ‘Average' 'C': 'Poor' 
"""