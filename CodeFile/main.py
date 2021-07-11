import pymysql
import sys
import tkinter.messagebox
from tkinter import *
import tkinter.tix
root = tkinter.tix.Tk()
semployee_id = StringVar()
sname = StringVar()
stitle = StringVar()
sphone = StringVar()
sSSN = StringVar()
sadderss = StringVar()
sinventory_id = StringVar()
sstore_id = StringVar()
sproduct_id = StringVar()
sinventory = StringVar()
def turn_save(event):
    # new recode
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='wsm01', port=3306,
                               charset='utf8')
    except:
        print("DATABASE ERROR！")
        conn.close()
        sys.exit()
    cur = conn.cursor()
    selectSQL = "Insert into employee values('" + semployee_id.get() + "','" + sname.get() + "'," + stitle.get() + "," + sphone.get() + "," + sadderss.get() + ",'" + sSSN.get() + "')"
    cur.execute(selectSQL)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('SUCCEED','RECODE SUCCEED!')
def turn_save0(event):
    # edit recode
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='wsm01', port=3306,
                               charset='utf8')
    except:
        print("DATABASE ERROR！")
        conn.close()
        sys.exit()
    cur = conn.cursor()
    selectSQL2 = "Insert into inventory values('" + sinventory_id.get() + "','" + sstore_id.get() + "'," + sproduct_id.get() + ",'" + sinventory.get() +"')"
    cur.execute(selectSQL2)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('SUCCEED','RECODE SUCCEED!')
def turn_property(event):
    getSQLDate()
def turn_property0(event):
    getSQLDate0()
def turn_property1(event):
    getSQLDate1()
def getSQLDate():
    # VIEW TABLE CONTENT
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='wsm01', port=3306,
                               charset='utf8')
    except:
        print("DATABASE ERROR！")
        conn.close()
        sys.exit()
    cur = conn.cursor()
    selectSQL = 'Select * from employee'
    cur.execute(selectSQL)
    for row in cur.fetchall():
        tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4],row[5]))
    cur.close()
    conn.close()
def getSQLDate0():
    # VIEW TABLE CONTENT
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='wsm01', port=3306,
                               charset='utf8')
    except:
        print("DATABASE ERROR！")
        conn.close()
        sys.exit()
    cur = conn.cursor()
    selectSQL0 = 'Select * from inventory'
    cur.execute(selectSQL0)
    for row in cur.fetchall():
        tree0.insert("", 0, text=row[0], values=(row[1], row[2], row[3]))
    cur.close()
    conn.close()

def getSQLDate1():
        # VIEW TABLE CONTENT
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='wsm01', port=3306,
                                   charset='utf8')
    except:
        print("DATABASE ERROR！")
        conn.close()
        sys.exit()
    cur = conn.cursor()
    selectSQL1 = 'Select * from inventory'
    cur.execute(selectSQL1)
    for row in cur.fetchall():
        tree1.insert("", 0, text=row[0], values=(row[1], row[2], row[3]))
    cur.close()
    conn.close()
import tkinter as tk
from tkinter.constants import *
from tkinter import ttk
from tkinter.constants import *
root.title("AW108 Inventory Management System DEMO ")
root.geometry("960x490")
n=ttk.Notebook(root)
f1=ttk.Frame(n,height=1024,width=800)
f2=ttk.Frame(n,height=1024,width=800)
f3=ttk.Frame(n,height=1024,width=800)
n.add(f1, text='Product')
n.add(f2, text='employee')
n.add(f3, text='inventory')
n.pack()
product = tk.Label(f1, text="Edit the inventory")
product.pack()
employee = tk.Label(f2, text="Add employee")
employee.pack()
inventory = tk.Label(f3, text="View the inventory")
inventory.pack()
tree0 = ttk.Treeview(f1)  # TABLE VIEW
tree0["columns"] = ("store", "product", "inventory")
tree0.column("store", width=150)
tree0.column("product", width=150)
tree0.column("inventory", width=150)
tree0.heading("store", text="Store")
tree0.heading("product", text="Product")
tree0.heading("inventory", text="Inventory")
tree0.pack(side="top")
bs0 = tk.Button(f1, text="SEARCH...", width=10)
bs0.bind("<Button-1>", turn_property0)  # bind()MOUSE
bs0.pack(padx=5,pady=5,side="top")
top0 = tkinter.tix.Frame(f1, relief=FLAT, bd=5,height=2,width=2)
top0.pack(padx=200,pady=0,side='left')
top0.sinventory_id = tkinter.tix.LabelEntry(top0, label="ID:", labelside='top',width='200')
top0.sinventory_id.pack(side="left")
top0.sinventory_id.entry['textvariable'] = sinventory_id
top0.sstore_id = tkinter.tix.LabelEntry(top0, label="Store:", labelside='top', )
top0.sstore_id.pack(side="left")
top0.sstore_id.entry['textvariable'] = sstore_id
top0.sproduct_id = tkinter.tix.LabelEntry(top0, label="Product:", labelside='top', )
top0.sproduct_id.pack(side="left")
top0.sproduct_id.entry['textvariable'] = sproduct_id
top0.sinventory = tkinter.tix.LabelEntry(top0, label="Inventory:", labelside='top', )
top0.sinventory.pack(side="left")
top0.sinventory.entry['textvariable'] = sinventory
Savebn0 = tk.Button(top0, text="Edit ventory", width=10)
Savebn0.bind("<Button-1>", turn_save0)
Savebn0.pack(padx=50,pady=50,side="right")
tree = ttk.Treeview(f2)  # TABLE VIEW
tree["columns"] = ("name", "ssn", "phone", "adderss","title")
tree.column("name", width=150)
tree.column("ssn", width=150)
tree.column("phone", width=150)
tree.column("adderss", width=150)
tree.column("title", width=150)
tree.heading("name", text="NAME")
tree.heading("ssn", text="SSN")
tree.heading("phone", text="PHONE")
tree.heading("adderss", text="ADDERSS")
tree.heading("title", text="TITLE")
tree.pack(side="top")
bs = tk.Button(f2, text="SEARCH...", width=10)
bs.bind("<Button-1>", turn_property)  # bind()MOUSE
bs.pack(padx=5,pady=5,side="top")
top = tkinter.tix.Frame(f2, relief=FLAT, bd=5,height=2,width=2)
top.pack(padx=200,pady=0,side='left')
top.semployee_id = tkinter.tix.LabelEntry(top, label="ID:", labelside='top',width='200')
top.semployee_id.pack(side="left")
top.semployee_id.entry['textvariable'] = semployee_id
top.sname = tkinter.tix.LabelEntry(top, label="NAME:", labelside='top', )
top.sname.pack(side="left")
top.sname.entry['textvariable'] = sname
top.title = tkinter.tix.LabelEntry(top, label="TITLE:", labelside='top', )
top.title.pack(side="left")
top.title.entry['textvariable'] = stitle
top.phone = tkinter.tix.LabelEntry(top, label="PHONE:", labelside='top', )
top.phone.pack(side="left")
top.phone.entry['textvariable'] = sphone
top.ssn = tkinter.tix.LabelEntry(top, label="SSN:", labelside='top', )
top.ssn.pack(side="left")
top.ssn.entry['textvariable'] = sSSN
top.adderss = tkinter.tix.LabelEntry(top, label="adderss:", labelside='top', )
top.adderss.pack(side="left")
top.adderss.entry['textvariable'] = sadderss
Savebn = tk.Button(top, text="Add new", width=10)
Savebn.bind("<Button-1>", turn_save)
Savebn.pack(padx=50,pady=50,side="right")
tree1 = ttk.Treeview(f3)  # TABLE VIEW
tree1["columns"] = ("store", "product", "inventory")
tree1.column("store", width=150)
tree1.column("product", width=150)
tree1.column("inventory", width=150)
tree1.heading("store", text="Store")
tree1.heading("product", text="Product")
tree1.heading("inventory", text="Inventory")
tree1.pack(side="top")
comvalue = tkinter.StringVar()
comboxlist=ttk.Combobox(f3,textvariable=comvalue)
comboxlist["values"]=("ALL","APPLE","HUAWEI")
comboxlist.current(0)
comboxlist.pack(padx=15,pady=15)
bs1 = tk.Button(f3, text="SEARCH...", width=10)
bs1.bind("<Button-1>", turn_property1)  # bind()MOUSE
bs1.pack(padx=5,pady=5,side="top")
root.mainloop()
