
"""
    We declare here, every variables that import from another files.
    We do this to we have a better organization in the structure that create our json.
    So in the future we will always add the new imports here.
    The folder where to save new arrays for extract random information it's called 'randomData'
"""

from tkinter import messagebox

"""
    We declare here a functions that generate random numbers like account bank, isss number, 
    dui number among other important fields that the employee needs
"""

def success_message():
    messagebox.showinfo("Successful query", "¡Insertions completed successfully!")

def error_message(error):
    print(f"Database connection error: {str(error)}")
