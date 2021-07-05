import random
from tkinter.constants import BOTH, BOTTOM, DISABLED, END, INSERT, LEFT, NORMAL, RIDGE, RIGHT, TOP, X, Y
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
    textView = tkinter.Text(GUI_Window, bg="DarkSlategray")
    textView.config(state=DISABLED)
    textView.pack()


    def generateButton():
        generatedPasswords = generatePassword()
        PasswordChecker.checkPassword(generatedPasswords)

        # Clears previous text and shows passwords in textView
        textView.config(state=NORMAL)

        textView.delete(1.0, END)
        pwdID = 0
        for each in generatedPasswords:
            pwdID += 1
            textView.insert(INSERT,f"{str(pwdID)}: {str(each)}\n")
        
        textView.config(state=DISABLED)
    generateButton = tkinter.Button(GUI_Window, text="Generate!", command=generateButton, bg="darkred")
    generateButton.pack(side=RIGHT, ipadx=100, ipady=30, padx=20) 
    
    # SAVES TXT FILE
    def savePasswords():

        if textView.compare("end-1c", "==", "1.0"):
            return
        else:
            textView.config(state=NORMAL)

            saveFile = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
            if saveFile == None:
                return
            saveFile.write(textView.get(1.0, END))
            saveFile.close()

        textView.config(state=DISABLED)
    saveButton = tkinter.Button(GUI_Window, text="Save! (.txt)", command=savePasswords, bg="DarkSlateGrey")
    saveButton.pack(side=RIGHT, ipady=30, ipadx=30, padx=15)


     # PASSWORD AMOUNT ENTRY UI
    amountOfPasswordsLabel = tkinter.Label(text="AMOUNT OF PASSWORDS: ")
    amountOfPasswordsLabel.pack(side=LEFT, padx=10)
    amountOfPasswords = tkinter.StringVar()
    amountOfPasswordsEntry = tkinter.Entry(GUI_Window, textvariable=amountOfPasswords, bg="DarkSlategray")
    amountOfPasswordsEntry.pack(side=LEFT)

    # PASSWORD LENGTH ENTRY UI
    passwordLengthLabel = tkinter.Label(text="LENGTH: ")
    passwordLengthLabel.pack(side=LEFT)
    passwordLength = tkinter.StringVar()
    passwordLengthEntry = tkinter.Entry(GUI_Window, textvariable=passwordLength, bg="DarkSlategray")
    passwordLengthEntry.pack(side=LEFT, padx=10)

        
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