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
        con=create_con()
        cursor=con.cursor()
        query="insert into products (sku,description,size,color,price,qty) values (%s,%s,%s,%s,%s,%s)"
        args=(e_sku.get(),e_desc.get(),e_size.get(),e_color.get(),e_price.get(),e_qty.get())
        cursor.execute(query,args)
        con.commit()
        con.close()
        e_sku.delete(0,'end')
        e_desc.delete(0,'end')
        e_size.delete(0,'end')
        e_color.delete(0,'end')
        e_price.delete(0,'end')
        e_qty.delete(0,'end')
        msg.showinfo("Product Add Status","Product added Successfully")

def search_product():
    e_desc.delete(0,'end')
    e_size.delete(0,'end')
    e_color.delete(0,'end')
    e_price.delete(0,'end')
    e_qty.delete(0,'end')
    if e_sku.get()=="":
        msg.showerror("Product Search","Please Enter SKU code")
    else:
        con = create_con()
        cursor=con.cursor()
        query = "select * from products where sku = %s"
        args=(e_sku.get(),)
        cursor.execute(query,args)
        data=cursor.fetchall()
        if data:
            for i in data:
                e_desc.insert(0,i[2])
                e_size.insert(0,i[3])
                e_color.insert(0,i[4])
                e_price.insert(0,i[5])
                e_qty.insert(0,i[6])
        else:
            msg.showerror("Search Status","SKU Code does not found")
        con.close()

# Update data
def update_product():
    if e_sku.get()=="" or e_desc.get()=="" or e_size.get()=="" or e_color.get()=="" or e_price.get()=="" or e_qty.get()=="":
        msg.showinfo("Product Status","All fields are Manadotary")
    else:
        con = create_con()
        cursor=con.cursor()
        query="update products set description=%s, size=%s, color=%s, price=%s, qty=%s where sku=%s"
        args = (e_desc.get(),e_size.get(),e_color.get(),e_price.get(),e_qty.get(),e_sku.get())
        cursor.execute(query,args)
        con.commit()
        con.close()
        e_sku.delete(0,"end")
        e_desc.delete(0,"end")
        e_size.delete(0,"end")
        e_color.delete(0,"end")
        e_price.delete(0,"end")
        e_qty.delete(0,"end")
        msg.showinfo("Update Status","Data Updated Successfully")


#Delete data
def delete_product():
    if e_sku.get()=="":
        msg.showinfo("Delete Status","SKU is mandatory to delete product")
    else:
        con = create_con() 
        cursor=con.cursor()
        query ="delete from products where sku = %s"
        args=(e_sku.get(),)
        ans=msg.askokcancel("Delete Status","Please confirm for delete")
        if ans:
            cursor.execute(query,args)
            con.commit()
            e_sku.delete(0,'end')
            e_desc.delete(0,'end')
            e_size.delete(0,'end')
            e_color.delete(0,'end')
            e_price.delete(0,'end')
            e_qty.delete(0,'end')
            msg.showinfo("Delete Status","Product is deleted Successfully")
        else:
            msg.showinfo("Delete Status","Product does not deleted")
        cursor.close()


    
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

search=Button(root,text="SEARCH",font=("Sans-serif 15"),fg="black",bg="orange", width=15, bd=6, command=search_product).place(x=300,y=400)

update=Button(root,text="UPDATE",font=("Sans-serif 15"),fg="black",bg="orange", width=15, bd=6, command=update_product).place(x=100,y=450)

delete=Button(root,text="DELETE",font=("Sans-serif 15"),fg="black",bg="orange", width=15, bd=6, command=delete_product).place(x=300,y=450)

#stock=Button(root,text="Stock",font=("Sans-serif 15"),fg="black",bg="orange", width=20, bd=6).place(x=200,y=500)


root.mainloop()


