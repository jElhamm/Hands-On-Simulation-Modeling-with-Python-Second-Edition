# *******************************************************************************************************
#                                                                                                       *
#                   Hands On Simulation Modeling with Python - Chapter 2                                *
#                                                                                                       *
#       This code defines a class PasswordGenerator for generating secure, random passwords.            *
#       The PasswordGenerator class includes a method generate_password that creates a password         *
#       of a specified length using a character set consisting of letters, digits, and special          *
#       characters. The method ensures randomness by shuffling the character set and the final          *
#       password. The main() function prompts the user to input the desired password length,            *
#       generates a password of that length, and displays it. Users can choose to generate              *
#       another password or exit the program. Error handling is included to ensure the password         *
#       length is valid.                                                                                *
#                                                                                                       *
# *******************************************************************************************************


import string
import random


class PasswordGenerator:
    def __init__(self):
        self.char_set = list(string.ascii_letters + string.digits + "()!$%^&*@#")           # Character set for password generation

    def generate_password(self, length):
        """Generate a random password of a given length."""
        if length < 1:
            raise ValueError("Password length must be at least 1.")

        random.shuffle(self.char_set)                                                       # Shuffle the character set to ensure randomness
        password = [random.choice(self.char_set) for _ in range(length)]                    # Generate the password
        random.shuffle(password)                                                            # Shuffle the password to ensure random distribution
        return "".join(password)

def main():
    generator = PasswordGenerator()
    print("\n\n", "*"*85)
    print("\n                     (:   Welcome to the Password Generator   :)  \n")
    print("*"*85)
    while True:
        try:
            length = int(input("\n\n---> How long should your password be? (Minimum length is 1): "))
            if length < 1:
                print("\n----> Length must be at least 1. Please try again.\n")
                continue
            
            password = generator.generate_password(length)
            print(f"\n----> Generated Password: {password}\n")
            another = input("----> Would you like to generate another password? (yes/no): ").strip().lower()
            if another not in ['yes', 'y']:
                print("\n\n", "*"*85)
                print("\n                   Thank you for using the Password Generator \n")
                print("*"*85 , "\n\n")
                break
        
        except ValueError as e:
            print(f"\n Error: {e}\n")


if __name__ == "__main__":
    main()
