from tkinter import *
import tkinter as tk
import mysql.connector                                          #mysql connector library
import tkinter.messagebox as msg


root = tk.Tk()                                                                             # it will open blank page

root.geometry("600x600")                                                    # size of web page
root.title("Product Management App")
root.resizable(width=False,height=False)                            # it will remove Maximise symbol from web page 


# Label and place
l_email=Label(root,text="Email", font=("Sans-serif 15"))
l_email.place(x = 30, y=50)

l_pwd = Label(root, text="Password",font=("Sans-serif 15"))
l_pwd.place(x = 30, y = 100)


#Entry box 
e_email = Entry(root, bd=2,width=30, font=("Sans-serif 15"))
e_email.place(x = 150, y=50)

e_pwd = Entry(root, bd=2,width=30, font=("Sans-serif 15"))
e_pwd.place(x = 150, y=100)

#Button
login=Button(root,text="LOGIN",font=("Sans-serif 15"),fg="black",bg="orange", width=10)
login.place(x=200,y=150)

root.mainloop()

