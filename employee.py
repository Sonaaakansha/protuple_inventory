
from tkinter import *
from tkinter import font
from turtle import title
from typing_extensions import Self
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class employeeClass:

  def __init__(self,root):
   self.root=root
   self.root.geometry("110x500+220+130")
   self.root.title("Inventory Management System")
   self.root.config(bg="white")
   self.root.focus_force()
#==========================================================================================
#All variables
self.var_searchby=StringVar()
self.var_searchtxt=StringVar()

self.var_emp_id=StringVar()
self.var_Gender=StringVar()
self.var_Contact=StringVar()
self.var_Name=StringVar()
self.var_dob=StringVar()
self.var_doj=StringVar()
self.var_email=StringVar()
self.var_pass=StringVar()
self.var_utype=StringVar()
self.var_address=StringVar()
self.var_salary=StringVar()

 #====searchFrame===
 SearchFrame=LabelFrame(self,root,text="Search Employee",font=("goudy old style",12,"bold")bd=2,relief=RIDGE,bg="white")
 SearchFrame.place(x=250,y=20,width=600,height=70)
  
 #====Options===
 cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15,))
 cmb_search.place(x=10,y=10,width=180)
 cmb_search.current(0)

 txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
 btn_search=Button(SearchFrame,text="Search",font=("goudy old styel",15)bg="#4caf50",fg="white",cursor="hand2").Place(x=410,y=9,width=150,height=30)

 #=====Title===
 title=Label(self,root,text="Employee Details",font=("goudy old style",15)bg="#0ff4d7d",fg="white").place(x=50,y=100,width=1000)

 #==Content===

 #row1
 lbl_empid=Label(self,root,text="Emp Id",font=("goudy old style",15)bg="white").place(x=50,y=150)
 lbl_gender=Label(self,root,text="Gender",font=("goudy old style",15)bg="white").place(x=350,y=150)
 lbl_contact=Label(self,root,text="Contact",font=("goudy old style",15)bg="white").place(x=750,y=150)
  
 txt_empid=Label(self,root,textvariable=self.var_empid,font=("goudy old style",15)bg="lightyellow").place(x=150,y=150,width=180)
 txt_gender=Label(self,root,textvariable=self.var_gender,font=("goudy old style",15)bg="white").place(x=500,y=150,width=180)

 cmb_gender=ttk.Combobox(SearchFrame,textvariable=self.var_gender,values=("Select","Male","Female","other"),state='readonly',justify=CENTER,font=("goudy old style",15,))
 cmb_gender.place(x=500,y=150,width=180)
 cmb_gender.current(0)


 txt_contact=Label(self,root,textvariable=self.var_contact,font=("goudy old style",15)bg="lightyellow").place(x=850,y=150,width=180)

#row2
 lbl_name=Label(self,root,text="Name",font=("goudy old style",15)bg="white").place(x=50,y=150)
 lbl_dob=Label(self,root,text="DOB",font=("goudy old style",15)bg="white").place(x=50,y=150)
 lbl_doj=Label(self,root,text="DOJ",font=("goudy old style",15)bg="white").place(x=50,y=150)

 txt_name=Label(self,root,textvariable=self.var_name,font=("goudy old style",15)bg="lightyellow").place(x=150,y=190,width=180)
 txt_dob=Label(self,root,textvariable=self.var_dob,font=("goudy old style",15)bg="white").place(x=500,y=190,width=180)
 txt_doj=Label(self,root,textvariable=self.var_doj,font=("goudy old style",15)bg="white").place(x=850,y=190,width=180)
  

#row3

 lbl_email=Label(self,root,text="Email",font=("goudy old style",15)bg="white").place(x=50,y=230)
 lbl_pass=Label(self,root,text="Password ",font=("goudy old style",15)bg="white").place(x=350,y=230)
 lbl_utype=Label(self,root,text="User type",font=("goudy old style",15)bg="white").place(x=750,y=230)
  
 txt_email=Label(self,root,textvariable=self.var_email,font=("goudy old style",15)bg="lightyellow").place(x=150,y=230,width=180)
 txt_pass=Label(self,root,textvariable=self.var_pass,font=("goudy old style",15)bg="white").place(x=500,y=230,width=180)
 cmb_utype=ttk.Combobox(SearchFrame,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15,))
 cmb_utype.place(x=850,y=230,width=180)
 cmb_utype.current(0)
  

#row4
 lbl_address=Label(self,root,text="Address",font=("goudy old style",15)bg="white").place(x=50,y=270)
 lbl_salary=Label(self,root,text="Salary ",font=("goudy old style",15)bg="white").place(x=500,y=270)
 
 self.txt_address=Text(self,root,font=("goudy old style",15)bg="lightyellow").place(x=150,y=270,width=180)
 self.txt_address.place(x=150,y=270,width=300,height=60)
 self.txt_salary=Text(self,root,textvariable=self.var_salary,font=("goudy old style",15)bg="lightyellow").place(x=600,y=270,width=180)
 
  
#====button====

 btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old styel",15)bg="#2196f3",fg="white",cursor="hand2").Place(x=410,y=9,width=150,height=28)
 btn_update=Button(self.root,text="Update",font=("goudy old styel",15)bg="#4caf50",fg="white",cursor="hand2").Place(x=620,y=9,width=150,height=28)
 btn_delete=Button(self.root,text="Delete",font=("goudy old styel",15)bg="#f44336",fg="white",cursor="hand2").Place(x=740,y=9,width=150,height=28)
 btn_clear=Button(self.root,text="Clear",font=("goudy old styel",15)bg="#607d8b",fg="white",cursor="hand2").Place(x=860,y=9,width=150,height=28)
 

#====Employee Details

 emp_frame=Frame(self.root,bd=3,relief=RIDGE)
 emp_frame.place(x=0,y=350,relwidth=1,height=150)

 scrolly=Scrollbar(emp_frame,orient=VERTICAL)
 scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
 
 self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
 scrollx.pack(side=BOTTOM,fill=X)
 scrolly.pack(side=RIGHT,fill=Y)
 scrollx.config(command=self.EmployeeTable.xview)
scrolly.config(command=self.EmployeeTable.yview)
 self.EmployeeTable.heading("eid",text="Employee Id")
 self.EmployeeTable.heading("name",text="Name")
 self.EmployeeTable.heading("email",text="Email")
 self.EmployeeTable.heading("gender",text="Gender")
 self.EmployeeTable.heading("contact",text="Contact")
 self.EmployeeTable.heading("dob",text="DOB")
 self.EmployeeTable.heading("doj",text="DOJ")
 self.EmployeeTable.heading("pass",text="Password")
 self.EmployeeTable.heading("utype",text="Usertype")
 self.EmployeeTable.heading("address",text="Address")
 self.EmployeeTable.heading("salary",text="Salary")

 self.EmployeeTable["show"]="headings"

 self.EmployeeTable.column("eid",width=90)
 self.EmployeeTable.column("name",width=100)
 self.EmployeeTable.column("email",width=100)
 self.EmployeeTable.column("gender",width=100)
 self.EmployeeTable.column("contact",width=100)
 self.EmployeeTable.column("dob",width=100)
 self.EmployeeTable.column("doj",width=100)
 self.EmployeeTable.column("pass",width=100)
 self.EmployeeTable.column("utype",width=100)
 self.EmployeeTable.column("address",width=100)
 self.EmployeeTable.column("salary",width=200)

 self.EmployeeTable.pack(fill=BOTH,expand=1)

 #==============================================================================================
 def add(self):
   con=sqlite3.connect(database=r'IMS.db')
   cur=con.cursor()
   try:
       if self.var_empid.get()=="":
       messagebox.showerror("Error","Employe Id must be required",parent=self.root)
        
       else:
         cur.execute("select *from employee where eid=?",(self.var_empid.get(),))
         row=cur.fetchone()
         if row!=None:
           messagebox.showerror("Error","this employee id already assigned,try different",parent=self.root)
         else:
             cur.execute("Insert into employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary)value")

   except Exception as ex:
     messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)


 if__name__="__main__":

     root=Tk()
    obj=employeeClass(root)
    root.mainloop()