import customtkinter
import tkinter 
from backend import *
from expense import Expense
import datetime
from tkcalendar import Calendar

myFont=("sans-seriff", 16)

current_time = datetime.datetime.now()

categories = ["Rent", "Utilities/Insurance", "Food", "Self-Care", "Dining Out",
              "Transportation", "Medicine", "Vacation", "Debt", 
              "Cleaning" ,"Entertainment", "Clothes", "Dog Needs", 
              "Dog Needs", "Dog Wants", "Misc"]

data = Database(db="expenses.db")

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
            if(expenseCost.get().isnumeric() == False or expenseCost.get() == ""):
                costEntry.configure(border_color = "red")
            elif(expenseName.get() == ""):
                nameEntry.configure(border_color = "red")
            elif(categoryMenu.get() == ""):
                categoryMenu.configure(border_color = "red")
            elif(expenseDate.get() == ""):
                dateButton.configure(border_color = "red")
            else:
                costEntry.configure(border_color = "gray")
                nameEntry.configure(border_color = "gray")
                categoryMenu.configure(border_color = "gray")
                dateButton.configure(border_color = "gray")
                newExpense = Expense(expenseName.get(), expenseCost.get(), categoryMenu.get(), expenseDate.get())
                data.insertExpense(newExpense)

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
        categoryMenu = customtkinter.CTkOptionMenu(master = root, font=myFont, values = categories)
        categoryMenu.grid(row = 2, column = 1)

        # Draw expense date label to screen
        dateLabel = customtkinter.CTkLabel(master = root, font=myFont, text= "Enter expense date")
        dateLabel.grid(row = 3, column = 0)

        def showCalendar():
            calendarWindow = tkinter.Toplevel(root)
            cal = Calendar(master = calendarWindow, selectmode = 'day', year = current_time.year)
            cal.grid(row= 1, column = 1, sticky="nswe")

            def saveDate():
                calendarWindow.destroy()
                dateButton.configure(text = cal.get_date())
                expenseDate.set(cal.get_date())
            selectButton = customtkinter.CTkButton(calendarWindow, text = "Select Date", command = saveDate)
            selectButton.grid(row = 2, column =1)
            
        # Draw expense date entry to screen
        expenseDate = customtkinter.StringVar()
        expenseDate.set(current_time.now().strftime("%m/%d/%Y"))
        dateButton = customtkinter.CTkButton(master = root, font=myFont, textvariable= expenseDate, command=showCalendar)
        dateButton.grid(row = 3, column = 1)

        # Enter Button
        button = customtkinter.CTkButton(master= root, font=myFont, text="Enter", command=validate_input)
        button.grid(row = 3, column = 2)

        


if __name__=='__main__':
    root = customtkinter.CTk()
    application = AppUI(root)
    root.mainloop()