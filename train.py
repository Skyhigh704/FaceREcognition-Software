from lib2to3.pytree import convert
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


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700+0+0")
        self.root.title("Face Recognizer")
        self.root.wm_iconbitmap("face_recognition_icon_154436.ico")

        title_lbl = Label(self.root, text="Train the sample", font=(
            "times new roman", 35, "bold"), bg="dodgerblue4", fg="white")
        title_lbl.place(x=0, y=0, width=1000, height=100)

        img1 = Image.open(
            r"C:\Users\User\Desktop\Face_Recognition_System\FaceREcognition Software\images\img1.jpg")
        img1 = img1.resize((1000, 700), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=100, width=1000, height=700)

        # image section on top

        # image section in bottom

        #button in middle

        b1 = Button(self.root, cursor="hand2", command=self.train_classifier,
                    text="Click here", font=(
                        "times new roman", 18, "bold"), bg="forestgreen", fg="white")
        b1.place(x=0, y=250, width=1000, height=60)

    def train_classifier(self):
        data_dir = ("data_sets")
        path = [os.path.join(data_dir, file)
                for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)
        # ============= Train the classifier==========
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("training.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Training datasets completed", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
