

import cv2
import os
import numpy as np
from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Persons:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700+0+0")
        self.root.title("Face Recognizer")
        self.root.wm_iconbitmap("face_recognition_icon_154436.ico")

        #======variables===#
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()
        self.var_phn_no = StringVar()
        self.var_dob = StringVar()
        self.var_year = StringVar()
        self.var_gender = StringVar()
        self.var_location = StringVar()

        img1 = Image.open(
            r"C:\Users\User\Desktop\Face_Recognition_System\FaceREcognition Software\images\login_bg_ca.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)

        img2 = Image.open(
            r"C:\Users\User\Desktop\Face_Recognition_System\FaceREcognition Software\images\chat_ca.png")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # bg image
        img3 = Image.open(
            r"C:\Users\User\Desktop\Face_Recognition_System\FaceREcognition Software\images\back.jpg")
        img3 = img3.resize((1600, 1000), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1000, height=700)

        # text
        img10 = Image.open(
            r"C:\Users\User\Desktop\Face_Recognition_System\FaceREcognition Software\images\person1.jpg")
        img10 = img10.resize((150, 150), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        img_label=Label(self.root,image=self.photoimg10)
        img_label.place(x=120,y=10,width=150,height=150)


        title_lbl = Label( self.root,text="Persons Details", font=(
            "times new roman", 35, "bold"),bg="royalblue4", fg="White")
        title_lbl.place(x=300, y=80, width=300, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=180, width=1000, height=500)

        # left label fram
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Person Details Here", font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=450, height=450)

        # left child frame-1
        child_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Put Info Here", font=(
            "times new roman", 12, "bold"))
        child_frame.place(x=10, y=50, width=430, height=150)
        # combobox1
        dep_label = Label(child_frame, bg="white", text="Location",
                          font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(child_frame, textvariable=self.var_location, font=(
            "times new roman", 12, "bold"), width=15, state="readonly")
        dep_combo.grid(row=0, column=1)
        dep_combo["values"] = ("select Location", "Barisal",
                               "Dhaka", "Khulna", "Rajshahi")
        dep_combo.current(0)
        # combobox2
        Gender_label = Label(child_frame, bg="white", text="Gender",
                             font=("times new roman", 12, "bold"))
        Gender_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        Gender_combo = ttk.Combobox(child_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), width=12, state="readonly")
        Gender_combo.grid(row=0, column=3)
        Gender_combo["values"] = ("select Gender", "Male",
                                  "Female", "Other")
        Gender_combo.current(0)
        # combobox3
        Year_label = Label(child_frame, bg="white", text="Year",
                           font=("times new roman", 12, "bold"))
        Year_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        Year_combo = ttk.Combobox(child_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), width=15, state="readonly")
        Year_combo.grid(row=1, column=1)
        Year_combo["values"] = ("select Year", "2022",
                                "2021", "2020", "2019")
        Year_combo.current(0)

        # left child frame-2
        child2_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Info Here", font=(
            "times new roman", 12, "bold"))
        child2_frame.place(x=10, y=200, width=430, height=225)
        # Person Id lebel now
        PersonId_label = Label(child2_frame, bg="white", text="User ID:",
                               font=("times new roman", 12, "bold"))
        PersonId_label.grid(row=0, column=0, padx=1, pady=5, sticky=W)
        # entry
        PersonId_entry = ttk.Entry(child2_frame, textvariable=self.var_id, width=12,
                                   font=("times new roman", 12, "bold"))
        PersonId_entry.grid(row=0, column=1, padx=0,
                            pady=5, sticky=W)

        # Person Name lebel now
        PersonName_label = Label(child2_frame, bg="white", text="Name:",
                                 font=("times new roman", 12, "bold"))
        PersonName_label.grid(row=0, column=2, padx=2, pady=5, sticky=W)
        # entry
        PersonName_entry = ttk.Entry(child2_frame, textvariable=self.var_name, width=15,
                                     font=("times new roman", 12, "bold"))
        PersonName_entry.grid(row=0, column=3, padx=1, pady=5, sticky=W)
        # Person Address lebel now
        PersonAddress_label = Label(child2_frame, bg="white", text="Address:",
                                    font=("times new roman", 12, "bold"))
        PersonAddress_label.grid(row=1, column=0, padx=2, pady=5, sticky=W)
        # entry
        PersonAddress_entry = ttk.Entry(child2_frame, textvariable=self.var_address, width=12,
                                        font=("times new roman", 12, "bold"))
        PersonAddress_entry.grid(row=1, column=1, padx=1, pady=5, sticky=W)
        # Person Email lebel now
        PersonEmail_label = Label(child2_frame, bg="white", text="Email:",
                                  font=("times new roman", 12, "bold"))
        PersonEmail_label.grid(row=1, column=2, padx=2, pady=5, sticky=W)
        # entry
        PersonEmail_entry = ttk.Entry(child2_frame, textvariable=self.var_email, width=15,
                                      font=("times new roman", 12, "bold"))
        PersonEmail_entry.grid(row=1, column=3, padx=1, pady=5, sticky=W)
        # Person Phn No lebel now
        PersonPhn_label = Label(child2_frame, bg="white", text="Phn No:",
                                font=("times new roman", 12, "bold"))
        PersonPhn_label.grid(row=2, column=0, padx=0, pady=5, sticky=W)
        # entry
        PersonPhn_entry = ttk.Entry(child2_frame, textvariable=self.var_phn_no, width=12,
                                    font=("times new roman", 12, "bold"))
        PersonPhn_entry.grid(row=2, column=1, padx=1, pady=5, sticky=W)
        # Person DOB lebel now
        PersonDob_label = Label(child2_frame, bg="white", text="DOB:",
                                font=("times new roman", 12, "bold"))
        PersonDob_label.grid(row=2, column=2, padx=0, pady=5, sticky=W)
        # entry
        PersonDob_entry = ttk.Entry(child2_frame, textvariable=self.var_dob, width=15,
                                    font=("times new roman", 12, "bold"))
        PersonDob_entry.grid(row=2, column=3, padx=1, pady=5, sticky=W)

        # radio button
        self.var_radio1 = StringVar()
        radionbtn1 = ttk.Radiobutton(child2_frame, variable=self.var_radio1, width=15,
                                     text="Take Photo sample", value="YES")
        radionbtn1.grid(row=5, column=0)
        #button 2#

        radionbtn2 = ttk.Radiobutton(child2_frame, variable=self.var_radio1, width=15,
                                     text="No Photo sample", value="NO")
        radionbtn2.grid(row=5, column=1)

        # child2's button frame
        btn_frame = LabelFrame(child2_frame, bd=2,
                               relief=RIDGE, text="Where ")
        btn_frame.place(x=1, y=140, width=400, height=55)
        # buttonSave
        save_btn = Button(btn_frame, command=self.add_data, text="Save", width=4,  font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        # buttonUpdate
        Update_btn = Button(btn_frame, command=self.update_data, text="Update", width=5, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        Update_btn.grid(row=0, column=1)
        # buttonDelete
        Delete_btn = Button(btn_frame, command=self.delete_data, text="Delete", width=5, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        Delete_btn.grid(row=0, column=2)
        # buttonREset
        Reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", width=5, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        Reset_btn.grid(row=0, column=3)
        # Take photo button
        Take_btn = Button(btn_frame, command=self.generate_dataset,text="Take photo", width=8, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        Take_btn.grid(row=0, column=4)
        # buttonupload
        up_btn = Button(btn_frame, text="Up Photo", width=7, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        up_btn.grid(row=0, column=5)

        # rightlabel frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Search Person Details", font=(
            "times new roman", 12, "bold"))
        right_frame.place(x=490, y=10, width=488, height=450)
#=====================search frame======================#
        # right label search frame
        right_search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=(
            "times new roman", 12, "bold"))
        right_search_frame.place(x=10, y=50, width=465, height=70)

        search_label = Label(right_search_frame, text="Search By", font=(
            "times new roman", 12, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=0, pady=5, sticky=W)

        Search_combo = ttk.Combobox(right_search_frame, font=(
            "times new roman", 12, "bold"), width=10, state="readonly")
        Search_combo.grid(row=0, column=1)
        Search_combo["values"] = ("Select", "ID",
                                  "Name", "Address", "Phone number")
        Search_combo.current(0)

        Search_entry = ttk.Entry(right_search_frame, width=15,
                                 font=("times new roman", 12, "bold"))
        Search_entry.grid(row=0, column=2, padx=5,
                          pady=5, sticky=W)

        Search_btn = Button(right_search_frame, text="Search", width=5, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        Search_btn.grid(row=0, column=3)
        # buttonREset
        show_btn = Button(right_search_frame, text="Show all", width=5, padx=5, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        show_btn.grid(row=0, column=4)
        #======table frame======#
        table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=140, width=465, height=290)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            "ID", "Name", "Address", "email", "phn no", "DOB", "year", "gender", "Location", "photo sample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID", text="User ID")
        self.student_table.heading("Name", text="User Name")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("email", text="User Email")
        self.student_table.heading("phn no", text="UserPhoneNo:")
        self.student_table.heading("DOB", text="Date of Birth")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("Location", text="User location")
        self.student_table.heading("photo sample", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phn no", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("year", width=70)
        self.student_table.column("gender", width=70)
        self.student_table.column("Location", width=80)
        self.student_table.column("photo sample", width=130)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fecth_data()

#======function declare====#
    def add_data(self):
        if self.var_location.get() == "Location" or self.var_name.get() == "" or self.var_id == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into person values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_address.get(),
                    self.var_email.get(),
                    self.var_phn_no.get(),
                    self.var_dob.get(),
                    self.var_year.get(),
                    self.var_gender.get(),
                    self.var_location.get(),
                    self.var_radio1.get()


                ))
                conn.commit()
                self.fecth_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "student details has been added succesfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Eror", f"Due To:{str(es)}", parent=self.root)

        #==============fecth data========#
    def fecth_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="", database="face_recognition_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from person")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
   #===========get cursor====#

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_address.set(data[2]),
        self.var_email.set(data[3]),
        self.var_phn_no.set(data[4]),
        self.var_dob.set(data[5]),
        self.var_year.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_location.set(data[8]),
        self.var_radio1.set(data[9])
#=====update function===#

    def update_data(self):
        if self.var_location.get() == "Location" or self.var_name.get() == "" or self.var_id == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)

        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update this Person's details?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="face_recognition_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update person set Name=%s,Address=%s,email=%s,phn_no=%s,DOB=%s,year=%s,gender=%s,Location=%s,photo=%s where ID=%s", (

                        self.var_name.get(),
                        self.var_address.get(),
                        self.var_email.get(),
                        self.var_phn_no.get(),
                        self.var_dob.get(),
                        self.var_year.get(),
                        self.var_gender.get(),
                        self.var_location.get(),
                        self.var_radio1.get(),
                        self.var_id.get()

                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Person's details successfully update complete", parent=self.root)
                conn.commit()
                self.fecth_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)
#======delete finction===#

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Person id is required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "person delete page", "Do you want to delete this person?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="face_recognition_system")
                    my_cursor = conn.cursor()
                    sql = "delete from person where id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fecth_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted person details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

#=====reset====#
    def reset_data(self):
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_address.set(""),
        self.var_email.set(""),
        self.var_phn_no.set(""),
        self.var_dob.set(""),
        self.var_year.set("select Year"),
        self.var_gender.set("select Gender"),
        self.var_location.set("select Location"),
        self.var_radio1.set("")


#=========Generate data set/Take a photo sample===========#

    def generate_dataset(self):
        if self.var_location.get() == "Location" or self.var_name.get() == "" or self.var_id == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)

        else:
            try:

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from person")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("Update person set Name=%s,Address=%s,email=%s,phn_no=%s,DOB=%s,year=%s,gender=%s,Location=%s,photo=%s where ID=%s", (

                    self.var_name.get(),
                    self.var_address.get(),
                    self.var_email.get(),
                    self.var_phn_no.get(),
                    self.var_dob.get(),
                    self.var_year.get(),
                    self.var_gender.get(),
                    self.var_location.get(),
                    self.var_radio1.get(),
                    self.var_id.get() == id+1

                ))
                conn.commit()
                self.fecth_data()
                self.reset_data()
                conn.close()
                #=====load predifined data====#
                face_classifier = cv2.CascadeClassifier(
                    'haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while(True):
                    ret, my_frame = cap.read()
                    print(my_frame)
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        filePath = "data_sets/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(filePath, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating data sets completed!!!")

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Persons(root)
    root.mainloop()
