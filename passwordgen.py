import random
import string

def generate_password(length=12):
    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random module to generate a password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    # Get user input for password length
    try:
        password_length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid integer for the password length.")
        return

    # Generate and display the password
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
