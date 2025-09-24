def main():
    file_obj = open("numbers.txt", "w")

    try:
        count = 10
        numbers = []
        print(f"Enter {count} numbers: ")
        for num in range(count):
            no = int(input())
            numbers.append(str(no))

        file_obj.write("\n".join(numbers))

    except ValueError as vobj:
        print("Invalid value entered | ", vobj)
        return

    file_obj.close()

if __name__ == "__main__":
    main()



"""
4. Accept 10 numbers from the user and write them into a file named numbers.txt,
each on a new line.
"""