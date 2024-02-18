import random
import string

def generate_password(length):
    # Define character sets for different complexity levels
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets based on complexity
    all_chars = lowercase + uppercase + digits + special_chars

    # Generate password using random.choices
    password = ''.join(random.choices(all_chars, k=length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer for the password length.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
