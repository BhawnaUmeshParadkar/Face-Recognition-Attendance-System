import os
import tkinter
import sqlite3
import subprocess
from tkinter import *
from train import Train
from tkinter import ttk
from time import strftime
from employee import Employee
from chatbot import ChatBot
from datetime import datetime
from PIL import Image,ImageTk
from tkinter import messagebox
from developer import developer
from attendance import Attendance
from face_recognition import Face_recognition
 
# Connect to SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')
conn.commit()

def register():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username already exists
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    if username != '':
        if c.fetchone() is not None:
            messagebox.showwarning('Registration failed', 'Username already exists')
            return
    else:
            messagebox.showinfo('Warning', 'Please provide valid username') 
    
    # Insert new user into database
    c.execute('INSERT INTO users VALUES (?, ?)', (username, password))
    conn.commit()

    messagebox.showinfo('Registration successful', 'You can now log in')

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password match a record in the database
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    if username != '':
        if c.fetchone() is not None:    
        
            messagebox.showinfo('Login successful', 'Welcome, ' + username)

            class Face_Recognition_System:
                
                def Exit_(self):
                        self.Exit_=tkinter.messagebox.askyesno("Face recognition","Are you want to exit this project",parent=self.root)
                        if self.Exit_ > 0:
                                self.root.destroy()
                                # specify the path of your .bat file
                                bat_file_path = "project.bat"

                                # use subprocess.run() to execute the .bat file
                                subprocess.run([bat_file_path], shell=True)
                        else:
                                return        

                def face_data(self):
                            self.new_window=Toplevel(self.root)
                            self.app=Face_recognition(self.new_window)
                def train_data(self):
                            self.new_window=Toplevel(self.root)
                            self.app=Train(self.new_window)
                def developer_data(self):
                            self.new_window=Toplevel(self.root)
                            self.app=developer(self.new_window)
                def attendance_data(self):
                            self.new_window=Toplevel(self.root)
                            self.app=Attendance(self.new_window)
                def employee_details(self):
                            self.new_window=Toplevel(self.root)
                            self.app=Employee(self.new_window)
                def chatbot(self):
                    self.new_window=Toplevel(self.root)
                    self.app=ChatBot(self.new_window)
                def open_img(self):
                    os.startfile("data")
                def __init__(self,root):
                    self.root=root
                    self.root.geometry("1530x790+0+0")
                    self.root.title("face Recognition System")
            

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

                    title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="black",fg="white")
                    title_lbl.place(x=5,y=5,width=1530,height="45")
                    
                    # time
                    # def time():
                    #         string = strftime('%H:%M:%S %p')
                    #         lbl.config(text = string)
                    #         lbl.after(1000, time)

                    # lbl =Label(title_lbl, font=('times new roman', 14, 'bold'), background ='white', foreground = 'blue') 
                    # lbl.place(x=0,y=(-15), width=110,height=50)
                    # time()

                    # Employee button
                    img4=Image.open("images/Employee-Information.jpg")
                    img4=img4.resize((300,300))
                    self.photoimg4=ImageTk.PhotoImage(img4)

                    b1=Button(bg_img,image=self.photoimg4,command=self.employee_details,cursor="hand2")
                    b1.place(x=200,y=100,width=300,height=220)

                    b1_1=Button(bg_img,text="Employee Details",command=self.employee_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
                    b1_1.place(x=200,y=300,width=300,height=40)

                    # Detect face button
                    img5=Image.open("images/Facial-Recognition-9.png")
                    img5=img5.resize((300,300), Image.LANCZOS)
                    self.photoimg5=ImageTk.PhotoImage(img5)

                    b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
                    b1.place(x=500,y=100,width=300,height=220)

                    b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black",fg="white")
                    b1_1.place(x=500,y=300,width=300,height=40)



                    # Attendance face button
                    img6=Image.open("images/attendance.jpeg")
                    img6=img6.resize((300,300), Image.LANCZOS)
                    self.photoimg6=ImageTk.PhotoImage(img6)

                    b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
                    b1.place(x=800,y=100,width=300,height=220)

                    b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black",fg="white")
                    b1_1.place(x=800,y=300,width=300,height=40)



                    # Help Desk button
                    img7=Image.open("images/chat-bot.jpg")
                    img7=img7.resize((300,300), Image.LANCZOS)
                    self.photoimg7=ImageTk.PhotoImage(img7)

                    b1=Button(bg_img,image=self.photoimg7,cursor="hand2", command=self.chatbot)
                    b1.place(x=1100,y=100,width=300,height=220)

                    b1_1=Button(bg_img,text="AI Assistant",cursor="hand2", command=self.chatbot, font=("times new roman",15,"bold"),bg="black",fg="white")
                    b1_1.place(x=1100,y=300,width=300,height=40)



                    # Train data
                    img8=Image.open("images/traindata.png")
                    img8=img8.resize((300,300), Image.LANCZOS)
                    self.photoimg8=ImageTk.PhotoImage(img8)

                    b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
                    b1.place(x=200,y=380,width=300,height=220)

                    b1_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="white")
                    b1_1.place(x=200,y=580,width=300,height=40)



                    # photos face button
                    img9=Image.open("images/face.jpg")
                    img9=img9.resize((300,300), Image.LANCZOS)
                    self.photoimg9=ImageTk.PhotoImage(img9)

                    b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
                    b1.place(x=500,y=380,width=300,height=220)

                    b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="white")
                    b1_1.place(x=500,y=580,width=300,height=40)



                    # Developer button
                    img10=Image.open("images/photos.jpg")
                    img10=img10.resize((300,300), Image.LANCZOS)
                    self.photoimg10=ImageTk.PhotoImage(img10)

                    b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
                    b1.place(x=800,y=380,width=300,height=220)

                    b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="black",fg="white")
                    b1_1.place(x=800,y=580,width=300,height=40)



                    # Exit  button
                    img11=Image.open("images/exit.jpg")
                    img11=img11.resize((300,300), Image.LANCZOS)
                    self.photoimg11=ImageTk.PhotoImage(img11)

                    b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.Exit_)
                    b1.place(x=1100,y=380,width=300,height=220)

                    b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.Exit_,font=("times new roman",15,"bold"),bg="black",fg="white")
                    b1_1.place(x=1100,y=580,width=300,height=40)
            obj=Face_Recognition_System(root)
            root.mainloop()
        else:
           messagebox.showwarning('Login failed', 'Invalid username or password')
    else:
        messagebox.showinfo('Warning', 'Please provide valid username') 

root = Tk()
root.title('Login / Register')

font = ('Helvetica', 16)  # Increase font size

username_label = Label(root, text='Username:', font=font)
username_label.pack(pady=10)  # Add padding
username_entry = Entry(root, font=font)
username_entry.pack(pady=10)  # Add padding

password_label = Label(root, text='Password:', font=font)
password_label.pack(pady=10)  # Add padding
password_entry = Entry(root, show='*', font=font)
password_entry.pack(pady=10)  # Add padding

login_button = Button(root, text='Login', command=login, font=font)
login_button.pack(pady=10)  # Add padding

register_button = Button(root, text='Register', command=register, font=font)
register_button.pack(pady=10)  # Add padding

if __name__ == "__main__":
    root.geometry("1530x790+0+0")
    root.mainloop()