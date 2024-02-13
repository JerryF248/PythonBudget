import customtkinter
import tkinter 

class AppUI():
    def __init__(self, root):
        self.root = root
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.root._state_before_windows_set_titlebar_color = 'zoomed'
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        self.root.title("Python Budget Application")

        def validate_input():
            if(typeVar.get().isnumeric()):
                print("number")
            else:
                typeVar.set("")
                typeEntry.configure(border_color = "red")
                print("not number")
                print(typeVar.get())


        # Types Label Box
        typeLabel = customtkinter.CTkLabel(master = self.root, font=("sans-seriff", 16), text= "Enter expense name")
        typeLabel.grid(row = 0, column = 0)

        # Class Entry Box
        typeVar = customtkinter.StringVar()
        typeEntry = customtkinter.CTkEntry(master = self.root, font=("sans-seriff", 16), textvariable= typeVar)
        typeEntry.grid(row = 0, column = 1)

        # Enter Button
        button = customtkinter.CTkButton(master=self.root, text="Enter", command=validate_input)
        button.grid(row = 0, column = 2)


if __name__=='__main__':
    root = customtkinter.CTk()
    application = AppUI(root)
    root.mainloop()