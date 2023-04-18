from tkinter import *
import tkinter as tk
import mysql.connector                                          #mysql connector library
import tkinter.messagebox as msg


root = tk.Tk()                                                                             # it will open blank page

root.geometry("600x600")                                                    # size of web page
root.title("Product Management App")
root.resizable(width=False,height=False)                            # it will remove Maximise symbol from web page 


l_name=Label(root,text="Name ", font=("Sans-serif 15"))
l_name.place(x = 30, y=50)
