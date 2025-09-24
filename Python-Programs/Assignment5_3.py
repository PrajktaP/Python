
def CheckVotingEligibility(age):
    if age >= 18:
        print("Eligible to vote.")
    else:
        print("Not eligible to vote.")

def main():
    while True:
        age = input("Enter you age: ")

        if age.isdigit():
            ValidAge = int(age)
            break
        else:
            print("Invalid Input.", end=" ")

    CheckVotingEligibility(ValidAge)

if __name__ == "__main__":
    main()


"""
Q3. Voting Eligibility Checker
Accept age from the user and check whether the person is eligible to vote. (age should be 18 or above.)
Expected Input:
Enter age: 19
Expected Output:
Eligible to vote.
"""