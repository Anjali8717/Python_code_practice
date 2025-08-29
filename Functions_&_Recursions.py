#  Write a program to greet a user with “Good day” using functions.
def goodDay(): 
    name = input("Enter the name :")
    print("Good day", name)  

goodDay()

# or
def goodDay(Name):
    print("Good day "  + Name)

goodDay("Rohan")

# Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = 34
b = 23
c = 21

print(greatest(a, b, c))

# Write a python program using function to convert Celsius to Fahrenheit.

def f_to_c(f):
    return 5*(f - 32)/9

f = int(input("Enter temperature in F : "))
print(f_to_c(f))


# Write a python function which converts inches to cms.

def inch_to_cms(inch):
    return inch* 2.54
n = int(input("Enter value in inches : "))
print(f"The value in cms is :{inch_to_cms(n)}")


# Write a python function to remove a given word from a list and strip it at the same time. 
def rem(l, word):
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n 
l = ["shubham", "harry", "Rohan", "anjali", "an"]

print(rem(l, "an"))
