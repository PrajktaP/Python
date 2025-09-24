import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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

def boxplot_of_marks(df, subject):
    plt.figure(figsize=(8, 6))
    plt.boxplot(df[subject], vert=True, patch_artist=True)

    plt.title(f"Boxplot for {subject} marks to check distribution and outliers")
    plt.ylabel(f"{subject} Marks")
    plt.grid(True, axis='y')
    plt.tight_layout()

    plt.show()

def main():
    df = create_dataframe()

    boxplot_of_marks(df, 'English')

if __name__ == "__main__":
    main()


"""
Q10: Plot a boxplot for English marks to check distribution and outliers.
"""