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

def register_page():
    root.destroy()
    import Registration

def login():
    
    if e_email.get()=="" or e_pwd.get()=="":
        l_msg1=Label(root,text="All fields are required Mandatory", font=("Sans-serif",15),fg="red").place(x=120 ,y=300)
    else:
        try:
            con=create_con()
            cursor=con.cursor()
            query = "select * from registration1 where email = %s"
            args=(e_email.get(),)
            cursor.execute(query,args)
            data=cursor.fetchall()
            #print(data)
            con.close()
            email=e_email.get()
            pwd=e_pwd.get()
            db=[]
            for i in data:
                for j in i:
                    db.append(j)
            #print(db)
            db_email=db[3]
            db_pwd=db[6]
            #print(email)
            
            if db_email==email:
                if db_pwd== pwd:
                    l_msg2=Label(root,text="Login Successfully", font=("Sans-serif",20)).place(x=150 ,y=350)
                    root.destroy()
                    import products
                else:
                    msg.showerror("Login Status","Password does not matched")
                    l_msg1=" "
            else:
                msg.showerror("Login Status","Email does not matched")
        except:
            msg.showerror("Login Status","Email does not matched ")
            
        
root = tk.Tk()                                                                             # it will open blank page

root.geometry("600x600")                                                    # size of web page
root.title("Product Management App")
root.resizable(width=False,height=False)                            # it will remove Maximise symbol from web page 
#root.config(bg="white")                                                        # White Backgound 


l_lable=Label(root,text="Product Management Application", font=("Sans-serif ",20),fg="white",bg="black").place(x =100, y=20)

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
login=Button(root,text="LOGIN",font=("Sans-serif 15"),fg="black",bg="orange", width=10,command=login)
login.place(x=200,y=250)

root.mainloop()

