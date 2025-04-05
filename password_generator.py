
# I made a small Python program that creates strong passwords. The user
# -enters a number, and the program gives a password using random letters, numbers, and symbols!
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for the password length
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
