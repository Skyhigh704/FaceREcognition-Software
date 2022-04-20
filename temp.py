
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


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700+0+0")
        self.root.title("Face Recognizer")
        self.root.wm_iconbitmap("face_recognition_icon_154436.ico")

        title_lbl = Label(self.root, text="Face Recognization System", font=(
            "times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1000, height=100)

        img1 = Image.open(
            r"C:\Users\User\Desktop\Face_Recognition_System\FaceREcognition Software\images\face6.jpeg")
        img1 = img1.resize((1000, 700), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=100, width=1000, height=700)

        # button
        b1 = Button(self.root, cursor="hand2", command=self.face_recog,
                    text="Identify", font=(
                        "times new roman", 18, "bold"), bg="blue", fg="white")
        b1.place(x=600, y=250, width=180, height=150)

        # ============face recognition====
    def face_recog(self):
        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("training.xml")

        cap = cv2.VideoCapture(0)

        font = cv2.FONT_HERSHEY_SIMPLEX

        id = 0

        cam = cv2.VideoCapture(0)
        cam.set(3, 640)
        cam.set(4, 480)

        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        while True:

            ret, img = cam.read()
            img = cv2.flip(img, 1)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )

            for(x, y, w, h) in faces:

                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

                id, confidence = clf.predict(gray[y:y+h, x:x+w])

                #  confidence
                confidence = int((100*(1-confidence/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face_recognition_system")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from person where ID="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute(
                    "select email from person where ID="+str(id))
                k = my_cursor.fetchone()
                k = "+".join(k)

                my_cursor.execute(
                    "select location from person where ID="+str(id))
                s = my_cursor.fetchone()
                s = "+".join(s)

                if confidence > 70:
                    confidence = "  {0}%".format(round(confidence))
                    cv2.putText(
                        img, f"Name:{i}", (x, y-100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"email:{k}", (x, y-70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Location:{s}", (x, y-40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, str(confidence), (x+5, y+h-5),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)

                else:
                    confidence = "  {0}%".format(round(confidence))
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(
                        img, "UnKnown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, str(confidence), (x+5, y+h-5),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)

            cv2.imshow('camera', img)

            m = cv2.waitKey(10) & 0xff  # 'ESC' for exiting
            if m == 27:
                break

        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
