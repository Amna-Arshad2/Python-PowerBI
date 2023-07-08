
""""
# Assignment 1B
1. Write a Python program to print the following string in a specific format (see the output).
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

"""

# Solution :
print('''
Twinkle, twinkle, little star,
         How I wonder what you are!
                 Up above the world so high,
                 Like a diamond in the sky.
Twinkle, twinkle, little star,
         How I wonder what you are
''')
            
                # OR
print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\t How I wonder what you are\n")                


# 2. Write a Python program to find out what version of Python you are using.
# Solution : 
import sys
print(f'You are currently using {sys.version} Python version \n')


# 3. Write a Python program to display the current date and time
# Solution :
import datetime as dt
curr_time = dt.datetime.now().time().strftime('%H:%M:%S')
curr_date = dt.datetime.now().date().strftime('%d/%m/%Y')
print(f'Current Date is: {curr_date} & Current Time is: {curr_time}')


# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Solution :
radius = float(input('Enter circle Radius: '))
area = 3.14 *(radius**2)
print(f'The area of circle with radius {radius} is: {round(area, 3)} sq.meter')


# 5. Write python programme which accepts user first name and last name and print them in reverse order with a space between them. 
# Solution : 
first_name = input('Enter your First name: ')
last_name = input('Enter your Last name: ')
full_name = last_name + " " + first_name
# full_name = f'{first_name[::-1]} {last_name[::-1]}' 
print('Reversed name: ', full_name)


# 6. Write python program which takes two input from users and print them addition
# Solution :
num1 = float(input('Enter first number:'))
num2 = float(input('Enter second number:'))
print(f'Sum of {num1} and {num2} is: {num1 + num2} \n')


# 7. write a programme that takes 5 inputs from user for different subject's marks, Total it and generate marksheet using grades
# Solution : 
courses = ['English','Urdu','Maths','Biology','Physics']
total_marks = 500
obtained_marks = []
marks_sum = 0
grades =[]
counter = 0

for course in courses:
    marks = float(input(f'Enter obtained marks in {course}: '))
    if  marks <0 or marks >100 :
        print('Please Enter marks between 0 - 100')
        break
    elif  marks >=90 and marks <=100 :
        grades.append("A+")
    elif marks >=80 :
        grades.append("A")
    elif marks >=70 :
        grades.append("B")
    elif marks >=60 :
        grades.append("C")
    elif marks >=50 :
        grades.append("D")
    elif marks >=33 :
        grades.append("E")
    elif marks < 33 :
        grades.append("F*")
        counter += 1
    else :
        print(f'Invalid Input!')
    
    obtained_marks.append(marks)
    marks_sum += marks
    
def marksheet(courses, obtained_marks, grades) :
    percentage = (marks_sum/total_marks)*100 

    print("-------------Student's Marksheets----------------------------\n")
    print('Subject Name\tTotal Marks\tObtained Marks\tGrade \n')
    for i in range(len(courses)):
        print(f'{courses[i]}\t\t100\t\t{obtained_marks[i]}\t\t{grades[i]} \n')

    print('-------------------------------------------------------------')
    print(f'Total \t\t{total_marks} \t\t{marks_sum}\t\t{round(percentage, 2)} % \n')
    
    if counter >=3 :
        print(f'You have failed* in {counter} subjects. :(')
        
marksheet(courses, obtained_marks, grades)      


# 8. write a programme which take input from user and identify that given number is even or odd
# Solution :
number = int(input('Enter any integer: '))  # No Decimal numbers
if number%2 == 0 :
    print(f'{number} is even number')
else:
    print(f'{number} is odd number')

