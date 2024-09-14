# ***********************************************************************************************
#                                                                                               *
#                   Hands On Simulation Modeling with Python - Chapter 2                        *
#                                                                                               *
#       This code defines a class TitleEncryptor for encrypting and decrypting text using       *
#       the Fernet symmetric encryption method from the cryptography library.                   *
#       The TitleEncryptor class has methods for encrypting (encrypt_title) and decrypting      *
#       (decrypt_title) text. In the main() function, an instance of TitleEncryptor is          *
#       created to encrypt a book title, then decrypt it to verify that the original text       *
#       can be recovered. The results, including the original, encrypted, and decrypted         *
#       titles, are displayed in a neatly formatted table using the tabulate library            *
#       with the "fancy_grid" style.                                                            *
#                                                                                               *
# ***********************************************************************************************


from cryptography.fernet import Fernet
from tabulate import tabulate


class TitleEncryptor:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_title(self, plain_text):
        return self.cipher.encrypt(plain_text.encode())

    def decrypt_title(self, encrypted_text):
        return self.cipher.decrypt(encrypted_text).decode()

def main():
    original_title = "Simulation Modeling with Python"
    encryptor = TitleEncryptor()
    encrypted_title = encryptor.encrypt_title(original_title)
    decrypted_title = encryptor.decrypt_title(encrypted_title)
    # Prepare data for tabulate
    table_data = [
        ["Original Book Title", original_title],
        ["Encrypted Title", encrypted_title],
        ["Decrypted Title", decrypted_title]
    ]
    # Print table with fancy_grid format
    print("\n\n")
    print(tabulate(table_data, headers=["Description", "Value"], tablefmt="fancy_grid"))
    print("\n\n")


if __name__ == "__main__":
    main()
