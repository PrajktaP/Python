import pandas as pd

def create_dataframe():
    line = "*"*100

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    print(line)

    # create Dataframe
    df = pd.DataFrame(data)
    print(f"Created DataFrame: \n{line}\n{df}\n")

    return df

def print_dataframe_details(df):
    line = "*"*100

    # display shape
    print(line)
    print(f"Shape of DataFrame (rows, columns): \n{line}\n{df.shape}\n")

    # display columns
    print(line)
    print(f"Columns in DataFrame: \n{line}\n{df.columns.to_list()}\n")

    # display Data types
    print(line)
    print(f"Data types in DataFrame: \n{line}\n{df.dtypes}\n")

def main():
    df = create_dataframe()
    print_dataframe_details(df)

if __name__ == "__main__":
    main()


"""
Q1: Create a DataFrame for student marks and print basic information like shape, columns, and data types.
data = {
'Name': ['Amit', 'Sagar', 'Pooja'],
'Math': [85, 90, 78],
'Science': [92, 88, 80],
'English': [75, 85, 82]
}
"""
