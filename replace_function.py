#Write a program to fill in a letter template given below with name and date. 
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
print(letter.replace("<|Name|>", "Anjali").replace("<|Date|>", "1 january 2025" ))





#Write a program to detect double space in a string.
Name = "Anjali is a good   girl"
print(Name.find("  "))

# Replace the double space with single space
print(Name.replace("  ", "" ))

# Write a program to format the following letter using escape sequence characters. 
letter = "Dear Sir, \nthis python course is nice. \nThanks!"

print(letter)

