
from email.mime import image
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from student import Persons
import os
from train import Train
from temp import Face_Recognition
import tkinter

def main():
    win=Tk()
    app=Face_Recognition_System(win)
    win.mainloop()


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700+0+0")
        self.root.title("Face Recognizer")
        self.root.wm_iconbitmap("face_recognition_icon_154436.ico")

        img1 = Image.open(
            r"C:\Users\User\Desktop\Face_Recognition_System\FaceREcognition Software\images\face2.jpg")
        img1 = img1.resize((1000, 700), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1000, height=700)

        
        # text
        title_lbl = Label(text="Find Your Face", font=(
            "times new roman", 45, "bold"), bg="deepskyblue4", fg="white")
        title_lbl.place(x=0, y=0, width=1000, height=100)

        # student button
        img3 = Image.open(
            r"C:\Users\User\Desktop\Face_Recognition_System\FaceREcognition Software\images\icon2.jpg")
        img3 = img3.resize((150, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(image=self.photoimg3,
                    command=self.persons_details, cursor="hand2")
        b1.place(x=10, y=300, width=150, height=150)

        b1_1 = Button(cursor="hand2",
                      text="Person Details",command=self.persons_details, font=(
                          "times new roman", 18, "bold"), bg="white", fg="dodgerblue4")
        b1_1.place(x=10, y=450, width=150, height=40)

        

        # train data
        img5 = Image.open(
            r"C:\Users\User\Desktop\Face_Recognition_System\FaceREcognition Software\images\train1.jpg")
        img5 = img5.resize((180, 180), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(image=self.photoimg5,
                    command=self.train_data, cursor="hand2")
        b1.place(x=180, y=300, width=180, height=150)

        b1 = Button(cursor="hand2", command=self.train_data,
                    text="Train Your Face", font=(
                        "times new roman", 18, "bold"), bg="white", fg="dodgerblue4")
        b1.place(x=180, y=450, width=180, height=40)

        # Photos
        img6 = Image.open(
            r"C:\Users\User\Desktop\Face_Recognition_System\FaceREcognition Software\images\photos.jpg")
        img6 = img6.resize((150, 150), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(image=self.photoimg6, cursor="hand2",
                    command=self.open_img)
        b1.place(x=650, y=300, width=150, height=150)

        b1 = Button(cursor="hand2", command=self.open_img,
                    text="Photos", font=(
                        "times new roman", 18, "bold"), bg="white", fg="dodgerblue4")
        b1.place(x=650, y=450, width=150, height=40)
        # face recognize
        img7 = Image.open(
            r"C:\Users\User\Desktop\Face_Recognition_System\FaceREcognition Software\images\face3.jpg")
        img7 = img7.resize((150, 150), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(image=self.photoimg7, cursor="hand2",
                    command=self.face_data)
        b1.place(x=830, y=300, width=160, height=150)

        b1 = Button(cursor="hand2", command=self.face_data,
                    text="face Recognize", font=(
                        "times new roman", 18, "bold"), bg="white", fg="dodgerblue4")
        b1.place(x=830, y=450, width=160, height=40)
        # Exit
        

        b1 = Button(cursor="hand2", command=self.iExit,
                    text="Exit", font=(
                        "times new roman", 18, "bold"), bg="dodgerblue4", fg="white")
        b1.place(x=425, y=590, width=150, height=40)

    def open_img(self):
        os.startfile("data_sets")
#=========Functions of buttons=====#

    def persons_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Persons(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure exit this app?", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
