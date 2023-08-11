from tkinter import *
import random

window = Tk()
window.config(padx=100, pady=100)

canv = Canvas(height=200, width=189)
img = PhotoImage(file="logo.png")
canv.create_image(100, 91 , image=img)
canv.grid(row=0, column=1)

def generatePassword():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
               "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    choices = [letters, special, numbers]
    password = ""

    for i in range(0, 10):
        rand = random.randint(0, 2)
        choice = str(choices[rand][random.randint(0, len(choices[rand])-1)])
        password += choice

    passwordEntry.delete(0, END)
    passwordEntry.insert(0, password)


def insertInformation():
    webInf = str(webEntry.get())
    nameInf = str(emailOrUsernameEntry.get())
    passwordInf = str(passwordEntry.get())

    print(webInf)
    with open("data.txt", "a") as data:
        data.write(f"{webInf} | {nameInf} | {passwordInf} \n")
        webEntry.delete(0, END)
        emailOrUsernameEntry.delete(0, END)
        passwordEntry.delete(0, END)


web = Label(text="Website:", font=("Ariel", 10, "bold"))
webEntry = Entry(width=35)

emailOrUsername = Label(text="Email/Username:", font=("Ariel", 10, "bold"))
emailOrUsernameEntry = Entry(width=35)

password = Label(text="Password:", font=("Ariel", 10, "bold"))
passwordEntry = Entry(width=21)

generateBtn = Button(text="Generate Password", width=12, command=generatePassword)
addBtn = Button(text="Add", width=35, command=insertInformation)

emailOrUsernameEntry.insert(0, "@gmail.com")
webEntry.insert(0, ".com")


web.grid(row=1, column=0)
emailOrUsername.grid(row=2, column=0)
password.grid(row=3, column=0)

webEntry.grid(row=1, column=1, columnspan=2)
emailOrUsernameEntry.grid(row=2, column=1, columnspan=2)
passwordEntry.grid(row=3, column=1, columnspan=2, sticky="w")
generateBtn.grid(row=3, column=2, sticky="w")
addBtn.grid(row=4, column=1, columnspan=2)

window.mainloop()


