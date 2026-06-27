from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognisation import Face_Recognition


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
       
        #first image
        img1=Image.open(r"D:\FRAS python\images\1.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img2=Image.open(r"D:\FRAS python\images\2.png")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third image
        img4=Image.open(r"D:\FRAS python\images\3.jpg")
        img4=img4.resize((550,130),Image.Resampling.LANCZOS)

        self.photoimage3=ImageTk.PhotoImage(img4)
        f_lbl=Label(self.root,image=self.photoimage3)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image
        img=Image.open(r"D:\FRAS python\images\bg.png")
        img=img.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimage)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label (bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)  
        
        #student button     
        img4=Image.open(r"D:\FRAS python\images\student 4.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimage4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
             

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)



        #detect face button     
        img5=Image.open(r"D:\FRAS python\images\face detection5.png")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimage5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)
             

        b2_2=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b2_2.place(x=500,y=300,width=220,height=40)
                     
        #session logs button     
        img6=Image.open(r"D:\FRAS python\images\logs6.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimage6,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)
             

        b3_3=Button(bg_img,text="SESSION LOGS",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b3_3.place(x=800,y=300,width=220,height=40)    

        #help button     
        img7=Image.open(r"D:\FRAS python\images\HELP6.png")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimage7,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)
             

        b4_4=Button(bg_img,text="HELP CENTER",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b4_4.place(x=1100,y=300,width=220,height=40)                           


        #train button     
        img8=Image.open(r"D:\FRAS python\images\traning 8.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimage8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=400,width=220,height=220)
             

        b5_5=Button(bg_img,text="MODEL TRAINING",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b5_5.place(x=200,y=600,width=220,height=40)  

        #detect face button     
        img9=Image.open(r"D:\FRAS python\images\DATA9.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimage9,cursor="hand2",command=self.open_image)
        b6.place(x=500,y=400,width=220,height=220)
             

        b6_6=Button(bg_img,text="PHOTOS LIBRARY",cursor="hand2",command=self.open_image,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b6_6.place(x=500,y=600,width=220,height=40)                   

        #DEVELOPER button     
        img10=Image.open(r"D:\FRAS python\images\DEVELOPER10.png")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimage10,cursor="hand2")
        b7.place(x=800,y=400,width=220,height=220)
             

        b7_7=Button(bg_img,text="DELOPER CONSOLE",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b7_7.place(x=800,y=600,width=220,height=40)  

        #log out button     
        img11=Image.open(r"D:\FRAS python\images\log out 11.png")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimage11,cursor="hand2")
        b8.place(x=1100,y=400,width=220,height=220)
             

        b8_8=Button(bg_img,text="LOG OUT",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b8_8.place(x=1100,y=600,width=220,height=40)  

    def open_image(self):
        os.startfile("data")


                    ##################Function button##############
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)            
    
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)      
   
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)   





if __name__ == "__main__":

    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
           