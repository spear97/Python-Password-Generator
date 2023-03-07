from tkinter import messagebox
from tkinter import *
import tkinter as tk

from Generator import *

class GUI(object):
    
    def __init__(self):

        #Create and Initialize Generator
        self.gen = Generator()

        # Create a window
        self.window = tk.Tk()

        # Set the window title
        self.window.title("Password Generator App")

        self.window.geometry('500x500')

        # Create a label for the name field
        self.name_label = tk.Label(self.window, text="Password Length:")
        self.name_label.pack()

        # Create an entry field for the user to enter their name
        self.user_entry = tk.Entry(self.window)
        self.user_entry.pack()

        # Create a label for the name field
        self.advistory_label = tk.Label(self.window, text="Passwords must be between 8 to 16 characters long!")
        self.advistory_label.pack()

        # Create a button to Generate Password
        self.Gen_button = tk.Button(self.window, text="Convert!", command=self.Gen_Pass)
        self.Gen_button.pack()

        # Create a label for the name field
        self.result_label = tk.Label(self.window, text="Result:")
        self.result_label.pack()

        # Create an entry field for the user to enter their name
        self.pass_result = tk.Entry(self.window)
        self.pass_result.pack()

        #Run Application
        self.window.mainloop()

    def Gen_Pass(self):

        #Attempt to Generate a Password
        try:

            #Convert the User Input from Type String to Type Integer
            x = int(self.user_entry.get())

            #Ensure that the Input is not less than 8 characters in length
            if x < 8:
                messagebox.showerror(title='ERROR!', message='Please Enter a minimum of 8 characters!')

            #Ensure that the Input is not greater than 16 characters in length
            elif x > 16:
                messagebox.showerror(title='ERROR!', message='Password Cannot Exceed a Maximum of 16 characters!')

            #Generate a Password for the User
            else:
                new_pass = self.gen.GeneratePassword(x)
                self.pass_result.delete(0, END)
                self.pass_result.insert(0,new_pass)

        #Ensure that all Inputs are inputs that can be easily converted from String to Integer
        except ValueError:
            messagebox.showerror(title='ERROR!', message='You Entered an Invalid Input! Please Enter an integer input!')




