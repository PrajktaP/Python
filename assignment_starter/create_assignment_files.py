import os

# Create a directory (or nested directories)
os.makedirs('my_directory', exist_ok=True)

base_path = "/Users/prajktaphisarekar/work/python/python_marvellous/Marvellous-Python-Assignments/"

assignment_num = int(input("Enter assignment number: "))
assignments_count = int(input("Enter how many assignments: "))

dir_name = base_path + f"Assignment_{assignment_num}"

os.makedirs(dir_name, exist_ok=True)

for i in range(assignments_count):
    file_obj = open(f"{dir_name}/Assignment{assignment_num}_{i+1}.py", "w")
    file_obj.close()

readme_obj = open(f"{dir_name}/readme.txt", "x")
readme_obj.close()