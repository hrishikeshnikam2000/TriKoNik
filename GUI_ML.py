from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
import csv
import os
from tkinter import ttk

gui = Tk()
gui.geometry("300x300")
gui.title('Machine Learning GUI')

class GUI(Frame):
    
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid()

        self.fnameLabel = Label(master, text="Enter Message as Recieved")
        self.fnameLabel.grid()

        self.fnameEntry = Entry(master)
        self.fnameEntry.grid()

        self.submitButton = Button(master, command=self.buttonClick, text="Submit")
        self.submitButton.grid()

    def buttonClick(self,master=None):
        print('hello')



if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()