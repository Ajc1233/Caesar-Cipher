import random
import sys

# A global constant defining the alphabet
LETTERS = "abcdefghijklmnopqrstuvwxyz"


def is_legal_key(key):
    """Checks the user generated key to ensure it is valid. Returns True or False"""
    # Returns true if the key is equal to the length of 26 characters and if all letters in the alphabet
    # are found within the user's key
    return len(key) == 26 and all([ch in key for ch in LETTERS])


def make_random_key():
    """Will define a random key for the user if they choose not to enter their own. Returns the key"""
    # Set the letters in the alphabet as a string.
    lst = list(LETTERS)
    # Shuffle the alphabet list into a random order
    random.shuffle(lst)
    # Set the list to a string and return that string.
    return ''.join(lst)


class SubstitutionCipher:
    """This class will hold the key used to encrypt/decrypt messages and the methods needed to allow the user to create
    their own key and encrypt/decrypt a message using the key."""

    def __init__(self, key=make_random_key()):
        self.key = key

    def get_key(self):
        return self.key

    def user_set_key(self):
        """Gets the user to input their key and key to see if it is valid."""
        new_key = input("To input a valid encryption key, you must enter each letter in the alphabet in a random order "
                        "and you can only enter each letter once. If you no longer want to change the key, enter Q.\n"
                        "Enter the key you would like to use: ")
        if new_key.lower() == "q":
            return
        # Checks the input for validity. If there is an error with the key, tell the user it was incorrect
        # and call the method again.
        if not is_legal_key(new_key.lower()):
            print("Incorrect key was inserted. Please try again.\n")
            return self.user_set_key()
        self.key = new_key.lower()

    def random_set_key(self):
        self.key = make_random_key()

    def encrypt_text(self, plaintext):
        """Takes the user message and encrypts it using the current key"""

        encrypted_message = ""
        for letter in plaintext:
            # If this letter of the message is not in the alphabet, add the character to the encrypted message as is
            if not letter.isalpha():
                encrypted_message += letter
                continue
            # Find and store the index of the lowercase letter within the alphabet
            location = LETTERS.find(letter.lower())
            # Use the location variable to get the matching index in the encryption key. If the letter from the user
            # message is lowercase, keep it how it is. If the user entered an uppercase letter, change the encrypted
            # letter to uppercase
            encrypted_message += self.key[location] if letter.islower() else self.key[location].upper()
        return encrypted_message

    def decrypt_text(self, ciphertext):
        """Takes the encrypted user message and decrypts it using the current key"""

        decrypted_message = ""
        for letter in ciphertext:
            # If this letter of the message is not in the alphabet, add the character to the decrypted message as is
            if not letter.isalpha():
                decrypted_message += letter
                continue
            # Find and store the index of the encrypted letter within the key
            location = self.key.find(letter.lower())
            # Use the location variable to get the matching index in the alphabet. If the letter from the user
            # message is lowercase, keep it how it is. If the user entered an uppercase letter, change the decrypted
            # letter to uppercase
            decrypted_message += LETTERS[location] if letter.islower() else LETTERS[location].upper()
        return decrypted_message


def change_key(cipher_obj):
    """Print the change key menu and wait for the user to make their selection"""

    # Use try-except block to catch non-numerical inputs
    try:
        change_how = int(input("""
Would you like to enter your own key or randomly generate a key?
1.Random
2.Insert key\n"""))
    except ValueError:
        print("Invalid selection. Please try again.")
        return change_key(cipher_obj)

    if change_how == 1:
        cipher_obj.random_set_key()
    elif change_how == 2:
        cipher_obj.user_set_key()


def menu_selection(user_selection, cipher_obj):
    """Use the user selection from the main function to determine which function/method to call"""

    if user_selection == 1:
        print(f"Current key: {cipher_obj.get_key()}")
    elif user_selection == 2:
        change_key(cipher_obj)
        print(f"The encryption key is now: {cipher_obj.get_key()}")
    elif user_selection == 3:
        print(f"Encrypted message: {cipher_obj.encrypt_text(input('Enter the message you would like to encrypt: '))}")
    elif user_selection == 4:
        print(f"Decrypted message: {cipher_obj.decrypt_text(input('Enter the message you would like to decrypt: '))}")
    elif user_selection == 5:
        print("Thank you for using my program!")
        sys.exit(0)
    else:
        print("Invalid selection. Please try again.")


def print_menu():
    """Print the main menu and wait for the user to make their selection. Returns their selection."""

    try:
        user_selection = int(input("""
Please select an option from the menu below:
1.Get encryption key
2.Change encryption key
3.Encrypt message
4.Decrypt message
5.Quit\n"""))
    except ValueError:
        print("Invalid selection. Please try again.")
        return print_menu()
    return user_selection


def main():
    """Creates the SubstitutionCipher object. Also calls the function to print the main menu and the function to
    enact their selection.
    """
    cipher = SubstitutionCipher()
    while True:
        user_selection = print_menu()
        menu_selection(user_selection, cipher)




if __name__ == '__main__':
    main()
