# Write a program to print multiplication table of a given number using for loop.

a = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{a} x {i} = {a*i}")

# Write a program to greet all the person names stored in a list ‘l’ and which starts with S. 
l = ["Harry", "Soham", "Sachin", "Rahul"] 

for name in l:
    if(name.startswith("S")):
        print(f"hello {name}") 

# Write a program to find whether a given number is prime or not.

n = int(input("enter the number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("This number is not prime")
        break
    else:
        print("This is prime number")

# Write a program to find the sum of first n natural numbers using while loop. 
n = int(input("Enter the number : "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i += 1

print(sum)

# Write a program to calculate the factorial of a given number using for loop. 

n = int(input("Enter the number : "))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")

'''
Write a program to print the following star pattern. 
  * 
 *** 
***** for n = 3
'''

n = int(input("Enter the number : "))
for i in range (1, n+1):
    print(" "*(n-i), end = "")
    print("*"*(2*i-1), end ="")
    print("")

'''
Write a program to print the following star pattern: 
* 
** 
***      for n = 3
'''
n = int(input("Enter the number : "))
for i in range (1, n+1):
    print("*"*i, end ="")
    print("")

'''
Write a program to print the following star pattern. 
* * * 
*   *   for n = 3 
* * *  '''
n = int(input("Enter the number: "))
for i in range (1, n+1):
    if(i==1 or i==n):
        print("*"*n, end = "")
    else:
        print("*", end="")
        print(" "*(n-2), end = "")
        print("*", end="")
    print("")


# Write a program to print multiplication table of n using for loops in reversed order.
n = int(input("Enter the number: "))
for i in range (1, 11):
    print(f"{n} x {11-i} = {n*(11-i)}")
    