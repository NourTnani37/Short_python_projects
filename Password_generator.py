# This project is to generate a random password with user inputs

import random
import string 

def pwd_generator(min_length, numbers = True, special= True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters 
    if numbers:
        characters += digits
    
    if special:
        characters += special 

    pwd = ""

    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length: 

        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits: 
            has_numbers = True

        if new_char in special:
            has_special = True
        
        meets_criteria = True
        
        if numbers:
            meets_criteria = has_numbers
        
        if special:
            meets_criteria = meets_criteria and has_special


    return pwd

min_length = int(input("Type the minimal length you want for your password:"))
has_numbers = input("Do you want your password to contain numbers (y/n) ?:").lower == "y"
has_special = input("Do you want your password to contain special characters (y/n) ?:").lower == "y"
   
pwd = pwd_generator(min_length, has_numbers, has_special)
print("The generated password is: ", pwd)