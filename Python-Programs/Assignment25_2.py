import pandas as pd

def create_dataframe():
    line = "*"*100

    data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]} 

    print(line)

    # create Dataframe
    df = pd.DataFrame(data)
    print(f"Created DataFrame: \n{line}\n{df}\n")

    return df

def convert_datatype(df, column, new_datatype):
    df['Age'] = df['Age'].astype(int)

def main():
    line = "*"*100

    df = create_dataframe()

    print(line)
    print(f"Before conversion: \n{line}\n{df.dtypes}\n")

    convert_datatype(df, 'Age', 'int')

    print(line)
    print(f"After conversion: \n{line}\n{df.dtypes}\n")

if __name__ == "__main__":
    main()


"""
Q2: Detect column data types and convert 'Age' from float to int. data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]} 
"""