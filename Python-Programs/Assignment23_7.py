import pandas as pd
import matplotlib.pyplot as plt
from Assignment23_1 import create_dataframe
from Assignment23_3 import add_column

def bar_plot(df):
    plt.figure(figsize=(8, 5))
    plt.bar(df['Name'], df['Total'], color='skyblue')

    plt.xlabel('Students')
    plt.ylabel('Total Marks')
    plt.title('Total Marks of All Students')
    plt.grid(True)

    plt.show()
    
def main():
    df = create_dataframe()
    add_column(df)
    bar_plot(df)

if __name__ == "__main__":
    main()


"""
Q7: Create a bar plot of student names vs total marks.
"""
