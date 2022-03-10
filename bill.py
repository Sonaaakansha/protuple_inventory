from msilib.schema import File
from operator import index
from pydoc import plain
from this import d
from tkinter import *
from tkinter import font
from turtle import title, width

from unicodedata import name
from unittest import result
from winreg import OpenKeyEx
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3
import time
import os
import tempfile


class BillingClass:
        def __init__(self, root):

            self.root.title("Inventory Management System | Developed By Aakansha")
            self.root.config(bg="white")
            self.cart_list = []
            self.chk_print = 0

    # ====title====
            self.icon_title = PhotoImage(file="C:\\Users\\Dell\\.vscode\\protuple_inventory\\4315251e5_Inventory-management-system-objectives.png")



def __init__(self, root):
    # ==========buttuon logout===============

    btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow",
                        cursor="hand2").place(x=1100, y=10, height=50, width=150)
    btn_logout = Button(self.root, text="Logout", command=self.logout, font=("times new roman", 15, "bold"),
                        bg="yellow", cursor="hand2").place(x=1100, y=10, height=50, width=150)

    # =========clock=========================



def __init__(self, root):
    self.lbl_net_pay = Label(billMenuFrame, text='Net Pay\n[0]', font=("goudy old style", 15, "bold"), bg="#607d8b",
                             fg="white")
    self.lbl_net_pay.place(x=246, y=5, width=160, height=70)

    btn_print = Button(billMenuFrame, text='Print', cursor="hand2", font=("goudy old style", 15, "bold"), bg="pink",
                       fg="white")
    btn_print = Button(billMenuFrame, text='Print', command=self.print_bill, cursor="hand2",
                       font=("goudy old style", 15, "bold"), bg="pink", fg="white")
    btn_print.place(x=2, y=80, width=120, height=50)

    btn_clear_all = Button(billMenuFrame, text='Clear All', cursor="hand2", font=("goudy old style", 15, "bold"),
                           bg="grey", fg="white")
    btn_clear_all = Button(billMenuFrame, text='Clear All', command=self.clear_all, cursor="hand2",
                           font=("goudy old style", 15, "bold"), bg="grey", fg="white")
    btn_clear_all.place(x=124, y=80, width=120, height=50)

    btn_generate = Button(billMenuFrame, text='Generate/Save', cursor="hand2", font=("goudy old style", 15, "bold"),
                          bg="#009688", fg="white")
    btn_generate = Button(billMenuFrame, text='Generate/Save', command=self.generate_bill, cursor="hand2",
                          font=("goudy old style", 15, "bold"), bg="#009688", fg="white")
    btn_generate.place(x=246, y=80, width=160, height=50)

    # ==================cartFrame==================================================




def __init__(self, root):
    self.lbl_instock = Label(Add_cartWidgetsFrame, text="In stock", font=("times new roman", 15), bg="white")
    self.lbl_instock.place(x=5, y=70)

    btn_clear_cart = Button(Add_cartWidgetsFrame, text="Clear", font=("times new roman", 15, "bold"), bg="grey",
                            cursor="hand2").place(x=180, y=70, width=150, height=30)
    btn_clear_cart = Button(Add_cartWidgetsFrame, text="Clear", command=self.clear_cart,
                            font=("times new roman", 15, "bold"), bg="grey", cursor="hand2").place(x=180, y=70,
                                                                                                   width=150, height=30)
    btn_add_cart = Button(Add_cartWidgetsFrame, text="Add | Update Cart", command=self.add_update_cart,
                          font=("times new roman", 15, "bold"), bg="orange", cursor="hand2").place(x=340, y=70,
                                                                                                   width=180, height=30)

    # =====================footer=====================================
    footer = Label(self.root, text="IMS-Inventory Management System", font=("times new roman", 11), bg="grey",
                   fg="white", bd=0, cursor="hand2").pack(side=BOTTOM, fill=X)

    self.show()
    # self.bill_top()
    self.update_date_time()

    # ===================All functions====================================================


def get_input(self, num):


    def get_data_cart(self, ev):

        self.var_pid.set(row[0])
    self.var_pname.set(row[1])
    self.var_price.set(row[2])
    self.lbl_instock.config(text=f"In stock [{str(row[3])}]")
    self.var_stock.set(row[3])
    self.var_qty.set('1')
    self.var_qty.set([3])
    self.lbl_instock.config(text=f"In stock [{str(row[4])}]")
    self.var_stock.set(row[4])


def add_update_cart(self):
    if self.var_pid.get() == '':
        messagebox.showerror('Error', "Please select product from list", parent=self.root)
    elif self.var_qty.get() == '':
        messagebox.showerror('Error', "Quantity is required", parent=self.root)
    elif int(self.var_qty.get()) > int(self.var_stock.get()):
        messagebox.showerror('Error', "Invalid Quantity", parent=self.root)
    else:


# price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
# price_cal=self.var_price.get()

def add_update_cart(self):
    self.bill_update()


def bill_update(self):
    bill_amt = 0
    net_pay = 0
    self.bill_amt = 0
    self.net_pay = 0
    self.discount = 0
    for row in self.cart_list:
        bill_amt = bill_amt + (float(row[2] * int(row[3])))
        self.bill_amt = self.bill_amt + (float(row[2] * int(row[3])))

    net_pay = bill_amt - ((bill_amt * 5) / 100)
    self.lbl_amt.config(text=f'Bill Amnt\n{str(bill_amt)}')
    self.lbl_net_pay.config(text=f'Net Amount\n{str(net_pay)}')
    self.discount = (self.bill_amt * 5) / 100
    self.net_pay = self.bill_amt - self.discount
    self.lbl_amt.config(text=f'Bill Amnt\n{str(self.bill_amt)}')
    self.lbl_net_pay.config(text=f'Net Amount\n{str(self.net_pay)}')
    self.cartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")




def show_cart(self):
    except Exception as ex:
    messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)


def generate_bill(self):
    if self.var_cname.get() == '' or self.var_contact.get() == '':
        messagebox.showerror("Error", f"Customer Details are required", parent=self.root)
    elif len(self.cart_list) == 0:
        messagebox.showerror("Error", f"Please add product to cart!!", parent=self.root)
    else:
        # ===============Bill Top==========
        self.bill_top()
        # ===============Bill Middle=======
        self.bill_middle()
        # ===============Bill Bottom=======
        self.bill_bottom()

        fp = open(f'bill/{str(self.invoice)}.txt', 'w')
        fp.write(self.txt_bill_area.get('1.0', END))
        fp.close()
        messagebox.showinfo('Saved', "Bill has been generated/Save in Backend", parent=self.root)
        self.chk_print = 1


def bill_top(self):
    self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
    bill_top_temp = f'''
\t\tXYZ-Inventory
\t Phone No. 846736**** , Delhi-1223001
{str("=" * 47)}
Customer Name:{self.var_cname.get()}
Ph No. {self.var_contact.get()}
Bill No.{str(self.invoice)}\t\t\tDate : {str(time.strftime("%d/%m/%Y"))}
{str("=" * 47)}
Product Name\t\t\tQTY\tPrice
{str("=" * 47)}
        '''
    self.txt_bill_area.delete('1.0', END)
    self.txt_bill_area.insert('1.0', bill_top_temp)


def bill_bottom(self):
    bill_bottom_temp = f'''
{str("=" * 47)}
Bill Amount\t\t\t\tRs.{self.bill_amt}
Discount\t\t\t\tRs.{self.discount}
Net Pay\t\t\t\tRs.{self.net_pay}
{str("=" * 47)}\n
        '''
    self.txt_bill_area.insert(END, bill_bottom_temp)


def bill_middle(self):
    con = sqlite3.connect(database=r'protuple_inventory.db')
    cur = con.cursor()
    try:
        for row in self.cart_list:

            pid = row[0]
            name = row[1]
            qty = int(row[4]) - int(row[3])
            if int(row[3]) == int(row[4]):
                status = 'Inactive'
            if int(row[3]) != int(row[4]):
                status = 'Active'

            price = float(row[2]) * int(row[3])
            price = str(price)
            self.txt_bill_area.insert(END, "\n " + name + "\t\t\t" + row[3] + "\tRs." + price)
            # ================update quantity in product table=============================
            cur.execute('Update product set qty=?,status=? where pid=?', (
                qty,
                status,
                pid
            ))
            con.commit()
            con.close()
            self.show()
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)


def clear_cart(self):
    self.var_pid.set('')
    self.var_pname.set('')
    self.var_price.set('')
    self.var_qty.set('')
    self.lbl_instock.config(text=f"In Stock")
    self.var_stock.set('')


def clear_all(self):
    del self.cart_list[:]
    self.var_cname.set('')
    self.var_contact.set('')
    self.txt_bill_area.delete('1.0', END)
    self.cartTitle.config(text=f"Cart \t Total Product: [0]")
    self.var_search.set('')
    self.clear_cart()
    self.show()
    self.show_cart()


def update_date_time(self):
    time_ = time.strftime("%I:%M:%S")
    date_ = time.strftime("%d-%m-%Y")
    self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
    self.lbl_clock.after(200, self.update_date_time)


def print_bill(self):
    if self.chk_print == 1:
        messagebox.showinfo('Print', "Please wait while printing", parent=self.root)
        new_file = tempfile.mktemp('.txt')
        open(new_file, 'w').write(self.txt_bill_area.get('1.0', END))
        os.startfile(new_file, 'print')
    else:
        messagebox.showerror('Print', "Please generate bill to print the receipt", parent=self.root)


def logout(self):
    self.root.destroy()
    os.system("python login.py")


if __name__ == "__main__":
    root = Tk()
    obj = BillingClass(root)
