import os
import re

def main():
    base_path = "/Users/prajktaphisarekar/work/python/python_marvellous/Marvellous-Python-Assignments/"
    assignment_num = int(input("Enter assignment number: "))
    dir_name = base_path + f"Assignment_{assignment_num}"
    file_name = f"{dir_name}/readme.txt"

    sobj = open("starter.py", "r")
    starter_content = sobj.read()

    fobj = open(file_name, "r")
    data = fobj.read()

    # Extract only the part starting from "1." using regex
    matches = re.split(r'(?=\b\d\.)', data)
    task_parts = [part.strip() for part in matches if re.match(r'^\d\.', part.strip())]
    
    # Now task_parts will contain exactly the 4 task blocks
    for i, task in enumerate(task_parts, 1):
        file_obj = open(f"{dir_name}/Assignment{assignment_num}_{i}.py", "w")
        file_obj.write(starter_content)
        file_obj.write(f"\n\n\n\n\"\"\"\n{task}\n\"\"\"\n")
        file_obj.close()

if __name__ == "__main__":
    main()
