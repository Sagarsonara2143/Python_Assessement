from tkinter import *
import tkinter as tk
import mysql.connector                                          #mysql connector library
import tkinter.messagebox as msg
from PIL import ImageTk, Image

#Connect to database
def create_con():
    return mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "python"
        )
root = tk.Tk()                                                                            

root.geometry("600x600")                                                   
root.title("Product Management App")
root.resizable(width=False,height=False)                            
#root.config(bg="white")                                                       


l_lable=Label(root,text="Product Management Page", font=("Sans-serif",20,"bold"),fg="red",bg="black", width=36).place(x =0, y=20)


login=Button(root,text="ADD",font=("Sans-serif 15","bold"),fg="Blue",bg="white", width=10).place(x=200,y=250)

root.mainloop()

