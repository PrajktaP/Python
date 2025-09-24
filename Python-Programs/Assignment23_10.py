import pandas as pd
import numpy as np
from Assignment23_1 import create_dataframe

def main():
    line = "*"*100

    df = create_dataframe()
    df.drop(columns = ['English'], inplace=True) # with inplace it updates the same df and returns

    print(line)
    print(f"DataFrame after dropping column 'English': \n{line}\n{df}\n")

if __name__ == "__main__":
    main()


"""
Q10: Drop the 'English' column from original DataFrame.
"""