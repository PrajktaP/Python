import pandas as pd

def find_science_toppers():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    students = {}

    for index, row in df.iterrows():
        if row['Science'] > 85:
            students[row['Name']] = row['Science']
    
    print(f"Following are students with more than 85 marks in Science: ")
    print(students)

def main():
    find_science_toppers()

if __name__ == "__main__":
    main()


"""
Q4: Display students who scored more than 85 in Science.
"""
