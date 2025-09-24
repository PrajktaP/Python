
---------------------- Assignment 1 ----------------------

1. Write a program which contains one function named as Fun(). That function should display
"Hello from Fun" on console.

2. Write a program which contains one function named
as ChkNum which accept one
parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.
Input 11                   Output : Odd Number
Input 8                    Output : Even Number

3. Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
Input : 11  5                      Output : 16

4. Write a program which display 5 times Marvellous on screen.
Output :
Marvellous
Marvellous
Marvellous
Marvellous
Marvellous

5. Write a program which display 10 to 1 on screen.
Output : 10 9 8 7 6 5 4 3 2 1

6. Write a program which accept number from user and check whether that number is positive or negative or zero.
Input : 11                  Output: Positive number 
Input : -8                  Output: Negative number
Input : 0                   Output: Zero

7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
Input : 8                   Output : False
Input : 25                  Output : True

8. Write a program which accept number from user and print that number of "*" on screen.
Input : 5            Output : * * * * *

9. Write a program which display first 10 even numbers on screen.
Output : 2 4 6 8 10 12 14 16 18 20

10. Write a program which accept name from user and display length of its name.
Input : Marvellous Output : 10

---------------------- Assignment 2 ----------------------

Assignment : 2

1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user.

2. Write a program which accept one number and display below pattern.
Input : 5
Output : * * * * *
* * * * *
* * * * *
* * * * *
* * * * *

3. Write a program which accept one number from user and return its factorial.
Input : 5 Output : 120

4.Write a program which accept one number form user and return addition of its factors.
Input : 12 Output : 16 (1+2+3+4+6)

5.Write a program which accept one number for user and check whether number is prime or not.
Input : 5 Output : It is Prime Number

6. Write a program which accept one number and display below pattern.
Input : 5
Output : * * * * *
* * * *
* * *
* *
*

7. Write a program which accept one number and display below pattern.
Input : 5
Output : 1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

8. Write a program which accept one number and display below pattern.
Input : 5
Output : 1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

9. Write a program which accept number from user and return number of digits in that number.
Input : 5187934 Output : 7

10. Write a program which accept number from user and return addition of digits in that number.
Input : 5187934 Output : 37
Note :
For each above question please create separate .py file as
Assignment2_1.py
Assignment2_2.py
Assignment2_3.py
Every applications logic should be enclosed in function.

---------------------- Assignment 3 ----------------------

Assignment : 3

1.Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130


2.Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56


3.Write a program which accept N numbers from user and store it into List. Return Minimum
number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5


4.Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3


5.Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54 (13 + 5 + 7 +2 + 5)

---------------------- Assignment 4 ----------------------

Assignment : 4

1.Write a program which contains one lambda function which accepts one parameter and return
power of two.
Input : 4 Output : 16
Input : 6 Output : 64


2.Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
Input : 4 3 Output : 12
Input : 6 3 Output : 18


3.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that
numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000


4.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204


5.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62

---------------------- Assignment 5 ----------------------

Python Programming Assignment based on data types on conditional logic

Q1. Arithmetic Operations on Two Numbers
Write a program to accept two integers from the user and display their:
• Sum
• Difference
• Product
• Division
Expected Input:
Enter first number: 10
Enter second number: 2
Expected Output:
Sum: 12
Difference: 8
Product: 20
Division: 5.0

Q2. Vowel or Consonant Check
Accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not,
print it's a consonant.
Expected Input:
Enter a character: e
Expected Output:
'e' is a vowel.

Q3. Voting Eligibility Checker
Accept age from the user and check whether the person is eligible to vote. (Age should be
18 or above.)
Expected Input:
Enter age: 19
Expected Output:
Eligible to vote.

Q4. Find Largest Among Three Numbers
Accept three numbers from the user and print the largest using nested if-else statements.
Expected Input:
Enter three numbers: 5 9 3
Expected Output:
Largest number is 9.

Q5. Even or Odd Number Check
Write a program to check whether the entered number is even or odd.
Expected Input:
Enter a number: 17
Expected Output:
17 is an odd number.

Q6. Celsius to Fahrenheit Converter
Accept temperature in Celsius and convert it to Fahrenheit using the formula:
F = (C × 9/5) + 32
Expected Input:
Enter temperature in Celsius: 25
Expected Output:
Temperature in Fahrenheit: 77.0°F

Q7. Area and Perimeter of Rectangle
Accept the length and width of a rectangle. Calculate and display the area and perimeter.
Expected Input:
Enter length: 5
Enter width: 3
Expected Output:
Area: 15
Perimeter: 16

---------------------- Assignment 6 ----------------------

Python Programming Assignment based on Loops

Q1. Write a program using a while loop to print numbers from 1 to 50.
Expected Output:
1 2 3 4 ... 50

Q2. Print Sum of Even Numbers Between 1 and 100. Use a loop to find and print the sum
of all even numbers from 1 to 100.
Expected Output:
Sum of even numbers between 1 to 100 is: 2550

Q3. Accept a number from the user and print its multiplication table up to 10.
Expected Input:
Enter a number: 7
Expected Output
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70

Q4. Accept a number and print its factorial using a for loop.
Expected Input:
Enter a number: 5
Expected Output:
Factorial of 5 is: 120

Q5. Accept a number from the user and check whether it is prime or not.
Expected Input:
Enter a number: 11
Expected Output:
11 is a prime number.

Q6. Print Triangle Pattern using Nested Loops
Expected Output:
*
* *
* * *
* * * *

Q7. Accept 5 numbers from the user. Find and print the largest number.
Expected Input:
Enter 5 numbers: 23 89 12 56 45
Expected Output:
Maximum number is: 89

---------------------- Assignment 7 ----------------------


Python Programming Assignment based on Lambda functions

Q1. Write two lambda functions:
• One to calculate square of a number
• Another to calculate cube of a number
Expected Input:
Enter a number: 3
Expected Output:
Square: 9
Cube: 27

Q2. Accept a list of integers from the user and use the map() function to double each
value.
Expected Input:
Enter list: 1 2 3 4 5
Expected Output:
Doubled list: [2, 4, 6, 8, 10]

Q3. Accept a list of numbers and use filter() to keep only even numbers.
Expected Input:
Enter list: 1 2 3 4 5 6
Expected Output:
Even numbers: [2, 4, 6]

Q4. Accept a list of numbers and use reduce() (from functools) to find the product of
all numbers.
Expected Input:
Enter list: 2 3 4
Expected Output:
Product: 24

Q5. Write a function that accepts a string and checks whether it is a palindrome.
Expected Input:
Enter a string: radar
Expected Output:
radar is a palindrome.

Q6. Write a function that accepts a list of integers and returns a list of prime numbers
using filter().
Expected Input:
Enter list: 10 11 12 13 14 15 16 17
Expected Output:
Prime numbers: [11, 13, 17]


---------------------- Assignment 8 ----------------------

Assignment : 8

1.Design python application which creates two thread named as even and odd. Even
thread will display first 10 even numbers and odd thread will display first 10 odd
numbers.

2.Design python application which creates two threads as evenfactor and oddfactor.
Both the thread accept one parameter as integer. Evenfactor thread will display
addition of even factors of given number and oddfactor will display addition of odd
factors of given number. After execution of both the thread gets completed main
thread should display message as “exit from main”.

3.Design python application which creates two threads as evenlist and oddlist. Both the
threads accept list of integers as parameter. Evenlist thread add all even elements
from input list and display the addition. Oddlist thread add all odd elements from input
list and display the addition.

4.Design python application which creates three threads as small, capital, digits. All the
threads accepts string as parameter. Small thread display number of small characters,
capital thread display number of capital characters and digits thread display number of
digits. Display id and name of each thread.

5.Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
screen. After execution of thread1 gets completed then schedule thread2.

---------------------- Assignment_9 ----------------------

1.Create a Python program that starts 3 threads, each printing numbers
from 1 to 5 with a delay of 1 second. Use threading.Thread.

2. Write a Python program using multiprocessing.Process to square a list of
numbers using multiple processes.

3. Create a Python program that uses multiprocessing.Pool to compute
factorial of numbers in a list.

4. Create a Python program that Compare execution time of summing
numbers from 1 to 10 million using normal function, threading, and
multiprocessing.

---------------------- Assignment 10 ----------------------

Assignment : 10

1.Write a program which contains one lambda function which accepts one parameter and return
power of two.
Input : 4 Input : 6 Output : 16
Output : 64

2.Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
Input : 4 3 Output : 12
Input : 6 3 Output : 18

3.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that
numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000

4.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204

5.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62

