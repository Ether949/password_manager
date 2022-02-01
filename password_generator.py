from tkinter import *
from tkinter import messagebox
import random

#-------Generate password-------#
char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "&", "*"]

def gen_password():
    pass_entry.delete(0, 100)
    for x in range(12):
        letter = random.choice(char_list)
        chance = random.randint(0, 4)
        if chance == 1:
            letter = letter.upper()
        pass_entry.insert(0, letter)


#-------Write to file-------#

def append_file():
    if len(email_entry.get()) == 0 or len(pass_entry.get()) == 0 or len(web_entry.get()) == 0:
        messagebox.showerror(title="Empty fields found", message="Please don't leave any fields empty.")
    else:
        shld_cont = messagebox.askokcancel(title="Continue?", message=f"Please double check your fields. \nWebsite: {web_entry.get()} \nEmail: {email_entry.get()} \nPassword: {pass_entry.get()}")
        if shld_cont:
            f = open("data.txt", "a")
            f.write(f"{web_entry.get()} | {email_entry.get()} | {pass_entry.get()}\n")
            f.close()
            web_entry.delete(0, 100)
            email_entry.delete(0, 100)
            pass_entry.delete(0, 100)


#----------User Interface---------#
#Window
window = Tk()
window.title("E's password manager")
window.config(padx=20, pady=20, bg="white", highlightthickness=0)

#Image
canv = Canvas(height=200, width=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="lock_key.png")
logo = lock_image.subsample(5, 5)
canv.create_image(100, 100, image=logo)
canv.grid(column=1, row =0)

#Labels
web_label = Label(text="Website:", padx=5, pady=5, bg="white", fg="black")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg="white", fg="black")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white", fg="black")
password_label.grid(column=0, row=3)

#Entries
web_entry = Entry(width=35, bg="white", fg="black", highlightthickness=0, insertbackground="black")
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=35, fg="black", bg="white", highlightthickness=0, insertbackground="black")
email_entry.grid(column=1, row=2, columnspan=2)

pass_entry = Entry(width=18, bg="white", fg="black", highlightthickness=0, insertbackground="black")
pass_entry.grid(column=1, row=3)

#Buttons
pass_button = Button(text="Generate password", highlightbackground="white", command=gen_password)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, highlightbackground="white", command=append_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
