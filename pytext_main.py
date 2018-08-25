import Tkinter
from Tkinter import *
import ScrolledText # because Tkinter does not support scrolling
import tkFileDialog
import tkMessageBox

root = Tkinter.Tk(className = "PyText - Text Editor")

textPad = ScrolledText.ScrolledText(root, width=100, height=80)

def new():
    print " "

def open_():
    # Open a file and display data
    print " "
def save(self):
    # Save file
    print " "
        
def exit_():
    # Exit Program
    print ""
    if tkMessageBox.askcancel("Quit","Do you want to quit?"):
        root.destroy() # Destroys the text editor

def about():
    # Display information

    label = tkMessageBox.showinfo("About","PyText is a Python-based text editor. \nCreated by Rushil Nagarsheth (github.com/rushil23)")

# Creating the Menu dialogs


menu=Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="New",command=new)
filemenu.add_command(label="Open..",command=open_)
filemenu.add_command(label="Save",command=save)
filemenu.add_command(label="Exit", command=exit_)


helpmenu = Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About",command=about)
    

textPad.pack()
root.mainloop()
