from tkinter import *
import math
import random
import tkinter.messagebox

root = Tk()
root.geometry("500x500")
root.title("Number Guesser")

number = random.randint(1,10)

def too_low():
    tkinter.messagebox.showinfo("messagebox", "Your geuss is too low. Try again")

def too_high():
    tkinter.messagebox.showinfo("messagebox", "Your geuss is too high. Try again")

def check_number():
    geuss = enter_geuss.get()
    geuss = int(geuss)
    if geuss < number:
        too_low()
    if geuss > number:
        too_high()
    if geuss == number:
        tkinter.messagebox.showinfo("Good Job!", "You geussed it right!")

def name_confirm():
    playername = enter_name.get()
    playername = str(playername)
    tkinter.messagebox.showinfo("Welcome","Well, " + playername + ",I am thinking of a number from 1 to 10.")

label = Label(root, text = "Welcome player. Let's get started!")
label.pack()

label_name = tkinter.Label(root, text="Enter your name player:")
label_name.place(x= 500, y=50)

enter_name = Entry(root,width = 20)
enter_name.place(x=650, y=50)

button = Button(root, text = "Confirm", command = name_confirm)
button.place(x=800,y=50)

label_geuss = Label(root,text = "Take a geuss player")
label_geuss.place(x=500,y=100)

enter_geuss = Entry(root,width = 20)
enter_geuss.place(x=650, y=100)

button_geuss = Button(root, text = "Confirm", command=check_number)
button_geuss.place(x=800,y=100)

root.mainloop()
