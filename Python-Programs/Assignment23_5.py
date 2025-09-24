import pandas as pd
from Assignment23_1 import create_dataframe

def replace_name(df, orig_name, new_name):
    df['Name'] = df['Name'].replace(orig_name, new_name)
    
def main():
    line = "*"*100

    df = create_dataframe()
    replace_name(df, 'Pooja', 'Puja')

    print(f"Updated DataFrame: \n{line}\n{df}\n")

if __name__ == "__main__":
    main()


"""
Q5: Replace 'Pooja' with 'Puja' in the 'Name' column.
"""
