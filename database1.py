from tkinter import *
import sqlite3

root = Tk()
root.geometry("350x600")
root.title("Database")


# create database to create one
connect = sqlite3.connect('address_book.db')

# create cursor
curser_ = connect.cursor()

# create cursor
# connect.execute("""  CREATE TABLE addresses (
#                               first_name text,
#                               last_name text,
#                               address text,
#                               city text,
#                               state text,
#                               zipcode integer
#                     )""")


def submit():
          connect = sqlite3.connect('address_book.db')
          cursers = connect.cursor()

          # insert data  into table
          cursers.execute("INSERT INTO addresses VALUES (:f_name, :l_name,:address, :city, :state, :zipcode)",
                    {
                              'f_name':f_name.get(),
                              'l_name':l_name.get(),
                              'address':address.get(),
                              'city':city.get(),
                              'state':state.get(),
                              'zipcode':zipcode.get(),
                    } )     

          connect.commit()
          connect.close()

          f_name.delete(0,END)
          l_name.delete(0,END)
          address.delete(0,END)
          city.delete(0,END)
          state.delete(0,END)
          zipcode.delete(0,END)



def query():
          connect = sqlite3.connect('address_book.db')
          cursers = connect.cursor()

          cursers.execute("SELECT *,oid FROM addresses")
          records = cursers.fetchall()
          # print(records)

          print_record = ''

          # root through labels which is a list 
          for items in records:
                    # printing each item from the list which is a tuple
                    print_record +=str(items[6])+".  "+ str(items[0]) +"     "+  str(items[1]) +"     " +  str(items[2]) +"     "+ str(items[3]) +"     "+ str(items[4]) +"     "+ str(items[5]) +"\n"
 
          qury_label = Label(root,text=print_record)
          qury_label.grid(row=8,column=0,columnspan=2)

          connect.commit()
          connect.close()



def delete():
          connect = sqlite3.connect('address_book.db')
          cursers = connect.cursor()

          cursers.execute("DELETE FROM addresses WHERE oid=" + delete_item.get())

          connect.commit()
          connect.close()




def update_record():
          connect = sqlite3.connect('address_book.db')
          cursers = connect.cursor()

          record_id = delete_item.get()

          cursers.execute(""" UPDATE addresses SET 
                              first_name = :first,
                              last_name = :last,
                              address = :address,
                              city = :city,
                              state = :state,
                              zipcode = :zipcode

                              WHERE oid =:oid""",
                              {
                                        'first':f_name_e.get(),
                                        'last':l_name_e.get(),
                                        'address':city_e.get(),
                                        'city':address_e.get(),
                                        'state':state_e.get(),
                                        'zipcode':zipcode_e.get(),

                                        'oid':record_id
                              }
                              )

          connect.commit()
          connect.close()

          editor.destroy()

         




def update():
          global editor
          editor = Tk()
          editor.title('update')
          editor.geometry('350x400')


          connect = sqlite3.connect('address_book.db')
          cursers = connect.cursor()

          # global record_id

          record_id = delete_item.get()
          cursers.execute("SELECT * FROM addresses WHERE oid = " + record_id)
          records = cursers.fetchall()

          global f_name_e
          global l_name_e
          global city_e
          global address_e
          global state_e
          global zipcode_e
          



          f_name_e = Entry(editor,width=30)
          f_name_e.grid(row=0,column=1,padx=20,pady=(20,0))

          l_name_e = Entry(editor,width=30)
          l_name_e.grid(row=1,column=1,padx=20,pady=(20,0))

          city_e = Entry(editor,width=30)
          city_e.grid(row=2,column=1,padx=20,pady=(20,0))

          address_e = Entry(editor,width=30)
          address_e.grid(row=3,column=1,padx=20,pady=(20,0))

          state_e = Entry(editor,width=30)
          state_e.grid(row=4,column=1,padx=20,pady=(20,0))

          zipcode_e = Entry(editor,width=30)
          zipcode_e.grid(row=5,column=1,padx=20,pady=(20,0))


          # -------------

          f_name_lable = Label(editor,text='first name')
          f_name_lable.grid(row=0,column=0)

          l_name_lable = Label(editor,text='last name')
          l_name_lable.grid(row=1,column=0)

          address_label = Label(editor,text='address')
          address_label.grid(row=2,column=0)

          city_lable = Label(editor,text='city')
          city_lable.grid(row=3,column=0)

          state_lable = Label(editor,text='state')
          state_lable.grid(row=4,column=0)

          zipcode_lable = Label(editor,text='zip code')
          zipcode_lable.grid(row=5,column=0)


          for record in records:
                    f_name_e.insert(0, record[0])
                    l_name_e.insert(0, record[1])
                    city_e.insert(0, record[2])
                    address_e.insert(0, record[3])
                    state_e.insert(0, record[4])
                    zipcode_e.insert(0, record[5])
                    
          
          
          btn_sub_e = Button(editor,text='update record',bg='white',command=update_record)
          btn_sub_e.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

          connect.commit()
          connect.close()



         

       



f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(20,0))

l_name = Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20,pady=(20,0))

city = Entry(root,width=30)
city.grid(row=2,column=1,padx=20,pady=(20,0))

address = Entry(root,width=30)
address.grid(row=3,column=1,padx=20,pady=(20,0))

state = Entry(root,width=30)
state.grid(row=4,column=1,padx=20,pady=(20,0))

zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20,pady=(20,0))


delete_item = Entry(root,width=30)
delete_item.grid(row=10,column=1,padx=20,pady=(20,0))

# -------------

f_name_lable = Label(root,text='first name')
f_name_lable.grid(row=0,column=0)

l_name_lable = Label(root,text='last name')
l_name_lable.grid(row=1,column=0)

address_label = Label(root,text='address')
address_label.grid(row=2,column=0)

city_lable = Label(root,text='city')
city_lable.grid(row=3,column=0)

state_lable = Label(root,text='state')
state_lable.grid(row=4,column=0)

zipcode_lable = Label(root,text='zip code')
zipcode_lable.grid(row=5,column=0)

delete_label = Label(root,text='select record')
delete_label.grid(row=10,column=0)

# ----------------------



btn_sub = Button(root,text='submit',bg='white',command=submit)
btn_sub.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=137)


# create a query btn
querybtn = Button(root,text="show record ",bg='white',command=query)
querybtn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=123)


# create a delete btn
delbtn = Button(root,text="delete record ",bg='white',command=delete)
delbtn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=120)

# update a delete btn
update_btn = Button(root,text="update record ",bg='white',command=update)
update_btn.grid(row=12,column=0,columnspan=2,padx=10,pady=10,ipadx=120)


connect.commit()
connect.close()

root.mainloop()

