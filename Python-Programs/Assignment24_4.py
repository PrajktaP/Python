import pandas as pd
import matplotlib.pyplot as plt

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

def pie_plot_for_one_student(df, student_name):
    student_row = df[df['Name'] == student_name].iloc[0]
    subjects = ['Math', 'Science', 'English']
    marks = [student_row[subj] for subj in subjects]

    plt.figure(figsize=(8, 8))
    plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'salmon'])
    plt.title("Marks for Sagar")
    plt.axis('equal')  # Equal aspect ratio makes the pie chart circular

    plt.show()


def main():
    df = create_dataframe()

    pie_plot_for_one_student(df, 'Sagar')

if __name__ == "__main__":
    main()


"""
Q4: Plot a pie chart of subject marks for 'Sagar'. 
"""