import os

def main():
    base_path = "/Users/prajktaphisarekar/work/python/python_marvellous/Marvellous-Python-Assignments/"
    assignment_num = int(input("Enter assignment number: "))
    dir_name = base_path + f"Assignment_{assignment_num}"
    file_name = f"{dir_name}/readme.txt"

    sobj = open("starter.py", "r")
    starter_content = sobj.read()

    fobj = open(file_name, "r")
    lst = fobj.readlines()

    for i in range(len(lst)):
        file_obj = open(f"{dir_name}/Assignment{assignment_num}_{i+1}.py", "w")
        file_obj.write(starter_content)
        file_obj.write(f"\n\n\n\"\"\"\n{lst[i]}\"\"\"")
        file_obj.close()
    

if __name__ == "__main__":
    main()
