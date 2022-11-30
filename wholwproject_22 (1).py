import os
import cv2
from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as font


path = 'C:\\Users\\GAUTAM\\Desktop\\faceimage_database'

camera_port = 0
rate_frame = 30   # rate_of_image=30


def click_photo(name):

    camera = cv2.VideoCapture(camera_port)

    # cv2.namedWindow("python to capture images")

    if button['text'] == 'click_images':

        button['text'] = "another user"
        os.chdir(path)
        Newfolder = name

        if Newfolder == "##":
            return

        os.makedirs(Newfolder)
        path2 = path+"\\"+Newfolder
        os.chdir(path2)
        img_count = 0

        newfolder = "images"
        os.makedirs(newfolder)
        path_images = path2+"\\"+newfolder



        while True:

            for i in range(rate_frame):

                ret, frame = camera.read()

                if not ret:
                    print("fail to capture image")
                    break

            cv2.imshow("image_frame", frame)

            k = cv2.waitKey(1)

            if img_count > 10:
                camera.release()
                cv2.destroyAllWindows()
                break

            else:

                os.chdir(path_images)
                image_name = "iamge_sample_{}.png".format(img_count)
                cv2.imwrite(image_name, frame)
                print("image is taken")
                img_count += 1

    else:
        button['text'] = "click_images"


# --------------------------------------------------------
win = Tk(className="face_racognation")

# win.resizable(1, 1)

win.geometry('700x500')
win.attributes('-topmost', 1)

myfont = font.Font(family="Arial", size=20, weight='bold')

label = Label(win, text="Face recognisation app", padx=500,pady=10, font=myfont, bg="lightblue")
label.pack()

gui = Frame(win, pady=80, padx=80, bg="lightBlue", borderwidth=5)
#gui.pack()

forth = Frame(win, padx=10, pady=10, bg="brown")

second = Frame(win, pady=100, padx=150, bg="orange")
second.place(x=150, y=90)

third = Frame(win, pady=20, padx=20)
third.place(x=575, y=600)

side = Frame(win, pady=20, padx=20, background="lightgreen")
side.place(x=0, y=55)

# -------------------------------------------------------------------


def show_frames():
    # Get the latest frame and convert into Image
    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image=img)
    label_cam.imgtk = imgtk
    label_cam.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    label.after(20, show_frames)
# this above camera opener is not undersatood -----------------------------------------


def exit():
    gui.quit()
    return


def save():
    if save_B['text'] == 'SAVE':
        save_B['text'] = "SAVED"

        name = entryname.get()
        reg = entryreg.get()
        phone = entryphonenumber.get()
        mail = entryemail.get()

        if (name == "" or phone == "" or reg == "" or mail == ""):
            MessageBox.showinfo("Insert status", "All fields are required")
        else:
            con = mysql.connect(host="localhost", user="root", password="1234567890", database="project_database1")
            cursor = con.cursor()
         #   pathimagetosave = str(path) + str('\\') + name + str('\\images') galat h error aa raha
            cursor.execute("INSERT into project_database1.clientinfo (name, reg_no, phone, email) VALUES ('"+name+"', '" + reg + "', '" + phone + "', '" + mail + "')  ")
            cursor.execute("commit");

            MessageBox.showinfo("Insert Status", "Inserted user information successfully")
            con.close()

        messagebox.showinfo('notification', 'ready to pose')
        name = entryname.get()
        # other type of message
        # messagebox.askokcancel("askokcancel", "Want to continue?")
        mysavelabel = Label(gui, text="done! "+name, bg="lightblue", fg="green")
        mysavelabel.grid(row=5, column=2)
        print(name)
        global button
        button = Button(gui, text="click_images", command=lambda: click_photo(name))
        button.grid(row=6, column=3)

    else:
        save_B['text'] = 'SAVE'


def clear():
    save_B['text'] = 'SAVE'
    if save_B['text'] == "SAVED":
        button['text'] = "click_images"

        button.destroy()
    entryname.delete(0, END)
    #entrypass.delete(0, END)
    return


def exit_2():

    win.quit()
    return


def switch_to_add():
    return_button.place(x=1200, y=70)
    gui.place(x=450, y=80)
    forth.place(x=500, y=70)
    second.place_forget()


def find():
    gui.place_forget()
    forth.place_forget()
    # return_button.place_forget()
    return_button.place(x=1200, y=70)
    second.place_forget()
    global label_cam
    label_cam = Label(win)
    label_cam.pack()
    global cap
    cap = cv2.VideoCapture(0)
    show_frames()

    print("added")


def back():
    gui.place_forget()
    return_button.place_forget()
    forth.place_forget()
    label_cam.pack_forget()
    cap.release()
    cv2.destroyAllWindows()
    second.place(x=450, y=80)
# -------------------------------------------------------------------


E_label = Label(gui, text="  ", bg="lightblue")

reg = Label(gui, text="Enter the registration no. : ", bg="lightblue", borderwidth=3, font="12")
entryreg = Entry(gui, width=35, borderwidth=5)

username = Label(gui, text="Enter the user name : ", bg="lightblue", borderwidth=3, font="12")
entryname = Entry(gui, width=35, borderwidth=5)

phonenumber = Label(gui, text="Enter phone number : ", bg="lightblue", borderwidth=3, font="12")
entryphonenumber = Entry(gui, width=35, borderwidth=5)

email = Label(gui, text="Enter email_id : ", bg="lightblue", borderwidth=3, font="12")
entryemail = Entry(gui, width=35, borderwidth=5)

save_B = Button(gui, text="SAVE", padx=24, pady=5, command=save, bg="orange", activeforeground="green")
exit_B = Button(gui, text="EXIT", padx=20, pady=4, command=exit)
clear_B = Button(gui, text="Clear", padx=24, pady=5, command=clear)

reg.grid(row=0, column=0)
entryreg.grid(row=0,column=1, columnspan=4, padx=10, pady=10)
username.grid(row=1, column=0)
entryname.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
phonenumber.grid(row=2, column=0)
entryphonenumber.grid(row=2, column=1, columnspan=4, padx=10, pady=10)
email.grid(row=3, column=0)
entryemail.grid(row=3, column=1, columnspan=4, padx=10, pady=10)

clear_B.grid(row=5, column=3)
save_B.grid(row=5, column=1)
exit_B.grid(row=8, column=2)
E_label.grid(row=7, column=2)


switch_B = Button(second, text=" ADD User ", font="arial 10 bold", command=switch_to_add, pady=8, padx=8)
button_check = Button(second, text="Find face", font="arial 12", command=find, pady=5, padx=9)
exit_b2 = Button(second, text="EXIT", font="arial 12", command=exit_2, padx=10, pady=1)
label_b = Label(second, text=" ", bg="orange")
label_b2 = Label(second, text="", bg="orange")

button_check.pack()
label_b.pack()
switch_B.pack()
label_b2.pack()
exit_b2.pack()

label1 = Label(third, text="copyright @rt", fg="red").pack()

return_button = Button(win, text="Return", font="12,bold", command=back)

label_side = Label(side, text="Instruction", bg="lightgreen", font="arial 19 ", padx=50, pady=10)
label_side.pack()

win.mainloop()
