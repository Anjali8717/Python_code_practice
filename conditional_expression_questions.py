# Write a program to find the greatest of four numbers entered by the user.
 
a1 = input("Enter the number :")
a2 = input("Enter the number :")
a3 = input("Enter the number :")
a4 = input("Enter the number :")

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greatest number", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greatest number", a2)

elif(a3>a2 and a3>a1 and a3>a4):
    print("a3 is greatest number", a3)

elif(a4>a2 and a4>a3 and a4>a1):
    print("a4 is greatest number", a4)

# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

# Check for total percentage 
total_percentage = 100*((marks1 + marks2 + marks3)/300)

if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print("'congrates' You are passed", total_percentage)

else:
    print("You are failed, better luck next time", total_percentage)

# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment: ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is spam")

else:
    print("This comment is not a spam")


# Write a program to find whether a given username contains less than 10 characters or not. 

username = input("Enter your username: ")

if(len(username)<10):
    print("Username is less than 10 characters")

else:
    print("All is well!!")


# Write a program which finds out whether a given name is present in a list or not.

l = ["Rohan", "mohan", "sohan", "tohan",]

name = input("Enter your name: ")

if(name in l):
    print("your name is in the list")

else:
    print("Your name is not in the list")


# Write a program to calculate the grade of a student from his marks from the following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50     => F

m = int(input("Enter students marks: "))

if(90<=m <=100):
    Grade = "Ex"

elif(80<=m <90):
    Grade = "A"

elif(70<=m <80):
    Grade = "B"

elif(60<=m <70):
    Grade = "c"

elif(50<=m <60):
    Grade = "D"

elif(m<50):
    Grade = "F"

print("Your grade is: ", Grade)



