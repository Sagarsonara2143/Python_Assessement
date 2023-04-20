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


l = Label(root,text="Products",font=("Sans-serif",25),fg="red", width=32,bg="black")
l.place(x=0 ,y=10)

#Label for products
l_sku = Label(root,text="SKU Code",font=("Sans-serif",15),fg="blue").place(x = 30, y=100)
l_desc = Label(root,text="Description",font=("Sans-serif",15),fg="blue").place(x = 30, y=150)
l_size = Label(root,text="Size",font=("Sans-serif",15),fg="blue").place(x = 30, y=200)
l_color = Label(root,text="Color",font=("Sans-serif",15),fg="blue").place(x = 30, y=250)
l_price = Label(root,text="Price",font=("Sans-serif",15),fg="blue").place(x = 30, y=300)

#Buttons


