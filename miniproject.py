from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("1300x900")
root.resizable(False,False)
root.title("ATTENDANCE MANAGEMENT SYSTEM")

def exit_gui():
    root.destroy()


def t_click():
    tusername=tuservalue.get()
    tpassword=tpassvalue.get()
    if tpassword=="123456":
        with open("teacher_recors.txt","a") as f:
            f.write(f"attendance recorded of (Mr/Mrs/Ms) {tuservalue.get()}\n")
        tmsg.showinfo("Attendance record","Your attendance has been recorded")
    else:
        tmsg.showinfo("Attendance record","Your PASSWORD is incorrect")


def onClick():
    username=uservalue.get()
    password=passvalue.get()
    if len(username)== 6 and password=="password":
        with open("students_records.txt","a") as f:
             f.write(f"attendance recorded of student {uservalue.get()}\n")
        tmsg.showinfo("Attendance record",  "Your attendance has been recorded")
    else:
        tmsg.showinfo("Attendance record","Either your USERNAME or PASSWORD is incorrect")

uservalue=None
passvalue=None
tuservalue=None
tpassvalue=None

def t_login():
       third_frame=Frame(bg="#d0ebdd")
       third_frame.place(x=0,y=0,width=1300,height=900)
       text_heading = Label(third_frame,text="ATTENDANCE MANAGEMENT SYSTEM", bg="#115566", fg="#ffffff",borderwidth=20,relief=FLAT,
                                            font="calibri 30 bold",pady=30)
       text_heading2 = Label(third_frame,text="**** Your username is your name****\n **** NATIONAL POST GRADUATE COLLEGE****", bg="#115566", fg="#bbeeee",borderwidth=5,relief=RIDGE,
                                            font="calibri 18 bold",pady=10)
       text_heading.pack(padx=200,fill=X)
       text_heading2.pack(side=BOTTOM,padx=300,pady=300,fill=X)
       user=Label(third_frame,text="USERNAME :",bg="#d0ebdd",fg="black",font="calibri 14 bold ")
       password=Label(third_frame,text="PASSWORD:",bg="#d0ebdd",fg="black",font="calibri 14 bold")
       user.place(x=500,y=200)
       password.place(x=500,y=300)
       global tuservalue
       tuservalue=StringVar()
       global tpassvalue
       tpassvalue=StringVar()
       tuserentry=Entry(third_frame,textvariable=tuservalue,borderwidth=2,font=("",12))
       tpassentry=Entry(third_frame,textvariable=tpassvalue,borderwidth=2,font=("",12),show='*')
       tuserentry.place(x=640,y=200)
       tpassentry.place(x=640,y=300)
       login_button=Button(third_frame,text="SUBMIT",borderwidth=5,bg="#52ab98",fg="white",font="Corbel 16 bold",relief=RAISED,command=t_click)
       login_button.place(x=640,y=350)
       back_button=Button(third_frame,text="BACK",borderwidth=5,bg="#52ab98",fg="white",font="Corbel 16 bold",relief=RAISED,command=home)
       back_button.place(x=640,y=450)

def login():
       second_frame=Frame(bg="#d0ebdd")
       second_frame.place(x=0,y=0,width=1300,height=900)
       text_heading = Label(second_frame,text="ATTENDANCE MANAGEMENT SYSTEM", bg="#115566", fg="#ffffff",borderwidth=20,relief=FLAT,
                                            font="calibri 30 bold",pady=30)
       text_heading2 = Label(second_frame,text="**** Your username is your rollno.****\n **** NATIONAL POST GRADUATE COLLEGE****", bg="#115566", fg="#bbeeee",borderwidth=5,relief=RIDGE,
                                            font="calibri 18 bold",pady=10)
       text_heading.pack(padx=200,fill=X)
       text_heading2.pack(side=BOTTOM,padx=300,pady=300,fill=X)
       user=Label(second_frame,text="USERNAME :",bg="#d0ebdd",fg="black",font="calibri 14 bold ")
       password=Label(second_frame,text="PASSWORD:",bg="#d0ebdd",fg="black",font="calibri 14 bold")
       user.place(x=500,y=200)
       password.place(x=500,y=300)
       global uservalue
       uservalue=StringVar()
       global passvalue
       passvalue=StringVar()
       userentry=Entry(second_frame,textvariable=uservalue,borderwidth=2,font=("",12))
       passentry=Entry(second_frame,textvariable=passvalue,borderwidth=2,font=("",12),show='*')
       userentry.place(x=640,y=200)
       passentry.place(x=640,y=300)
       login_button=Button(second_frame,text="SUBMIT",borderwidth=5,bg="#52ab98",fg="white",font="Corbel 16 bold",relief=RAISED,command=onClick)
       login_button.place(x=640,y=350)
       back_button=Button(second_frame,text="BACK",borderwidth=5,bg="#52ab98",fg="white",font="Corbel 16 bold",relief=RAISED,command=home)
       back_button.place(x=640,y=450)

def home():
    first_frame=Frame(bg="#d0ebdd")
    first_frame.place(x=0,y=0,width=1300,height=900)
    text_heading = Label(first_frame,text="ATTENDANCE MANAGEMENT SYSTEM", bg="#115566", fg="#ffffff",borderwidth=20,relief=FLAT,
                                            font="calibri 30 bold",pady=30)
    text_heading.pack(padx=200,fill=X)
    student_button=Button(first_frame,text="STUDENT LOGIN",borderwidth=10,bg="orange",fg="white",relief=RAISED,font="Corbel 16 bold",command=login)
    student_button.place(x=580,y=350)
    exit_button=Button(first_frame,text="EXIT",borderwidth=10,bg="orange",fg="white",relief=RAISED,font="Corbel 16 bold",command=exit_gui)
    exit_button.place(x=585,y=450)
    teacher_button=Button(first_frame,text="TEACHER LOGIN",borderwidth=10,bg="orange",fg="white",relief=RAISED,font="Corbel 16 bold",command=t_login)
    teacher_button.place(x=580,y=250)
home()
root.mainloop()
