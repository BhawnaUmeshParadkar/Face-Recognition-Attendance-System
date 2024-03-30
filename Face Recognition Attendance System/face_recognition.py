from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os
import numpy as np
 

class Face_recognition:
    def __init__(self,root):

        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=55)

        img_top=Image.open("images/recognize.png")
        img_top=img_top.resize((900,700), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        img_top2=Image.open("images/trainingjpg.jpg")
        img_top2=img_top2.resize((950,700), Image.LANCZOS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)
        f_lbl=Label(self.root,image=self.photoimg_top2)
        f_lbl.place(x=650,y=55,width=950,height=700)

        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="green")
        b1_1.place(x=365,y=620,width=200,height=40)

        # ---------Attendance-----------
    def mark_attendance(self,n,d,des):
        with open("faceAttendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((n not in name_list) and (d not in name_list) and (des not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{d},{des},{dtstring},{d1},present")


# face recognition
    def face_recog(self):
        def draw_boundry(img,classifier,scalefactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbours)
            co_ord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Magic@123", database="facedetector")
                my_cursor = conn.cursor()
                my_cursor.execute("select EmpName from student where EmpId="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select dep from student where EmpId="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select designation from student where EmpId="+str(id))
                des=my_cursor.fetchone()
                des="+".join(des)


                #my_cursor.execute("select EmpId from student where EmpId="+str(id))
                #i=my_cursor.fetchone()
                #i="+".join((i))



                if confidence>77:
                    #cv2.putText(img,f"id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"designation:{des}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(n,d,des)
               
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)    

                co_ord=[x,y,w,h]  
            
            return co_ord  

        def recognize(img,clf,faceCascade):
            co_ord=draw_boundry(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,face_cascade)
            cv2.imshow("Welcome to face recognition",img)
            

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()


