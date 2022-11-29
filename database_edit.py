from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def insert():
    id = e_client_id.get()
    name = e_name.get()
    reg = e_reg_no.get()
    phone = e_phone.get()
    mail = e_mail.get()

    if(id=="" or name=="" or phone=="" or reg=="" or mail==""):
        MessageBox.showinfo("Insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="1234567890", database="ktinker_database")
        cursor = con.cursor()
        cursor.execute("INSERT into ktinker_database.clientinfo (client_id,name, reg_no, phone, email) VALUES ('"+id+"', '"+name+"', '"+reg+"', '"+phone+"', '"+mail+"')")
        cursor.execute("commit");

        e_client_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_reg_no.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_mail.delete(0, 'end')
        show()
        MessageBox.showinfo("Insert Status", "Inserted successfully");
        con.close();


def delete():
    if(e_client_id.get()==""):
        MessageBox.showinfo("Delete status", "Id is required for deletion")
    else:
        con = mysql.connect(host="localhost", user="root", password="1234567890", database="ktinker_database")
        cursor = con.cursor()
        cursor.execute("delete from ktinker_database.clientinfo where client_id='"+e_client_id.get()+"'")
        cursor.execute("commit")

        e_client_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_reg_no.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_mail.delete(0, 'end')
        show()
        MessageBox.showinfo("Delete Status", "Deleted successfully");
        con.close();


def update():
    id = e_client_id.get()
    name = e_name.get()
    reg = e_reg_no.get()
    phone = e_phone.get()
    mail = e_mail.get()

    if (id == "" or name == "" or phone == "" or reg == "" or mail == ""):
        MessageBox.showinfo("Update status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="1234567890", database="ktinker_database")
        cursor = con.cursor()
        cursor.execute("update clientinfo set  name='"+name+"',reg_no='"+reg+"',phone='"+phone+"', email='"+mail+"' WHERE client_id='"+id+"' ")
        cursor.execute("commit")

        e_client_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_reg_no.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_mail.delete(0, 'end')

        show()
        MessageBox.showinfo("Update Status", "Updated successfully")
        con.close()


def get():
    if (e_client_id.get() == ""):
        MessageBox.showinfo("Fetch status", "Id is required for deletion")
    else:
        con = mysql.connect(host="localhost", user="root", password="1234567890", database="ktinker_database")
        cursor = con.cursor()
        cursor.execute("select * from ktinker_database.clientinfo WHERE client_id='"+e_client_id.get()+"'")
        rows=cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_reg_no.insert(0, row[2])
            e_phone.insert(0, row[3])
            e_mail.insert(0, row[4])


        con.close();


def show():
    con = mysql.connect(host="localhost", user="root", password="1234567890", database="ktinker_database")
    cursor = con.cursor()
    cursor.execute("select * from ktinker_database.clientinfo ")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData= str(row[0])+'     '+ row[1]
        list.insert(list.size()+1, insertData)

    con.close()


root = Tk(className="face recognation database")
root.geometry("600x300")
# root.title("tkinter-sql-database")
root.attributes('-topmost',1)

id=Label(root, text="client_id", font=('bold', 10))
id.place(x=20, y=30)

id=Label(root, text="name", font=('bold', 10))
id.place(x=20, y=60)

id=Label(root, text="reg_no", font=('bold', 10))
id.place(x=20, y=90)

id=Label(root,text="phone", font=('bold',10))
id.place(x=20, y=120)

id=Label(root, text="email", font=('bold', 10))
id.place(x=20, y=150)

e_client_id = Entry()
e_client_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

e_reg_no = Entry()
e_reg_no.place(x=150, y=90)

e_phone=Entry()
e_phone.place(x=150,y=120)

e_mail =Entry()
e_mail.place(x=150, y=150)

insert = Button(root, text="Insert", font=("bold", 10), bg="white", command=insert,padx=4,pady=4)
insert.place(x=20, y=200)

delete = Button(root, text="Delete", font=("bold", 10), bg="white", command=delete,padx=4,pady=4)
delete.place(x=100, y=200)

update = Button(root, text="Update", font=("bold", 10), bg="white", command=update,padx=4,pady=4)
update.place(x=180, y=200)

get = Button(root, text="Get", font=("bold", 10), bg="white", command=get,padx=4,pady=4)
get.place(x=270, y=200)
# get.pack()
list = Listbox(root)
list.place(x=290, y=30)

show()


root.mainloop()
