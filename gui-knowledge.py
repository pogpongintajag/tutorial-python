from tkinter import  *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI =Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี้คือชื้อโปรแกรม
GUI.geometry( '500x400')#นี้คือขนาดโปรแกรม

L1 =Label(GUI,text='โปรแกรมบันทึกเงินในบัญชีมีอยู่',font=('Angsana New',30),fg='green')
L1.place(x=30,y=40)
#########################
def Button2():
    text= 'ตอนนี่มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1=Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=80)
B2 = ttk. Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=120)

GUI.mainloop()
