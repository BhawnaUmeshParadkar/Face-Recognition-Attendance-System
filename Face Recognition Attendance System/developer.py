from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class developer:
    def __init__(self,root):

        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=55)

        img_top=Image.open("images/devloper_insideimg.jpg")
        img_top=img_top.resize((1530,740), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=740)




#frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=55,width=500,height=600)

# info
        
        intro_lbl=Label(main_frame,text="Hello,I am Bhawna Paradkar",font=("times new roman",20,"bold"),bg="white",fg="black")
        intro_lbl.place(x=0,y=5)


        intro_lbl=Label(main_frame,text="Introducing our Face RecoIgnition Attendance System using:",font=("times new roman",14,"bold"),bg="white",fg="black")
        intro_lbl.place(x=0,y=45)

        intro_lbl=Label(main_frame,text="\nPython\n"+"\nTKinter\n"+"\nOpenCV\n"+"\nMySql\n"+"\nPandas\n"+"\nLLM\n"+"\nLBPH Algorithm\n"+"\nHaar cascade Algorithm\n",font=("times new roman",13,"bold"),bg="white",fg="black")
        intro_lbl.place(x=0,y=70)




if __name__ == "__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()

