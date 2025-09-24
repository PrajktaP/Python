import pandas as pd
import matplotlib.pyplot as plt
from Assignment23_1 import create_dataframe
from Assignment23_3 import add_column

def line_chart_for_one_student(df, student_name):
    student_row = df[df['Name'] == student_name].iloc[0]
    subjects = ['Math', 'Science', 'English']
    marks = []
    for subj in subjects:
        marks.append(student_row[subj])

    plt.figure(figsize=(8, 5))
    plt.plot(subjects, marks, color='purple', linestyle='--', marker='o')

    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title('Marks for Amit')
    plt.grid(True)

    plt.show()

def main():
    df = create_dataframe()
    add_column(df)
    line_chart_for_one_student(df, 'Amit')

if __name__ == "__main__":
    main()


"""
Q8: Plot a line chart of marks for 'Amit' across all subjects
"""