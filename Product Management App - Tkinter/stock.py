from tkinter import *
from tkinter import ttk
#import tkinter as tk
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
class View:
    def __init__(self):
        con=create_con()
        cursor=con.cursor()
        query="select * from products"
        args=()
        cursor.execute(query,args)
        data=cursor.fetchall()

        tree = ttk.Treeview(root, column=("SKU", "Description", "Size","Color","Price"), show='headings', height=40)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="SKU")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Description")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Size")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Color")
        tree.heading("# 4", text="Price")
        
        for i in data:
            tree.insert('', 'end', text="1", values=(i))
            tree.pack()
        con.close()


root = Tk()                                                                            


root.geometry("1100x600")                                                   
root.title("Product Management App")
#root.resizable(width=False,height=False)                            
#root.config(bg="white")                                                       


#l_lable=Label(root,text="Product Management Page", font=("Sans-serif",20,"bold"),fg="red",bg="black", width=36).place(x =0, y=20)

#l_lable=Label(root,text="Stock", font=("Sans-serif",20,"bold"),fg="red",bg="black", width=36).place(x =120, y=150)

# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
#tree = ttk.Treeview(root, column=("SKU", "Description", "Size","Color","Price"), show='headings', height=10)
#tree.column("# 1", anchor=CENTER)
#tree.heading("# 1", text="SKU")
#tree.column("# 2", anchor=CENTER)
#tree.heading("# 2", text="Description")
#tree.column("# 3", anchor=CENTER)
#tree.heading("# 3", text="Size")
#tree.column("# 4", anchor=CENTER)
#tree.heading("# 4", text="Color")
#tree.column("# 5", anchor=CENTER)
#tree.heading("# 5", text="Price")

# Insert the data in Treeview widget
'''
tree.insert('', 'end', text="1", values=('Amit', 'Kumar', '17701'))
tree.insert('', 'end', text="1", values=('Ankush', 'Mathur', '17702'))
tree.insert('', 'end', text="1", values=('Manisha', 'Joshi', '17703'))
tree.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))



tree.pack()
'''
s1 = View()

root.mainloop()
