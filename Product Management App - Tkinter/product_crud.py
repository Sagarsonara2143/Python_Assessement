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

def add_product():
    l_msg=Label(root,text="All Fields are Mandatory",font=("Sans-serif",15,"bold"),fg="red")
    if e_sku.get()=="" or e_desc.get()=="" or e_size.get()=="" or e_color.get()=="" or e_price.get()=="" or e_qty.get()=="":
        #l_msg.place(x=180,y=68)
        msg.showinfo("Product Status","All fields are Manadotary")
    else:
        #l_msg.after(1000,l_msg.destroy())
        msg.showinfo("msg","Successfully")
        



root = tk.Tk()                                                                             

root.geometry("600x600")                                                        
root.title("Product Management App")
root.resizable(width=False,height=False) 


l = Label(root,text="Products",font=("Sans-serif",25),fg="red", width=32,bg="black")
l.place(x=0 ,y=10)

#Label for products
l_sku = Label(root,text="SKU Code",font=("Sans-serif",15,"bold"),fg="blue").place(x = 30, y=100)
l_desc   = Label(root,text="Description",font=("Sans-serif",15,"bold"),fg="blue").place(x = 30, y=150)
l_size = Label(root,text="Size",font=("Sans-serif",15,"bold"),fg="blue").place(x = 30, y=200)
l_color = Label(root,text="Color",font=("Sans-serif",15,"bold"),fg="blue").place(x = 30, y=250)
l_price = Label(root,text="Price",font=("Sans-serif",15,"bold"),fg="blue").place(x = 30, y=300)
l_qty = Label(root,text="Quantity",font=("Sans-serif",15,"bold"),fg="blue").place(x = 30, y=350)

#Textbox 
e_sku = Entry(root,bd=4, width=30,font=("Sans-serif",15))
e_sku.place(x=170, y=100)
e_desc = Entry(root,bd=2, width=30,font=("Sans-serif",15))
e_desc.place(x=170, y=150)
e_size = Entry(root,bd=2, width=30,font=("Sans-serif",15))
e_size.place(x=170, y=200)
e_color = Entry(root,bd=2, width=30,font=("Sans-serif",15))
e_color.place(x=170, y=250)
e_price = Entry(root,bd=2, width=30,font=("Sans-serif",15))
e_price.place(x=170, y=300)
e_qty = Entry(root,bd=2, width=30,font=("Sans-serif",15))
e_qty.place(x=170, y=350)

#Add Button
add=Button(root,text="ADD",font=("Sans-serif 15"),fg="black",bg="orange", width=15, bd=6, command=add_product).place(x=100,y=400)

search=Button(root,text="SEARCH",font=("Sans-serif 15"),fg="black",bg="orange", width=15, bd=6).place(x=300,y=400)

update=Button(root,text="UPDATE",font=("Sans-serif 15"),fg="black",bg="orange", width=15, bd=6).place(x=100,y=450)

delete=Button(root,text="DELETE",font=("Sans-serif 15"),fg="black",bg="orange", width=15, bd=6).place(x=300,y=450)

#stock=Button(root,text="Stock",font=("Sans-serif 15"),fg="black",bg="orange", width=20, bd=6).place(x=200,y=500)


root.mainloop()


