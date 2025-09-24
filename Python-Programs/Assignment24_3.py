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
    print(line)
    print(f"Normalized DataFrame: \n{line}\n{df}\n")

def add_column(df, column, column_values):
    line = "*"*100

    df[column] = column_values

    print(line)
    print(f"DataFrame after adding Gender: \n{line}\n{df}\n")

def one_hot_encode(df, column):
    line = "*"*100

    encoded_df = pd.get_dummies(df, columns=[column])

    print(line)
    print(f"DataFrame after encoding: \n{line}\n{encoded_df}\n")

def group_by_gender(df):
    groups_by_gender = df.groupby('Gender')[['Math', 'Science', 'English']].mean()
    print(groups_by_gender)


def main():
    df = create_dataframe()
    normalize_column(df, 'Math')

    gender_values = ['Male', 'Male', 'Female']
    add_column(df, 'Gender', gender_values)

    # one_hot_encode(df, 'Gender')

    group_by_gender(df)

if __name__ == "__main__":
    main()


"""
Q3: Group students by gender and calculate average marks. 
"""