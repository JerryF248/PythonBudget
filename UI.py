import customtkinter
import tkinter 
from backend import *
from expense import Expense

myFont=("sans-seriff", 16)

class AppUI():
    def __init__(self, root):

        # Create screen
        self.root = root
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.root._state_before_windows_set_titlebar_color = 'zoomed'
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
        self.root.title("Python Budget Application")

        # Get expense from user
        self.getUserExpense()


        # Get expense from user input
    def getUserExpense(self):

        # Validate input from user
        def validate_input():
            if(expenseName.get().isnumeric()):
                nameEntry.configure(border_color = "gray")
                print(expenseName.get())
            else:
                nameEntry.configure(border_color = "red")
                print("not number")
                print(expenseName.get())

        # Draw expense name label to screen
        nameLabel = customtkinter.CTkLabel(master = root, font=myFont, text= "Enter expense name")
        nameLabel.grid(row = 0, column = 0)

        # Draw expense name entry to screen
        expenseName = customtkinter.StringVar()
        nameEntry = customtkinter.CTkEntry(master = root, font=myFont, textvariable= expenseName)
        nameEntry.grid(row = 0, column = 1)

        # Draw expense cost label to screen
        costLabel = customtkinter.CTkLabel(master = root, font=myFont, text= "Enter expense cost")
        costLabel.grid(row = 1, column = 0)

        # Draw expense cost entry to screen
        expenseCost = customtkinter.StringVar()
        costEntry = customtkinter.CTkEntry(master = root, font=myFont, textvariable= expenseCost)
        costEntry.grid(row = 1, column = 1)

        # Draw expense category label to screen
        categoryLabel = customtkinter.CTkLabel(master = root, font=myFont, text= "Choose expense category")
        categoryLabel.grid(row = 2, column = 0)

        # Draw expense category entry to screen
        expenseCategory = customtkinter.StringVar()
        categoryEntry = customtkinter.CTkEntry(master = root, font=myFont, textvariable= expenseCategory)
        categoryEntry.grid(row = 2, column = 1)

        # Draw expense date label to screen
        dateLabel = customtkinter.CTkLabel(master = root, font=myFont, text= "Enter expense date")
        dateLabel.grid(row = 3, column = 0)

        # Draw expense date entry to screen
        expenseDate = customtkinter.StringVar()
        dateEntry = customtkinter.CTkEntry(master = root, font=myFont, textvariable= expenseDate)
        dateEntry.grid(row = 3, column = 1)

        # Enter Button
        button = customtkinter.CTkButton(master= root, font=myFont, text="Enter", command=validate_input)
        button.grid(row = 3, column = 2)

        


if __name__=='__main__':
    root = customtkinter.CTk()
    application = AppUI(root)
    root.mainloop()