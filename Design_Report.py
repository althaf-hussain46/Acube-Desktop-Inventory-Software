import datetime
from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from DB_Connection import*
from tkcalendar import DateEntry
from Class_Report import*

Con = DB_Connect()
Cur = Con.cursor()
rep_cls = cls_report()

def Set_Purchase_Report_Type(event):
    global rep_supplier_combo
    rep_from_date_entry.config(state="normal")
    rep_to_date_entry.config(state="normal")
    rep_cls.set_report_type(1)

    #************** Frame3 - Labels, Combo Box For Supplier- Settings BEGIN *********************
    rep_frame3 = Frame(Report_Form, width =190, height=208, bg='LightSteelBlue1')
    rep_frame3.place(x=5,y=260)

    Cur.execute("select distinct(name) from supplier_master order by name")
    rep_supplier_list = []
    for i in Cur.fetchall():
        rep_supplier_list.append(i[0])

    rep_supplier_label = Label(rep_frame3, text='Supplier', bg='LightSteelBlue1', font=('copper', 8))
    rep_supplier_label.place(x=20, y=2)
    rep_supplier_combo = ttk.Combobox(rep_frame3, value=rep_supplier_list, width=23, state='readonly')
    rep_supplier_combo.place(x=20, y=20)
    rep_supplier_combo.bind('<Return>', Show_Get_Focus)
    # ************** Frame3 - Labels, Combo Box For Supplier - Settings END *********************
    Con.commit()

def Set_Sales_Report_Type(event):
    global rep_customer_combo

    rep_from_date_entry.config(state="normal")
    rep_to_date_entry.config(state="normal")
    rep_cls.set_report_type(2)

    # ************** Frame4 - Labels, Combo Box For Supplier- Settings BEGIN *********************
    rep_frame4 = Frame(Report_Form, width=190, height=208, bg='LightSteelBlue1')
    rep_frame4.place(x=5, y=260)

    Cur.execute("select distinct(name) from customer_master order by name")
    rep_customer_list = []
    for i in Cur.fetchall():
        rep_customer_list.append(i[0])

    rep_customer_label = Label(rep_frame4, text='Customer', bg='LightSteelBlue1', font=('copper', 8))
    rep_customer_label.place(x=20, y=2)
    rep_customer_combo = ttk.Combobox(rep_frame4, value=rep_customer_list, width=23, state='readonly')
    rep_customer_combo.place(x=20, y=20)
    rep_customer_combo.bind('<Return>', Show_Get_Focus)
    # ************** Frame4 - Labels, Combo Box For Supplier - Settings END *********************
    Con.commit()

def Set_Stock_Report_Type(event):
    global rep_brand_combo, rep_product_combo, rep_design_name_combo, rep_color_combo, rep_size_combo

    rep_from_date_entry.config(state="disable")
    rep_to_date_entry.config(state="disable")
    rep_cls.set_report_type(3)
#************** Frame5 - Labels, Combo Box for Brand, Product, Design, Color, Size - Settings BEGIN *******************************
    rep_frame5 = Frame(Report_Form, width =190, height=208, bg='LightSteelBlue1')
    rep_frame5.place(x=5,y=260)

    Cur.execute("select distinct(brand) as Brand from item_master order by brand")
    brand_list = []
    for j in Cur.fetchall():
        brand_list.append(j[0])

    rep_brand_label = Label(rep_frame5, text='Brand', bg='LightSteelBlue1', font=('copper', 8))
    rep_brand_label.place(x=20, y=2)
    rep_brand_combo = ttk.Combobox(rep_frame5, value=brand_list, state='readonly')
    rep_brand_combo.place(x=20, y=20)
    rep_brand_combo.bind('<Return>', Product_Get_Focus)

    Cur.execute("select distinct(product) as Product from item_master order by product")
    product_list = []
    for k in Cur.fetchall():
        product_list.append(k[0])
    rep_product_label = Label(rep_frame5, text='Product', bg='LightSteelBlue1', font=('copper', 8))
    rep_product_label.place(x=20, y=42)
    rep_product_combo = ttk.Combobox(rep_frame5, value=product_list, state='readonly')
    rep_product_combo.place(x=20, y=60)
    rep_product_combo.bind('<Return>', Design_Name_Get_Focus)

    Cur.execute("select distinct(design) as Design_Name from item_master order by design")
    design_name_list = []
    for l in Cur.fetchall():
        design_name_list.append(l[0])

    rep_design_name_label = Label(rep_frame5, text='Design Name', bg='LightSteelBlue1', font=('copper', 8))
    rep_design_name_label.place(x=20, y=82)
    rep_design_name_combo = ttk.Combobox(rep_frame5, value=design_name_list, state='readonly')
    rep_design_name_combo.place(x=20, y=100)
    rep_design_name_combo.bind('<Return>', Color_Get_Focus)

    Cur.execute("select distinct(color) as Color from item_master order by color")
    color_list = []
    for m in Cur.fetchall():
        color_list.append(m[0])

    rep_color_label = Label(rep_frame5, text='Color', bg='LightSteelBlue1', font=('copper', 8))
    rep_color_label.place(x=20, y=122)
    rep_color_combo = ttk.Combobox(rep_frame5, value=color_list, state='readonly')
    rep_color_combo.place(x=20, y=140)
    rep_color_combo.bind('<Return>', Size_Get_Focus)

    Cur.execute("select distinct(size) as Size from item_master order by size")
    size_list = []
    for n in  Cur.fetchall():
        size_list.append(n[0])

    rep_size_label = Label(rep_frame5, text='Size', bg='LightSteelBlue1', font=('copper', 8))
    rep_size_label.place(x=20, y=162)
    rep_size_combo = ttk.Combobox(rep_frame5, value=size_list, state='readonly')
    rep_size_combo.place(x=20, y=180)
    rep_size_combo.bind('<Return>', Show_Get_Focus)
#*********** Frame5 - Labels, Combo Box for Brand, Product, Design, Color, Size - Settings END **********
    Con.commit()

def Clear_Attribute_Field(event):

    if rep_cls.get_report_type() == 1:
        rep_supplier_combo.set('')
        rep_supplier_combo.focus_set()
        for item in tree.get_children():
            tree.delete(item)

    elif rep_cls.get_report_type() == 2:
        rep_customer_combo.set('')
        rep_customer_combo.focus_set()
        for item in tree2.get_children():
            tree2.delete(item)

    elif rep_cls.get_report_type() == 3:
        rep_brand_combo.set('')
        rep_product_combo.set('')
        rep_design_name_combo.set('')
        rep_color_combo.set('')
        rep_size_combo.set('')
        rep_brand_combo.focus_set()
        for item in tree3.get_children():
            tree3.delete(item)

def Clear_Field_On_Radio_Button_Click():

    if not rep_cls.get_report_type():
        if rep_cls.get_report_type() == 1:
            rep_supplier_combo.set('')
            rep_supplier_combo.focus_set()
            for item in tree.get_children():
                tree.delete(item)

        elif rep_cls.get_report_type() == 2:
            rep_customer_combo.set('')
            rep_customer_combo.focus_set()
            for item in tree2.get_children():
                tree2.delete(item)

        elif rep_cls.get_report_type() == 3:
            rep_brand_combo.set('')
            rep_product_combo.set('')
            rep_design_name_combo.set('')
            rep_color_combo.set('')
            rep_size_combo.set('')
            rep_brand_combo.focus_set()
            for item in tree3.get_children():
                tree3.delete(item)



def  From_Date_Get_Focus(event):
    pass
def From_Date_Lost_Focus(event):
    pass
def  To_Date_Get_Focus(event):
    pass
def To_Date_Lost_Focus(event):
    pass
def Brand_Get_Focus(event):
    pass
def Product_Get_Focus(event):
    rep_product_combo.focus_set()

def Design_Name_Get_Focus(event):
    rep_design_name_combo.focus_set()

def Color_Get_Focus(event):
    rep_color_combo.focus_set()

def Size_Get_Focus(event):
    rep_size_combo.focus_set()

def Show_Get_Focus(event):
    rep_clear_button.focus_set()


def Show_From_Calendar(event):
    rep_from_date_entry.config(text=rep_from_date_entry.get())

def Show_To_Calendar(event):
    rep_to_date_entry.config(text=rep_to_date_entry.get())

def Tree_Get_Focus(event):
    form_bottom_label.configure(text="Select & Press [Enter] Key To View Purchase Item Details")

def Tree_Lost_Focus(event):
    form_bottom_label.configure(text="")

def Tree2_Get_Focus(event):
    form_bottom_label.configure(text="Select & Press [Enter] Key To View Sales Item Details")

def Tree2_Lost_Focus(event):
    form_bottom_label.configure(text="")


def Show_Report(event):
    dt = rep_from_date_entry.get_date()
    str1 = dt.strftime("%d-%m-%Y")

    if rep_cls.get_report_type() == 1: #PURCHASE REPORT
        f_date1 = rep_from_date_entry.get_date()
        f_date2 = f_date1.strftime("%Y-%m-%d")

        t_date1 = rep_to_date_entry.get_date()
        t_date2 = t_date1.strftime("%Y-%m-%d")

        treeview_for_purchase_report()
        form_top_label.config(text='P U R C H A S E   -   R E P O R T')
        qry = "select * from purchase_master where supp_name like '%" + rep_supplier_combo.get() + "%' and grn_date  between '" + f_date2 + "' and '" + t_date2 + "'"
        Cur.execute(qry)
        for item in tree.get_children():
            tree.delete(item)
        i = 0
        pur_rep_tot_item = 0
        pur_rep_tot_discount = 0
        pur_rep_tot_cgst = 0
        pur_rep_tot_sgst = 0
        pur_rep_tot_qty = 0
        pur_rep_tot_amount = 0
        for row in Cur:
            tree.insert('', i, text="", values=(row[0], Local_Date_Format(row[1]), row[2], row[3],Local_Date_Format(row[4]), row[5], row[6], row[7],row[8], row[9], row[10]))
            i = i + 1
            pur_rep_tot_qty = pur_rep_tot_qty + row[5]
            pur_rep_tot_item = pur_rep_tot_item + row[6]
            pur_rep_tot_discount = pur_rep_tot_discount + row[7]
            pur_rep_tot_cgst = pur_rep_tot_cgst + row[8]
            pur_rep_tot_sgst = pur_rep_tot_sgst + row[9]
            pur_rep_tot_amount = pur_rep_tot_amount + row[10]
        tree.insert("", "end", values=("", "", "", "", "", "", "", "", "", ""))
        tree.insert("", "end", values=("Total", "", "", "", "", pur_rep_tot_qty, pur_rep_tot_item, pur_rep_tot_discount, pur_rep_tot_cgst, pur_rep_tot_sgst, pur_rep_tot_amount))
        Con.commit()
    elif rep_cls.get_report_type() == 2:#SALES REPORT
        f_date1 = rep_from_date_entry.get_date()
        f_date2 = f_date1.strftime("%Y-%m-%d")

        t_date1 = rep_to_date_entry.get_date()
        t_date2 = t_date1.strftime("%Y-%m-%d")

        treeview_for_sales_report()
        form_top_label.config(text='S A L E S   -   R E P O R T')
        qry = "select * from sales_master where cust_name like '%" + rep_customer_combo.get() + "%' and bill_date  between '" + f_date2 + "' and '" + t_date2 + "'"
        Cur.execute(qry)
        for item in tree2.get_children():
            tree2.delete(item)
        i = 0
        sal_rep_tot_item = 0
        sal_rep_tot_discount = 0
        sal_rep_tot_cgst = 0
        sal_rep_tot_sgst = 0
        sal_rep_tot_qty = 0
        sal_rep_tot_amount = 0
        for row in Cur:
            tree2.insert('', i, text="", values=(row[0], Local_Date_Format(row[1]), row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            i = i + 1
            sal_rep_tot_qty = sal_rep_tot_qty + row[3]
            sal_rep_tot_item = sal_rep_tot_item + row[4]
            sal_rep_tot_discount = sal_rep_tot_discount + row[5]
            sal_rep_tot_cgst = sal_rep_tot_cgst + row[6]
            sal_rep_tot_sgst = sal_rep_tot_sgst + row[7]
            sal_rep_tot_amount = sal_rep_tot_amount + row[8]
        tree2.insert("", "end", values=("", "", "", "", "", "", "", "", ""))
        tree2.insert("", "end", values=("Total", "", "", sal_rep_tot_qty, sal_rep_tot_item, sal_rep_tot_discount, sal_rep_tot_cgst,
        sal_rep_tot_sgst, sal_rep_tot_amount))
        Con.commit()



    elif rep_cls.get_report_type() == 3:#STOCK REPORT
        treeview_for_stock_report()
        form_top_label.config(text='S T O C K   -   R E P O R T')
        qry = "select * from stock_balance where bal_qty >0 and brand   like '%{}%' and product like '%{}%' and design like '%{}%' " \
              "and color like '%{}%' and sizes like '%{}%'"\
            .format(rep_brand_combo.get(), rep_product_combo.get(), rep_design_name_combo.get(), rep_color_combo.get(),
            rep_size_combo.get())
        Cur.execute(qry)

        for item in tree3.get_children():
            tree3.delete(item)
        i = 0
        stock_report_tot_qty = 0
        stock_report_tot_amount = 0
        for row in Cur:
            tree3.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            i = i + 1
            stock_report_tot_qty = stock_report_tot_qty + row[8]
            stock_report_tot_amount = stock_report_tot_amount + row[9]
        tree3.insert("", "end", values=("", "", "", "", "", "", "", "", "", ""))
        tree3.insert("", "end", values=("Total", "", "", "", "", "", "", "", stock_report_tot_qty, stock_report_tot_amount))
        Con.commit()

def Local_Date_Format(date2):
    local_date = date2.strftime("%d-%m-%Y")
    return local_date

def treeview_for_purchase_report():
    global tree, rep_frame2
    # ********************** Frame2 - PURCHASE TREEVIEW SETTINGS - BEGIN **************************
    rep_frame2 = Frame(Report_Form)
    rep_frame2.pack(pady=5)
    rep_frame2.place(x=200, y=60)
    rep_frame2.pack_propagate(False)
    rep_frame2.configure(width=1090, height=436, bg='white')

    col = ('grn_no', 'grn_date', 'supplier', 'bill_no', 'bill_date', 'qty', 'item_value', 'discount', 'cgst', 'sgst', 'bill_amount')
    tree = ttk.Treeview(rep_frame2, height=19, show='headings', columns=col)
    # tree['show']='headings'
    tree.pack(fill=tk.X, pady=5)
    style1 = ttk.Style(rep_frame2)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading", foreground='white', background='#57a1f8', font='14')
    style1.configure("Treeview", foreground='black', background='white', fieldbackground='white',
                     font=('times new roman', 10))
    style1.map('Treeview', background=[('selected', '#87CEFA')])

    tree.column("grn_no", width=75, minwidth=50, anchor=tk.W)
    tree.column("grn_date", width=90, minwidth=50, anchor=tk.W)
    tree.column("supplier", width=200, minwidth=200, anchor=tk.W)
    tree.column("bill_no", width=100, minwidth=50, anchor=tk.W)
    tree.column("bill_date", width=90, minwidth=50, anchor=tk.W)
    tree.column("qty", width=40, minwidth=50, anchor=tk.E)
    tree.column("item_value", width=100, minwidth=50, anchor=tk.E)
    tree.column("discount", width=80, minwidth=50, anchor=tk.E)
    tree.column("cgst", width=100, minwidth=50, anchor=tk.E)
    tree.column("sgst", width=100, minwidth=50, anchor=tk.E)
    tree.column("bill_amount", width=100, minwidth=50, anchor=tk.E)

    tree.heading("grn_no", text="GRN No.", anchor=tk.W)
    tree.heading("grn_date", text="GRN Date", anchor=tk.W)
    tree.heading("supplier", text="Supplier", anchor=tk.W)
    tree.heading("bill_no", text="Bill No.", anchor=tk.W)
    tree.heading("bill_date", text="Bill Date", anchor=tk.W)
    tree.heading("qty", text="Qty", anchor=tk.E)
    tree.heading("item_value", text="Item Value", anchor=tk.E)
    tree.heading("discount", text="Discount", anchor=tk.W)
    tree.heading("cgst", text="CGST @ 9%", anchor=tk.W)
    tree.heading("sgst", text="SGST @ 9%", anchor=tk.W)
    tree.heading("bill_amount", text="Bill Amount", anchor=tk.E)

    vsb = ttk.Scrollbar(rep_frame2, orient="vertical")
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(rep_frame2, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)
    tree.pack()
    tree.bind('<Double-1>', Select_Purchase_Grn_No)
    tree.bind('<Return>', Select_Purchase_Grn_No)
    tree.bind('<FocusIn>', Tree_Get_Focus)
    tree.bind('<FocusOut>', Tree_Lost_Focus)
# ********************** Frame2 - PURCHASE TREEVIEW SETTINGS - END **************************

def treeview_for_sales_report():
    global tree2, rep_frame2
    # ********************** Frame2 - SALES REPORT TREEVIEW SETTINGS - BEGIN **************************
    rep_frame2 = Frame(Report_Form)
    rep_frame2.pack(pady=5)
    rep_frame2.place(x=200, y=60)
    rep_frame2.pack_propagate(False)
    rep_frame2.configure(width=1090, height=436, bg='white')

    col = ('bill_no', 'bill_date', 'customer', 'qty', 'item_value', 'discount', 'cgst', 'sgst', 'bill_amount')
    tree2 = ttk.Treeview(rep_frame2, height=19, show='headings', columns=col)
    tree2.pack(fill=tk.X, pady=5)
    style1 = ttk.Style(rep_frame2)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading", foreground='white', background='#57a1f8', font='14')
    style1.configure("Treeview", foreground='black', background='white', fieldbackground='white',
                     font=('times new roman', 10))
    style1.map('Treeview', background=[('selected', '#87CEFA')])

    tree2.column("bill_no", width=75, minwidth=50, anchor=tk.W)
    tree2.column("bill_date", width=90, minwidth=50, anchor=tk.W)
    tree2.column("customer", width=200, minwidth=200, anchor=tk.W)
    tree2.column("qty", width=50, minwidth=50, anchor=tk.E)
    tree2.column("item_value", width=100, minwidth=50, anchor=tk.E)
    tree2.column("discount", width=80, minwidth=50, anchor=tk.E)
    tree2.column("cgst", width=100, minwidth=50, anchor=tk.E)
    tree2.column("sgst", width=100, minwidth=50, anchor=tk.E)
    tree2.column("bill_amount", width=100, minwidth=50, anchor=tk.E)

    tree2.heading("bill_no", text="Bill No.", anchor=tk.W)
    tree2.heading("bill_date", text="Bill Date", anchor=tk.W)
    tree2.heading("customer", text="Customer", anchor=tk.W)
    tree2.heading("qty", text="Qty", anchor=tk.E)
    tree2.heading("item_value", text="Item Value", anchor=tk.E)
    tree2.heading("discount", text="Discount", anchor=tk.W)
    tree2.heading("cgst", text="CGST @ 9%", anchor=tk.W)
    tree2.heading("sgst", text="SGST @ 9%", anchor=tk.W)
    tree2.heading("bill_amount", text="Bill Amount", anchor=tk.E)

    vsb = ttk.Scrollbar(rep_frame2, orient="vertical")
    vsb.configure(command=tree2.yview)
    tree2.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(rep_frame2, orient="horizontal")
    hsb.configure(command=tree2.xview)
    tree2.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)
    tree2.pack()
    tree2.bind('<Double-1>', Select_Sales_Bill_No)
    tree2.bind('<Return>', Select_Sales_Bill_No)
    tree2.bind('<FocusIn>', Tree2_Get_Focus)
    tree2.bind('<FocusOut>', Tree2_Lost_Focus)

# ********************** Frame2 - SALES REPORT TREEVIEW SETTINGS - END **************************

def Select_Sales_Bill_No(event):
    # ********************** SALES BILL NO. FETCHING - BEGIN **************************
    global bill_no_selected, bill_no
    bill_no_selected = tree2.selection()

    for row in bill_no_selected:
        bill_no = tree2.item(row, 'values')[0]

    Show_Sales_Items()
# ********************** PURCHASE GRN NO. FETCHING - END **************************


def Show_Sales_Items():
    global sal_item_tree, sal_item_form, sal_item_treeview
# ********************** SALES ITEM TREEVIEW SETTINGS - BEGIN **************************
    sal_item_form = Toplevel(Report_Form)
    sal_item_form.grab_set()

    sal_item_form.resizable(False, False)
    sal_item_form.geometry("1000x320+300+220")
    col = ('brand', 'product', 'design', 'color', 'size', 'mrp', 'rate', 'gst', 'id', 'qty', 'amount')

    sal_item_treeview = ttk.Treeview(sal_item_form, height=16, show='headings', columns=col)
    sal_item_treeview.pack(fill=tk.X, pady=5)
    style1 = ttk.Style(sal_item_form)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading", foreground='white', background='#57a1f8', font='14')
    style1.configure("Treeview", foreground='black', background='white', fieldbackground='white', font=('times new roman', 10))
    style1.map('Treeview', background=[('selected', '#63B8FF')])

    sal_item_treeview.column("brand", width=120, minwidth=50, anchor=tk.W)
    sal_item_treeview.column("product", width=120, minwidth=50, anchor=tk.W)
    sal_item_treeview.column("design", width=120, minwidth=50, anchor=tk.W)
    sal_item_treeview.column("color", width=120, minwidth=50, anchor=tk.W)
    sal_item_treeview.column("size", width=60, minwidth=50, anchor=tk.W)
    sal_item_treeview.column("mrp", width=50, minwidth=50, anchor=tk.E)
    sal_item_treeview.column("rate", width=50, minwidth=50, anchor=tk.E)
    sal_item_treeview.column("gst", width=30, minwidth=40, anchor=tk.E)
    sal_item_treeview.column("id", width=30, minwidth=50, anchor=tk.E)
    sal_item_treeview.column("qty", width=30, minwidth=50, anchor=tk.E)
    sal_item_treeview.column("amount", width=100, minwidth=50, anchor=tk.E)

    sal_item_treeview.heading("brand", text="BRAND", anchor=tk.W)
    sal_item_treeview.heading("product", text="PRODUCT", anchor=tk.W)
    sal_item_treeview.heading("design", text="DESIGN NAME", anchor=tk.W)
    sal_item_treeview.heading("color", text="COLOR", anchor=tk.W)
    sal_item_treeview.heading("size", text="SIZE", anchor=tk.W)
    sal_item_treeview.heading("mrp", text="MRP", anchor=tk.W)
    sal_item_treeview.heading("rate", text="RATE", anchor=tk.W)
    sal_item_treeview.heading("gst", text="GST", anchor=tk.E)
    sal_item_treeview.heading("id", text="ID", anchor=tk.E)
    sal_item_treeview.heading("qty", text="QTY", anchor=tk.E)
    sal_item_treeview.heading("amount", text="AMOUNT", anchor=tk.E)

    vsb = ttk.Scrollbar(sal_item_form, orient="vertical")
    vsb.configure(command=sal_item_treeview.yview)
    sal_item_treeview.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(sal_item_form, orient="horizontal")
    hsb.configure(command=sal_item_treeview.xview)
    sal_item_treeview.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)
    sal_item_treeview.pack()
    Cur.execute("select*from sales_item where bill_no = {} ".format(bill_no))
    sal_rep_title = "Sales Item Details For Bill No. " + str(bill_no)
    sal_item_form.title(sal_rep_title)
    a = Cur.fetchall()
    i = 0
    j = 0
    item_tot_qty = 0
    item_tot_amount = 0
    for row in a:
            sal_item_treeview.insert('', j, text="", values=(row[3], row[4], row[5], row[6], row[7], row[8], row[9], "18", row[2], row[10], row[11]))
            j = j+1
            item_tot_qty = item_tot_qty + row[10]
            item_tot_amount = item_tot_amount + row[11]

    sal_item_treeview.insert("", "end", values=("", "", "", "", "", "", "", "", "", "", ""))
    sal_item_treeview.insert("", "end", values=("Total", "", "", "", "", "", "", "", "", item_tot_qty, item_tot_amount))


    sal_item_treeview.focus_set()
    sal_item_treeview.bind("<Escape>", Close_sal_item_treeview)

    child_id = sal_item_treeview.get_children()[0]
    sal_item_treeview.focus(child_id)
    sal_item_treeview.selection_set(child_id)

# *****************************   SALES ITEM TREEVIEW SETTINGS - END     ********************************************

def Close_sal_item_treeview(event):
    sal_item_form.destroy()


def treeview_for_stock_report():
    global tree3, rep_frame2
    # ********************** Frame2 - STOCK REPORT REPORT TREEVIEW SETTINGS - BEGIN **************************
    rep_frame2 = Frame(Report_Form)
    rep_frame2.pack(pady=5)
    rep_frame2.place(x=200, y=60)
    rep_frame2.pack_propagate(False)
    rep_frame2.configure(width=1090, height=436, bg='white')

    col = ('item_id', 'brand', 'product', 'design', 'color', 'sizes', 'mrp', 'rate', 'qty', 'amount')
    tree3 = ttk.Treeview(rep_frame2, height=19, show='headings', columns=col)
    tree3.pack(fill=tk.X, pady=5)
    style1 = ttk.Style(rep_frame2)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 10))
    style1.configure("Treeview.Heading", foreground='white', background='#57a1f8', font='14')
    style1.configure("Treeview", foreground='black', background='white', fieldbackground='white',
                     font=('times new roman', 12))
    style1.map('Treeview', background=[('selected', '#87CEFA')])

    tree3.column("item_id", width=50, minwidth=50, anchor=tk.W)
    tree3.column("brand", width=150, minwidth=50, anchor=tk.W)
    tree3.column("product", width=150, minwidth=150, anchor=tk.W)
    tree3.column("design", width=200, minwidth=50, anchor=tk.W)
    tree3.column("color", width=150, minwidth=50, anchor=tk.W)
    tree3.column("sizes", width=75, minwidth=50, anchor=tk.W)
    tree3.column("mrp", width=75, minwidth=50, anchor=tk.E)
    tree3.column("rate", width=75, minwidth=50, anchor=tk.E)
    tree3.column("qty",width=50, minwidth=50, anchor=tk.E)
    tree3.column("amount", width=100, minwidth=50, anchor=tk.E)

    tree3.heading("item_id", text="ID", anchor=tk.W)
    tree3.heading("brand", text="Brand", anchor=tk.W)
    tree3.heading("product", text="Product", anchor=tk.W)
    tree3.heading("design", text="Design Name", anchor=tk.W)
    tree3.heading("color", text="Color", anchor=tk.W)
    tree3.heading("sizes", text="Size", anchor=tk.W)
    tree3.heading("mrp", text="Mrp", anchor=tk.W)
    tree3.heading("rate", text="Rate", anchor=tk.W)
    tree3.heading("qty", text="Qty", anchor=tk.W)
    tree3.heading("amount", text="Value", anchor=tk.W)

    vsb = ttk.Scrollbar(rep_frame2, orient="vertical")
    vsb.configure(command=tree3.yview)
    tree3.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(rep_frame2, orient="horizontal")
    hsb.configure(command=tree3.xview)
    tree3.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)
    tree3.pack()


# ********************** Frame2 - STOCK REPORT TREEVIEW SETTINGS - END **************************

def Select_Purchase_Grn_No(event):
    # ********************** PURCHASE GRN NO. FETCHING - BEGIN **************************
    global grn_no_selected, grn_no
    grn_no_selected = tree.selection()

    for row in grn_no_selected:
        grn_no = tree.item(row, 'values')[0]

    Show_Purchase_Items()
# ********************** PURCHASE GRN NO. FETCHING - END **************************


def Show_Purchase_Items():
    global pur_item_tree, pur_item_form, pur_item_treeview
# ********************** PURCHASE ITEM TREEVIEW SETTINGS - BEGIN **************************
    pur_item_form = Toplevel(Report_Form)
    pur_item_form.grab_set()

    pur_item_form.resizable(False, False)
    pur_item_form.geometry("1000x320+300+220")
    col = ('brand', 'product', 'design', 'color', 'size', 'mrp', 'rate', 'gst', 'id', 'qty', 'amount')

    pur_item_treeview = ttk.Treeview(pur_item_form, height=16, show='headings', columns=col)
    pur_item_treeview.pack(fill=tk.X, pady=5)
    style1 = ttk.Style(pur_item_form)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading", foreground='white', background='#57a1f8', font='14')
    style1.configure("Treeview", foreground='black', background='white', fieldbackground='white',
                     font=('times new roman', 10))
    style1.map('Treeview', background=[('selected', '#63B8FF')])

    pur_item_treeview.column("brand", width=120, minwidth=50, anchor=tk.W)
    pur_item_treeview.column("product", width=120, minwidth=50, anchor=tk.W)
    pur_item_treeview.column("design", width=120, minwidth=50, anchor=tk.W)
    pur_item_treeview.column("color", width=120, minwidth=50, anchor=tk.W)
    pur_item_treeview.column("size", width=60, minwidth=50, anchor=tk.W)
    pur_item_treeview.column("mrp", width=50, minwidth=50, anchor=tk.E)
    pur_item_treeview.column("rate", width=50, minwidth=50, anchor=tk.E)
    pur_item_treeview.column("gst", width=30, minwidth=40, anchor=tk.E)
    pur_item_treeview.column("id", width=30, minwidth=50, anchor=tk.E)
    pur_item_treeview.column("qty", width=30, minwidth=50, anchor=tk.E)
    pur_item_treeview.column("amount", width=100, minwidth=50, anchor=tk.E)

    pur_item_treeview.heading("brand", text="BRAND", anchor=tk.W)
    pur_item_treeview.heading("product", text="PRODUCT", anchor=tk.W)
    pur_item_treeview.heading("design", text="DESIGN NAME", anchor=tk.W)
    pur_item_treeview.heading("color", text="COLOR", anchor=tk.W)
    pur_item_treeview.heading("size", text="SIZE", anchor=tk.W)
    pur_item_treeview.heading("mrp", text="MRP", anchor=tk.W)
    pur_item_treeview.heading("rate", text="RATE", anchor=tk.W)
    pur_item_treeview.heading("gst", text="GST", anchor=tk.E)
    pur_item_treeview.heading("id", text="ID", anchor=tk.E)
    pur_item_treeview.heading("qty", text="QTY", anchor=tk.E)
    pur_item_treeview.heading("amount", text="AMOUNT", anchor=tk.E)

    vsb = ttk.Scrollbar(pur_item_form, orient="vertical")
    vsb.configure(command=pur_item_treeview.yview)
    pur_item_treeview.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(pur_item_form, orient="horizontal")
    hsb.configure(command=pur_item_treeview.xview)
    pur_item_treeview.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)
    pur_item_treeview.pack()
    Cur.execute("select*from purchase_item where grn_no = {} ".format(grn_no))
    pur_rep_title = "Purchase Item Details For GRN No. " + str(grn_no)
    pur_item_form.title(pur_rep_title)
    a = Cur.fetchall()
    i = 0
    j = 0
    item_tot_qty = 0
    item_tot_amount = 0
    for row in a:
        Cur.execute("select * from item_master where item_id = {} ".format(row[2]))
        for row2 in Cur:
            pur_item_treeview.insert('', j, text="", values=(row2[0], row2[1], row2[2], row2[3], row2[4], row2[5], row2[6], row2[7], row2[9], row[3], row[4]))
            j = j+1
            item_tot_qty = item_tot_qty + row[3]
            item_tot_amount = item_tot_amount + row[4]

    pur_item_treeview.insert("", "end", values=("", "", "", "", "", "", "", "", "", "", ""))
    pur_item_treeview.insert("", "end", values=("Total", "", "", "", "", "", "", "", "", item_tot_qty, item_tot_amount))


    pur_item_treeview.focus_set()
    pur_item_treeview.bind("<Escape>", Close_pur_item_treeview)

    child_id = pur_item_treeview.get_children()[0]
    pur_item_treeview.focus(child_id)
    pur_item_treeview.selection_set(child_id)

# *****************************   PURCHASE ITEM TREEVIEW SETTINGS - END     ********************************************

def Close_pur_item_treeview(event):
    pur_item_form.destroy()

def Design_Report_Form_Load():
    global Report_Form, rep_show_button, rep_clear_button, form_top_label, form_bottom_label
    global rep_brand_combo_tv, rep_product_combo_tv, rep_design_name_combo_tv, rep_color_combo_tv, rep_size_combo_tv
    global rep_from_date_entry, rep_to_date_entry, rep_frame3
    global rep_from_date_entry_tv, rep_to_date_entry_tv

    rep_from_date_entry_tv = StringVar()
    rep_to_date_entry_tv = StringVar()
    rep_brand_combo_tv = StringVar()
    rep_product_combo_tv = StringVar()
    rep_design_name_combo_tv = StringVar()
    rep_color_combo_tv = StringVar()
    rep_size_combo_tv = StringVar()

    Report_Form = Tk()
    Report_Form.title('')
    Report_Form.geometry("1300x560+20+70")
    Report_Form.config(bg='white')
    Report_Form.resizable(False,False)
    #form_top_label = Label(Report_Form, text="R E P O R T ", width=1300, bg="#57a1f8", fg='white', font=('Microsoft Yahei UI Light', 26, 'bold'))
    form_top_label = Label(Report_Form, text="R E P O R T ", width=1300, bg="#57a1f8", fg='white',font=('impact', 26, 'bold'))
    form_top_label.pack()

#****************************** RADIO BUTTON - SETTINGS BEGIN ********************************
    radio_value = IntVar()
    rep_purchase_radio = Radiobutton(Report_Form, text='Purchase', variable=radio_value, value=1, bg='white', fg='#57a1f8', font=('impact', 16, 'bold'))
    rep_purchase_radio.place(x=20, y=70)
    rep_purchase_radio.bind('<ButtonRelease>', Set_Purchase_Report_Type)

    rep_sales_radio = Radiobutton(Report_Form, text='Sales', variable=radio_value, value=2, bg='white',  fg='#57a1f8', font=('impact', 16, 'bold'))
    rep_sales_radio.place(x=20, y=100)
    rep_sales_radio.bind('<ButtonRelease>', Set_Sales_Report_Type)

    rep_stock_radio = Radiobutton(Report_Form, text='Stock', variable=radio_value, value=3, bg='white',  fg='#57a1f8', font=('impact', 16, 'bold'))
    rep_stock_radio.place(x=20, y=130)
    rep_stock_radio.bind('<ButtonRelease>', Set_Stock_Report_Type)
#****************************** RADIO BUTTON - SETTINGS END ********************************

# ************** Frame1 - Lables, Date Entry Box - Settings BEGIN *******************************
    rep_frame1 = Frame(Report_Form, width =190, height=90, bg='LightSteelBlue1')
    rep_frame1.place(x=5,y=170)

    rep_from_date_label = Label(rep_frame1, text='From', bg ='LightSteelBlue1', font=('copper',8))
    rep_from_date_label.place(x=20, y=0)
    rep_from_date_entry = DateEntry(rep_frame1, selectmode='day', textvariable=rep_from_date_entry_tv,width=10, date_pattern='dd-mm-yyyy')
    rep_from_date_entry.place(x=20, y=20)
    rep_from_date_entry.bind('<ButtonRelease>', Show_To_Calendar)

    rep_to_date_label = Label(rep_frame1, text='To', bg ='LightSteelBlue1', font=('copper',8))
    rep_to_date_label.place(x=20, y=42)
    rep_to_date_entry = DateEntry(rep_frame1, selectmode='day', textvariable=rep_to_date_entry_tv,width=10, date_pattern='dd-mm-yyyy')
    rep_to_date_entry.place(x=20, y=60)
    rep_to_date_entry.bind('<ButtonRelease>', Show_To_Calendar)

# ************** Frame1 - Labels, Date Entry Box - Settings END *******************************



#************** Bottom Buttons & Labels - Settings BEGIN *******************************

    rep_show_button = Button(Report_Form, text='S H O W', bg='#63B8FF', fg='white', width=7, font=('bold', 10))
    rep_show_button.place(x=20, y=470)
    rep_show_button.bind('<Return>', Show_Report)
    rep_show_button.bind('<ButtonRelease>', Show_Report)

    rep_clear_button = Button(Report_Form, text='C L E A R', bg='#63B8FF', fg='white', width=7, font=('bold', 10))
    rep_clear_button.place(x=90, y=470)
    rep_clear_button.bind('<Return>', Clear_Attribute_Field)
    rep_clear_button.bind('<ButtonRelease>', Clear_Attribute_Field)

    form_bottom_label = Label(Report_Form, width=800, bg="#57a1f8", fg='white',font=('impact', 16))
    form_bottom_label.pack(side=BOTTOM)
#************** Bottom Buttons & Labels - Settings END *******************************


