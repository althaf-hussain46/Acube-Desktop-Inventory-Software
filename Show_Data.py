import Design_Supplier
from  DB_Connection import*
import tkinter as tk
from tkinter import ttk
from tkinter import*
from tkinter import messagebox as mb
from Class_Supplier import*
cls = Cls_Supplier_Master()

Con = DB_Connect()
Cur = Con.cursor()

def Show_Supplier_Records(event,qry):
        global tree
        global show_data_form
        show_data_form = tk.Toplevel()
        show_data_form.geometry('600x150+300+250')
        show_data_form.title('Supplier Details')

        Cur.execute(cls.get_supp_qry())
        col = ('name', 'address', 'locality', 'city', 'pincode', 'state', 'phone', 'email', 'gst_no','crt_date','id')
        tree = ttk.Treeview(show_data_form, height=5,show='headings',columns=col)
        style1 = ttk.Style(show_data_form)
        style1.theme_use('clam')
        style1.configure(".", font=('times new roman',12))
        style1.configure("Treeview", foreground='black', background='orange', fieldbackground='black', font=('times new roman',12))
        style1.map('Treeview',background=[('selected', 'grey28')])

        tree.column("name", width=200, minwidth=50, anchor=tk.CENTER)
        tree.column("address", width=300, minwidth=50, anchor=tk.CENTER)
        tree.column("locality", width=100, minwidth=50, anchor=tk.CENTER)
        tree.column("city", width=100, minwidth=50, anchor=tk.CENTER)
        tree.column("pincode", width=80, minwidth=50, anchor=tk.CENTER)
        tree.column("state", width=120, minwidth=50, anchor=tk.CENTER)
        tree.column("phone", width=80, minwidth=50, anchor=tk.CENTER)
        tree.column("email", width=180, minwidth=50, anchor=tk.CENTER)
        tree.column("gst_no", width=120, minwidth=50, anchor=tk.CENTER)
        tree.column("crt_date", width=120, minwidth=50, anchor=tk.CENTER)
        tree.column("id", width=120, minwidth=50, anchor=tk.CENTER)

        tree.heading("name", text="SUPPLIER NAME", anchor=tk.CENTER)
        tree.heading("address", text="ADDRESS", anchor=tk.CENTER)
        tree.heading("locality", text="LOCALITY", anchor=tk.CENTER)
        tree.heading("city", text="CITY", anchor=tk.CENTER)
        tree.heading("pincode", text="PINCODE", anchor=tk.CENTER)
        tree.heading("state", text="STATE", anchor=tk.CENTER)
        tree.heading("phone", text="PHONE", anchor=tk.CENTER)
        tree.heading("email", text="EMAIL", anchor=tk.CENTER)
        tree.heading("gst_no", text="GST NO.", anchor=tk.CENTER)
        tree.heading("crt_date", text="CREATED ON", anchor=tk.CENTER)
        tree.heading("id", text="ID", anchor=tk.CENTER)

        i = 0
        for row in Cur:
            tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            i = i+1

        vsb = ttk.Scrollbar(show_data_form, orient="vertical")
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y, side= RIGHT)

        hsb = ttk.Scrollbar(show_data_form,orient="horizontal")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X, side=BOTTOM)

        tree.pack()
        tree.bind("<Return>", Select_Supplier_Data)


def Select_Supplier_Data(event):
    item=tree.selection()
    global cur_name
    for i in item:
        cur_name = tree.item(i, 'values')[0] + '1'
        print(len(cur_name))
        if len(tree.item(i, 'values')[0]) > 0:
            cls.set_supp_name(tree.item(i,'values')[0])
            cls.set_supp_address(tree.item(i,'values')[1])
            cls.set_supp_locality(tree.item(i,'values')[2])
            cls.set_supp_city(tree.item(i,'values')[3])
            cls.set_supp_pincode(tree.item(i,'values')[4])
            cls.set_supp_state(tree.item(i,'values')[5])
            cls.set_supp_phone(tree.item(i,'values')[6])
            cls.set_supp_email(tree.item(i,'values')[7])
            cls.set_supp_gst(tree.item(i,'values')[8])
            cls.set_supp_crt_date(tree.item(i,'values')[9])
            cls.set_supp_id(tree.item(i,'values')[10])

            cls.set_supp_record_found('1')
            print(cls.get_supp_record_found())
        else:
            cls.set_supp_record_found('0')

        show_data_form.withdraw()
