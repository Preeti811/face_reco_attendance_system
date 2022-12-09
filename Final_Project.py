import os
import cv2
from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as font
import numpy as np
import faceRecognition as fr
from datetime import datetime

path = 'C:\\Users\\GAUTAM\\Desktop\\faceimage_database\\training_images'

camera_port = 0

rate_frame = 10             # rate_of_iamge=10

# sql functions ++++++++++++++++++++++++++++++++++++++++++++++++++++


def show():
     con = mysql.connect(host="localhost", user="root", password="1234567890", database="project_db1")
     cursor = con.cursor()
     cursor.execute("select * from project_db1.new_table")
     rows = cursor.fetchall()
     list.delete(0, list.size())

     for row in rows:
         insertdata = str(row[0])+'     ' + row[1]
         list.insert(list.size()+1, insertdata)

#     con.close()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def click_photo(dregistration):
    # gui.place_forget()
    # return_button.place_forget()
    # forth.place_forget()
    # label_cam.pack_forget()
    six.pack()

    camera = cv2.VideoCapture(camera_port)

    # cv2.namedWindow("python to capture images")

    if button['text'] == 'click_images':

        button['text'] = "another user"

        os.chdir(path)

        Newfolder = dregistration

        if Newfolder == "##":
            return

        os.makedirs(Newfolder)

        path2 = path + "\\" + Newfolder

        img_count = 0

        path_images = path2


        while True:

            for i in range(rate_frame):

                ret, frame = camera.read()

                if not ret:
                    print("fail to capture image")
                    break

                #show_framecam(frame)
                cv2.imshow("image_frame", frame)


            #camera_win = cv2.imshow("image_frame", frame)

            k = cv2.waitKey(1)

            if img_count > 70:
                camera.release()
                cv2.destroyAllWindows()
                break

            else:

                os.chdir(path_images)

                image_name = str(dregistration) + "_image_{}.png".format(img_count)

                cv2.imwrite(image_name, frame)

                print("image is taken")

                img_count += 1
    else:
        button['text'] = "click_images"
        entryregi.delete(0, 'end')
        entryname.delete(0, 'end')
        entryphone.delete(0, 'end')
        entrybranch.delete(0, 'end')
        entryemail.delete(0, 'end')

    faces, faceID = fr.labels_for_training_data('C:\\Users\\GAUTAM\\Desktop\\faceimage_database\\training_images')
    face_recognizer = fr.train_classifier(faces, faceID)
    face_recognizer.write('C:\\Users\\GAUTAM\\Desktop\\faceimage_database\\trainingData.yml')


# def show_framecam(frame):
#     cv2.imshow("image_frame", frame)
#     # Get the latest frame and convert into Image
#     cam_image = cv2.cvtColor(frame[1], cv2.COLOR_BGR2RGB)
#     imgcam = Image.fromarray(cam_image)
#     # Convert image to PhotoImage
#     cam_imgtk = ImageTk.PhotoImage(image=imgcam)
#     label_wincam.imgtk = cam_imgtk
#     label_wincam.configure(image=cam_imgtk)
#      # Repeat after an interval to capture continiously
#     label_wincam.after(20,show_framecam)

# --------------------------------------------------------
win = Tk(className="face_racognation")

win.resizable(1, 1)

win.geometry('1000x600')

win.attributes('-topmost', 1)

myfont = font.Font(family="Arial", size=20, weight='bold')

label = Label(win, text="Face recognisation app", padx=500,
              pady=10, font=myfont, bg="lightblue")
label.pack()

gui = Frame(win, bg="lightBlue", pady=80, padx=80, borderwidth=5)
# gui.pack()
forth = Frame(win, padx=10, pady=10, bg="brown")

second = Frame(win, bg="orange", pady=100, padx=150)
second.place(x=450, y=170)

third = Frame(win, pady=20, padx=20)
third.place(x=575, y=600)

side = Frame(win, pady=20, padx=20, background="lightgreen")
side.place(x=0, y=55)

six = Frame(win)


# -------------------------------------------------------------------

def markAttendance(name):
  with open('Attendance.csv', 'r+') as f:
    myDataList = f.readlines()
    nameList = []
    for line in myDataList:
        entry = line.split(',')
        nameList.append(entry[0])
    if name not in nameList:
        now = datetime.now()
        dtString = now.strftime('%H:%M:%S')
        f.writelines(f'\n{name},{dtString}')
        print('attendance marked : ' + name )



def show_frames():
    # # Get the latest frame and convert into Image
    # cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    # img = Image.fromarray(cv2image)
    # # Convert image to PhotoImage
    # imgtk = ImageTk.PhotoImage(image=img)
    # label_cam.imgtk = imgtk
    # label_cam.configure(image=imgtk)
    # Repeat after an interval to capture continiously


    #ret, cv2image = cap.read()  # captures frame and returns boolean value and captured image
    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    faces_detected, gray_img = fr.faceDetection(cv2image)

    for face in faces_detected:
        (x, y, w, h) = face
        roi_gray = gray_img[y:y + w, x:x + h]
        label_reg, confidence = face_recognizer.predict(roi_gray)  # predicting the label of given image
        # print("confidence:", confidence)        #will print confidence value lesser the value,better the match
        # print("label:", label_reg)              #will print registration no of person detected
        fr.draw_rect(cv2image, face)
        predicted_name = str(label_reg)
        if confidence < 50:
            fr.put_text(cv2image, predicted_name, x, y)
            markAttendance(str(label_reg))

    resized_img = cv2.resize(cv2image, (1000, 600))


    img = Image.fromarray(resized_img)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image=img)
    label_cam.imgtk = imgtk
    label_cam.configure(image=imgtk)
    label.after(20, show_frames)


def exit():
    gui.quit()
    return


def save():                                       #working appropriately
    if save_B['text'] == 'SAVE':
        save_B['text'] = "SAVED"

        dregistration = entryregi.get()
        dname = entryname.get()
        dphone = entryphone.get()
        dbranch = entrybranch.get()
        demail = entryemail.get()

        if dregistration == "" or dname == "":
            messagebox.showinfo("Insert status", "All fields are required")
        else:
            mysavelabel = Label(win, text="done! " + dname, bg="lightblue", fg="green", font="bold 12")
            mysavelabel.place(x=650, y=100)
            print(dname)
            print(dregistration)
            print(dphone)
            print(demail)
            print(dbranch)
            global button
            button = Button(gui, text="click_images", command=lambda: click_photo(dregistration))
            button.grid(row=9, column=9)

            con = mysql.connect(host="localhost", user="root", password="1234567890", database="project_db1")
            cursor = con.cursor()
            cursor.execute("INSERT into project_db1.new_table (registration,name,phone,branch,email) VALUES ('"+dregistration+"', '"+dname+"', '"+dphone+"','"+dbranch+"' ,'"+demail+"') ")
            cursor.execute("commit")

            show()
            messagebox.showinfo("Insert Status", "Inserted successfully")



            con.close()

        # other type of message
        # MessageBox.askokcancel("askokcancel", "Want to continue?")


    else:
        save_B['text'] = 'SAVE'


def clear():                                                  #working appropriately
    save_B['text'] = 'SAVE'
    if save_B['text'] == "SAVED":
        button['text'] = "click_images"

        button.destroy()

    entryname.delete(0, END)
    entryregi.delete(0, END)
    entryphone.delete(0, 'end')
    entrybranch.delete(0, 'end')
    entryemail.delete(0, 'end')
    return


def exit_2():
    win.quit()
    return


def switch_to_add():
    return_button.place(x=1200, y=70)
    gui.place(x=260, y=55)
    forth.place(x=500, y=70)
    second.place_forget()
    show()



def find():
    gui.place_forget()
    forth.place_forget()
    # return_button.place_forget()
    return_button.place(x=1300, y=70)
    second.place_forget()
    global label_cam
    label_cam = Label(win)
    label_cam.pack()
    global cap
    global face_recognizer
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('C:\\Users\\GAUTAM\\Desktop\\faceimage_database\\trainingData.yml')  # Load saved training data
    cap = cv2.VideoCapture(0)
    show_frames()


    #print("added")


def back():
    gui.place_forget()
    return_button.place_forget()
    forth.place_forget()
    label_cam.pack_forget()
    cap.release()
    cv2.destroyAllWindows()
    second.place(x=450, y=80)


# -------------------------------------------------------------------
####sql function run after save only ++++++++++++++++++++++++++++++++++++++++++++++


def delete():                                               #working appropriately
     if entryregi.get()=="":
        messagebox.showinfo("Delete status", "Id is required for deletion")

     else:
        con = mysql.connect(host="localhost", user="root", password="1234567890", database="project_db1")
        cursor = con.cursor()
        cursor.execute("delete from project_db1.new_table where registration='"+entryregi.get()+"'")
        cursor.execute("commit")


        entryregi.delete(0, 'end')
        entryname.delete(0, 'end')
        entryphone.delete(0, 'end')
        entrybranch.delete(0, 'end')
        entryemail.delete(0, 'end')

        show()
        messagebox.showinfo("Delete Status", "Deleted successfully")
        con.close()


def _update():                                                 #working properly

    dregistration = entryregi.get()
    dname = entryname.get()
    dphone = entryphone.get()
    dbranch = entrybranch.get()
    demail = entryemail.get()

    if (dregistration == "" or dname == "" or dphone == "" or dbranch == "" or demail == ""):
        MessageBox.showinfo("Update status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="1234567890", database="project_db1")
        cursor = con.cursor()
        cursor.execute("update new_table set  name='"+dname+"',phone='"+dphone+"',branch='"+dbranch+"', email='"+demail+"' WHERE registration='"+dregistration+"' ")
        cursor.execute("commit")

        entryregi.delete(0, 'end')
        entryname.delete(0, 'end')
        entryphone.delete(0, 'end')
        entrybranch.delete(0, 'end')
        entryemail.delete(0, 'end')

        show()
        MessageBox.showinfo("Update Status", "Updated successfully")
        con.close()


def _get():                                         #working properly
    if (entryregi.get() == ""):
        MessageBox.showinfo("Fetch status", "Id is required for deletion")
    else:
        con = mysql.connect(host="localhost", user="root", password="1234567890", database="project_db1")
        cursor = con.cursor()
        cursor.execute("select * from project_db1.new_table WHERE registration='"+entryregi.get()+"'")
        rows=cursor.fetchall()

        for row in rows:
            entryname.insert(0, row[1])
            entryphone.insert(0, row[2])
            entrybranch.insert(0, row[3])
            entryemail.insert(0, row[4])


        con.close()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


E1_label = Label(gui, text="  ", bg="lightblue")
E2_label = Label(gui, text="  ", bg="lightblue")

username = Label(gui, text="Enter the user name : ",
                 bg="lightblue", borderwidth=3, font="12")
regi = Label(gui, text="Enter the registration number : ",
             bg="lightblue", borderwidth=3, font="12")
phone = Label(gui, text="Enter the phone number : ",
              bg="lightblue", borderwidth=3, font="12")
branch = Label(gui, text="Enter the branch : ",
               bg="lightblue", borderwidth=3, font="12")
email = Label(gui, text="Enter the Email id : ",
              bg="lightblue", borderwidth=3, font="12")

entryname = Entry(gui, width=35, borderwidth=5)
#entryname.insert(0, "user name xyz")
entrybranch = Entry(gui, width=35, borderwidth=5)
entryphone = Entry(gui, width=35, borderwidth=5)
entryemail = Entry(gui, width=35, borderwidth=5)
entryregi = Entry(gui, width=35, borderwidth=5)

# button__________________________________________

Bdelete = Button(gui, text="Delete", font=("bold", 10), padx=10, pady=5, command=delete)

update = Button(gui, text="Update", font=("bold", 10), padx=10, pady=5, command=_update)

get = Button(gui, text="Get", font=("bold", 10), padx=15, pady=5,command=_get)

data_label = LabelFrame(gui, text="Database", font="bold", bg="lightblue")
list = Listbox(data_label)
list.pack()

save_B = Button(gui, text="SAVE", padx=24, pady=5, command=save,
                bg="orange", activeforeground="green")
exit_B = Button(gui, text="EXIT", padx=20, pady=4, command=exit)

clear_B = Button(gui, text="Clear", padx=24, pady=5, command=clear)

# ______________________________________________________________

regi.grid(row=0, column=0)
entryregi.grid(row=0, column=1, columnspan=4, padx=2, pady=10)
username.grid(row=1, column=0)
entryname.grid(row=1, column=1, columnspan=4, padx=2, pady=10)
phone.grid(row=2, column=0)
entryphone.grid(row=2, column=1, columnspan=4, padx=2, pady=10)
branch.grid(row=3, column=0)
entrybranch.grid(row=3, column=1, columnspan=4, padx=2, pady=10)
email.grid(row=4, column=0)
entryemail.grid(row=4, column=1, columnspan=4, padx=2, pady=10)
clear_B.grid(row=5, column=3, padx=5)
save_B.grid(row=5, column=1, padx=5)
E1_label.grid(row=6, column=2)
get.grid(row=7, column=1)
update.grid(row=7, column=3)
Bdelete.grid(row=7, column=6)
E2_label.grid(row=8, column=2)
exit_B.grid(row=9, column=3)
data_label.grid(row=0, column=10, columnspan=10, rowspan=10)

# ===========================================2222
switch_B = Button(second, text=" ADD User ", font="arial 10 bold",
                  command=switch_to_add, pady=8, padx=8)
button_check = Button(second, text="Find face",
                      font="arial 12", command=find, pady=5, padx=9)
exit_b2 = Button(second, text="EXIT", font="arial 12",
                 command=exit_2, padx=10, pady=1)
label_b = Label(second, text=" ", bg="orange")
label_b2 = Label(second, text="", bg="orange")

button_check.pack()
label_b.pack()
switch_B.pack()
label_b2.pack()
exit_b2.pack()

label1 = Label(third, text="copyright @rt", fg="red")

return_button = Button(win, text="Return", font="12,bold", command=back)

label_side = Label(side, text="Instruction", bg="lightgreen",
                   font="arial 19 ", padx=50, pady=10)
label_side.pack()
label1.pack()
label_wincam = Label(six)
label_wincam.pack()
# show()

win.mainloop()