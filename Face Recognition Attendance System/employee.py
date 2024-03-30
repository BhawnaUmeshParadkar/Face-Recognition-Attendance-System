
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

# Changed Student to Employee in this file

class Employee:
    def __init__(self,root):

        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        # *****variables*******
        self.var_dep=StringVar()
        self.var_designation=StringVar()
        self.var_year=StringVar()
        self.var_empType=StringVar()
        self.var_EmpId=StringVar()
        self.var_EmpName=StringVar()
        self.var_section=StringVar()
        self.var_salary=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_remark=StringVar()


        #first image
        img=Image.open("images/developer.jpg")
        img=img.resize((500,130), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # #second image
        img1=Image.open("images/bg_img.jpg")
        img1=img1.resize((130,130), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # #third image
        img2=Image.open("images/developer.jpg")
        img2=img2.resize((550,130), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)



        # bg img

        img3=Image.open("images/plain-bg.png")
        img3=img3.resize((1530,710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)




        title_lbl=Label(bg_img,text="Employee Management System",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)


# frame

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)
# left label frame

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee  Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)


        img_left=Image.open("images/facedetector.jpg")
        img_left=img_left.resize((720,130), Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)


        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
# current course
        employee_info_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Employee Information",font=("times new roman",12,"bold"))
        employee_info_frame.place(x=5,y=135,width=720,height=115)
# Department
        dep_label=Label(employee_info_frame,text="Department Name",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(employee_info_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","IT & ERP","Admin","DNW","CED")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
# Designation

        course_label=Label(employee_info_frame,text="Designation",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(employee_info_frame,textvariable=self.var_designation,font=("times new roman",13,"bold"),state="read only",width=20)
        course_combo["values"]=("Select designation","GM","AGM","DGM","Administrative","Engineer")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


#  Joining Year

        year_label=Label(employee_info_frame,text="Joining Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(employee_info_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","2021","2022","2023","2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


# Employement Type

        semester_label=Label(employee_info_frame,text="EmployeeType",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(employee_info_frame,textvariable=self.var_empType,font=("times new roman",13,"bold"),state="read only",width=20)
        semester_combo["values"]=("Select Emp_type","Permanant","Contract based","Apprenticeship ","Trainees")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


# class student information
        class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

# Employee id
        studentId_label=Label(class_student_frame,text="EmployeeId:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_EmpId,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

# Employee name      
        studentName_label=Label(class_student_frame,text="Employee Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_EmpName,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)  


# Department   
        class_div_label=Label(class_student_frame,text="Section:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_section,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)  

# Salary    
        roll_no_label=Label(class_student_frame,text="Salary:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_salary,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)  


# Gender     
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

       # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W) 

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="read only",width=18)
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)





 # DOB    
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)  


# Email      
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)  



# phone no     
        phone_label=Label(class_student_frame,text="contact No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)  

 # Address     
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)  


# Remark
        address_label=Label(class_student_frame,text="Remark:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_remark,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)  



# radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes") 
        radiobtn1.grid(row=6,column=0) 

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No") 
        radiobtn2.grid(row=6,column=1)  
# button frames
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")  
        btn_frame.place(x=0,y=200,width=715,height=35) 


        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)


        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")  
        btn_frame1.place(x=0,y=235,width=715,height=35) 


        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take  photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)


        update_photo_btn=Button(btn_frame1,text="Update  photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
          

# right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)


        img_right=Image.open("images/facedetector.jpg")
        img_right=img_right.resize((720,130), Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)


        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)
# search system

        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)


        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="green")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="read only",width=15)
        search_combo["values"]=("Select ","ID","Name","Dep","Designation")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W) 



        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")

        showAll_btn.grid(row=0,column=4,padx=4)
# table frame

        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Department","Designation","Year","Emp_type","EmpId","EmpName","Section","Salary","gender","dob","email","phone","address","Remark","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

       
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Designation",text="Designation") 
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Emp_type",text="Emp_type") 
        self.student_table.heading("EmpId",text="EmpId") 
        self.student_table.heading("EmpName",text="EmpName")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Salary",text="Salary")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("dob",text="dob")
        self.student_table.heading("email",text="email") 
        self.student_table.heading("phone",text="phone")
        self.student_table.heading("address",text="address")
        self.student_table.heading("Remark",text="Remark")
        self.student_table.heading("Photo",text="ImgSampleStatus")
        self.student_table["show"]="headings"

        
        self.student_table.column("Department",width=100)
        self.student_table.column("Designation",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Emp_type",width=100)
        self.student_table.column("EmpId",width=100)
        self.student_table.column("EmpName",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Salary",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("Remark",width=100)
        self.student_table.column("Photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

   #function

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_EmpName.get()=="" or self.var_EmpId.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
             try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Magic@123", database="facedetector")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_dep.get(),
                        self.var_designation.get(),
                        self.var_year.get(),
                        self.var_empType.get(),
                        self.var_EmpId.get(),
                        self.var_EmpName.get(),
                        self.var_section.get(),
                        self.var_salary.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_remark.get(),
                        self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Data added successfully", parent=self.root)
                
             except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)
      # fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Magic@123", database="facedetector")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit() 
        conn.close()  
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)  
        data=content["values"]       

        self.var_dep.set(data[0]),
        self.var_designation.set(data[1]),
        self.var_year.set(data[2]),
        self.var_empType.set(data[3]),
        self.var_EmpId.set(data[4]),
        self.var_EmpName.set(data[5]),
        self.var_section.set(data[6]),
        self.var_salary.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_remark.set(data[13]),
        self.var_radio1.set(data[14])

#update function
    def update_data(self):
         if self.var_dep.get()=="Select Department" or self.var_EmpName.get()=="" or self.var_EmpId.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=self.root)

         else:
             try:
                 update=messagebox.askyesno("Update","Do you want to update details",parent=self.root) 
                 if update:
                     conn = mysql.connector.connect(host="localhost", username="root", password="Magic@123", database="facedetector")
                     my_cursor = conn.cursor()
                     my_cursor.execute("UPDATE student SET dep=%s,designation=%s,year=%s,empType=%s,EmpName=%s,section=%s,salary=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,remark=%s,PhotoSample=%s where EmpId=%s",(
                        self.var_dep.get(),
                        self.var_designation.get(),
                        self.var_year.get(),
                        self.var_empType.get(),
                        
                        self.var_EmpName.get(),
                        self.var_section.get(),
                        self.var_salary.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_remark.get(),
                        self.var_radio1.get(),
                        self.var_EmpId.get()
                        ))

                 else:
                     if not update:
                         return
                 messagebox.showinfo("Success","Employee details successfully update",parent=self.root)
                 conn.commit()
                 self.fetch_data()
                 
                 conn.close()
             except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# delete function
    def delete_data(self):
        if self.var_EmpId.get()=="":
            messagebox.showerror("Error","Employee id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Employee delete page","Do you want to delete this employee",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Magic@123", database="facedetector")
                    my_cursor = conn.cursor()
                    sql="delete from student where EmpId=%s"
                    val=(self.var_EmpId.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return  
                conn.commit()
                self.fetch_data()
                 
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted employee details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




#reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_designation.set("Select designation")
        self.var_year.set("Select Year")
        self.var_empType
        self.set("Select Emp_type")
        self.var_EmpId.set("")
        self.var_EmpName.set("")
        self.var_section.set("")
        self.var_salary.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_remark.set("")
        self.var_radio1.set("")



        # ***** generate data set take photo sample *****
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_EmpName.get()=="" or self.var_EmpId.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
             try:
                 conn = mysql.connector.connect(host="localhost", username="root", password="Magic@123", database="facedetector")
                 my_cursor = conn.cursor()
                 my_cursor.execute("select * from student")
                 myresult=my_cursor.fetchall()
                 id=0
                 for x in myresult:
                     id+=1

                 my_cursor.execute("UPDATE student SET dep=%s,designation=%s,year=%s,empType=%s,EmpName=%s,section=%s,salary=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,remark=%s,PhotoSample=%s where EmpId=%s",(
                        self.var_dep.get(),
                        self.var_designation.get(),
                        self.var_year.get(),
                        self.var_empType.get(),
                        
                        self.var_EmpName.get(),
                        self.var_section.get(),
                        self.var_salary.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_remark.get(),
                        self.var_radio1.get(),
                        self.var_EmpId.get()==id+1

                        ))
                 conn.commit()
                 self.fetch_data()
                 #self.reset_data()
                 conn.close()


                 # load predefind data on face frontals from open cv
                 face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                 def face_cropped(img):
                     grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                     faces=face_classifier.detectMultiScale(grey,1.3,5)
                     #scaling factor=1.3
                     #minimum neighbour=5

                     for(x,y,w,h) in faces:
                         face_cropped=img[y:y+h,x:x+w]
                         return face_cropped
                     
                 cap=cv2.VideoCapture(0)
                 img_id=0
                 while True:
                        ret,myframe=cap.read()
                        if face_cropped(myframe) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(myframe),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("cropped face",face)

                        
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                             break
                 cap.release()
                 cv2.destroyAllWindows()
                 messagebox.showinfo("result","generating data sets completed") 





             except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()








