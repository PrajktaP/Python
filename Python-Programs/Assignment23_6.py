import pandas as pd
from Assignment23_1 import create_dataframe
from Assignment23_3 import add_column

def sort_dataframe(df, col):
    line = "*"*100

    df.sort_values(by=col, ascending=False, inplace=True)

    print(line)
    print(f"DataFrame Sorted by Total marks: \n{line}\n{df}\n")
    
def main():
    df = create_dataframe()
    add_column(df)
    sort_dataframe(df, 'Total')

if __name__ == "__main__":
    main()


"""
Q6: Sort the DataFrame by 'Total' marks in descending order.
"""
