import os

def main():
    file_name = input("Enter the name of the file that you want to ready from: ")

    if(os.path.exists(file_name)):
        print("File exists in current directory.")
        file_obj = open(file_name, "r")

        # Internally, readlines() reads the file from beginning to end 
        # and splits the content into a list of lines, using the newline character (\n) as the delimiter.
        lines = file_obj.readlines()

        for line in lines:
            words = line.split() # default is split on whitespace
            num_of_words = len(words)
            print("Number of words in line: ", num_of_words)
            if(num_of_words > 5):
                print(line)

        file_obj.close()
    else:
        print("File does not exist in current directory.")

if __name__ == "__main__":
    main()



"""
5. Write a program to read a file line by line and display only those lines that contain
more than 5 words.
"""