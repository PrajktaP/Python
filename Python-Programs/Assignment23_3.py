import pandas as pd
from Assignment23_1 import create_dataframe

def add_column(df):
    line = "*"*100

    # Adding column 'Total'
    df['Total'] = df['Math'] + df['Science'] + df['English']

    print(line)
    # Dataframe after adding column 'Total'
    print(f"Dataframe after adding column 'Total': \n{line}\n{df}\n")

def main():
    df = create_dataframe()
    add_column(df)

if __name__ == "__main__":
    main()


"""
Q3: Add a new column 'Total' to the DataFrame as the sum of all subject marks.
"""
