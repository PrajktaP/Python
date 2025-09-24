import pandas as pd

def create_dataframe():
    line = "*"*100

    data = {'Age': [18, 22, 25, 30, 35]} 

    print(line)

    # create Dataframe
    df = pd.DataFrame(data)

    print(f"Created DataFrame: \n{line}\n{df}\n")

    return df

def normalize_column(df, column):
    line = "*"*100

    min = df[column].min()
    max = df[column].max()
    df[column] = (df[column] - min) / (max - min)

    # create Dataframe
    print(line)
    print(f"Normalized DataFrame: \n{line}\n{df}\n")

def main():
    df = create_dataframe()
    normalize_column(df, 'Age')

if __name__ == "__main__":
    main()


"""
Q7: Normalize 'Age' column using Min-Max Scaling. data = {'Age': [18, 22, 25, 30, 35]} 
"""