
import email
from logging import root
from pydoc import plain
from tkinter import*
from turtle import title
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import os
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="lightblue")
        #==========Images====================
        self.log_img=Image.open("C:\\Users\\leena\\Downloads\\Project Pic\\log1.jpg")
        self.log_img=self.log_img.resize((390,380),Image.ANTIALIAS)
        self.log_img=ImageTk.PhotoImage(self.log_img)
        lbl_img=Label(self.root,image=self.log_img,bd=2)
        lbl_img.place(x=200,y=110)

        #================login frame=================
        self.employee_id=StringVar()
        self.password=StringVar()
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        lbl_user=Label(login_frame,text="Eployee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)

        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="lightgrey").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="Paswword",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="lightgrey").place(x=50,y=240,width=250)

        btnlogin=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",cursor="hand2").place(x=50,y=300,width=250,height=35)
        hr=Label(login_frame,bg="lightgray").place(x=50,y=380,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgrey",font=("times new roman",15,"bold")).place(x=150,y=355)

        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_window,font=("times new roman",13),bg="white",fg="#00759e",bd=0,activebackground="white",activeforeground="#00759e").place(x=100,y=390)

        #=================frame2=============================
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)
        lbl_reg=Label(register_frame,text="Subscribe | Like | Share",font=("times new roman",13),bg="white").place(x=0,y=20,relwidth=1)


    def login(self):
        con=sqlite3.connect(database=r'protuple_inventory.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def forget_window(self):
        con=sqlite3.connect(database=r'protuple_inventory.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror("Error","Employee ID required",parent=self.root)
            else:
             cur.execute("select utype from employee where eid=?",(self.employee_id.get(),))
             email=cur.fetchone()
            if email==None:
                messagebox.showerror("Error","Invalid Employee ID try again",parent=self.root)
            else:

                self.forget_win=Toplevel(self.root)
                self.forget_win.title('RESET Passwprd')
                self.forget_win.geometry('400x350+500+100')
                self.forget_win.focus_force()

                title=Label(self.forget_win,text="Reset Password",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)





root=Tk()
obj=Login(root)
root.mainloop()
