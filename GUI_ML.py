from tkinter import *
from tkinter.filedialog import askopenfilename
import csv
import os
from tkinter import ttk

gui = Tk()

gui.title('Machine Learning GUI')

class GUI(Frame):
    
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid()

        self.fnameLabel = Label(master, text="First Name")
        self.fnameLabel.grid()

        self.fnameEntry = Entry(master)
        self.fnameEntry.grid()

        self.lnameLabel = Label(master, text="Last Name")
        self.lnameLabel.grid()

        self.lnameEntry = Entry(master)
        self.lnameEntry.grid()

        self.submitButton = Button(master, command=self.buttonClick, text="Submit")
        self.submitButton.grid()


    def buttonClick(self):
    """ handle button click event and output text from entry area"""
    print('hello')    # Trigger action tommorow cause it's 2:30



if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()