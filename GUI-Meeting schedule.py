from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('ตารางการประชุม')
GUI.geometry('500x400')
GUI['bg'] = 'yellow'

L1 = Label(GUI,text='ตารางการประชุมปี 2023',font=('Angsana New',30),fg='blue')
L1.place(x=30,y=20)

def Button2():
    text = 'ทีมการตลาด 11.00-12.00น.'
    messagebox.showinfo('31 มกราคม',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='เดือนมกราคม',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = 'ทีมฝ่ายขาย 14.00-15.00น.'
    messagebox.showinfo('28 กุมภาพันธ์',text)

FB2 = Frame(GUI)
FB2.place(x=100,y=180)
B3 = ttk.Button(FB1,text='เดือนกุมภาพันธ์',command=Button3)
B3.pack(ipadx=20,ipady=20)
