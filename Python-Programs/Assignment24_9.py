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

def rename_column(df, old_name, new_name):
    line = "*"*100

    # df.rename(columns={'OldName': 'NewName'})
    df.rename(columns={old_name: new_name}, inplace=True)

    print(line)
    print(f"DataFrame after updating column 'Math': \n{line}\n{df}\n")

def main():
    df = create_dataframe()

    rename_column(df, 'Math', 'Mathematics')

if __name__ == "__main__":
    main()


"""
Q9: Rename 'Math' column to 'Mathematics'. 
"""