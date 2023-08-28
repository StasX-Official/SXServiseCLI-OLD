import string
import random

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def command_generate_password():
    password_length = int(input("Enter the length of the password: "))
    password = generate_random_password(password_length)
    print("Generated password:", password)
