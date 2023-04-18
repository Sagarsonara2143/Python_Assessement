from tkinter import *
import tkinter as tk
import mysql.connector                                          #mysql connector library
import tkinter.messagebox as msg


#Connect to database
def create_con():
    return mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "python"
        )
#print(create_con())            #call function to check code of function is execute or not


def register():
    state=opt_state.get()
    if e_name.get()=="" or e_contact.get()=="" or e_email.get()=="" or r_gender.get==""or state=="" or e_pwd.get=="":
        l_msg=Label(root,text="All fields are Mandatory ", font=("Sans-serif 14"))
        l_msg.place(x = 200, y=400)
    else:
        if e_pwd.get() == e_cpwd.get():
            con=create_con()
            cursor=con.cursor()
            query="insert into registration1 (name,contact,email,gender,state,password) values (%s,%s,%s,%s,%s,%s)"
            args = (e_name.get(),e_contact.get(),e_email.get(),r_gender.get(),state,e_pwd.get())
            cursor.execute(query,args)
            con.commit()
            con.close()
            e_name.delete(0,'end')
            e_contact.delete(0,'end')
            e_email.delete(0,'end')
            r_gender.set("None")
            opt_state.set("----select----")
            e_pwd.delete(0,'end')
            l_msg.delete(0,'end')
            msg.showinfo("Registration Status","Registration form created Successfully")
        
            root.destroy()
            import page
        else:
             l_msg=Label(root,text="Password and confirm password does not match", font=("Sans-serif 14"),fg="red")
             l_msg.place(x = 100, y=400)
            
root = tk.Tk()                                                                             # it will open blank page

root.geometry("600x600")                                                    # size of web page
root.title("Product Management App")
root.resizable(width=False,height=False)                            # it will remove Maximise symbol from web page 

#Create a Label and place in root

l_title = Label(root,text="                    Please Enter details below                      ",font=("Arial bold",18), fg="white")
l_title.place(x = 0, y=0)
l_title.config(bg="orange")

l_name=Label(root,text="Name ", font=("Sans-serif 15"))
l_name.place(x = 30, y=50)

l_contact=Label(root,text="Contact", font=("Sans-serif 15"))
l_contact.place(x = 30, y=100)

l_email=Label(root,text="Email", font=("Sans-serif 15"))
l_email.place(x = 30, y=150)

l_gender=Label(root,text="Gender", font=("Sans-serif 15"))
l_gender.place(x = 30, y=200)

l_state=Label(root,text="State", font=("Sans-serif 15"))
l_state.place(x = 30, y=250)

l_pwd=Label(root,text="Password", font=("Sans-serif 15"))
l_pwd.place(x = 30, y=300)

l_cpwd=Label(root,text="Confirm Password", font=("Sans-serif 15"))
l_cpwd.place(x =30, y=350)




#Create a textbox and radio button and drop down list

e_name = Entry(root, bd=2, width=30,font=("Sans-serif 15"))
e_name.place(x = 200, y=50)

e_contact = Entry(root, bd=2, width=30,font=("Sans-serif 15"))
e_contact.place(x = 200, y=100)

e_email = Entry(root, bd=2, width=30,font=("Sans-serif 15"))
e_email.place(x = 200, y=150)

r_gender=tk.StringVar()
male=tk.Radiobutton(root, text="Male",value="male", variable=r_gender,font=("Sans-serif 15"),indicatoron=0)
female=tk.Radiobutton(root, text="Female",value="female", variable=r_gender,font=("Sans-serif 15"),indicatoron=0)
male.place(x=200, y=200)
female.place(x=270,y=200)


#Selection for State
opt_state=StringVar(root)
opt_state.set("----select----")
d_state=OptionMenu(root,opt_state, "Gujarat","Rajasthan","Delhi","Punjab","Maharashtra","UP","Kerala")
d_state.place(x=200,y=250)
d_state.config(font=("Sans-serif 15"),width=26)

menu = root.nametowidget(d_state.menuname)                           # Get menu for set font size.
menu.config(font=("Sans-serif 15"))                                             # Set the dropdown menu's font


e_pwd = Entry(root, show="*",bd=2, width=30,font=("Sans-serif 15"))
e_pwd.place(x = 200, y=300)

e_cpwd = Entry(root, show="*",bd=2, width=30,font=("Sans-serif 15"))
e_cpwd.place(x = 200, y=350)


#Register Button
register=Button(root,text="REGISTER",font=("Sans-serif 15"),fg="black",bg="orange",command=register)
register.place(x=200,y=450)


root.mainloop()
