import os

def main():
    file_name = input("Enter the name of the file that you want to ready from: ")

    if(os.path.exists(file_name)):
        print("File exists in current directory.")
        file_obj = open(file_name, "r")
        contents = file_obj.read()
        print("File contents: ", contents)

        file_obj.seek(0)  # move pointer back to start
        # lines = contents.split("\n") # this is valid if each sentence is on new line
        # Internally, readlines() reads the file from beginning to end 
        # and splits the content into a list of lines, using the newline character (\n) as the delimiter.
        lines = file_obj.readlines()
        print("Number of lines in the file: ", len(lines))

        words = contents.split() # default is split on whitespace
        print("Number of words in the file: ", len(words))

        file_obj.close()
    else:
        print("File does not exist in current directory.")

if __name__ == "__main__":
    main()



"""
3. Write a Python script to count the number of lines, words, and characters in a given file.
"""