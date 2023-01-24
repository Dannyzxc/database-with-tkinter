from tkinter import *
import sqlite3

root = Tk()
root.geometry("400x400")
root.title("Database")


my_lable = Label(root,text="hello world")
my_lable.pack()


# create database to create one
connect = sqlite3.connect('address_book.db')

# create cursor
curser_ = connect.cursor()

# create cursor
connect.execute("""  CREATE TABLE addresses (
                              first_name text,
                              last_name text,
                              address text,
                              city text,
                              state text,
                              zipcode integer
                    )""")

# commit changes
connect.commit()

# close connection
connect.close()


root.mainloop()

