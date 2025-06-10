import os

def main():
    base_path = "/Users/prajktaphisarekar/work/python/python_marvellous/Marvellous-Python-Assignments/"
    assignment_num = int(input("Enter assignment number: "))
    dir_name = base_path + f"Assignment_{assignment_num}"

    file_name = f"{dir_name}/readme.txt"

    if(os.path.exists(file_name)):
        print("File exists in current directory.")
        file_obj = open(file_name, "r")
        contents = file_obj.read()
        print("File contents before: ", contents)

        contents = contents.replace('“', '\'').replace('”', '\'').replace('"', '\'').replace('\n', ' ')
        print("File contents after: ", contents)
        file_obj.close()

        file_obj = open(file_name, "w")
        file_obj.write(contents)
        file_obj.close()
    else:
        print("File does not exist in current directory.")

if __name__ == "__main__":
    main()

