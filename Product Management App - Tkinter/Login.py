from tkinter import *
import tkinter as tk
import mysql.connector                                          #mysql connector library
import tkinter.messagebox as msg
from PIL import ImageTk, Image


def register_page():
    root.destroy()
    import Registration
    

root = tk.Tk()                                                                             # it will open blank page

root.geometry("600x600")                                                    # size of web page
root.title("Product Management App")
root.resizable(width=False,height=False)                            # it will remove Maximise symbol from web page 
#root.config(bg="white")


l_lable=Label(root,text="Product Management Application", font=("Sans-serif ",20),fg="red",bg="yellow").place(x =70, y=20)

# Label and place
l_email=Label(root,text="Email", font=("Sans-serif 15"))
l_email.place(x = 30, y=100)

l_pwd = Label(root, text="Password",font=("Sans-serif 15"))
l_pwd.place(x = 30, y = 150)

l_text=Label(root, text="Need an account ?",font=("Sans-serif ",12)).place(x=350, y=200)
l_reg =Button(root, text="Sign up",font=("Sans-serif 14 underline"),fg="blue",command = register_page, bd=0)
l_reg.place(x=350, y=220)

#Entry box 
e_email = Entry(root, bd=2,width=30, font=("Sans-serif 15"))
e_email.place(x = 150, y=100)

e_pwd = Entry(root, bd=2,width=30, font=("Sans-serif 15"))
e_pwd.place(x = 150, y=150)

#Button
login=Button(root,text="LOGIN",font=("Sans-serif 15"),fg="black",bg="orange", width=10)
login.place(x=200,y=250)

root.mainloop()

