import sqlite3
def create_db():
    con=sqlite3.connect(database=r'IMS.db')
    cur=con.cursor()
    cur.execute("create table if not exists employee(eid integer primary key autoincrement,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()
    
    create_db()