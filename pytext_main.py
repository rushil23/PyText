import Tkinter
from Tkinter import *
import ScrolledText # because Tkinter does not support scrolling
import tkFileDialog
import tkMessageBox

root = Tkinter.Tk(className = "PyText - Text Editor")

textPad = ScrolledText.ScrolledText(root, width=100, height=80)

def open():
    # Open a file and display data

def save(self):
    # Save file


def exit():
    # Exit Program

    if tkMessageBox.askcancel("Quit","Do you want to quit?"):
        root.destroy() # Destroys the text editor

def about():
    # Display information

    label = tkMessageBox.showinfo("About","PyText is a Python-based text editor. \nCreated by Rushil Nagarsheth (github.com/rushil23")

# Creating the Menu dialogs

menu=Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label="File",menu=filemenu)
    

textPad.pack()
root.mainloop()
