from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox 

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

     ###########variable#############
        self.var_dep=StringVar()
        self.var_course=StringVar()     
        self.var_year=StringVar()     
        self.var_semester=StringVar()     
        self.var_id=StringVar()     
        self.var_name=StringVar()     
        self.var_div=StringVar()     
        self.var_roll=StringVar()     
        self.var_gender=StringVar()     
        self.var_dob=StringVar()     
        self.var_email=StringVar()     
        self.var_phone=StringVar()     
        self.var_address=StringVar()     
        self.var_teacher=StringVar()     

        #first image
        img1=Image.open(r"images\1.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img2=Image.open(r"images\2.png")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third image
        img4=Image.open(r"images\3.jpg")
        img4=img4.resize((550,130),Image.Resampling.LANCZOS)

        self.photoimage3=ImageTk.PhotoImage(img4)
        f_lbl=Label(self.root,image=self.photoimage3)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image
        img=Image.open(r"images\bg.png")
        img=img.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimage)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label (bg_img,text="STUDENT MANAGMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)   

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=12,y=55,width=1500,height=600) 

        #left side label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold")) 
        Left_frame.place(x=10,y=10,width=760,height=580)   

        img_left=Image.open(r"D:\FRAS python\images\traning 8.jpg")
        img_left=img_left.resize((750,130),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimage)
        f_lbl.place(x=5,y=0,width=750,height=130)

        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current cource information",font=("times new roman",12,"bold")) 
        current_course_frame.place(x=5,y=135,width=760,height=125)   

        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg='white')
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"))
        dep_combo['values']=("Select Depatments",'computer','it','civil','mechanical')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
        course_label=Label(current_course_frame,text='Course',font=("times new roman",13,'bold'),bg='white')
        course_label.grid(row=0,column=2,padx=10,sticky=W) 

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,'bold'),width=20)     
        course_combo['values']=("Select course",'FF','SE','TE','BE')
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10,sticky=W)

        #year
        
        year_label = Label(current_course_frame, text="Year",font=('times new roman',13,'bold'), bg='white')
        year_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=('times new roman',13,'bold'), width=20)
        year_combo['values'] = ("Select year",'1','2','3','4')
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, sticky=W)
         
        #Semester
        semester_label = Label(current_course_frame, text='Semester',font=("times new roman",13,'bold'), bg='white')
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,'bold'), width=20)
        semester_combo['values'] = ("Select semester",'1','2','3','4')
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=10, sticky=W)

        #class student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="class student information",font=("times new roman",12,"bold")) 
        class_Student_frame.place(x=5,y=250,width=760,height=300)   

        
        #student id
        studentId_label=Label(class_Student_frame,text='StudentID',
                              font=("times new roman",13,'bold'),bg='white') 
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,
                                  textvariable=self.var_id,
                                  width=20,
                                  font=("times new roman",13,'bold'))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #studen name
        studentName_label=Label(class_Student_frame,
                                text='StudentName',font=("times new roman",13,'bold'),bg='white') 
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,'bold'))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)

        #class division
        class_div_label=Label(class_Student_frame,text='classdivision',font=("times new roman",13,'bold'),bg='white') 
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        class_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,'bold'))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll no
        roll_no_label=Label(class_Student_frame,text='roll no',font=("times new roman",13,'bold'),bg='white') 
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,'bold'))
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #Gender
        gender_label=Label(class_Student_frame,text='Gender',font=("times new roman",13,'bold'),bg='white') 
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,'bold'))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_Student_frame,text='dob',font=("times new roman",13,'bold'),bg='white') 
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob, width=20, font=("times new roman",13,'bold'))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
      
        #email
        email_label=Label(class_Student_frame,text='email',font=("times new roman",13,'bold'),bg='white') 
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,'bold'))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
       
        #phone no
        phone_div_label=Label(class_Student_frame,text='phone no',font=("times new roman",13,'bold'),bg='white') 
        phone_div_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,'bold'))
        phone_div_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #address
        address_div_label=Label(class_Student_frame,text='address',font=("times new roman",13,'bold'),bg='white') 
        address_div_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,'bold'))
        address_div_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
      
        #teacher name
        teacher_div_label=Label(class_Student_frame,text='Teacher name',font=("times new roman",13,'bold'),bg='white') 
        teacher_div_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,'bold'))
        teacher_div_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        #radio buttons
        self.var_radio=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio,text="Take photo sample",value="yes")
        radiobtn1.grid(row=6,column=0)
         
        self.var_radio=StringVar() 
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio,text="No photo sample",value="no")
        radiobtn2.grid(row=6,column=1)    
        #buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)  

        #savebutton
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        #updATE     
        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        #delete                
        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        #reset                 
        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)  

         #take photo sample               
        takesample_btn=Button(btn_frame1,text="Take a photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        takesample_btn.grid(row=0,column=0)              
         # updtephoto    
        updatephoto_btn=Button(btn_frame1,text="Update photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=0,column=1)              
              
      

        #right side label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold")) 
        Right_frame.place(x=780,y=10,width=720,height=580)  
        
        img_Right=Image.open(r"D:\FRAS python\images\stu.jpg")
        img_Right=img_Right.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimage_Right=ImageTk.PhotoImage(img_Right)

        f_lbl=Label(Right_frame,image=self.photoimage_Right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #========search system==========#
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",12,"bold")) 
        search_frame.place(x=5,y=135,width=710,height=70)  

        search_label=Label(search_frame,text='Search By',font=("times new roman",15,'bold'),bg='red',fg='white') 
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo = ttk.Combobox(search_frame,font=("times new roman",13,'bold'), width=15)
        search_combo['values'] = ("Select ","Roll_no","phone_no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,'bold'))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)        


        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame,text="Show_All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)        
#table#####################################
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE) 
        table_frame.place(x=5,y=210,width=710,height=350) 

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","gender","phone","address","photo","teacher"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="photosamplestatus")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.column("dep",width=100)
    ##########function delaration#############
     
    def add_data(self):
        if (
            self.var_dep.get() == "Select Depatments" or
            self.var_name.get() == "" or
            self.var_id.get() == "" or
            self.var_year.get() == "Select year" or
            self.var_semester.get() == "Select semester" or
            self.var_phone.get() == "" or
            self.var_roll.get() == "" or
            self.var_course.get() == "Select course"
        ):
            messagebox.showerror("Error", "All fields are required")
        else:
            pass


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
           