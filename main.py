import random
import PasswordChecker
import tkinter

def generatePassword():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"
    
    while True:
        try:
            amountOfPasswords = int(input("How many passwords would you like to generate?: "))
            break
        except:
                print("Please insert a value of atleast 1.")
        
    while True:
        try:
            lengthOfPassword = int(input("Please insert your password length: "))
            break
        except:
            print("Please insert a value of atleast 1.")


    passwordList = []
    for password in range(amountOfPasswords):
        passwords = ""
        for character in range(lengthOfPassword):
            passwords += random.choice(characters)
        passwordList.append(passwords)
    return passwordList


def main():
    generatedPasswords = generatePassword()
    PasswordChecker.checkPassword(generatedPasswords)

    # Implement the possibilty to save passwords on a text file
    


main()