from tkinter import *
top = Tk()
top.title("Fuckin' Bank")
top.geometry("500x600")
appTitle = Label(top, text = "Employee Login",  font=("Arial", 25))
appTitle.pack()
username_label = Label(top, text = "Username")
username_label.pack()
username = StringVar()
username_entry = Entry(top, textvariable=username)
username_entry.pack()
top.mainloop()
