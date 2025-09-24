import pandas as pd

def create_dataframe():
    line = "*"*100

    data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']} 

    print(line)

    # create Dataframe
    df = pd.DataFrame(data)

    print(f"Created DataFrame: \n{line}\n{df}\n")

    return df

def one_hot_encode(df, column):
    line = "*"*100

    encoded_df = pd.get_dummies(df, columns=[column])

    print(line)
    print(f"DataFrame after encoding: \n{line}\n{encoded_df}\n")

def main():
    df = create_dataframe()

    one_hot_encode(df, 'Department')

if __name__ == "__main__":
    main()


"""
Q4: Apply One-Hot Encoding to a 'Department' column. data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']} 
"""