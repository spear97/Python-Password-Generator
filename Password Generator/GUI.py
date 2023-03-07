import tkinter as tk
#from Converter import *

class GUI(object):
    
    def __init__(self):

        # Create a window
        self.window = tk.Tk()

        # Set the window title
        self.window.title("Roman Numeral Conversion App")

        self.window.geometry('500x500')

        # Create a label for the name field
        self.name_label = tk.Label(self.window, text="Click the Button to Generate a Password:")
        self.name_label.pack()

        # Create an entry field for the user to enter their name
        #self.user_entry = tk.Entry(self.window)
        #self.user_entry.pack()

        # Create a button to trigger the welcome message
        self.greet_button = tk.Button(self.window, text="Convert!", command=self.Convert_Value)
        self.greet_button.pack()

        # Create a label to display the welcome message
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        #Run Application
        self.window.mainloop()

    def Convert_Value(self):
        self.result_label.config(text='Invalid Input Entered! Please Input a Valid Input!')
            





