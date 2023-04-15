import pyttsx3
from tkinter import *
from PIL import Image,ImageTk
from googletrans import Translator

#windowform
root=Tk()
root.title('PHIÊN DỊCH')
root.geometry('800x500')
load=Image.open('background.jpg')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)

name=Label(root,text='PHIÊN DỊCH',fg='black',bd=0,bg='#FBFBFB')
name.config(font=('Helvetica',30))
name.pack(pady=10)

box1=Text(root,width=28,height=8,font=("ROBOTO",16))
box1.place(x=20,y=80)

box2=Text(root,width=28,height=8,font=("ROBOTO",16))
box2.place(x=420,y=80)

Button_frame=Frame(root).pack(side=BOTTOM)
def clear():
    box1.delete(1.0,END)
    box2.delete(1.0,END)
def translate():
    INPUT = box1.get(1.0,END)
    print(INPUT)
    t = Translator()
    a = t.translate(INPUT, src='vi', dest='en')
    b=a.text 
    box2.insert(END,b)
def speach():
    SPEACH = box2.get(1.0,END)
    e = pyttsx3.init()
    e.say(SPEACH)
    e.runAndWait()

trans_button=Button(Button_frame,text='Dịch',height=2,width=10, font=(('Arial'),10,'bold'),bg='#303030',fg='#FFFFFF',command=translate)
trans_button.place(x=20,y=300) 
clear_button=Button(Button_frame,text='Xóa',height=2,width=10, font=(('Arial'),10,'bold'),bg='#303030',fg='#FFFFFF',command=clear)
clear_button.place(x=140,y=300)
clear_button=Button(Button_frame,text='Đọc',height=2,width=10, font=(('Arial'),10,'bold'),bg='#303030',fg='#FFFFFF',command=speach)
clear_button.place(x=260,y=300)  
    
root.mainloop()