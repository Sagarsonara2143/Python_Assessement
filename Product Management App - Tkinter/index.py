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


l = Label(root,text="Products",font=("Sans-serif",25),fg="red", width=30,bg="black")
l.place(x=15 ,y=10)
