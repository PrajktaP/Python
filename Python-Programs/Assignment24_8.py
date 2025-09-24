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

def histogram_of_marks(df, subject):
    plt.figure(figsize=(8, 6))
    plt.hist(df[subject], bins=10, color="skyblue", edgecolor = 'black')

    plt.title(f"Histogram of {subject} marks")
    plt.xlabel(f"{subject} Marks")
    plt.ylabel('Number of Students')
    plt.grid(True)
    plt.tight_layout()

    plt.show()

def main():
    df = create_dataframe()

    histogram_of_marks(df, 'Math')

if __name__ == "__main__":
    main()


"""
Q8: Plot a histogram of math marks. 
"""