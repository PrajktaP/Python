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

def normalize_column(df, column):
    line = "*"*100

    min = df[column].min()
    max = df[column].max()
    df[column] = (df[column] - min) / (max - min)

    # create Dataframe
    print(f"Normalized DataFrame: \n{line}\n{df}\n")

def main():
    df = create_dataframe()
    normalize_column(df, 'Math')

if __name__ == "__main__":
    main()


"""
Q1: Normalize the 'Math' scores using Min-Max scaling. 

Normalized= x - min / max - min
"""