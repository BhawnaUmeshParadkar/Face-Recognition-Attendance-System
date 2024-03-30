from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):

        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")



        # variables
        self.var_attendence_name=StringVar()
        self.var_attendence_dep=StringVar()
        self.var_attendence_des=StringVar()
        self.var_attendence_time=StringVar()
        self.var_attendence_date=StringVar()
        self.var_attendence=StringVar()


        #first image
        img=Image.open("images/developer.jpg")
        img=img.resize((500,150), Image.LANCZOS)
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
        img2=img2.resize((550,150), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


         # bg img

        img3=Image.open("images/plain-bg.png")
        img3=img3.resize((1530,710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="Attendance Management System",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # frame

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        # left frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendane  Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open("images/office.png")
        img_left=img_left.resize((720,145), Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=725,height=370)

        # labels and entrys



        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


# Employee name      
        Name_label=Label(left_inside_frame,text="Employee Name:",font=("times new roman",13,"bold"),bg="white")
        Name_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendence_name,font=("times new roman",13,"bold"))
        Name_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)  


# Department   
        class_div_label=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendence_dep,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W) 


        # designation
        des_label=Label(left_inside_frame,text="Designation",font=("times new roman",13,"bold"),bg="white")
        des_label.grid(row=1,column=0,padx=10,sticky=W) 

        class_div_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendence_des,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W) 


# time
        time_label=Label(left_inside_frame,text="Time",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=1,column=2,padx=10,sticky=W) 

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendence_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W) 
# date
        date_label=Label(left_inside_frame,text="Date",font=("times new roman",13,"bold"),bg="white")
        date_label.grid(row=2,column=0,padx=10,sticky=W) 

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attendence_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W) 


     # Attendance
        a_label=Label(left_inside_frame,text="Attendance Status",font=("times new roman",13,"bold"),bg="white")
        a_label.grid(row=3,column=1)

        self.a_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_attendence,font="comicsansns 11 bold",state="readonly")
        self.a_status["values"]=("Status","Present","Absent")
        self.a_status.grid(row=3,column=2,pady=8)
        self.a_status.current(0)
# buttons
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")  
        btn_frame.place(x=0,y=300,width=715,height=35) 


        ImportCSV_btn=Button(btn_frame,text="ImportCSV",command=self.import_csv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        ImportCSV_btn.grid(row=0,column=0)

        ExportCSV_btn=Button(btn_frame,text="ExportCSV",command=self.export_csv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        ExportCSV_btn.grid(row=0,column=1)


        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


   
# right framr

        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")  
        table_frame.place(x=5,y=5,width=700,height=455) 

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReport_table=ttk.Treeview(table_frame,columns=("EmpName","Department","Designation","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReport_table.xview)
        scroll_y.config(command=self.AttendanceReport_table.yview)

        self.AttendanceReport_table.heading("EmpName",text="EmpName")
        self.AttendanceReport_table.heading("Department",text="Department")
        self.AttendanceReport_table.heading("Designation",text="Designation")
        self.AttendanceReport_table.heading("time",text="Time")
        self.AttendanceReport_table.heading("date",text="Date")
        
        self.AttendanceReport_table.heading("attendance",text="Attendance")

        self.AttendanceReport_table["show"]="headings"

        self.AttendanceReport_table.column("EmpName",width=100)
        self.AttendanceReport_table.column("Department",width=100)
        self.AttendanceReport_table.column("Designation",width=100)
        self.AttendanceReport_table.column("time",width=100)
        self.AttendanceReport_table.column("date",width=100)
        self.AttendanceReport_table.column("attendance",width=100)

        self.AttendanceReport_table.pack(fill=BOTH,expand=1)

        self.AttendanceReport_table.bind("<ButtonRelease>",self.get_cursor)

        # fetch data
    def fetch_data(self,rows) :
        self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())
        for i in rows:
            self.AttendanceReport_table.insert("",END,values=i)

# import csv
    def import_csv(self):
        global mydata 
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open csv", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)   

# export csv
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save csv", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline='') as myfile:
                csvwriter = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    csvwriter.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+" successfully")    
               

        except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReport_table.focus()
        content=self.AttendanceReport_table.item(cursor_row)  
        row=content['values']
        self.var_attendence_name.set(row[0])    
        self.var_attendence_dep.set(row[1])  
        self.var_attendence_des.set(row[2])  
        self.var_attendence_time.set(row[3]) 
        self.var_attendence_date.set(row[4])
        self.var_attendence.set(row[5]) 

        
    def reset_data(self):
        
        self.var_attendence_name.set("")    
        self.var_attendence_dep.set("")  
        self.var_attendence_des.set("")  
        self.var_attendence_time.set("") 
        self.var_attendence_date.set("")
        self.var_attendence.set("")                           
                                  

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()