from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label (self.root,text="FACE DETECTION",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
#1image
        img_top=Image.open(r"D:\FRAS python\images\d1.jpg")
        img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
        self.photoimage_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimage_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
#2image
        img_bottom=Image.open(r"D:\FRAS python\images\d2.jpg")
        img_bottom=img_bottom.resize((950,700),Image.Resampling.LANCZOS)
        self.photoimage_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimage_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)


        # button
        b1_1=Button(f_lbl,text="DETECT FACE",command=self.face_recog,cursor="hand2",font=("times new roman",20,"bold"),bg="lightgreen",fg="white")
        b1_1.place(x=395,y=550,width=200,height=40)


    ##########face recognition
    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Alam@123",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_id=%s", (id,))
                n = my_cursor.fetchone()
                n = n[0] if n else ""

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id=%s", (id,))
                r = my_cursor.fetchone()
                r = r[0] if r else ""

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id=%s", (id,))
                d = my_cursor.fetchone()
                d = d[0] if d else ""

                if confidence>77:
                    cv2.putText(img,f"roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                     cv2.putText(img,"UNKNOWN FACE",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) 

                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,255,255),"face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()        
                