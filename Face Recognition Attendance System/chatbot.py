from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from openai import OpenAI
import os
from dotenv import load_dotenv

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("790x790+0+0")
        self.root.bind('<Return>', self.enter_func)

        main_frame = Frame(self.root, bd=4, bg='powder blue', width=790)
        main_frame.pack()

        img_chat = Image.open('images/chatbot.jpg')
        img_chat = img_chat.resize((80, 80), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, compound=LEFT, image=self.photoimg,
                            text="Have any queries? Feel free to ask...", font=('arial', 25, 'bold'), fg='grey', bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('arial', 14),
                         yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frm = Frame(self.root, bd=4, bg='white', width=730)
        btn_frm.pack()

        label = Label(btn_frm, text=" Ask your query: ", font=('arial', 14, 'bold'), fg='green', bg='white')
        label.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = ttk.Entry(btn_frm, width=40, font=('times new roman', 16, 'bold'))
        self.entry.grid(row=0, column=1, padx=5, sticky=W)

        self.send_btn = Button(btn_frm, text="SEND", command=self.send_message, width=8, font=('arial', 15, 'bold'), bg='green', fg='white')
        self.send_btn.grid(row=0, column=2, padx=5, sticky=W)

        self.clear_btn = Button(btn_frm, text="Clear chat", command=self.clear_data, width=8, font=('arial', 15, 'bold'), bg='#000000', fg='white')
        self.clear_btn.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label1 = Label(btn_frm, text=self.msg, font=('arial', 14, 'bold'), fg='red', bg='white')
        self.label1.grid(row=0, column=0, padx=5, sticky=W)

        # Initialize chatbot API
        load_dotenv()
        self.client = OpenAI(
            base_url="https://api-inference.huggingface.co/v1",
            api_key=os.environ.get('HUGGINGFACEHUB_API_TOKEN')
        )

    def enter_func(self, event):
        self.send_message() 

    def send_message(self):
        user_input = self.entry.get().strip()

        if not user_input:
            self.msg = 'Please enter some input'
            self.label1.config(text=self.msg, fg='red')
            return

        self.text.insert(END, '\n\nYou: ' + user_input)

        # Retrieve response from the chatbot
        response = self.chat_with_bot(user_input)

        self.text.insert(END, '\n\nBot: ' + response)

        self.entry.delete(0, END)  # Clear the entry field

        self.text.yview(END)

    def clear_data(self):
        self.text.delete(1.0, END)
        self.entry.delete(0, END)

    def chat_with_bot(self, user_input):
        # Fetch the response from the chatbot API
        response = self.client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=[{"role": "user", "content": user_input}, {"role": "assistant", "content": "I am an assistant for a Face Recognition based Employee Attendance System Project. I am helplful and nice and give short answers on my project under 60 words. Features of my project are- training facial data, marking attandence by identifying face of employees. User need to go to train section of the app to train the system to identify their face and mark the attendance. Don't forget to greet people."}],
            temperature=0.5,
            max_tokens=100,
        )

        # Access the content of the response
        content = response.choices[0].message.content

        return content

if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
