#  Write a program to accept marks of 6 students and display them in a sorted manner. 

marks = []
F1 = int(input("Enter marks of the student: "))
marks.append(F1)
F2 = int(input("Enter marks of the student: "))
marks.append(F2)
F3 = int(input("Enter marks of the student: "))
marks.append(F3)
F4 = int(input("Enter marks of the student: "))
marks.append(F4)
F5 = int(input("Enter marks of the student: "))
marks.append(F5)
F6 = int(input("Enter marks of the student: "))
marks.append(F6)

marks.sort()
print(marks)

# Write a program to count the number of zeros in the following tuple: 
a = (7, 0, 8, 0, 0, 9) 

n = a.count(0)
print(n)
