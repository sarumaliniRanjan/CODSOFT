import random
import string

def generate_password(length):
    # Define possible characters (letters, digits, and punctuation)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password by randomly selecting characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Prompt the user to specify the desired password length
length = int(input("Enter the desired password length: "))

# Generate and display the password
generated_password = generate_password(length)
print(f"Generated password: {generated_password}")