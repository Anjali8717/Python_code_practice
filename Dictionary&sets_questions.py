#Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! 

Words = {
    "Tum" : "you",
    "kursi" : "chair",
    "darwaja" : "Gate"
}

Word = input("Enter the word you want meaning of :")
print(Words[Word])


# Write a program to input eight numbers from the user and display all the unique numbers (once). 

s = set()
n = input("Enter number :")
s.add(n)
n = input("Enter number :")
s.add(n)
n = input("Enter number :")
s.add(n)
n = input("Enter number :")
s.add(n)
n = input("Enter number :")
s.add(n)
n = input("Enter number :")
s.add(n)
n = input("Enter number :")
s.add(n)
n = input("Enter number :")
s.add(n)

print(s)

 #Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 

d = {}

name = input("Enter friends name :")
language = input("Enter language name :")
d.update({name : language})

name = input("Enter friends name :")
language = input("Enter language name :")
d.update({name : language})

name = input("Enter friends name  :")
language = input("Enter language name :")
d.update({name : language})

name = input("Enter friends name :")
language = input("Enter language name :")
d.update({name : language})

print(d) 



