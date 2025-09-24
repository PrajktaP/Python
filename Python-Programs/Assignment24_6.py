import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

def add_total_column(df):
    line = "*"*100

    # Adding column 'Total'
    df['Total'] = df['Math'] + df['Science'] + df['English']

    print(line)
    # Dataframe after adding column 'Total'
    print(f"Dataframe after adding column 'Total': \n{line}\n{df}\n")

def add_status_column(df):
    line = "*"*100

    # Adding column 'Status'
    df['Status'] = np.where(df['Total'] > 250, 'Pass', 'Fail')

    print(line)
    # Dataframe after adding column 'Status'
    print(f"Dataframe after adding column 'Status': \n{line}\n{df}\n")

def count_students_passed(df):
    line = "*"*100

    students_passed_count = (df['Status'] == 'Pass').sum()

    print(line)
    print(f"Number of students who passed: {students_passed_count}")
    print(line)

def main():
    df = create_dataframe()

    # Add column 'Total'
    add_total_column(df)

    # Add column 'Status'
    add_status_column(df)

    count_students_passed(df)

if __name__ == "__main__":
    main()


"""
Q6: Count how many students passed. 
"""