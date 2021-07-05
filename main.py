import random
from tkinter.constants import BOTTOM, END, INSERT, LEFT, RIGHT, TOP
import PasswordChecker
import tkinter
from tkinter import filedialog


def main():

    # TKINTER BASE
    GUI_Window = tkinter.Tk()
    GUI_Window.tk_setPalette("black")
    GUI_Window.geometry("900x600")
    GUI_Window.resizable(False, False)
    GUI_Window.title("Secure Password Generator!")

    heading = tkinter.Label(GUI_Window, text="SPG! made by Christian", font=("Helvetica", 14))
    heading.pack(ipadx=10, ipady=10)


    # TEXTVIEW UI
    textView = tkinter.Text(GUI_Window)
    textView.pack()


    # PASSWORD AMOUNT ENTRY UI
    amountOfPasswordsLabel = tkinter.Label(text="AMOUNT OF PASSWORDS: ")
    amountOfPasswordsLabel.pack(ipadx=10, ipady=10, side=LEFT)
    amountOfPasswords = tkinter.StringVar()
    amountOfPasswordsEntry = tkinter.Entry(GUI_Window, textvariable=amountOfPasswords)
    amountOfPasswordsEntry.pack(ipadx=10, ipady=4, side=LEFT)


    # PASSWORD LENGTH ENTRY UI
    passwordLengthLabel = tkinter.Label(text="LENGTH OF PASSWORDS: ")
    passwordLengthLabel.pack(ipadx=10, ipady=10, side=LEFT)
    passwordLength = tkinter.StringVar()
    passwordLengthEntry = tkinter.Entry(GUI_Window, textvariable=passwordLength)
    passwordLengthEntry.pack(ipadx=10, ipady=4, side=LEFT)


    # SAVES TXT FILE
    def savePasswords():
        saveFile = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if saveFile == None:
            return
        saveFile.write(textView.get(1.0, END))
        saveFile.close()
    saveButton = tkinter.Button(GUI_Window, text="Save! (.txt)", command=savePasswords)
    saveButton.pack(ipadx=198, ipady=10, side=BOTTOM)

    def generateButton():
        generatedPasswords = generatePassword()
        PasswordChecker.checkPassword(generatedPasswords)

        # Clears previous text and shows passwords in textView
        textView.delete(1.0, END)
        pwdID = 0
        for each in generatedPasswords:
            pwdID += 1
            textView.insert(INSERT,f"{str(pwdID)}: {str(each)}\n")
    generateButton = tkinter.Button(GUI_Window, text="Generate!", command=generateButton)
    generateButton.pack(ipadx=200, ipady=10, side=BOTTOM)  
        
    # PASSWORD GENERATION
    def generatePassword():
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().?0123456789"

        passwordList = []
        for password in range(int(amountOfPasswords.get())):
            passwords = ""
            for character in range(int(passwordLength.get())):
                passwords += random.choice(characters)
            passwordList.append(passwords)
        return passwordList

    GUI_Window.mainloop()


    


main()