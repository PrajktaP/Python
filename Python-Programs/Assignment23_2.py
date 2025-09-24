import pandas as pd
from Assignment23_1 import create_dataframe

def print_statistics(df):
    line = "*"*100

    print(line)
    # Statistics of the dataframe
    print(f"Statistics of the Dataframe: \n{line}\n{df.describe()}\n")

def main():
    df = create_dataframe()
    print_statistics(df)

if __name__ == "__main__":
    main()


"""
Q2: Use the DataFrame from Q1 and print descriptive statistics using .describe().
"""
