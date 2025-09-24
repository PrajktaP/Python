
---------------------- Assignment 11 ----------------------

As we discussed in the session before writing recursive solution please write the code using iteration.

1. Print Numbers Using Recursion
Write a recursive function to print numbers from 1 to N.
Expected Output (for n=5):
1 2 3 4 5

2. Factorial Using Recursion
Write a recursive function to calculate factorial of a number.
factorial(5) → 120

3. Sum of Digits
Write a recursive function to calculate the sum of digits of a number.
sum_of_digits(1234) → 10

4. Power Function Using Recursion
Write a recursive function to calculate x^n.
power(2, 3) → 8

5. Count Zeros in a Number (Recursively)
Write a recursive function to count how many zeros are in the given number.
count_zeros(1020300) → 4

6. Sum of First N Natural Numbers
Write a recursive function to calculate sum from 1 to n.
sum_n(5) → 15

7. Print Pattern Using Recursion (Right Triangle)
Write a recursive function to print the following pattern:
*
* *
* * *
* * * *

---------------------- Assignment 12 ----------------------

1.Write a program which contains one class named as Demo.
Demo class contains two instance variables as no1 ,no2.
That class contains one class variable as Value.
There are two instance methods of class as Fun and Gun which displays values of instance
variables.
Initialise instance variable in init method by accepting the values from user.
After creating the class create the two objects of Demo class as
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)
Now call the instance methods as
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()

2. Write a program which contains one class named as Circle.
Circle class contains three instance variables as Radius ,Area, Circumference.
That class contains one class variable as PI which is initialise to 3.14.
Inside init method initialise all instance variables to 0.0.
There are three instance methods inside class as Accept(), CalculateArea, CalculateCircumference(), Display(). 
Accept method will accept value of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable Area.
CalculateCircumference() method will calculate circumference of circle and store it into instance
variable Circumference.
And Display() method will display value of all the instance variables as Radius , Area,
Circumference.
After designing the above class call all instance methods by creating multiple objects.

3. Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.

---------------------- Assignment 13 ----------------------

1. Write a program which contains one class named as BookStore.
BookStore class contains two instance variables as Name ,Author.
That class contains one class variable as NoOfBooks which is initialise to 0.
There is one instance methods of class as Display which displays name, Author and number of books.
Initialise instance variable in init method by accepting the values from user as name and author.
Inside init method increment value of NoOfBooks by one.
After creating the class create the two objects of BookStore class as
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()     # Linux System Programming by Robert Love. No of books : 1
Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()     # C Programming by Dennis Ritchie. No of books : 2


2. Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialise to 10.5.
Inside init method initialise all name and amount variables by accepting the values from user.
There are
Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable
Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects.


3. Write a program which contains one class named as Numbers.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There
are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required.
After designing the above class call all instance methods by creating multiple objects.

---------------------- Assignment 14 ----------------------

1. Create a class Employee with attributes name, emp_id, and salary. Create objects
of this class and print their details using a method.
Expected Output:
Name: Rohit, ID: 101, Salary: 50000

2. Write a class Rectangle with length and width. Add a method to compute area and
perimeter.
Area: 50, Perimeter: 30

3. Create a class Book with private attribute __price. Add methods to get and set the
price. Show encapsulation.

4. Create a class Student with name, roll_no, and a class variable school_name. Print
student details and school name. Change the school name using class name.

5. Create a class BankAccount with account_number, name, and balance. Use
__init__ and create methods for deposit, withdraw, and displaying balance.

6. Create a class Calculator with methods for add, subtract, multiply, divide. Ask user
input for values and call methods accordingly.

7. Create a base class Person with name and age. Derive a class Teacher with subject
and salary. Use super() to call base class constructor and print both.

8. Create a class Vehicle with method start(). Derive class Car and override the
method start() with additional behavior. Show method overriding.

9. Create a class Product with attributes name and price. Implement __eq__ method
to compare two products if they are equal in price.

10. Demonstrate private, protected and public access modifiers using a class Employee
with attributes: __salary, _department, name.

---------------------- Assignment 15 ----------------------

1.Write a program which accepts file name from user and check whether that file exists in
current directory or not.
Input : Demo.txt
Check whether Demo.txt exists or not.
2. Write a program which accept file name from user and open that file and display the contents
of that file on screen.
Input : Demo.txt
Display contents of Demo.txt on console.
3.Write a program which accept file name from user and create new file named as Demo.txt and
copy all contents from existing file into new file. Accept file name through command line
arguments.
Input : ABC.txt
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt
4.Write a program which accept two file names from user and compare contents of both the
files. If both the files contains same contents then display success otherwise display failure.
Accept names of both the files from command line.
Input : Demo.txt
Hello.txt
Compare contents of Demo.txt and Hello.txt
5. Accept file name and one string from user and return the frequency of that string from file.
Input : Demo.txt
Marvellous
Search “Marvellous” in Demo.txt

---------------------- Assignment 16 ----------------------

1. Write a Python program to create a text file named student.txt and write the
names of 5 students into it.

2. Write a program to read and display the contents of a file data.txt.

3. Write a Python script to count the number of lines, words, and characters in a
given file.

4. Accept 10 numbers from the user and write them into a file named numbers.txt,
each on a new line.

5. Write a program to read a file line by line and display only those lines that contain
more than 5 words.

6. Write a Python program to copy the contents of one file (source.txt) into another
file (destination.txt).

7. Create a file marks.txt with student name and marks. Then read the file and
display students who scored more than 75 marks.

8. Write a script to remove all blank lines from a file. Save the cleaned output to a new file.

---------------------- Assignment 17 ----------------------

1. Write a Python script that prints 'Jay Ganesh...' every 2 seconds. Use the schedule.every(2).seconds.do(...) function. 
2. Schedule a task that displays the current date and time every minute using the datetime module. 
3. Write a program that schedules a function to print 'Do Coding..!' every 30 minutes. 
4. Create a task that runs once every day at 9:00 AM and prints 'Namskar...' 
5. Schedule a job that runs every 5 minutes to write the current time to a file Marvellous.txt. 
6. Write a script that schedules multiple tasks: one to print 'Lunch Time!' at 1 PM, and another to print 'Wrap up work' at 6 PM. 
7. Schedule a function that performs file backup every hour and writes a log entry into backup_log.txt. 
8. Write a script that simulates checking for email updates every 10 seconds. (Use a print statement like 'Checking mail...' instead of real email logic.)

---------------------- Assignment 18 ----------------------

1. Write a program which accepts file name from user and check whether that file exists in current directory or not. Input : Demo.txt Check whether Demo.txt exists or not. 
2. Write a program which accept file name from user and open that file and display the contents of that file on screen. Input : Demo.txt Display contents of Demo.txt on console. 
3. Write a program which accept file name from user and create new file named as Demo.txt and copy all contents from existing file into new file. Accept file name through command line Input : ABC.txt Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt 
4. Write a program which accept two file names from user and compare contents of both the files. If both the files contains same contents then display success otherwise display failure. Accept names of both the files from command line. Input: Demo.txt Hello.txt Compare contents of Demo.txt and Hello.txt 
5. Accept file name and one string from user and return the frequency of that string from file. Input : Demo.txt Marvellous. Search 'Marvellous' in Demo.txt 


---------------------- Assignment 19 ----------------------

Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

1. Design automation script which accept directory name and file extension from user. Display all files with that extension. Usage : DirectoryFileSearch.py 'Demo''.txt' Demo is name of directory and txt is the extension that we want to search. 
2. Design automation script which accept directory name and two file extensions from user. Rename all files with first file extension with the second file extention. Usage : DirectoryRename.py 'Demo''.txt' '.doc' Demo is name of directory and txt is the extension that we want to search and rename with .doc. After execution this script each txt file gets renamed as .doc. 
3. Design automation script which accept two directory names. Copy all files from first directory into second directory. Second directory should be created at run time. Usage : DirectoryCopy.py 'Demo' 'Temp' Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files from Demo to Temp. 
4. Design automation script which accept two directory names and one file extension. Copy all files with the specified extension from first directory into second directory. Second directory should be created at run time. Usage : DirectoryCopyExt.py 'Demo' 'Temp' '.exe' Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files with extension .exe from Demo to Temp.

---------------------- Assignment 21 ----------------------

Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.
1.Design automation script which display information of running processes as its name, PID,
Username.
Usage : ProcInfo.py
2.Design automation script which accept process name and display information of that process if
it is running.
Usage : ProcInfo.py Notepad
3. Design automation script which accept directory name from user and create log file in that
directory which contains information of running processes as its name, PID, Username.
Usage : ProcInfoLog.py Demo
Demo is name of Directory.
4. Design automation script which accept directory name and mail id from user and create log
file in that directory which contains information of running processes as its name, PID,
Username. After creating log file send that log file to the specified mail.
Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
Demo is name of Directory.
marvellousinfosystem@gmail.com is the mail id.

---------------------- Assignment 22 ----------------------

Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.
Design automation script which performs following task.
Accept Directory name from user and delete all duplicate files from the specified directory by
considering the checksum of files.
Create one Directory named as Marvellous and inside that directory create log file which
maintains all names of duplicate files which are deleted.
Name of that log file should contains the date and time at which that file gets created.
Accept duration in minutes from user and perform task of duplicate file removal after the specific
time interval.
Accept Mail id from user and send the attachment of the log file.
Mail body should contains statistics about the operation of duplicate file removal.
Mail body should contains below things :
Starting time of scanning
Total number of files scanned
Total number of duplicate files found
Consider below command line options for the gives script
DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
- DuplicateFileRemoval.py
Name of python automation script
- E:/Data/Demo
Absolute path of directory which may contains duplicate files
- 50
Time interval of script in minutes
- marvellousinfosystem@gmail.com
Mail ID of the receiver
Note :
For every separate task write separate function.
Write all user defined functions in one user defined module.
Use proper validation techniques.
Provide Help and usage option for script.
Create one Readme file which contains description of our script, details of command line options.

---------------------- Assignment 23 ----------------------

Q1: Create a DataFrame for student marks and print basic information like shape, columns, and
data types.
data = {
'Name': ['Amit', 'Sagar', 'Pooja'],
'Math': [85, 90, 78],
'Science': [92, 88, 80],
'English': [75, 85, 82]
}
Note : Consider the same dataset for this as well as next assignment.
Q2: Use the DataFrame from Q1 and print descriptive statistics using .describe().
Q3: Add a new column 'Total' to the DataFrame as the sum of all subject marks.
Q4: Display students who scored more than 85 in Science.
Q5: Replace 'Pooja' with 'Puja' in the 'Name' column.
Q6: Sort the DataFrame by 'Total' marks in descending order.
Q7: Create a bar plot of student names vs total marks.
Q8: Plot a line chart of marks for 'Amit' across all subjects.a
Q9: Create a DataFrame with missing values and fill them with column mean.
data2 = {
'Name': ['Amit', 'Sagar', 'Pooja'],
'Math': [np.nan, 76, 88],
'Science': [91, np.nan, 85]
}
Q10: Drop the 'English' column from original DataFrame.

---------------------- Assignment 24 ----------------------

Q1: Normalize the 'Math' scores using Min-Max scaling. 
Q2: Create a gender column and perform one-hot encoding. 
Q3: Group students by gender and calculate average marks. 
Q4: Plot a pie chart of subject marks for 'Sagar'. 
Q5: Add a new column 'Status' where students with total >= 250 are 'Pass', else 'Fail'. 
Q6: Count how many students passed. 
Q7: Export the final DataFrame to a CSV file. 
Q8: Plot a histogram of math marks. 
Q9: Rename 'Math' column to 'Mathematics'. 
Q10: Plot a boxplot for English marks to check distribution and outliers.

----------------------  ----------------------

A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
For example:
The number 28 is a perfect number because:
Its divisors (excluding 28) are: 1, 2, 4, 7, 14
If you add them up: 1 + 2 + 4 + 7 + 14 = 28
