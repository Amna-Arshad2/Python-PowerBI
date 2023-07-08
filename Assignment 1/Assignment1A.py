# Assignment # 1A ( Marksheet )
# 1) Take input marks of Eng, Isl and Maths out of 100 in 3 different variable
# 2) Mentioned Variable of Total Marks and assign 300 to it 
# 3) Calculate percentage
# 4) Mentioned grade using conditional statement like I explained in cLass 

# Solution:
marks_eng = float(input("Enter your English marks: "))
marks_isl = float(input("Enter your Islamiat marks: "))
marks_maths = float(input("Enter your Maths marks: "))
total_marks = 300

if (marks_eng<0 or marks_eng>100) or (marks_isl<0 or marks_isl>100) or (marks_maths<0 or marks_maths>100) :
    print('Invalid Input!, Please Enter positive integer between 0 to 100')
else:    
    obtained_marks = marks_eng + marks_isl + marks_maths
    percentage = (obtained_marks/total_marks)*100

    if percentage >=90 :
        grade = "A+"
    elif percentage >=80 :
        grade = "A"
    elif percentage >=70 :
        grade = "B"
    elif percentage >=60 :
        grade = "C"
    elif percentage >=50 :
        grade = "D"
    elif percentage >=33 :
        grade = "E"
    else :
        grade = "F"

    print(f'you have obtained {obtained_marks} marks with {round(percentage,2)}% marks') 
    print(f'your Grade is {grade}')
