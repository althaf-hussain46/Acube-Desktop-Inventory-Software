import datetime
import os
from tkinter import*
import tkinter as tk
from tkinter import ttk
from DB_Connection import*
from datetime import*
from datetime import datetime
from tkinter import messagebox
from Class_Purchase_Entry import*
from tkcalendar import DateEntry
from Class_Report import*

cls_rep = cls_report()

obj_cls_pur_entry = cls_purchase_entry()
Con = DB_Connect()
Cur = Con.cursor()
Cur1 = Con.cursor()
Cur2 = Con.cursor()
global field1
s_no = 0
total_qty1 = 0
total_amount1 = 0.00
dt=datetime.today()
newdate = dt.strftime("%d-%m-%Y")
def Show_Calendar(event):
    pur_bill_date_entry.config(text=pur_bill_date_entry_tv.get())

def set_focus_pur_grn_no(event):
    form_bottom_label.config(text="To List GRN No.'s Type 2 & Press [F1] Key")

def set_focus_pur_supp_list(event):
    form_bottom_label.config(text="Choose Supplier Name From The List")

def set_focus_pur_bill_no(event):
    pur_bill_no_entry.focus_set()
    pur_bill_no_entry.selection_range(0,len(str(pur_bill_no_entry_tv.get())))
    form_bottom_label.config(text="Enter Bill No.      Maximum Allowed Characters - 25")

def set_focus_pur_bill_date(event):
    pur_bill_date_entry.focus_set()
    pur_bill_date_entry.selection_range(0, len(str(pur_bill_date_entry_tv.get())))
    form_bottom_label.config(text="Click To Choose Date        Press [Enter] Key to Proceed")

def set_focus_pur_brand(event):
    pur_brand_entry.focus_set()
    obj_cls_pur_entry.set_pur_field_focus("Brand")
    pur_brand_entry.selection_range(0, len(str(pur_brand_entry_tv.get())))
    form_bottom_label.config(text="Enter Brand Name To Create       Maximum Allowed Characters - 25        To List Brand Press [F1]        To List ITEMS Press [F2]")

def lost_focus_pur_brand(event):
    form_bottom_label.config(text="")

def set_focus_pur_product(event):
    pur_product_entry.focus_set()
    obj_cls_pur_entry.set_pur_field_focus("Product")
    pur_product_entry.selection_range(0, len(str(pur_product_entry_tv.get())))
    form_bottom_label.config(text="Enter Product Name To Create        Maximum Allowed Characters - 25        To List Product Press [F1]")

def set_focus_pur_design_name(event):
    pur_design_name_entry.focus_set()
    obj_cls_pur_entry.set_pur_field_focus("Design")
    pur_design_name_entry.selection_range(0, len(str(pur_design_name_entry_tv.get())))
    form_bottom_label.config(text="Enter Design Name To Create        Maximum Allowed Characters - 25        To List Design Press [F1]")

def set_focus_pur_color(event):
    pur_color_entry.focus_set()
    obj_cls_pur_entry.set_pur_field_focus("Color")
    pur_color_entry.selection_range(0, len(str(pur_color_entry_tv.get())))
    form_bottom_label.config(text="Enter Color To Create        Maximum Allowed Characters - 25        To List Color Press [F1]")

def set_focus_pur_size(event):
    pur_size_entry.focus_set()
    obj_cls_pur_entry.set_pur_field_focus("Size")
    pur_size_entry.selection_range(0, len(str(pur_size_entry_tv.get())))
    form_bottom_label.config(text="Enter Size To Create        Maximum Allowed Characters - 15        To List Sizes Press [F1]")

def set_focus_pur_mrp(event):
    pur_mrp_entry.focus_set()
    pur_mrp_entry.selection_range(0, len(str(pur_mrp_entry_tv.get())))
    form_bottom_label.config(text="Enter Mrp        Maximum Allowed Number Including Decimal - 10")

def set_focus_pur_rate(event):
    pur_rate_entry.focus_set()
    pur_rate_entry.selection_range(0, len(str(pur_rate_entry_tv.get())))
    form_bottom_label.config(text="Enter Rate        Maximum Allowed Number Including Decimal - 10")

def set_focus_pur_qty():
    pur_qty_entry.focus_set()
    pur_qty_entry.selection_range(0, len(str(pur_qty_entry_tv.get())))

def set_focus_pur_qty1(event):
    pur_qty_entry.focus_set()
    pur_qty_entry.selection_range(0, len(str(pur_qty_entry_tv.get())))
    form_bottom_label.config(text="Enter Qty        Integer Numbers Only")

def set_focus_pur_discount(event):
    form_bottom_label.config(text="Enter Discount Amount        Maximum Allowed Number Including Decimal - 10")

def set_focus_insert_button(event):
    form_bottom_label.config(text="To Add Purchase Press - [INSERT]")
    pur_insert_button.config(bg="#87CEFA", fg="black")

def set_focus_edit_button(event):
    form_bottom_label.config(text="To Modify Purchase Press - [EDIT]")
    pur_edit_button.config(bg="#87CEFA", fg="black")

def set_focus_delete_button(event):
    form_bottom_label.config(text="To Remove Purchase Press - [DELETE]")
    pur_delete_button.config(bg="#87CEFA", fg="black")

def set_focus_export_button(event):
    form_bottom_label.config(text="To Export Purchase Press - [REPORT]")
    pur_export_button.config(bg="#87CEFA", fg="black")

def set_focus_quit_button(event):
    form_bottom_label.config(text="To Exit This Form Press - [QUIT]")
    pur_quit_button.config(bg="#87CEFA", fg="black")

def focus_out_insert_button(evcnt):
    form_bottom_label.config(text="To Insert Purchase Press - [INSERT]       To Edit Purchase Press - [EDIT]       To Delete Purchase Press - [DELETE]       To Export Purchase Press - [REPORT]        To Move Next Button Press - [Tab]")
    pur_insert_button.config(bg="Grey35", fg="white")

def focus_out_edit_button(event):
    form_bottom_label.config(text="To Insert Purchase Press - [INSERT]       To Edit Purchase Press - [EDIT]       To Delete Purchase Press - [DELETE]       To Export Purchase Press - [REPORT]        To Move Next Button Press - [Tab]")
    pur_edit_button.config(bg="Grey35", fg="white")

def focus_out_delete_button(event):
    form_bottom_label.config(text="To Insert Purchase Press - [INSERT]       To Edit Purchase Press - [EDIT]       To Delete Purchase Press - [DELETE]       To Export Purchase Press - [REPORT]        To Move Next Button Press - [Tab]")
    pur_delete_button.config(bg="Grey35", fg="white")

def focus_out_export_button(event):
    form_bottom_label.config(text="To Insert Purchase Press - [INSERT]       To Edit Purchase Press - [EDIT]       To Delete Purchase Press - [DELETE]       To Export Purchase Press - [REPORT]        To Move Next Button Press - [Tab]")
    pur_export_button.config(bg="Grey35", fg="white")

def focus_out_quit_button(event):
    form_bottom_label.config(text="To Insert Purchase Press - [INSERT]       To Edit Purchase Press - [EDIT]       To Delete Purchase Press - [DELETE]       To Export Purchase Press - [REPORT]        To Move Next Button Press - [Tab]")
    pur_quit_button.config(bg="Grey35", fg="white")

def set_focus_save_button(event):
    pur_save_button.focus_set()
    form_bottom_label.config(text="To Save This Purchase Entries Press [Enter] Key")
    pur_save_button.config(bg="#87CEFA", fg="black" )

def focus_out_save_button(event):
    pur_save_button.config(bg="Grey35", fg="white")

def set_focus_update_button(event):
    pur_save_button.config(bg="#87CEFA", fg="black")
    form_bottom_label.config(text="To Update This Purchase Entries Press [Enter] Key")

def focus_out_update_button(event):
    pur_save_button.config(bg="Grey35", fg="white")

def set_focus_delete2_button(event):
    pur_delete_button.focus_set()
    pur_delete_button.config(bg="#87CEFA", fg="black")
    form_bottom_label.config(text="To Delete This Purchase Entries Press [Enter] Key")

def focus_out_delete2_button(event):
    pur_delete_button.config(bg="Grey35", fg="white")

def set_focus_export_to_excel(event):
    pur_export_button.config(bg="#87CEFA", fg="black")
    form_bottom_label.config(text="To View Purchase In Excel Press [Enter] Key")

def focus_out_export_to_excel(event):
    pur_export_button.config(bg="Grey35", fg="white")

def set_focus_cancel_button(event):
    pur_cancel_button.config(bg="#87CEFA", fg="black")
    print(obj_cls_pur_entry.get_pur_button_clicked())
    if obj_cls_pur_entry.get_pur_button_clicked == 'report':
        form_bottom_label.config(text=" ")
    else:
        form_bottom_label.config(text="To Undo The Changes Made To This Purchase Entries Press [Enter] Key")

def focus_out_cancel_button(event):
    pur_cancel_button.config(bg="Grey35", fg="white")
    form_bottom_label.config(text="")

def set_focus_treeview(event):
    if obj_cls_pur_entry.get_pur_button_clicked() == "insert" or obj_cls_pur_entry.get_pur_button_clicked() == "edit":
        form_bottom_label.config(text="To Delete The Row Press [Delete] Key")
    else:
        form_bottom_label.config(text="")

def Validate_Decimal_Number(inp):

    if inp.isdigit():
        return True
    elif inp == "":
        return True
    elif inp == '.':
        return inp
    else:
        return False

def Validate_Integer_Number(inp):
    if inp.isdigit():
        return True
    elif inp == "":
        return True
    else:
        return False

def Supplier_Name_Fetching():
    name = list()
    Cur.execute("select name from supplier_master order by name")
    for supplier_name in Cur:
        name.append(supplier_name[0])

    return name

def Refresh_cust_Data2(records):
    for item in tree.get_children():
        tree.delete(item)
    i = 0
    for row in records:
        tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        # tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        i = i + 1

def Select_Item_Data(event):
    if obj_cls_pur_entry.get_pur_button_clicked() == "insert" or obj_cls_pur_entry.get_pur_button_clicked() == "edit":
        dum1 = tree.selection()

        for row4 in dum1:
            pur_brand_entry_tv.set(tree.item(row4, 'values')[0])
            pur_product_entry_tv.set(tree.item(row4, 'values')[1])
            pur_design_name_entry_tv.set(tree.item(row4, 'values')[2])
            pur_color_entry_tv.set(tree.item(row4, 'values')[3])
            pur_size_entry_tv.set(tree.item(row4, 'values')[4])
            pur_mrp_entry_tv.set(tree.item(row4, 'values')[5])
            pur_rate_entry_tv.set(tree.item(row4, 'values')[6])
            pur_gst_entry_tv.set(tree.item(row4, 'values')[7])
            pur_id_entry_tv.set(tree.item(row4, 'values')[8])
            pur_qty_entry_tv.set(tree.item(row4, 'values')[9])
            pur_amount_entry_tv.set(tree.item(row4, 'values')[10])

def Add_Purchase_Items_In_Treeview(event):
    global total_qty1, total_amount1
    Cur.execute("select*from item_master where item_id = {}".format(pur_id_entry_tv.get()))
    for row in Cur:
        pur_amount_entry_tv.set(row[6] * pur_qty_entry_tv.get())
        tree.insert("", "end", text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[9], pur_qty_entry_tv.get(), pur_amount_entry_tv.get()))
    total_qty1 = obj_cls_pur_entry.get_pur_tot_qty() + pur_qty_entry_tv.get()
    total_amount1 = obj_cls_pur_entry.get_pur_tot_amount() + pur_amount_entry_tv.get()
    obj_cls_pur_entry.set_pur_tot_qty(total_qty1)
    obj_cls_pur_entry.set_pur_tot_amount(round(total_amount1, 2))
    pur_tot_qty_entry_tv.set(total_qty1)
    pur_tot_amount_entry_tv.set(round(total_amount1, 2))
    Purchase_Bill_Amt_Calculate(total_amount1)
    pur_qty_entry.config(state="disable")
    form_bottom_label.config(text="Enter Brand Name To Create       Maximum Allowed Characters - 25        To List Brand Press [F1]        To List ITEMS Press [F2]")
    pur_brand_entry.focus_set()
    pur_brand_entry.selection_range(0,len(pur_brand_entry_tv.get()))


def Purchase_Bill_Amt_Calculate(n):
    dum_cgst = ((n-float(pur_discount_entry_tv.get()))*9)/100
    dum_sgst = ((n-float(pur_discount_entry_tv.get()))*9)/100
    obj_cls_pur_entry.set_pur_discount(float(pur_discount_entry_tv.get()))
    obj_cls_pur_entry.set_pur_cgst(round(dum_cgst, 2))
    obj_cls_pur_entry.set_pur_sgst(round(dum_sgst, 2))
    tot_amt = n - obj_cls_pur_entry.get_pur_discount() + obj_cls_pur_entry.get_pur_cgst() + obj_cls_pur_entry.get_pur_sgst()
    obj_cls_pur_entry.set_pur_bill_amount(round(tot_amt, 2))
    pur_cgst_entry_tv.set(obj_cls_pur_entry.get_pur_cgst())
    pur_sgst_entry_tv.set(obj_cls_pur_entry.get_pur_sgst())
    pur_bill_amt_entry_tv.set(obj_cls_pur_entry.get_pur_bill_amount())

def Purchase_Bill_Amt_Calculate2(event):
    Purchase_Bill_Amt_Calculate(obj_cls_pur_entry.get_pur_tot_amount())

def Validate_Number(inp):
    if inp == "":
        return True
    try:
        int(inp)
        if len(inp) <= 3:
            return True
        else:
            return False
    except ValueError:
            return False


def Validate_Number2(inp):
    if inp == "":
        return True
    try:
        float(inp)
        if len(inp) <= 8:
            return True
        else:
            return False
    except ValueError:
        if inp == ".":
            return True
        else:
            return False


def Validate_Integer_Number2(event):
    if event.keycode >= 48 and event.keycode <=57:
        print("key pressed", event.char)
        return int(event.char)
    else:
        print('nothing')
        event.delete(1)
        return None

def Validate_Integer_Number3(event):
    if event.char.isdigit():
        return int(event.char)
    else:
        return None

def Set_Zero(event):
    if event.widget.get() == "":
        event.widget.insert(0, "0.0")
        Purchase_Bill_Amt_Calculate(obj_cls_pur_entry.get_pur_tot_amount())

def Delete_Purchase_Items_In_Treeview(event):
    global total_qty2, total_amount2
    if obj_cls_pur_entry.get_pur_button_clicked() == "insert" or obj_cls_pur_entry.get_pur_button_clicked() == "edit":
        item = tree.selection()
        for i in item:
            total_qty2 = obj_cls_pur_entry.get_pur_tot_qty() - int(tree.item(i, 'values')[9])
            total_amount2 = obj_cls_pur_entry.get_pur_tot_amount() - float(tree.item(i, 'values')[10])
        obj_cls_pur_entry.set_pur_tot_qty(total_qty2)
        obj_cls_pur_entry.set_pur_tot_amount(total_amount2)
        pur_tot_qty_entry_tv.set(total_qty2)
        pur_tot_amount_entry_tv.set(total_amount2)
        tree.delete(item)
        Purchase_Bill_Amt_Calculate(total_amount2)
        pur_cgst_entry_tv.set(obj_cls_pur_entry.get_pur_cgst())
        pur_sgst_entry_tv.set(obj_cls_pur_entry.get_pur_sgst())
        pur_bill_amt_entry_tv.set(obj_cls_pur_entry.get_pur_bill_amount())
        if len(tree.selection()) == 0:
            child_id = tree.get_children()[0]
            tree.focus(child_id)
            tree.selection_set(child_id)

def item_id_creation(event):
    brand1 = pur_brand_entry_tv.get()
    product1 = pur_product_entry_tv.get()
    design1 = pur_design_name_entry_tv.get()
    color1 = pur_color_entry_tv.get()
    size1 = pur_size_entry_tv.get()
    mrp1 = pur_mrp_entry_tv.get()
    rate1 = pur_rate_entry_tv.get()
    gst1 = pur_gst_entry_tv.get()
    crt_date1 = date.today().strftime("%Y-%m-%d")

    d_mrp = str(pur_mrp_entry_tv.get())
    d_rate = str(pur_rate_entry_tv.get())
    if len(pur_brand_entry_tv.get().strip()) > 0 and len(pur_product_entry_tv.get().strip()) > 0 and \
            len(pur_design_name_entry_tv.get().strip()) > 0 and len(pur_color_entry_tv.get().strip()) > 0 and \
            len(pur_size_entry_tv.get().strip()) > 0 and len(d_mrp.strip()) > 0 and len(d_rate.strip()) > 0:
        Cur.execute("select max(item_id) as dum_id from item_master")
        data = Cur.fetchall()
        for row in data:
            i = row[0]
        i = str(i)
        if i == 'None':
            pur_id_entry_tv.set(1)
            Cur.execute("insert into item_master (brand,product,design,color,size,mrp,rate,gst,crt_date,item_id) values('{}','{}','{}','{}','{}',{},{},{},'{}',{})".format(brand1,product1,design1,color1,size1,mrp1,rate1,gst1,crt_date1, pur_id_entry_tv.get()))
            Con.commit()
            pur_qty_entry.config(state="normal")
        else:
            pur_id_entry_tv.set(int(i) + 1)
            pur_qty_entry.config(state="normal")
            Cur.execute("select brand, product, design, color, size, mrp, rate, gst, crt_date, item_id from item_master where brand='{}' and product ='{}' and design ='{}' and color = '{}' and size = '{}'  and mrp = {} and rate = {} and gst = {}".format(brand1,product1,design1,color1,size1,mrp1,rate1,gst1))
            data1 = Cur.fetchall()
            if not data1:
                Cur.execute("insert into item_master (brand,product,design,color,size,mrp,rate,gst,crt_date,item_id) values('{}','{}','{}','{}','{}',{},{},{},'{}',{})".format(brand1, product1, design1, color1, size1, mrp1, rate1, gst1, crt_date1, pur_id_entry_tv.get()))
                Con.commit()
            else:
                for row2 in data1:
                    dum_data2 = row2[9]
                dum_data2
                pur_id_entry_tv.set(dum_data2)
        set_focus_pur_qty()
        form_bottom_label.config(text="Enter Qty        Integer Numbers Only")

    else:
        messagebox.showinfo('', "Enter All Fields")
        form_bottom_label.config(text="Enter Brand Name To Create       Maximum Allowed Characters - 25        To List Brand Press [F1]        To List ITEMS Press [F2]")
        pur_brand_entry.focus_set()

def Show_Field_Master(event):
    global field_form, field_treeview

    field_form = tk.Toplevel()
    field_form.title('')
    field_form.resizable(False, False)
    field_form.geometry("150x148+672+300")
    col = ('field_name')
    field_treeview = ttk.Treeview(field_form, height=6, show='headings', columns=col)
    field_treeview.pack(fill=tk.X, pady=5)
    style1 = ttk.Style(field_form)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading", foreground='white', background='Grey35', font='14')
    style1.configure("Treeview", foreground='black', background='#87CEFA', fieldbackground='#B0E2FF',
                     font=('times new roman', 10))
    style1.map('Treeview', background=[('selected', 'Grey35')])

    field_treeview.column("field_name", width=150, minwidth=150, anchor=tk.W)

    field_treeview.heading("field_name", text=obj_cls_pur_entry.get_pur_field_focus() + ' List', anchor=tk.W)

    vsb = ttk.Scrollbar(field_form, orient="vertical")
    vsb.configure(command=field_treeview.yview)
    field_treeview.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    field_treeview.pack()

    if obj_cls_pur_entry.get_pur_field_focus() == "Brand":
        Cur.execute("select distinct(brand) from item_master where brand like '" + pur_brand_entry_tv.get() + "%' order by brand")
    elif obj_cls_pur_entry.get_pur_field_focus() == "Product":
        Cur.execute("select distinct(product) from item_master where product like '" + pur_product_entry_tv.get() + "%' order by product")
    elif obj_cls_pur_entry.get_pur_field_focus() == "Design":
        Cur.execute("select distinct(design) from item_master where design like '" + pur_design_name_entry_tv.get() + "%' order by design")
    elif obj_cls_pur_entry.get_pur_field_focus() == "Color":
        Cur.execute("select distinct(color) from item_master where color like '" + pur_color_entry_tv.get() + "%' order by color")
    elif obj_cls_pur_entry.get_pur_field_focus() == "Size":
        Cur.execute("select distinct(size) from item_master where size like '" + pur_size_entry_tv.get() + "%' order by size")

    for row in Cur:
        field_treeview.insert("", END, values=row)

    field_treeview.focus_set()

    field_treeview.bind("<Double-1>", Select_Field)
    field_treeview.bind("<Return>", Select_Field)
    field_treeview.bind("<Escape>", Close_Field_Treeview)

    child_id = field_treeview.get_children()[0]
    field_treeview.focus(child_id)
    field_treeview.selection_set(child_id)

def Select_Field(event):
    field_selected = field_treeview.selection()

    for row in field_selected:
        if obj_cls_pur_entry.get_pur_field_focus() == "Brand":
            pur_brand_entry_tv.set(field_treeview.item(row, 'values')[0])
        elif obj_cls_pur_entry.get_pur_field_focus() == "Product":
            pur_product_entry_tv.set(field_treeview.item(row, 'values')[0])
        elif obj_cls_pur_entry.get_pur_field_focus() == "Design":
            pur_design_name_entry_tv.set(field_treeview.item(row, 'values')[0])
        elif obj_cls_pur_entry.get_pur_field_focus() == "Color":
            pur_color_entry_tv.set(field_treeview.item(row, 'values')[0])
        elif obj_cls_pur_entry.get_pur_field_focus() == "Size":
            pur_size_entry_tv.set(field_treeview.item(row, 'values')[0])

    field_form.destroy()
    if obj_cls_pur_entry.get_pur_field_focus() == "Brand":
        pur_product_entry.focus_set()
    elif obj_cls_pur_entry.get_pur_field_focus() == "Product":
        pur_design_name_entry.focus_set()
    elif obj_cls_pur_entry.get_pur_field_focus() == "Design":
        pur_color_entry.focus_set()
    elif obj_cls_pur_entry.get_pur_field_focus() == "Color":
        pur_size_entry.focus_set()
    elif obj_cls_pur_entry.get_pur_field_focus() == "Size":
        pur_mrp_entry.focus_set()


def Close_Field_Treeview(event):
    obj_cls_pur_entry.set_pur_field_focus("")
    field_form.destroy()


def Show_Item_Master(event):
    global item_form, item_treeview

    item_form = tk.Toplevel()
    item_form.title('ITEMS List')
    item_form.resizable(False, False)
    item_form.geometry("640x148+672+300")
    col = ('brand', 'product', 'design', 'color', 'size', 'mrp', 'rate', 'gst', 'id')
    item_treeview = ttk.Treeview(item_form, height=6, show='headings', columns=col)
    item_treeview.pack(fill=tk.X, pady=5)
    style1 = ttk.Style(item_form)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading", foreground='white', background='Grey35', font='14')
    style1.configure("Treeview", foreground='black', background='#87CEFA', fieldbackground='#B0E2FF',
                     font=('times new roman', 10))
    style1.map('Treeview', background=[('selected', 'Grey35')])

    item_treeview.column("brand", width=80, minwidth=50, anchor=tk.W)
    item_treeview.column("product", width=90, minwidth=50, anchor=tk.W)
    item_treeview.column("design", width=130, minwidth=50, anchor=tk.W)
    item_treeview.column("color", width=70, minwidth=50, anchor=tk.W)
    item_treeview.column("size", width=50, minwidth=50, anchor=tk.W)
    item_treeview.column("mrp", width=60, minwidth=50, anchor=tk.E)
    item_treeview.column("rate", width=60, minwidth=50, anchor=tk.E)
    item_treeview.column("gst", width=40, minwidth=40, anchor=tk.S)
    item_treeview.column("id", width=40, minwidth=40, anchor=tk.E)

    item_treeview.heading("brand", text="BRAND", anchor=tk.W)
    item_treeview.heading("product", text="PRODUCT", anchor=tk.W)
    item_treeview.heading("design", text="DESIGN NAME", anchor=tk.W)
    item_treeview.heading("color", text="COLOR", anchor=tk.W)
    item_treeview.heading("size", text="SIZE", anchor=tk.W)
    item_treeview.heading("mrp", text="MRP", anchor=tk.E)
    item_treeview.heading("rate", text="RATE", anchor=tk.E)
    item_treeview.heading("gst", text="GST", anchor=tk.S)
    item_treeview.heading("id", text="ID", anchor=tk.E)

    vsb = ttk.Scrollbar(item_form, orient="vertical")
    vsb.configure(command=item_treeview.yview)
    item_treeview.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(item_form, orient="horizontal")
    hsb.configure(command=item_treeview.xview)
    item_treeview.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)
    item_treeview.pack()

    Cur.execute("select*from item_master where design like '%"+pur_brand_entry_tv.get()+"%' order by design, brand, product")

    i = 0
    for row in Cur:
        item_treeview.insert('',i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[9]))
        i = i+1

    item_treeview.focus_set()

    item_treeview.bind("<Double-1>", Select_Item)
    item_treeview.bind("<Return>", Select_Item)
    item_treeview.bind("<Escape>", Close_Item_Treeview)

    child_id = item_treeview.get_children()[0]
    item_treeview.focus(child_id)
    item_treeview.selection_set(child_id)

    # *****************************   Frame4 - TREEVIEW SETTINGS - END     ********************************************

def Close_Item_Treeview(event):
    item_form.destroy()


def Select_Item(event):
    item_selected = item_treeview.selection()

    for row in item_selected:

        pur_brand_entry_tv.set(item_treeview.item(row, 'values')[0])
        pur_product_entry_tv.set(item_treeview.item(row, 'values')[1])
        pur_design_name_entry_tv.set(item_treeview.item(row, 'values')[2])
        pur_color_entry_tv.set(item_treeview.item(row, 'values')[3])
        pur_size_entry_tv.set(item_treeview.item(row, 'values')[4])
        pur_mrp_entry_tv.set(item_treeview.item(row, 'values')[5])
        pur_rate_entry_tv.set(item_treeview.item(row, 'values')[6])
        pur_gst_entry_tv.set(item_treeview.item(row, 'values')[7])
        pur_id_entry_tv.set(item_treeview.item(row, 'values')[8])
    item_form.destroy()
    if pur_id_entry_tv.get() > 0:
        pur_qty_entry.config(state='normal')
        pur_qty_entry.focus_set()
        pur_qty_entry.selection_range(0, len(str(pur_qty_entry_tv.get())))

def String_To_Date(get_str):
    date_format = datetime.strptime(get_str, "%Y-%m-%d")
    return date_format.strftime("%d-%m-%Y")

def Save_Button_Click(event):
    grn_no1 = pur_grn_no_entry_tv.get()
    grn_date1 = date.today().strftime("%Y-%m-%d")
    supp_name1 = pur_sup_list_combo.get()
    bill_no1 = pur_bill_no_entry_tv.get()
    str_date1 = str(pur_bill_date_entry_tv.get())
    bill_date1 = datetime.strptime(str_date1, "%d-%m-%Y")
    bill_qty1 = pur_tot_qty_entry_tv.get()
    item_total1 = pur_tot_amount_entry_tv.get()
    less_amt1 = pur_discount_entry_tv.get()
    cgst_amt1 = pur_cgst_entry_tv.get()
    sgst_amt1 = pur_sgst_entry_tv.get()
    bill_amt1 = pur_bill_amt_entry_tv.get()

    if len(supp_name1.strip()) > 0 and len(bill_no1.strip()) > 0 and bill_qty1 > 0 and less_amt1 >= 0:
        if len(bill_no1.strip()) <= 25  and  len(str(less_amt1).strip()) <= 10:
            Cur.execute("select max(grn_no) as grn_nos from purchase_master")
            for row in Cur:
                id_no = row[0]

            if id_no == None:
                id_no = 20230001
            else:
                id_no = id_no + 1

            Cur.execute("insert into purchase_master (grn_no,grn_date,supp_name,bill_no,bill_date,bill_qty,"
                        "item_total,less_amt,cgst_amt,sgst_amt,bill_amt) "
                        "values({},'{}','{}','{}','{}',{},{},{},{},{},{})"
                        .format(grn_no1,grn_date1,supp_name1,bill_no1,bill_date1,bill_qty1,
                        item_total1,less_amt1,cgst_amt1,sgst_amt1,bill_amt1))
            Con.commit()
            k = 0
            for k in tree.get_children():
                Cur.execute("insert into purchase_item (grn_no,grn_date,item_id,item_qty,item_amount) "
                            "values({},'{}',{},{},{})"
                            .format(grn_no1, grn_date1, tree.item(k,'value')[8], tree.item(k,'value')[9],
                            tree.item(k,'value')[10]))
                Con.commit()
                dum_item_id = int(tree.item(k,'value')[8])
                qry2 = "select * from stock_balance where item_id = {}".format(dum_item_id)
                Cur.execute(qry2)
                check_item_id = Cur.fetchall()
                if not check_item_id:
                    Cur.execute("insert into stock_balance (item_id,brand,product,design,color,sizes,mrp,rate,"
                                "bal_qty,bal_amount) values({},'{}','{}','{}','{}','{}',{},{},{},{})"
                                .format(tree.item(k,'value')[8],tree.item(k,'value')[0],tree.item(k,'value')[1],
                                tree.item(k,'value')[2],tree.item(k,'value')[3],tree.item(k,'value')[4],
                                tree.item(k,'value')[5],tree.item(k,'value')[6],tree.item(k,'value')[9],
                                tree.item(k,'value')[10]))
                    Con.commit()
                else:
                    for m in check_item_id:
                        dum_tot_qty = int(m[8]) + int(tree.item(k, 'value')[9])
                        dum_tot_amt = float(m[9]) + float(tree.item(k, 'value')[10])
                        print(dum_tot_qty)
                        print(dum_tot_amt)
                        qry3 = "update stock_balance set bal_qty = {}, bal_amount = {} where item_id = {}"\
                            .format(dum_tot_qty,dum_tot_amt, dum_item_id)
                        Cur.execute(qry3)
                        Con.commit()

            messagebox.showinfo('', "PURCHASE Entry Added Successfully")
            Purchase_Form.destroy()
            Design_Purchase_Form_Load()
        else:
            messagebox.showwarning('', 'Enter Details As Per The Limitations')
    else:
        messagebox.showwarning('', 'Enter Data In All Fields')
        Purchase_Form.focus_set()
        pur_save_button.focus_set()


def Purchase_Insert(event):
    global pur_grn_no_entry, pur_grn_date_entry, pur_sup_list_combo, pur_bill_no_entry, pur_bill_date_entry,\
           pur_brand_entry, pur_product_entry, pur_design_name_entry, pur_color_entry, pur_size_entry,\
           pur_mrp_entry, pur_rate_entry, pur_gst_entry, pur_id_entry, pur_qty_entry, pur_amount_entry
    global pur_tot_qty_entry, pur_tot_amount_entry, pur_discount_entry, pur_cgst_entry, pur_sgst_entry, pur_bill_amt_entry

    global a3, pur_frame3, pur_save_button, pur_cancel_button
    global pur_grn_no_entry_tv, pur_grn_date_entry_tv, pur_sup_list_combo_tv, pur_bill_no_entry_tv, pur_bill_date_entry_tv, \
        pur_brand_entry_tv, pur_product_entry_tv, pur_design_name_entry_tv, pur_color_entry_tv, pur_size_entry_tv, \
        pur_mrp_entry_tv, pur_rate_entry_tv, pur_gst_entry_tv, pur_id_entry_tv, pur_qty_entry_tv, pur_amount_entry_tv,\
        pur_tot_qty_entry_tv, pur_tot_amount_entry_tv, pur_discount_entry_tv, pur_cgst_entry_tv, pur_sgst_entry_tv,\
        pur_bill_amt_entry_tv

    form_top_label.configure(text="P U R C H A S E     I N S E R T")
    obj_cls_pur_entry.set_pur_button_clicked("insert")
    pur_grn_no_entry_tv = tk.IntVar()
    pur_grn_date_entry_tv = tk.StringVar()
    pur_bill_no_entry_tv = tk.StringVar()
    pur_bill_date_entry_tv = tk.StringVar()
    pur_brand_entry_tv = tk.StringVar()
    pur_product_entry_tv = tk.StringVar()
    pur_design_name_entry_tv = tk.StringVar()
    pur_color_entry_tv = tk.StringVar()
    pur_size_entry_tv = tk.StringVar()
    pur_mrp_entry_tv = tk.DoubleVar()
    pur_rate_entry_tv = tk.DoubleVar()
    pur_gst_entry_tv = tk.IntVar()
    pur_id_entry_tv = tk.IntVar()
    pur_qty_entry_tv = tk.IntVar()
    pur_amount_entry_tv = tk.DoubleVar()
    pur_tot_qty_entry_tv = tk.IntVar()
    pur_tot_amount_entry_tv = tk.DoubleVar()
    pur_discount_entry_tv = tk.DoubleVar()
    pur_cgst_entry_tv = tk.DoubleVar()
    pur_sgst_entry_tv = tk.DoubleVar()
    pur_bill_amt_entry_tv = tk.DoubleVar()

    obj_cls_pur_entry.set_pur_tot_qty(0)
    obj_cls_pur_entry.set_pur_tot_amount(0.00)

    pur_rate_entry_tv.set(0.00)
    pur_id_entry_tv.set('')
    pur_qty_entry_tv.set(0)
    pur_discount_entry_tv.set(0.00)
    pur_cgst_entry_tv.set(0.00)
    pur_sgst_entry_tv.set(0.00)
    pur_bill_amt_entry_tv.set(0.00)

    pur_insert_button.destroy()
    pur_edit_button.destroy()
    pur_delete_button.destroy()
    pur_export_button.destroy()
    pur_quit_button.destroy()

    # *****************************    Frame1 - LABEL & ENTRY BOX SETTINGS - BEGIN     ********************************************
    pur_frame1 = Frame(Purchase_Form, width=380, height=40, bg='#B0E2FF')
    pur_frame1.place(x=10, y=48)

    pur_grn_no_label = Label(pur_frame1, text="GRN No.", bg='#B0E2FF', font=('bold'))
    pur_grn_no_label.place(x=5, y=10)

    pur_grn_date_label = Label(pur_frame1, text="Date", bg='#B0E2FF', font=('bold'))
    pur_grn_date_label.place(x=200, y=10)

    pur_grn_no_entry = Entry(pur_frame1, textvariable=pur_grn_no_entry_tv)
    pur_grn_no_entry.place(x=75, y=10)
    pur_grn_no_entry.config(state='disable')

    pur_grn_date_entry = Entry(pur_frame1, textvariable=pur_grn_date_entry_tv)
    pur_grn_date_entry.place(x=250, y=10)
    pur_grn_date_entry.config(state='disable')

    Cur.execute("select max(grn_no) as m_grn_no from purchase_master")
    data = Cur.fetchall()
    for row in data:
        i = row[0]
    i = str(i)
    if i=='None':
        pur_grn_no_entry_tv.set(20230001)
    else:
        i = int(i)
        i += 1
        pur_grn_no_entry_tv.set(i)

    pur_grn_date_entry_tv.set(newdate)
    # *****************************   Frame1 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************   Frame2 - LABEL &  ENTRY BOX SETTINGS - BEGIN     ********************************************
    pur_frame2 = Frame(Purchase_Form, width=380, height=100, bg='#B0E2FF')
    pur_frame2.place(x=10, y=95)

    supplier_list_label = Label(pur_frame2, text="Supplier List", bg='#B0E2FF', font=('bold'))
    supplier_list_label.place(x=5, y=10)

    pur_bill_no_label = Label(pur_frame2, text="Bill No.", bg='#B0E2FF', font=('bold'))
    pur_bill_no_label.place(x=5, y=35)

    pur_bill_date_label = Label(pur_frame2, text="Bill Date", bg='#B0E2FF', font=('bold'))
    pur_bill_date_label.place(x=5, y=60)

    supplier_list = Supplier_Name_Fetching()
    pur_sup_list_combo = ttk.Combobox(pur_frame2, value=supplier_list, width=40, state='readonly')
    pur_sup_list_combo.set('')
    pur_sup_list_combo.place(x=100, y=10)
    pur_sup_list_combo.bind("<FocusIn>", set_focus_pur_supp_list)
    pur_sup_list_combo.bind("<Return>", set_focus_pur_bill_no)
    pur_sup_list_combo.focus_set()

    pur_bill_no_entry = Entry(pur_frame2, textvariable=pur_bill_no_entry_tv)
    pur_bill_no_entry.place(x=100, y=35)
    pur_bill_no_entry.bind("<FocusIn>", set_focus_pur_bill_no)
    pur_bill_no_entry.bind("<Return>", set_focus_pur_bill_date)

    pur_bill_date_entry = DateEntry(pur_frame2, selectmode='day', textvariable=pur_bill_date_entry_tv, state='readonly', width=18, date_pattern='dd-mm-yyyy')
    pur_bill_date_entry.place(x=100, y=60)
    pur_bill_date_entry.bind("<ButtonRelease>", Show_Calendar)
    pur_bill_date_entry.bind("<Return>", set_focus_pur_brand)

    # *****************************   Frame2 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************   Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    pur_frame3 = LabelFrame(Purchase_Form, text="ITEM CREATION", width=640, height=148, bg='#B0E2FF', font=('bold', 12))
    pur_frame3.place(x=650, y=48)

    pur_brand_label = Label(pur_frame3, text="Brand", font=('bold'), bg='#B0E2FF')
    pur_brand_label.place(x=10, y=2)

    pur_product_label = Label(pur_frame3, text="Product", font=('bold'), bg='#B0E2FF')
    pur_product_label.place(x=10, y=27)

    pur_design_name_label = Label(pur_frame3, text="Design Name", font=('bold'), bg='#B0E2FF')
    pur_design_name_label.place(x=10, y=52)

    pur_color_label = Label(pur_frame3, text="Color", font=('bold'), bg='#B0E2FF')
    pur_color_label.place(x=10, y=77)

    pur_size_label = Label(pur_frame3, text="Size", font=('bold'), bg='#B0E2FF')
    pur_size_label.place(x=10, y=102)

    pur_mrp_label = Label(pur_frame3, text="Mrp", font=('bold'), bg='#B0E2FF')
    pur_mrp_label.place(x=250, y=2)

    pur_rate_label = Label(pur_frame3, text="Rate", font=('bold'), bg='#B0E2FF')
    pur_rate_label.place(x=250, y=27)

    pur_gst_label = Label(pur_frame3, text="GST", font=('bold'), bg='#B0E2FF')
    pur_gst_label.place(x=250, y=52)

    pur_id_label = Label(pur_frame3, text="ID", font=('bold'), bg='#B0E2FF')
    pur_id_label.place(x=250, y=77)

    pur_qty_label = Label(pur_frame3, text="Qty", font=('bold'), bg='#B0E2FF')
    pur_qty_label.place(x=250, y=102)

    pur_amount_label = Label(pur_frame3, text="Amount", font=('bold'), bg='#B0E2FF')
    pur_amount_label.place(x=430, y=2)

    pur_brand_entry = Entry(pur_frame3, textvariable=pur_brand_entry_tv)
    pur_brand_entry.place(x=120, y=5)
    pur_brand_entry.bind("<F1>", Show_Field_Master)
    pur_brand_entry.bind("<F2>", Show_Item_Master)
    pur_brand_entry.bind("<Return>", set_focus_pur_product)
    pur_brand_entry.bind("<FocusIn>", set_focus_pur_brand)
    pur_brand_entry.bind("<FocusOut>", lost_focus_pur_brand)

    pur_product_entry = Entry(pur_frame3, textvariable=pur_product_entry_tv)
    pur_product_entry.place(x=120, y=30)
    pur_product_entry.bind("<F1>", Show_Field_Master)
    pur_product_entry.bind("<Return>", set_focus_pur_design_name)
    pur_product_entry.bind("<FocusIn>", set_focus_pur_product)

    pur_design_name_entry = Entry(pur_frame3, textvariable=pur_design_name_entry_tv)
    pur_design_name_entry.place(x=120, y=55)
    pur_design_name_entry.bind("<F1>", Show_Field_Master)
    pur_design_name_entry.bind("<Return>", set_focus_pur_color)
    pur_design_name_entry.bind("<FocusIn>", set_focus_pur_design_name)

    pur_color_entry = Entry(pur_frame3, textvariable=pur_color_entry_tv)
    pur_color_entry.place(x=120, y=80)
    pur_color_entry.bind("<F1>", Show_Field_Master)
    pur_color_entry.bind("<Return>", set_focus_pur_size)
    pur_color_entry.bind("<FocusIn>", set_focus_pur_color)

    pur_size_entry = Entry(pur_frame3, textvariable=pur_size_entry_tv)
    pur_size_entry.place(x=120, y=105)
    pur_size_entry.bind("<F1>", Show_Field_Master)
    pur_size_entry.bind("<FocusIn>", set_focus_pur_size)
    pur_size_entry.bind("<Return>", set_focus_pur_mrp)

    pur_mrp_entry = Entry(pur_frame3, textvariable=pur_mrp_entry_tv, justify='right')
    pur_mrp_entry.place(x=300, y=5)
    reg1 = pur_mrp_entry.register(Validate_Number2)
    pur_mrp_entry.config(validate="key", validatecommand=(reg1, '%P'))
    pur_mrp_entry.bind("<FocusIn>", set_focus_pur_mrp)
    pur_mrp_entry.bind("<Return>", set_focus_pur_rate)

    pur_rate_entry = Entry(pur_frame3, textvariable=pur_rate_entry_tv, justify='right')
    pur_rate_entry.place(x=300, y=30)
    reg2 = pur_rate_entry.register(Validate_Number2)
    pur_rate_entry.config(validate="key", validatecommand=(reg2, '%P'))
    pur_rate_entry.bind("<FocusIn>", set_focus_pur_rate)
    pur_rate_entry.bind("<Return>", item_id_creation)

    pur_gst_entry = Entry(pur_frame3, state="disable", textvariable=pur_gst_entry_tv, justify='right')
    pur_gst_entry_tv.set(18)
    pur_gst_entry.place(x=300, y=55)

    pur_id_entry = Entry(pur_frame3, state="disable", textvariable=pur_id_entry_tv, justify='right', font=(9), width=5)
    pur_id_entry.place(x=300, y=80)

    pur_qty_entry = Entry(pur_frame3, textvariable=pur_qty_entry_tv, justify='right', width=5)
    pur_qty_entry.place(x=300, y=105)
    pur_qty_entry.config(state="disable")
    reg = pur_qty_entry.register(Validate_Number)
    pur_qty_entry.config(validate="key", validatecommand=(reg, '%P'))
    pur_qty_entry.bind("<FocusIn>", set_focus_pur_qty1)
    pur_qty_entry.bind("<Return>", Add_Purchase_Items_In_Treeview)

    pur_amount_entry = Entry(pur_frame3, state="disable", textvariable=pur_amount_entry_tv, justify='right')
    pur_amount_entry.place(x=500, y=5)
    # *****************************   Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - END     ********************************************


    # *****************************     Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    pur_tot_qty_label = Label(Purchase_Form, text="Total", font=('bold', 12))
    pur_tot_qty_label.place(x=1000, y=420)

    pur_discount_label = Label(Purchase_Form, text="Discount", font=('bold', 12))
    pur_discount_label.place(x=1000, y=450)

    pur_cgst_label = Label(Purchase_Form, text="CGST @ 9%", font=('bold', 12))
    pur_cgst_label.place(x=1000, y=480)

    pur_sgst_label = Label(Purchase_Form, text="SGST @ 9%", font=('bold', 12))
    pur_sgst_label.place(x=1000, y=510)

    pur_bill_amt_label = Label(Purchase_Form, text="Bill Amount", font=('bold', 12))
    pur_bill_amt_label.place(x=1000, y=540)

    pur_tot_qty_entry = Entry(Purchase_Form, font=('bold', 12), width=5, state='disable', textvariable=pur_tot_qty_entry_tv, justify='right')
    pur_tot_qty_entry.place(x=1100, y=420)

    pur_tot_amount_entry = Entry(Purchase_Form, font=('bold', 12), width=14, state='disable', textvariable=pur_tot_amount_entry_tv, justify='right')
    pur_tot_amount_entry.place(x=1155, y=420)

    pur_discount_entry = Entry(Purchase_Form, font=('bold', 12), textvariable=pur_discount_entry_tv, justify='right')
    pur_discount_entry.place(x=1100, y=450)
    reg3 = pur_discount_entry.register(Validate_Number2)
    pur_discount_entry.config(validate="key", validatecommand=(reg3, '%P'))
    pur_discount_entry.bind("<Return>", set_focus_save_button)
    pur_discount_entry.bind("<KeyRelease>", Purchase_Bill_Amt_Calculate2)
    pur_discount_entry.bind("<Tab>", Purchase_Bill_Amt_Calculate2)
    pur_discount_entry.bind("<FocusIn>", set_focus_pur_discount)
    pur_discount_entry.bind("<FocusOut>", Set_Zero)


    pur_cgst_entry = Entry(Purchase_Form, font=('bold', 12), state='disable', textvariable=pur_cgst_entry_tv, justify='right')
    pur_cgst_entry.place(x=1100, y=480)

    pur_sgst_entry = Entry(Purchase_Form, font=('bold', 12), state='disable', textvariable=pur_sgst_entry_tv, justify='right')
    pur_sgst_entry.place(x=1100, y=510)

    pur_bill_amt_entry = Entry(Purchase_Form, font=('bold', 12), state='disable', textvariable=pur_bill_amt_entry_tv, justify='right')
    pur_bill_amt_entry.place(x=1100, y=540)

    pur_save_button = Button(Purchase_Form, text='S A V E', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_save_button.place(x=535, y=520)
    pur_save_button.bind('<Return>', Save_Button_Click)
    pur_save_button.bind("<FocusIn>", set_focus_save_button)
    pur_save_button.bind("<FocusOut>", focus_out_save_button)

    pur_cancel_button = Button(Purchase_Form, text='C A N C E L', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_cancel_button.place(x=710, y=520)
    pur_cancel_button.bind("<Return>", Design_Purchase_Form_Load_destroy2)
    pur_cancel_button.bind("<ButtonRelease>", Design_Purchase_Form_Load_destroy2)
    pur_cancel_button.bind("<FocusIn>",  set_focus_cancel_button)
    pur_cancel_button.bind("<FocusOut>", focus_out_cancel_button)

# *****************************     Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS -  END     ********************************************

def Design_Purchase_Form_Load_destroy2(event):
    Purchase_Form.destroy()
    Design_Purchase_Form_Load()

def Design_Purchase_Form_Load_destroy(event):
    Purchase_Form.destroy()

def Update_Button_Click(event):
    grn_no1 = pur_grn_no_entry_tv.get()
    grn_date11 = str(pur_grn_date_entry_tv.get())
    grn_date1 = datetime.strptime(grn_date11, "%d-%m-%Y")
    supp_name1 = pur_sup_list_combo.get()
    bill_no1 = pur_bill_no_entry_tv.get()
    str_date1 = str(pur_bill_date_entry_tv.get())
    bill_date1 = datetime.strptime(str_date1, "%d-%m-%Y")
    bill_qty1 = pur_tot_qty_entry_tv.get()
    item_total1 = pur_tot_amount_entry_tv.get()
    less_amt1 = pur_discount_entry_tv.get()
    cgst_amt1 = pur_cgst_entry_tv.get()
    sgst_amt1 = pur_sgst_entry_tv.get()
    bill_amt1 = pur_bill_amt_entry_tv.get()

    if len(supp_name1.strip()) > 0 and len(bill_no1.strip()) > 0 and bill_qty1 > 0 and less_amt1 >= 0:

        if len(bill_no1.strip()) <= 25 and len(str(less_amt1).strip()) <= 10:

            Cur.execute("delete from purchase_item where grn_no = {}".format(pur_grn_no_entry_tv.get()))
            Con.commit()

            for row in obj_cls_pur_entry.get_pur_original_data():
                Cur.execute(
                    "update stock_balance set bal_qty = bal_qty - {}, bal_amount = bal_amount - {} where item_id = {}".format(
                        row[3], row[4], row[2]))
                Con.commit()

            Cur.execute("Update purchase_master set  supp_name = '{}', bill_no = '{}', bill_date = '{}', bill_qty = {},"
                        " item_total = {}, less_amt = {}, cgst_amt = {}, sgst_amt = {}, bill_amt = {} where grn_no = {}"
                        .format(supp_name1, bill_no1, bill_date1, bill_qty1, item_total1, less_amt1,
                                cgst_amt1, sgst_amt1, bill_amt1, grn_no1))
            Con.commit()

            k = 0
            for k in tree.get_children():
                Cur.execute("insert into purchase_item (grn_no,grn_date,item_id,item_qty,item_amount) "
                            "values({},'{}',{},{},{})"
                            .format(grn_no1, grn_date1, tree.item(k, 'value')[8], tree.item(k, 'value')[9],
                                    tree.item(k, 'value')[10]))
                Con.commit()
                dum_item_id = int(tree.item(k, 'value')[8])
                qry2 = "select * from stock_balance where item_id = {}".format(dum_item_id)
                Cur.execute(qry2)
                check_item_id = Cur.fetchall()
                if not check_item_id:
                    Cur.execute("insert into stock_balance (item_id,brand,product,design,color,sizes,mrp,rate,"
                                "bal_qty,bal_amount) values({},'{}','{}','{}','{}','{}',{},{},{},{})"
                                .format(tree.item(k, 'value')[8], tree.item(k, 'value')[0], tree.item(k, 'value')[1],
                                        tree.item(k, 'value')[2], tree.item(k, 'value')[3], tree.item(k, 'value')[4],
                                        tree.item(k, 'value')[5], tree.item(k, 'value')[6], tree.item(k, 'value')[9],
                                        tree.item(k, 'value')[10]))
                    Con.commit()
                else:
                    for m in check_item_id:
                        dum_tot_qty = int(m[8]) + int(tree.item(k, 'value')[9])
                        dum_tot_amt = float(m[9]) + float(tree.item(k, 'value')[10])
                        print(dum_tot_qty)
                        print(dum_tot_amt)
                        qry3 = "update stock_balance set bal_qty = {}, bal_amount = {} where item_id = {}" \
                            .format(dum_tot_qty, dum_tot_amt, dum_item_id)
                        Cur.execute(qry3)
                        Con.commit()

            messagebox.showinfo('', "PURCHASE Details Updated Successfully")
            Purchase_Form.destroy()
            Design_Purchase_Form_Load()
        else:
            messagebox.showwarning('', 'Enter Details As Per The Limitations')
    else:
        messagebox.showwarning('', 'Enter Data In All Fields')
        Purchase_Form.focus_set()
        pur_save_button.focus_set()


def Purchase_Edit(event):
    global pur_grn_no_entry, pur_grn_date_entry, pur_sup_list_combo, pur_bill_no_entry, pur_bill_date_entry,\
           pur_brand_entry, pur_product_entry, pur_design_name_entry, pur_color_entry, pur_size_entry,\
           pur_mrp_entry, pur_rate_entry, pur_gst_entry, pur_id_entry, pur_qty_entry, pur_amount_entry
    global pur_tot_qty_entry, pur_tot_amount_entry, pur_discount_entry, pur_cgst_entry, pur_sgst_entry, pur_bill_amt_entry

    global a3, pur_frame3, pur_save_button, pur_cancel_button
    global pur_grn_no_entry_tv, pur_grn_date_entry_tv, pur_sup_list_combo_tv, pur_bill_no_entry_tv, pur_bill_date_entry_tv, \
        pur_brand_entry_tv, pur_product_entry_tv, pur_design_name_entry_tv, pur_color_entry_tv, pur_size_entry_tv, \
        pur_mrp_entry_tv, pur_rate_entry_tv, pur_gst_entry_tv, pur_id_entry_tv, pur_qty_entry_tv, pur_amount_entry_tv,\
        pur_tot_qty_entry_tv, pur_tot_amount_entry_tv, pur_discount_entry_tv, pur_cgst_entry_tv, pur_sgst_entry_tv,\
        pur_bill_amt_entry_tv

    form_top_label.configure(text="P U R C H A S E      E D I T")
    obj_cls_pur_entry.set_pur_button_clicked("edit")
    pur_grn_no_entry_tv = tk.IntVar()
    pur_grn_date_entry_tv = tk.StringVar()
    pur_bill_no_entry_tv = tk.StringVar()
    pur_bill_date_entry_tv = tk.StringVar()
    pur_brand_entry_tv = tk.StringVar()
    pur_product_entry_tv = tk.StringVar()
    pur_design_name_entry_tv = tk.StringVar()
    pur_color_entry_tv = tk.StringVar()
    pur_size_entry_tv = tk.StringVar()
    pur_mrp_entry_tv = tk.DoubleVar()
    pur_rate_entry_tv = tk.DoubleVar()
    pur_gst_entry_tv = tk.IntVar()
    pur_id_entry_tv = tk.IntVar()
    pur_qty_entry_tv = tk.IntVar()
    pur_amount_entry_tv = tk.DoubleVar()
    pur_tot_qty_entry_tv = tk.IntVar()
    pur_tot_amount_entry_tv = tk.DoubleVar()
    pur_discount_entry_tv = tk.DoubleVar()
    pur_cgst_entry_tv = tk.DoubleVar()
    pur_sgst_entry_tv = tk.DoubleVar()
    pur_bill_amt_entry_tv = tk.DoubleVar()


    pur_mrp_entry_tv.set(0.00)
    pur_rate_entry_tv.set(0.00)
    pur_id_entry_tv.set('')
    pur_qty_entry_tv.set(0)
    pur_discount_entry_tv.set(0.00)
    pur_cgst_entry_tv.set(0.00)
    pur_sgst_entry_tv.set(0.00)
    pur_bill_amt_entry_tv.set(0.00)

    pur_insert_button.destroy()
    pur_edit_button.destroy()
    pur_delete_button.destroy()
    pur_export_button.destroy()
    pur_quit_button.destroy()

    # *****************************   EDIT - Frame1 - LABEL & ENTRY BOX SETTINGS - BEGIN     ********************************************
    pur_frame1 = Frame(Purchase_Form, width=380, height=40, bg='#B0E2FF')
    pur_frame1.place(x=10, y=48)

    pur_grn_no_label = Label(pur_frame1, text="GRN No.", bg='#B0E2FF', font=('bold'))
    pur_grn_no_label.place(x=5, y=10)

    pur_grn_date_label = Label(pur_frame1, text="Date", bg='#B0E2FF', font=('bold'))
    pur_grn_date_label.place(x=200, y=10)

    pur_grn_no_entry = Entry(pur_frame1, textvariable=pur_grn_no_entry_tv)
    pur_grn_no_entry.place(x=75, y=10)
    pur_grn_no_entry.config(state='normal')
    pur_grn_no_entry_tv.set("")
    pur_grn_no_entry.focus_set()
    pur_grn_no_entry.bind("<FocusIn>", set_focus_pur_grn_no)
    pur_grn_no_entry.bind("<F1>", Show_Purchase_Master)


    pur_grn_date_entry = Entry(pur_frame1, textvariable=pur_grn_date_entry_tv)
    pur_grn_date_entry.place(x=250, y=10)
    pur_grn_date_entry.config(state='disable')


    # *****************************  EDIT - Frame1 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************  EDIT - Frame2 - LABEL &  ENTRY BOX SETTINGS - BEGIN     ********************************************
    pur_frame2 = Frame(Purchase_Form, width=380, height=100, bg='#B0E2FF')
    pur_frame2.place(x=10, y=95)

    supplier_list_label = Label(pur_frame2, text="Supplier List", bg='#B0E2FF', font=('bold'))
    supplier_list_label.place(x=5, y=10)

    pur_bill_no_label = Label(pur_frame2, text="Bill No.", bg='#B0E2FF', font=('bold'))
    pur_bill_no_label.place(x=5, y=35)

    pur_bill_date_label = Label(pur_frame2, text="Bill Date", bg='#B0E2FF', font=('bold'))
    pur_bill_date_label.place(x=5, y=60)

    supplier_list = Supplier_Name_Fetching()
    pur_sup_list_combo = ttk.Combobox(pur_frame2, value=supplier_list, width=40, state='disable')
    pur_sup_list_combo.set('')
    pur_sup_list_combo.place(x=100, y=10)
    pur_sup_list_combo.bind("<FocusIn>", set_focus_pur_supp_list)
    pur_sup_list_combo.bind("<Return>", set_focus_pur_bill_no)


    pur_bill_no_entry = Entry(pur_frame2, textvariable=pur_bill_no_entry_tv)
    pur_bill_no_entry.place(x=100, y=35)
    pur_bill_no_entry.config(state="disable")
    pur_bill_no_entry.bind("<Return>", set_focus_pur_bill_date)

    pur_bill_date_entry = DateEntry(pur_frame2, selectmode='day', textvariable=pur_bill_date_entry_tv, state='disable', width=18, date_pattern='dd-mm-yyyy')
    pur_bill_date_entry.place(x=100, y=60)
    pur_bill_date_entry.bind("<ButtonRelease>", Show_Calendar)
    pur_bill_date_entry.bind("<Return>", set_focus_pur_brand)

    # *****************************   EDIT - Frame2 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************   EDIT - Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    pur_frame3 = LabelFrame(Purchase_Form, text="ITEM CREATION", width=640, height=148, bg='#B0E2FF', font=('bold', 12))
    pur_frame3.place(x=650, y=48)

    pur_brand_label = Label(pur_frame3, text="Brand", font=('bold'), bg='#B0E2FF')
    pur_brand_label.place(x=10, y=2)

    pur_product_label = Label(pur_frame3, text="Product", font=('bold'), bg='#B0E2FF')
    pur_product_label.place(x=10, y=27)

    pur_design_name_label = Label(pur_frame3, text="Design Name", font=('bold'), bg='#B0E2FF')
    pur_design_name_label.place(x=10, y=52)

    pur_color_label = Label(pur_frame3, text="Color", font=('bold'), bg='#B0E2FF')
    pur_color_label.place(x=10, y=77)

    pur_size_label = Label(pur_frame3, text="Size", font=('bold'), bg='#B0E2FF')
    pur_size_label.place(x=10, y=102)

    pur_mrp_label = Label(pur_frame3, text="Mrp", font=('bold'), bg='#B0E2FF')
    pur_mrp_label.place(x=250, y=2)

    pur_rate_label = Label(pur_frame3, text="Rate", font=('bold'), bg='#B0E2FF')
    pur_rate_label.place(x=250, y=27)

    pur_gst_label = Label(pur_frame3, text="GST", font=('bold'), bg='#B0E2FF')
    pur_gst_label.place(x=250, y=52)

    pur_id_label = Label(pur_frame3, text="ID", font=('bold'), bg='#B0E2FF')
    pur_id_label.place(x=250, y=77)

    pur_qty_label = Label(pur_frame3, text="Qty", font=('bold'), bg='#B0E2FF')
    pur_qty_label.place(x=250, y=102)

    pur_amount_label = Label(pur_frame3, text="Amount", font=('bold'), bg='#B0E2FF')
    pur_amount_label.place(x=430, y=2)

    pur_brand_entry = Entry(pur_frame3, textvariable=pur_brand_entry_tv)
    pur_brand_entry.place(x=120, y=5)
    pur_brand_entry.config(state="disable")
    pur_brand_entry.bind("<F1>", Show_Field_Master)
    pur_brand_entry.bind("<F2>", Show_Item_Master)
    pur_brand_entry.bind("<Return>", set_focus_pur_product)
    pur_brand_entry.bind("<FocusIn>", set_focus_pur_brand)
    pur_brand_entry.bind("<FocusOut>", lost_focus_pur_brand)

    pur_product_entry = Entry(pur_frame3, textvariable=pur_product_entry_tv)
    pur_product_entry.place(x=120, y=30)
    pur_product_entry.config(state="disable")
    pur_product_entry.bind("<F1>", Show_Field_Master)
    pur_product_entry.bind("<FocusIn>", set_focus_pur_product)
    pur_product_entry.bind("<Return>", set_focus_pur_design_name)

    pur_design_name_entry = Entry(pur_frame3, textvariable=pur_design_name_entry_tv)
    pur_design_name_entry.place(x=120, y=55)
    pur_design_name_entry.config(state="disable")
    pur_design_name_entry.bind("<F1>", Show_Field_Master)
    pur_design_name_entry.bind("<FocusIn>", set_focus_pur_design_name)
    pur_design_name_entry.bind("<Return>", set_focus_pur_color)

    pur_color_entry = Entry(pur_frame3, textvariable=pur_color_entry_tv)
    pur_color_entry.place(x=120, y=80)
    pur_color_entry.config(state="disable")
    pur_color_entry.bind("<F1>", Show_Field_Master)
    pur_color_entry.bind("<FocusIn>", set_focus_pur_color)
    pur_color_entry.bind("<Return>", set_focus_pur_size)

    pur_size_entry = Entry(pur_frame3, textvariable=pur_size_entry_tv)
    pur_size_entry.place(x=120, y=105)
    pur_size_entry.config(state="disable")
    pur_size_entry.bind("<F1>", Show_Field_Master)
    pur_size_entry.bind("<FocusIn>", set_focus_pur_size)
    pur_size_entry.bind("<Return>", set_focus_pur_mrp)

    pur_mrp_entry = Entry(pur_frame3, textvariable=pur_mrp_entry_tv, justify='right')
    pur_mrp_entry.place(x=300, y=5)
    pur_mrp_entry.config(state="disable")
    reg1 = pur_mrp_entry.register(Validate_Number2)
    pur_mrp_entry.config(validate="key", validatecommand=(reg1, '%P'))
    pur_mrp_entry.bind("<FocusIn>", set_focus_pur_mrp)
    pur_mrp_entry.bind("<Return>", set_focus_pur_rate)

    pur_rate_entry = Entry(pur_frame3, textvariable=pur_rate_entry_tv, justify='right')
    pur_rate_entry.place(x=300, y=30)
    pur_rate_entry.config(state="disable")
    reg2 = pur_rate_entry.register(Validate_Number2)
    pur_rate_entry.config(validate="key", validatecommand=(reg2, '%P'))
    pur_rate_entry.bind("<FocusIn>", set_focus_pur_rate)
    pur_rate_entry.bind("<Return>", item_id_creation)

    pur_gst_entry = Entry(pur_frame3, state="disable", textvariable=pur_gst_entry_tv, justify='right')
    pur_gst_entry_tv.set(18)
    pur_gst_entry.place(x=300, y=55)

    pur_id_entry = Entry(pur_frame3, state="disable", textvariable=pur_id_entry_tv, justify='right', font=(9), width=5)
    pur_id_entry.place(x=300, y=80)

    pur_qty_entry = Entry(pur_frame3, textvariable=pur_qty_entry_tv, justify='right', width=5)
    pur_qty_entry.place(x=300, y=105)
    pur_qty_entry.config(state="disable")
    reg = pur_qty_entry.register(Validate_Number)
    pur_qty_entry.config(validate="key", validatecommand=(reg, '%P'))

    pur_qty_entry.bind("<FocusIn>", set_focus_pur_qty1)
    pur_qty_entry.bind("<Return>", Add_Purchase_Items_In_Treeview)

    pur_amount_entry = Entry(pur_frame3, state="disable", textvariable=pur_amount_entry_tv, justify='right')
    pur_amount_entry.place(x=500, y=5)
    # *****************************   EDIT - Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - END     ********************************************


    # *****************************     EDIT - Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    pur_tot_qty_label = Label(Purchase_Form, text="Total", font=('bold', 12))
    pur_tot_qty_label.place(x=1000, y=420)

    pur_discount_label = Label(Purchase_Form, text="Discount", font=('bold', 12))
    pur_discount_label.place(x=1000, y=450)

    pur_cgst_label = Label(Purchase_Form, text="CGST @ 9%", font=('bold', 12))
    pur_cgst_label.place(x=1000, y=480)

    pur_sgst_label = Label(Purchase_Form, text="SGST @ 9%", font=('bold', 12))
    pur_sgst_label.place(x=1000, y=510)

    pur_bill_amt_label = Label(Purchase_Form, text="Bill Amount", font=('bold', 12))
    pur_bill_amt_label.place(x=1000, y=540)

    pur_tot_qty_entry = Entry(Purchase_Form, font=('bold', 12), width=5, state='disable', textvariable=pur_tot_qty_entry_tv, justify='right')
    pur_tot_qty_entry.place(x=1100, y=420)

    pur_tot_amount_entry = Entry(Purchase_Form, font=('bold', 12), width=14, state='disable', textvariable=pur_tot_amount_entry_tv, justify='right')
    pur_tot_amount_entry.place(x=1155, y=420)

    pur_discount_entry = Entry(Purchase_Form, font=('bold', 12), textvariable=pur_discount_entry_tv, justify='right')
    pur_discount_entry.place(x=1100, y=450)
    pur_discount_entry.config(state="disable")
    reg3 = pur_discount_entry.register(Validate_Number2)
    pur_discount_entry.config(validate="key", validatecommand=(reg3, '%P'))
    pur_discount_entry.bind("<Return>", set_focus_save_button)
    pur_discount_entry.bind("<KeyRelease>", Purchase_Bill_Amt_Calculate2)
    pur_discount_entry.bind("<Tab>", Purchase_Bill_Amt_Calculate2)
    pur_discount_entry.bind("<FocusIn>", set_focus_pur_discount)
    pur_discount_entry.bind("<FocusOut>", Set_Zero)

    pur_cgst_entry = Entry(Purchase_Form, font=('bold', 12), state='disable', textvariable=pur_cgst_entry_tv, justify='right')
    pur_cgst_entry.place(x=1100, y=480)

    pur_sgst_entry = Entry(Purchase_Form, font=('bold', 12), state='disable', textvariable=pur_sgst_entry_tv, justify='right')
    pur_sgst_entry.place(x=1100, y=510)

    pur_bill_amt_entry = Entry(Purchase_Form, font=('bold', 12), state='disable', textvariable=pur_bill_amt_entry_tv, justify='right')
    pur_bill_amt_entry.place(x=1100, y=540)

    pur_save_button = Button(Purchase_Form, text='U P D A T E', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_save_button.place(x=535, y=520)
    pur_save_button.bind('<Return>', Update_Button_Click)
    pur_save_button.bind("<ButtonRelease>", Update_Button_Click)
    pur_save_button.bind("<FocusIn>", set_focus_update_button)
    pur_save_button.bind("<FocusOut>", focus_out_update_button)
    pur_cancel_button = Button(Purchase_Form, text='C A N C E L', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_cancel_button.place(x=710, y=520)
    pur_cancel_button.bind("<Return>", Design_Purchase_Form_Load_destroy2)
    pur_cancel_button.bind("<ButtonRelease>", Design_Purchase_Form_Load_destroy2)
    pur_cancel_button.bind("<FocusIn>", set_focus_cancel_button)
    pur_cancel_button.bind("<FocusOut>", focus_out_cancel_button)

# *****************************     EDIT - Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS -  END     ********************************************


def Purchase_Delete(event):
    global pur_grn_no_entry, pur_grn_date_entry, pur_sup_list_combo, pur_bill_no_entry, pur_bill_date_entry, \
        pur_brand_entry, pur_product_entry, pur_design_name_entry, pur_color_entry, pur_size_entry, \
        pur_mrp_entry, pur_rate_entry, pur_gst_entry, pur_id_entry, pur_qty_entry, pur_amount_entry
    global pur_tot_qty_entry, pur_tot_amount_entry, pur_discount_entry, pur_cgst_entry, pur_sgst_entry, pur_bill_amt_entry

    global a3, pur_frame3, pur_delete_button, pur_cancel_button
    global pur_grn_no_entry_tv, pur_grn_date_entry_tv, pur_sup_list_combo_tv, pur_bill_no_entry_tv, pur_bill_date_entry_tv, \
        pur_brand_entry_tv, pur_product_entry_tv, pur_design_name_entry_tv, pur_color_entry_tv, pur_size_entry_tv, \
        pur_mrp_entry_tv, pur_rate_entry_tv, pur_gst_entry_tv, pur_id_entry_tv, pur_qty_entry_tv, pur_amount_entry_tv, \
        pur_tot_qty_entry_tv, pur_tot_amount_entry_tv, pur_discount_entry_tv, pur_cgst_entry_tv, pur_sgst_entry_tv, \
        pur_bill_amt_entry_tv

    form_top_label.configure(text="P U R C H A S E      D E L E T E")
    obj_cls_pur_entry.set_pur_button_clicked("delete")
    pur_grn_no_entry_tv = tk.IntVar()
    pur_grn_date_entry_tv = tk.StringVar()
    pur_bill_no_entry_tv = tk.StringVar()
    pur_bill_date_entry_tv = tk.StringVar()
    pur_brand_entry_tv = tk.StringVar()
    pur_product_entry_tv = tk.StringVar()
    pur_design_name_entry_tv = tk.StringVar()
    pur_color_entry_tv = tk.StringVar()
    pur_size_entry_tv = tk.StringVar()
    pur_mrp_entry_tv = tk.DoubleVar()
    pur_rate_entry_tv = tk.DoubleVar()
    pur_gst_entry_tv = tk.IntVar()
    pur_id_entry_tv = tk.IntVar()
    pur_qty_entry_tv = tk.IntVar()
    pur_amount_entry_tv = tk.DoubleVar()
    pur_tot_qty_entry_tv = tk.IntVar()
    pur_tot_amount_entry_tv = tk.DoubleVar()
    pur_discount_entry_tv = tk.DoubleVar()
    pur_cgst_entry_tv = tk.DoubleVar()
    pur_sgst_entry_tv = tk.DoubleVar()
    pur_bill_amt_entry_tv = tk.DoubleVar()

    pur_mrp_entry_tv.set(0.00)
    pur_rate_entry_tv.set(0.00)
    pur_id_entry_tv.set('')
    pur_qty_entry_tv.set(0)
    pur_discount_entry_tv.set(0.00)
    pur_cgst_entry_tv.set(0.00)
    pur_sgst_entry_tv.set(0.00)
    pur_bill_amt_entry_tv.set(0.00)

    pur_insert_button.destroy()
    pur_edit_button.destroy()
    pur_delete_button.destroy()
    pur_export_button.destroy()
    pur_quit_button.destroy()

    # *****************************   DELETE - Frame1 - LABEL & ENTRY BOX SETTINGS - BEGIN     ********************************************
    pur_frame1 = Frame(Purchase_Form, width=380, height=40, bg='#B0E2FF')
    pur_frame1.place(x=10, y=48)

    pur_grn_no_label = Label(pur_frame1, text="GRN No.", bg='#B0E2FF', font=('bold'))
    pur_grn_no_label.place(x=5, y=10)

    pur_grn_date_label = Label(pur_frame1, text="Date", bg='#B0E2FF', font=('bold'))
    pur_grn_date_label.place(x=200, y=10)

    pur_grn_no_entry = Entry(pur_frame1, textvariable=pur_grn_no_entry_tv)
    pur_grn_no_entry.place(x=75, y=10)
    pur_grn_no_entry.config(state='normal')
    pur_grn_no_entry_tv.set("")
    pur_grn_no_entry.bind("<F1>", Show_Purchase_Master)
    pur_grn_no_entry.bind("<FocusIn>", set_focus_pur_grn_no)
    pur_grn_no_entry.focus_set()

    pur_grn_date_entry = Entry(pur_frame1, textvariable=pur_grn_date_entry_tv)
    pur_grn_date_entry.place(x=250, y=10)
    pur_grn_date_entry.config(state='disable')

    # *****************************  DELETE - Frame1 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************  DELETE - Frame2 - LABEL &  ENTRY BOX SETTINGS - BEGIN     ********************************************
    pur_frame2 = Frame(Purchase_Form, width=380, height=100, bg='#B0E2FF')
    pur_frame2.place(x=10, y=95)

    supplier_list_label = Label(pur_frame2, text="Supplier List", bg='#B0E2FF', font=('bold'))
    supplier_list_label.place(x=5, y=10)

    pur_bill_no_label = Label(pur_frame2, text="Bill No.", bg='#B0E2FF', font=('bold'))
    pur_bill_no_label.place(x=5, y=35)

    pur_bill_date_label = Label(pur_frame2, text="Bill Date", bg='#B0E2FF', font=('bold'))
    pur_bill_date_label.place(x=5, y=60)

    supplier_list = Supplier_Name_Fetching()
    pur_sup_list_combo = ttk.Combobox(pur_frame2, value=supplier_list, width=40, state='disable')
    pur_sup_list_combo.set('')
    pur_sup_list_combo.place(x=100, y=10)
    pur_sup_list_combo.bind("<Return>", set_focus_pur_bill_no)


    pur_bill_no_entry = Entry(pur_frame2, textvariable=pur_bill_no_entry_tv)
    pur_bill_no_entry.place(x=100, y=35)
    pur_bill_no_entry.config(state="disable")
    pur_bill_no_entry.bind("<Return>", set_focus_pur_bill_date)

    pur_bill_date_entry = DateEntry(pur_frame2, selectmode='day', textvariable=pur_bill_date_entry_tv, state='disable',
                                    width=18, date_pattern='dd-mm-yyyy')
    pur_bill_date_entry.place(x=100, y=60)
    pur_bill_date_entry.bind("<ButtonRelease>", Show_Calendar)
    pur_bill_date_entry.bind("<Return>", set_focus_pur_brand)

    # *****************************   DELETE - Frame2 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************   DELETE - Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    pur_frame3 = LabelFrame(Purchase_Form, text="ITEM CREATION", width=640, height=148, bg='#B0E2FF', font=('bold', 12))
    pur_frame3.place(x=650, y=48)

    pur_brand_label = Label(pur_frame3, text="Brand", font=('bold'), bg='#B0E2FF')
    pur_brand_label.place(x=10, y=2)

    pur_product_label = Label(pur_frame3, text="Product", font=('bold'), bg='#B0E2FF')
    pur_product_label.place(x=10, y=27)

    pur_design_name_label = Label(pur_frame3, text="Design Name", font=('bold'), bg='#B0E2FF')
    pur_design_name_label.place(x=10, y=52)

    pur_color_label = Label(pur_frame3, text="Color", font=('bold'), bg='#B0E2FF')
    pur_color_label.place(x=10, y=77)

    pur_size_label = Label(pur_frame3, text="Size", font=('bold'), bg='#B0E2FF')
    pur_size_label.place(x=10, y=102)

    pur_mrp_label = Label(pur_frame3, text="Mrp", font=('bold'), bg='#B0E2FF')
    pur_mrp_label.place(x=250, y=2)

    pur_rate_label = Label(pur_frame3, text="Rate", font=('bold'), bg='#B0E2FF')
    pur_rate_label.place(x=250, y=27)

    pur_gst_label = Label(pur_frame3, text="GST", font=('bold'), bg='#B0E2FF')
    pur_gst_label.place(x=250, y=52)

    pur_id_label = Label(pur_frame3, text="ID", font=('bold'), bg='#B0E2FF')
    pur_id_label.place(x=250, y=77)

    pur_qty_label = Label(pur_frame3, text="Qty", font=('bold'), bg='#B0E2FF')
    pur_qty_label.place(x=250, y=102)

    pur_amount_label = Label(pur_frame3, text="Amount", font=('bold'), bg='#B0E2FF')
    pur_amount_label.place(x=430, y=2)

    pur_brand_entry = Entry(pur_frame3, textvariable=pur_brand_entry_tv)
    pur_brand_entry.place(x=120, y=5)
    pur_brand_entry.config(state="disable")
    pur_brand_entry.bind("<F1>", Show_Field_Master)
    pur_brand_entry.bind("<F2>", Show_Item_Master)
    pur_brand_entry.bind("<Return>", set_focus_pur_product)
    pur_brand_entry.bind("<FocusIn>", set_focus_pur_brand)

    pur_product_entry = Entry(pur_frame3, textvariable=pur_product_entry_tv)
    pur_product_entry.place(x=120, y=30)
    pur_product_entry.config(state="disable")
    pur_product_entry.bind("<F1>", Show_Field_Master)
    pur_product_entry.bind("<Return>", set_focus_pur_design_name)
    pur_product_entry.bind("<FocusIn>", set_focus_pur_product)

    pur_design_name_entry = Entry(pur_frame3, textvariable=pur_design_name_entry_tv)
    pur_design_name_entry.place(x=120, y=55)
    pur_design_name_entry.config(state="disable")
    pur_design_name_entry.bind("<F1>", Show_Field_Master)
    pur_design_name_entry.bind("<Return>", set_focus_pur_color)
    pur_design_name_entry.bind("<FocusIn>", set_focus_pur_design_name)

    pur_color_entry = Entry(pur_frame3, textvariable=pur_color_entry_tv)
    pur_color_entry.place(x=120, y=80)
    pur_color_entry.config(state="disable")
    pur_color_entry.bind("<F1>", Show_Field_Master)
    pur_color_entry.bind("<Return>", set_focus_pur_size)
    pur_color_entry.bind("<FocusIn>", set_focus_pur_color)

    pur_size_entry = Entry(pur_frame3, textvariable=pur_size_entry_tv)
    pur_size_entry.place(x=120, y=105)
    pur_size_entry.config(state="disable")
    pur_size_entry.bind("<F1>", Show_Field_Master)
    pur_size_entry.bind("<Return>", set_focus_pur_mrp)
    pur_size_entry.bind("<FocusIn>", set_focus_pur_size)

    pur_mrp_entry = Entry(pur_frame3, textvariable=pur_mrp_entry_tv, justify='right')
    pur_mrp_entry.place(x=300, y=5)
    pur_mrp_entry.config(state="disable")
    pur_mrp_entry.bind("<FocusIn>", set_focus_pur_mrp)
    pur_mrp_entry.bind("<Return>", set_focus_pur_rate)

    pur_rate_entry = Entry(pur_frame3, textvariable=pur_rate_entry_tv, justify='right')
    pur_rate_entry.place(x=300, y=30)
    pur_rate_entry.config(state="disable")
    pur_rate_entry.bind("<FocusIn>", set_focus_pur_rate)
    pur_rate_entry.bind("<Return>", item_id_creation)

    pur_gst_entry = Entry(pur_frame3, state="disable", textvariable=pur_gst_entry_tv, justify='right')
    pur_gst_entry_tv.set(18)
    pur_gst_entry.place(x=300, y=55)

    pur_id_entry = Entry(pur_frame3, state="disable", textvariable=pur_id_entry_tv, justify='right', font=(9), width=5)
    pur_id_entry.place(x=300, y=80)

    pur_qty_entry = Entry(pur_frame3, textvariable=pur_qty_entry_tv, justify='right', width=5)
    pur_qty_entry.place(x=300, y=105)
    pur_qty_entry.config(state="disable")

    pur_amount_entry = Entry(pur_frame3, state="disable", textvariable=pur_amount_entry_tv, justify='right')
    pur_amount_entry.place(x=500, y=5)
    # *****************************   DELETE - Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - END     ********************************************

    # *****************************     DELETE - Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    pur_tot_qty_label = Label(Purchase_Form, text="Total", font=('bold', 12))
    pur_tot_qty_label.place(x=1000, y=420)

    pur_discount_label = Label(Purchase_Form, text="Discount", font=('bold', 12))
    pur_discount_label.place(x=1000, y=450)

    pur_cgst_label = Label(Purchase_Form, text="CGST @ 9%", font=('bold', 12))
    pur_cgst_label.place(x=1000, y=480)

    pur_sgst_label = Label(Purchase_Form, text="SGST @ 9%", font=('bold', 12))
    pur_sgst_label.place(x=1000, y=510)

    pur_bill_amt_label = Label(Purchase_Form, text="Bill Amount", font=('bold', 12))
    pur_bill_amt_label.place(x=1000, y=540)

    pur_tot_qty_entry = Entry(Purchase_Form, font=('bold', 12), width=5, state='disable',
                              textvariable=pur_tot_qty_entry_tv, justify='right')
    pur_tot_qty_entry.place(x=1100, y=420)

    pur_tot_amount_entry = Entry(Purchase_Form, font=('bold', 12), width=14, state='disable',
                                 textvariable=pur_tot_amount_entry_tv, justify='right')
    pur_tot_amount_entry.place(x=1155, y=420)

    pur_discount_entry = Entry(Purchase_Form, font=('bold', 12), textvariable=pur_discount_entry_tv, justify='right')
    pur_discount_entry.place(x=1100, y=450)
    pur_discount_entry.config(state="disable")


    pur_cgst_entry = Entry(Purchase_Form, font=('bold', 12), state='disable', textvariable=pur_cgst_entry_tv,
                           justify='right')
    pur_cgst_entry.place(x=1100, y=480)

    pur_sgst_entry = Entry(Purchase_Form, font=('bold', 12), state='disable', textvariable=pur_sgst_entry_tv,
                           justify='right')
    pur_sgst_entry.place(x=1100, y=510)

    pur_bill_amt_entry = Entry(Purchase_Form, font=('bold', 12), state='disable', textvariable=pur_bill_amt_entry_tv,
                               justify='right')
    pur_bill_amt_entry.place(x=1100, y=540)

    pur_delete_button = Button(Purchase_Form, text='D E L E T E', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_delete_button.place(x=535, y=520)
    pur_delete_button.bind('<Return>', Delete_Button_Click)
    pur_delete_button.bind("<ButtonRelease>", Delete_Button_Click)
    pur_delete_button.bind("<FocusIn>", set_focus_delete2_button)
    pur_delete_button.bind("<FocusOut>", focus_out_delete2_button)
    pur_cancel_button = Button(Purchase_Form, text='C A N C E L', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_cancel_button.place(x=710, y=520)
    pur_cancel_button.bind("<Return>", Design_Purchase_Form_Load_destroy2)
    pur_cancel_button.bind("<ButtonRelease>", Design_Purchase_Form_Load_destroy2)
    pur_cancel_button.bind("<FocusIn>", set_focus_cancel_button)
    pur_cancel_button.bind("<FocusOut>", focus_out_cancel_button)

# *****************************     DELETE - Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS -  END     ********************************************

def Delete_Button_Click(event):
    grn_no1 = str(pur_grn_no_entry_tv.get())
    delete_confirm=messagebox.askquestion("", "Do You Want To Delete All Items Of This GRN No. "+grn_no1)
    if delete_confirm == "yes":
        Cur.execute("delete from purchase_item where grn_no = {}".format(pur_grn_no_entry_tv.get()))
        Con.commit()
        Cur.execute("delete from purchase_master where grn_no = {}".format(pur_grn_no_entry_tv.get()))
        Con.commit()

        for row in obj_cls_pur_entry.get_pur_original_data():
            Cur.execute(
                "update stock_balance set bal_qty = bal_qty - {}, bal_amount = bal_amount - {} where item_id = {}".format(
                    row[3], row[4], row[2]))
            Con.commit()
        messagebox.showinfo('', "GRN "+grn_no1+" Deleted Successfully")
        Purchase_Form.destroy()
        Design_Purchase_Form_Load()
    else:
        Purchase_Form.focus_set()

def Show_Purchase_Master(event):
    global pur_mas_form, pur_mas_treeview

    pur_mas_form = tk.Toplevel()
    pur_mas_form.title('PURCHASE ENTRY List')
    pur_mas_form.geometry("1200x200+100+200")
    pur_mas_form.resizable(False,False)
    col = ('grn_no', 'grn_date', 'supp_name', 'bill_no', 'bill_date', 'bill_qty', 'item_total', 'less_amt', 'cgst_amt', 'sgst_amt', 'bill_amt')
    pur_mas_treeview = ttk.Treeview(pur_mas_form, height=8, show='headings', columns=col)
    pur_mas_treeview.pack(fill=tk.X, pady=5)
    style1 = ttk.Style(pur_mas_form)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading", foreground='white', background='Grey35', font='14')
    style1.configure("Treeview", foreground='black', background='#87CEFA', fieldbackground='#B0E2FF',
                     font=('times new roman', 10))
    style1.map('Treeview', background=[('selected', 'Grey35')])

    pur_mas_treeview.column("grn_no", width=80, minwidth=50, anchor=tk.W)
    pur_mas_treeview.column("grn_date", width=90, minwidth=50, anchor=tk.W)
    pur_mas_treeview.column("supp_name", width=200, minwidth=50, anchor=tk.W)
    pur_mas_treeview.column("bill_no", width=100, minwidth=50, anchor=tk.W)
    pur_mas_treeview.column("bill_date", width=90, minwidth=50, anchor=tk.W)
    pur_mas_treeview.column("bill_qty", width=60, minwidth=50, anchor=tk.E)
    pur_mas_treeview.column("item_total", width=100, minwidth=50, anchor=tk.E)
    pur_mas_treeview.column("less_amt", width=100, minwidth=40, anchor=tk.E)
    pur_mas_treeview.column("cgst_amt", width=120, minwidth=50, anchor=tk.E)
    pur_mas_treeview.column("sgst_amt", width=120, minwidth=50, anchor=tk.E)
    pur_mas_treeview.column("bill_amt", width=120, minwidth=50, anchor=tk.E)

    pur_mas_treeview.heading("grn_no", text="GRN No.", anchor=tk.W)
    pur_mas_treeview.heading("grn_date", text="GRN Date", anchor=tk.W)
    pur_mas_treeview.heading("supp_name", text="Supplier Name", anchor=tk.W)
    pur_mas_treeview.heading("bill_no", text="Bill No.", anchor=tk.W)
    pur_mas_treeview.heading("bill_date", text="Bill Date", anchor=tk.W)
    pur_mas_treeview.heading("bill_qty", text="Bill Qty", anchor=tk.E)
    pur_mas_treeview.heading("item_total", text="Item Total", anchor=tk.E)
    pur_mas_treeview.heading("less_amt", text="Less Amount", anchor=tk.E)
    pur_mas_treeview.heading("cgst_amt", text="CGST Amount", anchor=tk.E)
    pur_mas_treeview.heading("sgst_amt", text="SGST Amount", anchor=tk.E)
    pur_mas_treeview.heading("bill_amt", text="Bill Amount", anchor=tk.E)

    vsb = ttk.Scrollbar(pur_mas_form, orient="vertical")
    vsb.configure(command=pur_mas_treeview.yview)
    pur_mas_treeview.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(pur_mas_form, orient="horizontal")
    hsb.configure(command=pur_mas_treeview.xview)
    pur_mas_treeview.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)
    pur_mas_treeview.pack()

    Cur.execute("select*from purchase_master  where grn_no like '%"+str(pur_grn_no_entry_tv.get())+"%' order by grn_no desc")
    i = 0
    for row in Cur:

        pur_mas_treeview.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        i = i + 1

    pur_mas_treeview.focus_set()

    pur_mas_treeview.bind("<Double-1>", Select_GRN)
    pur_mas_treeview.bind("<Return>", Select_GRN)
    pur_mas_treeview.bind("<Escape>", Close_Pur_Mas_Treeview)

    child_id = pur_mas_treeview.get_children()[0]
    pur_mas_treeview.focus(child_id)
    pur_mas_treeview.selection_set(child_id)

    # *****************************   Frame4 - TREEVIEW SETTINGS - END     ********************************************


def Select_GRN(event):

        GRN_selected = pur_mas_treeview.selection()
        for row in GRN_selected:
            pur_grn_no_entry_tv.set(pur_mas_treeview.item(row, 'values')[0])
            grn_date1 = pur_mas_treeview.item(row, 'values')[1]
            pur_grn_date_entry_tv.set(String_To_Date(grn_date1))
            pur_sup_list_combo.set(pur_mas_treeview.item(row, 'values')[2])
            pur_bill_no_entry_tv.set(pur_mas_treeview.item(row, 'values')[3])
            bill_date1 = pur_mas_treeview.item(row, 'values')[4]
            pur_bill_date_entry_tv.set(String_To_Date(bill_date1))
            pur_tot_qty_entry_tv.set(pur_mas_treeview.item(row, 'values')[5])
            obj_cls_pur_entry.set_pur_tot_qty(pur_tot_qty_entry_tv.get())
            pur_tot_amount_entry_tv.set(pur_mas_treeview.item(row, 'values')[6])
            obj_cls_pur_entry.set_pur_tot_amount(pur_tot_amount_entry_tv.get())
            pur_discount_entry_tv.set(pur_mas_treeview.item(row, 'values')[7])
            pur_cgst_entry_tv.set(pur_mas_treeview.item(row, 'values')[8])
            pur_sgst_entry_tv.set(pur_mas_treeview.item(row, 'values')[9])
            pur_bill_amt_entry_tv.set(pur_mas_treeview.item(row, 'values')[10])
        pur_mas_form.destroy()
        pur_grn_no_entry.config(state='disable')
        pur_sup_list_combo.focus_set()
        Cur.execute("select*from purchase_item where grn_no = {}".format(pur_grn_no_entry_tv.get()))
        i=0
        old_data = Cur.fetchall()
        obj_cls_pur_entry.set_pur_original_data(old_data)
        for row2 in old_data:
            Cur.execute("select*from item_master where item_id = {}".format(row2[2]))

            for row3 in Cur.fetchall():
                tree.insert('', i, text="", values=(row3[0], row3[1], row3[2], row3[3], row3[4], row3[5], row3[6], row3[7], row3[9], row2[3], row2[4]))
                i = i+1

        if obj_cls_pur_entry.get_pur_button_clicked() == "edit":
            pur_sup_list_combo.config(state="readonly")
            pur_bill_date_entry.config(state="normal")
            pur_bill_no_entry.config(state="normal")
            pur_brand_entry.config(state="normal")
            pur_product_entry.config(state="normal")
            pur_design_name_entry.config(state="normal")
            pur_color_entry.config(state="normal")
            pur_size_entry.config(state="normal")
            pur_mrp_entry.config(state="normal")
            pur_rate_entry.config(state="normal")
            pur_qty_entry.config(state="normal")
            pur_discount_entry.config(state="normal")
            pur_sup_list_combo.focus_set()
        elif obj_cls_pur_entry.get_pur_button_clicked() == "delete":
            pur_delete_button.focus_set()
        elif obj_cls_pur_entry.get_pur_button_clicked() == "report":
            pur_export_button.focus_set()

def Close_Pur_Mas_Treeview(event):
        pur_mas_form.destroy()


def Purchase_Export(event):
    global pur_grn_no_entry, pur_grn_date_entry, pur_sup_list_combo, pur_bill_no_entry, pur_bill_date_entry, \
        pur_brand_entry, pur_product_entry, pur_design_name_entry, pur_color_entry, pur_size_entry, \
        pur_mrp_entry, pur_rate_entry, pur_gst_entry, pur_id_entry, pur_qty_entry, pur_amount_entry
    global pur_tot_qty_entry, pur_tot_amount_entry, pur_discount_entry, pur_cgst_entry, pur_sgst_entry, pur_bill_amt_entry

    global a3, pur_frame3, pur_export_button, pur_cancel_button
    global pur_grn_no_entry_tv, pur_grn_date_entry_tv, pur_sup_list_combo_tv, pur_bill_no_entry_tv, pur_bill_date_entry_tv, \
        pur_brand_entry_tv, pur_product_entry_tv, pur_design_name_entry_tv, pur_color_entry_tv, pur_size_entry_tv, \
        pur_mrp_entry_tv, pur_rate_entry_tv, pur_gst_entry_tv, pur_id_entry_tv, pur_qty_entry_tv, pur_amount_entry_tv, \
        pur_tot_qty_entry_tv, pur_tot_amount_entry_tv, pur_discount_entry_tv, pur_cgst_entry_tv, pur_sgst_entry_tv, \
        pur_bill_amt_entry_tv

    form_top_label.configure(text="P U R C H A S E      E X P O R T")
    obj_cls_pur_entry.set_pur_button_clicked("report")
    pur_grn_no_entry_tv = tk.IntVar()
    pur_grn_date_entry_tv = tk.StringVar()
    pur_bill_no_entry_tv = tk.StringVar()
    pur_bill_date_entry_tv = tk.StringVar()
    pur_brand_entry_tv = tk.StringVar()
    pur_product_entry_tv = tk.StringVar()
    pur_design_name_entry_tv = tk.StringVar()
    pur_color_entry_tv = tk.StringVar()
    pur_size_entry_tv = tk.StringVar()
    pur_mrp_entry_tv = tk.DoubleVar()
    pur_rate_entry_tv = tk.DoubleVar()
    pur_gst_entry_tv = tk.IntVar()
    pur_id_entry_tv = tk.IntVar()
    pur_qty_entry_tv = tk.IntVar()
    pur_amount_entry_tv = tk.DoubleVar()
    pur_tot_qty_entry_tv = tk.IntVar()
    pur_tot_amount_entry_tv = tk.DoubleVar()
    pur_discount_entry_tv = tk.DoubleVar()
    pur_cgst_entry_tv = tk.DoubleVar()
    pur_sgst_entry_tv = tk.DoubleVar()
    pur_bill_amt_entry_tv = tk.DoubleVar()

    pur_mrp_entry_tv.set(0.00)
    pur_rate_entry_tv.set(0.00)
    pur_id_entry_tv.set('')
    pur_qty_entry_tv.set(0)
    pur_discount_entry_tv.set(0.00)
    pur_cgst_entry_tv.set(0.00)
    pur_sgst_entry_tv.set(0.00)
    pur_bill_amt_entry_tv.set(0.00)

    pur_insert_button.destroy()
    pur_edit_button.destroy()
    pur_delete_button.destroy()
    pur_export_button.destroy()
    pur_quit_button.destroy()

    # *****************************   EXPORT - Frame1 - LABEL & ENTRY BOX SETTINGS - BEGIN     ********************************************
    pur_frame1 = Frame(Purchase_Form, width=380, height=40, bg='#B0E2FF')
    pur_frame1.place(x=10, y=48)

    pur_grn_no_label = Label(pur_frame1, text="GRN No.", bg='#B0E2FF', font=('bold'))
    pur_grn_no_label.place(x=5, y=10)

    pur_grn_date_label = Label(pur_frame1, text="Date", bg='#B0E2FF', font=('bold'))
    pur_grn_date_label.place(x=200, y=10)

    pur_grn_no_entry = Entry(pur_frame1, textvariable=pur_grn_no_entry_tv)
    pur_grn_no_entry.place(x=75, y=10)
    pur_grn_no_entry.config(state='normal')
    pur_grn_no_entry_tv.set("")
    pur_grn_no_entry.bind("<F1>", Show_Purchase_Master)
    pur_grn_no_entry.bind("<FocusIn>", set_focus_pur_grn_no)
    pur_grn_no_entry.focus_set()

    pur_grn_date_entry = Entry(pur_frame1, textvariable=pur_grn_date_entry_tv)
    pur_grn_date_entry.place(x=250, y=10)
    pur_grn_date_entry.config(state='disable')

    # *****************************  EXPORT - Frame1 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************  EXPORT - Frame2 - LABEL &  ENTRY BOX SETTINGS - BEGIN     ********************************************
    pur_frame2 = Frame(Purchase_Form, width=380, height=100, bg='#B0E2FF')
    pur_frame2.place(x=10, y=95)

    supplier_list_label = Label(pur_frame2, text="Supplier List", bg='#B0E2FF', font=('bold'))
    supplier_list_label.place(x=5, y=10)

    pur_bill_no_label = Label(pur_frame2, text="Bill No.", bg='#B0E2FF', font=('bold'))
    pur_bill_no_label.place(x=5, y=35)

    pur_bill_date_label = Label(pur_frame2, text="Bill Date", bg='#B0E2FF', font=('bold'))
    pur_bill_date_label.place(x=5, y=60)

    supplier_list = Supplier_Name_Fetching()
    pur_sup_list_combo = ttk.Combobox(pur_frame2, value=supplier_list, width=40, state='disable')
    pur_sup_list_combo.set('')
    pur_sup_list_combo.place(x=100, y=10)
    pur_sup_list_combo.bind("<Return>", set_focus_pur_bill_no)


    pur_bill_no_entry = Entry(pur_frame2, textvariable=pur_bill_no_entry_tv)
    pur_bill_no_entry.place(x=100, y=35)
    pur_bill_no_entry.config(state="disable")
    pur_bill_no_entry.bind("<Return>", set_focus_pur_bill_date)

    pur_bill_date_entry = DateEntry(pur_frame2, selectmode='day', textvariable=pur_bill_date_entry_tv, state='disable',
                                    width=18, date_pattern='dd-mm-yyyy')
    pur_bill_date_entry.place(x=100, y=60)
    pur_bill_date_entry.bind("<ButtonRelease>", Show_Calendar)
    pur_bill_date_entry.bind("<Return>", set_focus_pur_brand)

    # *****************************   EXPORT - Frame2 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************   EXPORT - Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    pur_frame3 = LabelFrame(Purchase_Form, text="ITEM CREATION", width=640, height=148, bg='#B0E2FF', font=('bold', 12))
    pur_frame3.place(x=650, y=48)

    pur_brand_label = Label(pur_frame3, text="Brand", font=('bold'), bg='#B0E2FF')
    pur_brand_label.place(x=10, y=2)

    pur_product_label = Label(pur_frame3, text="Product", font=('bold'), bg='#B0E2FF')
    pur_product_label.place(x=10, y=27)

    pur_design_name_label = Label(pur_frame3, text="Design Name", font=('bold'), bg='#B0E2FF')
    pur_design_name_label.place(x=10, y=52)

    pur_color_label = Label(pur_frame3, text="Color", font=('bold'), bg='#B0E2FF')
    pur_color_label.place(x=10, y=77)

    pur_size_label = Label(pur_frame3, text="Size", font=('bold'), bg='#B0E2FF')
    pur_size_label.place(x=10, y=102)

    pur_mrp_label = Label(pur_frame3, text="Mrp", font=('bold'), bg='#B0E2FF')
    pur_mrp_label.place(x=250, y=2)

    pur_rate_label = Label(pur_frame3, text="Rate", font=('bold'), bg='#B0E2FF')
    pur_rate_label.place(x=250, y=27)

    pur_gst_label = Label(pur_frame3, text="GST", font=('bold'), bg='#B0E2FF')
    pur_gst_label.place(x=250, y=52)

    pur_id_label = Label(pur_frame3, text="ID", font=('bold'), bg='#B0E2FF')
    pur_id_label.place(x=250, y=77)

    pur_qty_label = Label(pur_frame3, text="Qty", font=('bold'), bg='#B0E2FF')
    pur_qty_label.place(x=250, y=102)

    pur_amount_label = Label(pur_frame3, text="Amount", font=('bold'), bg='#B0E2FF')
    pur_amount_label.place(x=430, y=2)

    pur_brand_entry = Entry(pur_frame3, textvariable=pur_brand_entry_tv)
    pur_brand_entry.place(x=120, y=5)
    pur_brand_entry.config(state="disable")
    pur_brand_entry.bind("<F1>", Show_Field_Master)
    pur_brand_entry.bind("<F2>", Show_Item_Master)
    pur_brand_entry.bind("<Return>", set_focus_pur_product)
    pur_brand_entry.bind("<FocusIn>", set_focus_pur_brand)

    pur_product_entry = Entry(pur_frame3, textvariable=pur_product_entry_tv)
    pur_product_entry.place(x=120, y=30)
    pur_product_entry.config(state="disable")
    pur_product_entry.bind("<F1>", Show_Field_Master)
    pur_product_entry.bind("<Return>", set_focus_pur_design_name)
    pur_product_entry.bind("<FocusIn>", set_focus_pur_product)

    pur_design_name_entry = Entry(pur_frame3, textvariable=pur_design_name_entry_tv)
    pur_design_name_entry.place(x=120, y=55)
    pur_design_name_entry.config(state="disable")
    pur_design_name_entry.bind("<F1>", Show_Field_Master)
    pur_design_name_entry.bind("<Return>", set_focus_pur_color)
    pur_design_name_entry.bind("<FocusIn>", set_focus_pur_design_name)

    pur_color_entry = Entry(pur_frame3, textvariable=pur_color_entry_tv)
    pur_color_entry.place(x=120, y=80)
    pur_color_entry.config(state="disable")
    pur_color_entry.bind("<F1>", Show_Field_Master)
    pur_color_entry.bind("<Return>", set_focus_pur_size)
    pur_color_entry.bind("<FocusIn>", set_focus_pur_color)

    pur_size_entry = Entry(pur_frame3, textvariable=pur_size_entry_tv)
    pur_size_entry.place(x=120, y=105)
    pur_size_entry.config(state="disable")
    pur_size_entry.bind("<F1>", Show_Field_Master)
    pur_size_entry.bind("<Return>", set_focus_pur_mrp)
    pur_size_entry.bind("<FocusIn>", set_focus_pur_size)

    pur_mrp_entry = Entry(pur_frame3, textvariable=pur_mrp_entry_tv, justify='right')
    pur_mrp_entry.place(x=300, y=5)
    pur_mrp_entry.config(state="disable")
    pur_mrp_entry.bind("<FocusIn>", set_focus_pur_mrp)
    pur_mrp_entry.bind("<Return>", set_focus_pur_rate)

    pur_rate_entry = Entry(pur_frame3, textvariable=pur_rate_entry_tv, justify='right')
    pur_rate_entry.place(x=300, y=30)
    pur_rate_entry.config(state="disable")
    pur_rate_entry.bind("<FocusIn>", set_focus_pur_rate)
    pur_rate_entry.bind("<Return>", item_id_creation)

    pur_gst_entry = Entry(pur_frame3, state="disable", textvariable=pur_gst_entry_tv, justify='right')
    pur_gst_entry_tv.set(18)
    pur_gst_entry.place(x=300, y=55)

    pur_id_entry = Entry(pur_frame3, state="disable", textvariable=pur_id_entry_tv, justify='right', font=(9), width=5)
    pur_id_entry.place(x=300, y=80)

    pur_qty_entry = Entry(pur_frame3, textvariable=pur_qty_entry_tv, justify='right', width=5)
    pur_qty_entry.place(x=300, y=105)
    pur_qty_entry.config(state="disable")

    pur_amount_entry = Entry(pur_frame3, state="disable", textvariable=pur_amount_entry_tv, justify='right')
    pur_amount_entry.place(x=500, y=5)
    # *****************************   DELETE - Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - END     ********************************************

    # *****************************     DELETE - Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    pur_tot_qty_label = Label(Purchase_Form, text="Total", font=('bold', 12))
    pur_tot_qty_label.place(x=1000, y=420)

    pur_discount_label = Label(Purchase_Form, text="Discount", font=('bold', 12))
    pur_discount_label.place(x=1000, y=450)

    pur_cgst_label = Label(Purchase_Form, text="CGST @ 9%", font=('bold', 12))
    pur_cgst_label.place(x=1000, y=480)

    pur_sgst_label = Label(Purchase_Form, text="SGST @ 9%", font=('bold', 12))
    pur_sgst_label.place(x=1000, y=510)

    pur_bill_amt_label = Label(Purchase_Form, text="Bill Amount", font=('bold', 12))
    pur_bill_amt_label.place(x=1000, y=540)

    pur_tot_qty_entry = Entry(Purchase_Form, font=('bold', 12), width=5, state='disable',
                              textvariable=pur_tot_qty_entry_tv, justify='right')
    pur_tot_qty_entry.place(x=1100, y=420)

    pur_tot_amount_entry = Entry(Purchase_Form, font=('bold', 12), width=14, state='disable',
                                 textvariable=pur_tot_amount_entry_tv, justify='right')
    pur_tot_amount_entry.place(x=1155, y=420)

    pur_discount_entry = Entry(Purchase_Form, font=('bold', 12), textvariable=pur_discount_entry_tv, justify='right')
    pur_discount_entry.place(x=1100, y=450)
    pur_discount_entry.config(state="disable")


    pur_cgst_entry = Entry(Purchase_Form, font=('bold', 12), state='disable', textvariable=pur_cgst_entry_tv,
                           justify='right')
    pur_cgst_entry.place(x=1100, y=480)

    pur_sgst_entry = Entry(Purchase_Form, font=('bold', 12), state='disable', textvariable=pur_sgst_entry_tv,
                           justify='right')
    pur_sgst_entry.place(x=1100, y=510)

    pur_bill_amt_entry = Entry(Purchase_Form, font=('bold', 12), state='disable', textvariable=pur_bill_amt_entry_tv,
                               justify='right')
    pur_bill_amt_entry.place(x=1100, y=540)

    pur_export_button = Button(Purchase_Form, text='Export To Excel', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_export_button.place(x=535, y=520)
    pur_export_button.bind("<ButtonRelease>", Export_Button_Click)
    pur_export_button.bind("<Return>", Export_Button_Click)
    pur_export_button.bind("<FocusIn>", set_focus_export_to_excel)
    pur_export_button.bind("<FocusOut>", focus_out_export_to_excel)

    pur_cancel_button = Button(Purchase_Form, text='Cancel', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_cancel_button.place(x=710, y=520)
    pur_cancel_button.bind("<Return>", Design_Purchase_Form_Load_destroy2)
    pur_cancel_button.bind("<ButtonRelease>", Design_Purchase_Form_Load_destroy2)
    pur_cancel_button.bind("<FocusIn>", set_focus_cancel_button)
    pur_cancel_button.bind("<FocusOut>", focus_out_cancel_button)

# *****************************     EXPORT  - Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS -  END     ********************************************

def Export_Button_Click(event):
    Cur.execute("select * from  purchase_master where grn_no = '{}'".format(pur_grn_no_entry.get()))

    for row in Cur.fetchall():
        cls_rep.set_grn_no(row[0])
        cls_rep.set_grn_date(row[1])
        cls_rep.set_supp_name(row[2])
        cls_rep.set_bill_no(row[3])
        cls_rep.set_bill_date(row[4])
        cls_rep.set_bill_qty(row[5])
        cls_rep.set_item_total(row[6])
        cls_rep.set_less_amount(row[7])
        cls_rep.set_cgst_amt(row[8])
        cls_rep.set_sgst_amt(row[9])
        cls_rep.set_bill_amount(row[10])

    Cur2.execute("select * from purchase_item where grn_no = '{}'".format(pur_grn_no_entry.get()))
    purchase_item_data = []
    for row in Cur2.fetchall():
        purchase_item_data.append(row)

    file_name1 = "Purchase GRN " + pur_grn_no_entry.get() + " " + pur_grn_date_entry.get() + ".xlsx"
    pur_report_export_to_excel(file_name1, "Purchase", purchase_item_data)

    filepath = r"C:\Users\SYED\AcubeProjects\Status Plus\Purchase GRN " + pur_grn_no_entry.get() + " " + pur_grn_date_entry.get() + ".xlsx"

    os.startfile(filepath)
    Purchase_Form.focus_set()
    pur_grn_no_entry.focus_set()

def pur_report_export_to_excel( workbookname:str, worksheetname:str, pur_item_data:list):
    item_master_header = ["Brand", "Product", "Design Name", "Color", "Size", "Mrp", "Rate", "GST", "ID", "Qty", "Amount"]
    workbook = xlsxwriter.Workbook(workbookname)
    worksheet = workbook.add_worksheet(worksheetname)

    worksheet.merge_range('A1:K1', cls_rep.get_supp_name(), workbook.add_format({'align': 'center', 'font_size': 18, 'bg_color': '#698B69'}))
    Cur1.execute("select * from  supplier_master where name = '{}'".format(cls_rep.get_supp_name()))
    sup_details = []
    for row in Cur1.fetchone():
        sup_details.append(row)

    worksheet.merge_range('A2:K2', sup_details[1] +", "+ sup_details[2], workbook.add_format({'align': 'center', 'bg_color': 'white'})) #address & locality
    worksheet.merge_range('A3:K3', sup_details[3] + "-" + str(sup_details[4]) + "," + sup_details[5], workbook.add_format({'align': 'center', 'bg_color': 'white'})) #city, pincode & state
    worksheet.merge_range('A4:B4', "Phone No. : "+ str(sup_details[6]), workbook.add_format({'align': 'left', 'bg_color': 'white'}))
    worksheet.merge_range('C4:E4', "GST No. :" + sup_details[8], workbook.add_format({'align': 'center', 'bg_color': 'white'}))
    worksheet.merge_range('F4:K4', "Email : "+sup_details[7], workbook.add_format({'align': 'right', 'bg_color': 'white'}))
    worksheet.merge_range('A5:K5',"", workbook.add_format({'top': 1, 'bg_color': 'white'}))
    worksheet.merge_range('A6:B6', "GRN : "+ str(cls_rep.get_grn_no()), workbook.add_format({'align': 'left', 'bg_color': 'white', 'bold': 'True'}))
    worksheet.merge_range('H6:K6', "Bill No. : " + str(cls_rep.get_bill_no()), workbook.add_format({'align': 'right', 'bg_color': 'white', 'bold': 'True'}))
    worksheet.merge_range('A7:B7', "GRN Date : "+ str(pur_grn_date_entry.get()), workbook.add_format({'align': 'left', 'bg_color': 'white', 'bold': 'True'}))
    worksheet.merge_range('H7:K7', "Bill Date : "+ str(pur_bill_date_entry.get()), workbook.add_format({'align': 'right', 'bg_color': 'white', 'bold': 'True'}))
    worksheet.merge_range('C6:G7', "", workbook.add_format({'bg_color': 'white'}))
    worksheet.merge_range('A8:K8', "", workbook.add_format({'bg_color': 'white'}))
    worksheet.set_column(8, 0, 18)#brand
    worksheet.set_column(8, 1, 18)#product
    worksheet.set_column(8, 2, 20)#design
    worksheet.set_column(8, 3, 9)#color
    worksheet.set_column(8, 4, 9)#size
    worksheet.set_column(8, 5, 9)#mrp
    worksheet.set_column(8, 6, 9)#rate
    worksheet.set_column(8, 7, 4)#GST
    worksheet.set_column(8, 8, 4)#id
    worksheet.set_column(8, 9, 4)#qty

    for index, row in enumerate(item_master_header):
        worksheet.write(8,index, row, workbook.add_format({'bg_color': '#698B69', 'bold': 'True'}))

    row_count = 9
    for index1, row1 in enumerate(pur_item_data):
        Cur2.execute("select * from item_master where item_id = {}".format(row1[2]))
        row_count = row_count+1


        for row2 in Cur2.fetchall():
            if (index1 + 9)%2 == 0 :
                worksheet.write(index1+9,0, row2[0], workbook.add_format({'align': 'left', 'bg_color': '#7FFFD4'})) #brand
                worksheet.write(index1+9, 1, row2[1], workbook.add_format({'align': 'left', 'bg_color': '#7FFFD4'})) #product
                worksheet.write(index1 + 9, 2, row2[2], workbook.add_format({'align': 'left', 'bg_color': '#7FFFD4'})) #design
                worksheet.write(index1 + 9, 3, row2[3], workbook.add_format({'align': 'left', 'bg_color': '#7FFFD4'})) #color
                worksheet.write(index1 + 9, 4, row2[4], workbook.add_format({'align': 'left', 'bg_color': '#7FFFD4'})) #size
                worksheet.write(index1 + 9, 5, row2[5], workbook.add_format({'align':'right', 'num_format': '####.00', 'bg_color': '#7FFFD4'})) #mrp
                worksheet.write(index1 + 9, 6, row2[6], workbook.add_format({'align':'right', 'num_format': '####.00', 'bg_color': '#7FFFD4'})) #rate
                worksheet.write(index1 + 9, 7, row2[7], workbook.add_format({'align': 'center', 'bg_color': '#7FFFD4'})) #gst
                worksheet.write(index1 + 9, 8, row2[9], workbook.add_format({'align': 'center', 'bg_color': '#7FFFD4'})) #item_id
                worksheet.write(index1 + 9, 9, row1[3], workbook.add_format({'align': 'right', 'bg_color': '#7FFFD4'})) #item_qty
                worksheet.write(index1 + 9, 10, row1[4], workbook.add_format({'align':'right', 'num_format': '####.00', 'bg_color': '#7FFFD4'})) #item_amount
            else:
                worksheet.write(index1+9,0, row2[0], workbook.add_format({'align': 'left', 'bg_color': '#C1FFC1'})) #brand
                worksheet.write(index1+9, 1, row2[1], workbook.add_format({'align': 'left', 'bg_color': '#C1FFC1'})) #product
                worksheet.write(index1 + 9, 2, row2[2], workbook.add_format({'align': 'left', 'bg_color': '#C1FFC1'})) #design
                worksheet.write(index1 + 9, 3, row2[3], workbook.add_format({'align': 'left', 'bg_color': '#C1FFC1'})) #color
                worksheet.write(index1 + 9, 4, row2[4], workbook.add_format({'align': 'left', 'bg_color': '#C1FFC1'})) #size
                worksheet.write(index1 + 9, 5, row2[5], workbook.add_format({'align':'right', 'num_format': '####.00', 'bg_color': '#C1FFC1'})) #mrp
                worksheet.write(index1 + 9, 6, row2[6], workbook.add_format({'align':'right', 'num_format': '####.00', 'bg_color': '#C1FFC1'})) #rate
                worksheet.write(index1 + 9, 7, row2[7], workbook.add_format({'align': 'center', 'bg_color': '#C1FFC1'})) #gst
                worksheet.write(index1 + 9, 8, row2[9], workbook.add_format({'align': 'center', 'bg_color': '#C1FFC1'})) #item_id
                worksheet.write(index1 + 9, 9, row1[3], workbook.add_format({'align': 'right', 'bg_color': '#C1FFC1'})) #item_qty
                worksheet.write(index1 + 9, 10, row1[4], workbook.add_format({'align':'right', 'num_format': '####.00', 'bg_color': '#C1FFC1'})) #item_amount

    rc = "G" + str(row_count+1) + ":I" + str(row_count+1)
    worksheet.merge_range(rc, "Total ", workbook.add_format({'align': 'left', 'bg_color': '#C1FFC1', 'bold': 'True'}))
    worksheet.write(row_count, 9, str(cls_rep.get_bill_qty()), workbook.add_format({'top':1, 'align':'right', 'bg_color': '#C1FFC1', 'bold': 'True'}))
    worksheet.write(row_count, 10, str(cls_rep.get_item_total()), workbook.add_format({'top':1, 'align':'right', 'num_format': '####.00', 'bg_color': '#C1FFC1', 'bold': 'True'}))
    rc = "G" + str(row_count+2) + ":J" + str(row_count+2)
    worksheet.merge_range(rc, "Discount Amount ", workbook.add_format({'bg_color': '#C1FFC1', 'bold': 'True'}))
    worksheet.write(row_count+1, 10, str(cls_rep.get_less_amount()), workbook.add_format({'align':'right', 'num_format': '####.00', 'bg_color': '#C1FFC1', 'bold': 'True'}))
    rc = "G" + str(row_count+3) + ":J" + str(row_count+3)
    worksheet.merge_range(rc, "Taxable ", workbook.add_format({'bg_color': '#C1FFC1', 'bold': 'True'}))
    worksheet.write(row_count+2, 10, str(cls_rep.get_item_total()-cls_rep.get_less_amount()), workbook.add_format({'top':1, 'align':'right', 'num_format': '####.00', 'bg_color': '#C1FFC1', 'bold': 'True'}))
    rc = "G" + str(row_count + 4) + ":J" + str(row_count + 4)
    worksheet.merge_range(rc, "CGST @ 9% ", workbook.add_format({'bg_color': '#C1FFC1', 'bold': 'True'}))
    worksheet.write(row_count + 3, 10, str(cls_rep.get_cgst_amt()), workbook.add_format({'align': 'right', 'num_format': '####.00', 'bg_color': '#C1FFC1', 'bold': 'True'}))
    rc = "G" + str(row_count+5) + ":J" + str(row_count+5)
    worksheet.merge_range(rc, "SGST @ 9% ", workbook.add_format({'bg_color': '#C1FFC1', 'bold': 'True'}))
    worksheet.write(row_count+4, 10, str(cls_rep.get_sgst_amt()), workbook.add_format({'align':'right', 'num_format': '####.00', 'bg_color': '#C1FFC1', 'bold': 'True'}))
    rc = "G" + str(row_count+6) + ":J" + str(row_count+6)
    worksheet.merge_range(rc, "Bill Amount ", workbook.add_format({'bold': 'True', 'bg_color': '#C1FFC1', 'font_size': 12}))
    worksheet.write(row_count+5, 10, str(cls_rep.get_bill_amount()), workbook.add_format({'top':1, 'bottom': 1, 'align':'right', 'num_format': '####.00', 'font_size': 12, 'bold': 'True', 'bg_color': '#C1FFC1'}))
    workbook.close()

def Design_Purchase_Form_Load():
    global Purchase_Form, form_top_label, form_bottom_label, pur_frame1, tree, pur_frame4
    global pur_insert_button, pur_edit_button, pur_delete_button, pur_export_button, pur_quit_button

    Purchase_Form = tk.Toplevel()
    Purchase_Form.geometry("1300x600+24+51")
    Purchase_Form.title("")
    form_top_label = Label(Purchase_Form, text="P  U  R  C  H  A  S  E", width=1200, bg="#63B8FF", fg="black", font=('copper', 20, 'bold'))
    form_top_label.pack()


    #*****************************    Frame1 - LABEL & ENTRY BOX SETTINGS - BEGIN     ********************************************
    pur_frame1 = Frame(Purchase_Form, width=380, height=40, bg='#B0E2FF')
    pur_frame1.place(x=10,y=48)

    pur_grn_no_label = Label(pur_frame1, text="GRN No.", bg='#B0E2FF', font=('bold'))
    pur_grn_no_label.place(x=5, y=10)

    pur_grn_date_label = Label(pur_frame1, text="Date", bg='#B0E2FF', font=('bold'))
    pur_grn_date_label.place(x=200, y=10)

    pur_grn_no_entry = Entry(pur_frame1)
    pur_grn_no_entry.place(x=75, y=10)
    pur_grn_no_entry.config(state='disable')

    pur_grn_date_entry = Entry(pur_frame1)
    pur_grn_date_entry.place(x=250, y=10)
    pur_grn_date_entry.config(state='disable')
    #*****************************   Frame1 - LABEL & ENTRY BOX SETTINGS - END     ********************************************


    #*****************************   Frame2 - LABEL &  ENTRY BOX SETTINGS - BEGIN     ********************************************
    pur_frame2 = Frame(Purchase_Form, width=380, height=100, bg='#B0E2FF')
    pur_frame2.place(x=10, y=95)

    supplier_list_label = Label(pur_frame2, text="Supplier List", bg='#B0E2FF',  font=('bold'))
    supplier_list_label.place(x=5, y=10)

    pur_bill_no_label = Label(pur_frame2, text="Bill No.", bg='#B0E2FF',  font=('bold'))
    pur_bill_no_label.place(x=5, y=35)

    pur_bill_date_label = Label(pur_frame2, text="Bill Date", bg='#B0E2FF',  font=('bold'))
    pur_bill_date_label.place(x=5, y=60)


    supplier_list = Supplier_Name_Fetching()
    pur_sup_list_combo = ttk.Combobox(pur_frame2, value=supplier_list, width=40, state='readonly')
    pur_sup_list_combo.set('')
    pur_sup_list_combo.place(x=100, y=10)
    pur_sup_list_combo.config(state='disable')

    pur_bill_no_entry = Entry(pur_frame2)
    pur_bill_no_entry.place(x=100, y=35)
    pur_bill_no_entry.config(state='disable')

    pur_bill_date_entry = DateEntry(pur_frame2, state='disable', width=18)
    pur_bill_date_entry.place(x=100, y=60)
    #pur_bill_date_entry.config(state='disable')
# *****************************   Frame2 - LABEL & ENTRY BOX SETTINGS - END     ********************************************


# *****************************   Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    pur_frame3 = LabelFrame(Purchase_Form, text="ITEM CREATION", width=640, height=148, bg='#B0E2FF', font=('bold', 12))
    pur_frame3.place(x=650, y=48)

    pur_brand_label = Label(pur_frame3, text="Brand", font=('bold'), bg='#B0E2FF')
    pur_brand_label.place(x=10, y=2)

    pur_product_label = Label(pur_frame3, text="Product", font=('bold'), bg='#B0E2FF')
    pur_product_label.place(x=10, y=27)

    pur_design_name_label = Label(pur_frame3, text="Design Name", font=('bold'), bg='#B0E2FF')
    pur_design_name_label.place(x=10, y=52)

    pur_color_label = Label(pur_frame3, text="Color", font=('bold'), bg='#B0E2FF')
    pur_color_label.place(x=10, y=77)

    pur_size_label = Label(pur_frame3, text="Size", font=('bold'), bg='#B0E2FF')
    pur_size_label.place(x=10, y=102)

    pur_mrp_label = Label(pur_frame3, text="Mrp", font=('bold'), bg='#B0E2FF')
    pur_mrp_label.place(x=250, y=2)

    pur_rate_label = Label(pur_frame3, text="Rate", font=('bold'), bg='#B0E2FF')
    pur_rate_label.place(x=250, y=27)

    pur_gst_label = Label(pur_frame3, text="GST", font=('bold'), bg='#B0E2FF')
    pur_gst_label.place(x=250, y=52)

    pur_id_label = Label(pur_frame3, text="ID", font=('bold'), bg='#B0E2FF')
    pur_id_label.place(x=250, y=77)

    pur_qty_label = Label(pur_frame3, text="Qty", font=('bold'), bg='#B0E2FF')
    pur_qty_label.place(x=250, y=102)

    pur_amount_label = Label(pur_frame3, text="Amount", font=('bold'), bg='#B0E2FF')
    pur_amount_label.place(x=430, y=2)


    pur_brand_entry = Entry(pur_frame3, state="disable")
    pur_brand_entry.place(x=120, y=5)

    pur_product_entry = Entry(pur_frame3, state="disable")
    pur_product_entry.place(x=120, y=30)

    pur_design_name_entry = Entry(pur_frame3, state="disable")
    pur_design_name_entry.place(x=120, y=55)

    pur_color_entry = Entry(pur_frame3, state="disable")
    pur_color_entry.place(x=120, y=80)

    pur_size_entry = Entry(pur_frame3, state="disable")
    pur_size_entry.place(x=300, y=30)

    pur_mrp_entry = Entry(pur_frame3, state="disable")
    pur_mrp_entry.place(x=120, y=105)

    pur_rate_entry = Entry(pur_frame3, state="disable")
    pur_rate_entry.place(x=300, y=5)

    pur_gst_entry = Entry(pur_frame3, state="disable")
    pur_gst_entry.place(x=300, y=55)

    pur_id_entry = Entry(pur_frame3, state="disable", font=(8), width=5)
    pur_id_entry.place(x=300, y=80)

    pur_qty_entry = Entry(pur_frame3, state="disable", width=5)
    pur_qty_entry.place(x=300, y=105)

    pur_amount_entry = Entry(pur_frame3, state="disable")
    pur_amount_entry.place(x=500, y=5)

# *****************************   Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - END     ********************************************


# *****************************    Frame4 - TREEVIEW SETTINGS - BEGIN     ********************************************

    pur_frame4 = Frame(Purchase_Form)
    pur_frame4.pack(pady=5)
    pur_frame4.place(x=10, y=210)
    pur_frame4.pack_propagate(False)
    pur_frame4.configure(width=1280, height=196, bg='#B0E2FF')
    global col

    col = ('brand', 'product', 'design', 'color', 'size', 'mrp', 'rate', 'gst', 'id', 'qty', 'amount')
    tree = ttk.Treeview(pur_frame4, height=8, show='headings', columns=col)
    # tree['show']='headings'
    tree.pack(fill=tk.X,pady=5)
    style1 = ttk.Style(pur_frame4)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading",foreground='white', background='Grey35', font='14')
    style1.configure("Treeview", foreground='white', background='Grey35', fieldbackground='#B0E2FF',
                     font=('times new roman', 10))
    style1.map('Treeview', background=[('selected', '#B0E2FF')])


    tree.column("brand", width=150, minwidth=50, anchor=tk.W)
    tree.column("product", width=150, minwidth=50, anchor=tk.W)
    tree.column("design", width=200, minwidth=50, anchor=tk.W)
    tree.column("color", width=150, minwidth=50, anchor=tk.W)
    tree.column("size", width=50, minwidth=50, anchor=tk.W)
    tree.column("mrp", width=50, minwidth=50, anchor=tk.E)
    tree.column("rate", width=50, minwidth=50, anchor=tk.E)
    tree.column("gst", width=50, minwidth=50, anchor=tk.S)
    tree.column("id", width=50, minwidth=50, anchor=tk.S)
    tree.column("qty", width=50, minwidth=50, anchor=tk.E)
    tree.column("amount", width=100, minwidth=100, anchor=tk.E)

    tree.heading("brand", text="BRAND", anchor=tk.W)
    tree.heading("product", text="PRODUCT", anchor=tk.W)
    tree.heading("design", text="DESIGN NAME", anchor=tk.W)
    tree.heading("color", text="COLOR", anchor=tk.W)
    tree.heading("size", text="SIZE", anchor=tk.W)
    tree.heading("mrp", text="MRP", anchor=tk.E)
    tree.heading("rate", text="RATE", anchor=tk.E)
    tree.heading("gst", text="GST", anchor=tk.S)
    tree.heading("id", text="ID", anchor=tk.S)
    tree.heading("qty", text="QTY", anchor=tk.E)
    tree.heading("amount", text="AMOUNT", anchor=tk.E)


    vsb = ttk.Scrollbar(pur_frame4, orient="vertical")
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(pur_frame4, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)

    tree.pack()
    tree.bind("<Return>", Select_Item_Data)
    tree.bind("<ButtonRelease>", Select_Item_Data)
    tree.bind("<Delete>", Delete_Purchase_Items_In_Treeview)
    tree.bind("<FocusIn>", set_focus_treeview)

    # *****************************   Frame4 - TREEVIEW SETTINGS - END     ********************************************

    # *****************************     Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    pur_tot_qty_label = Label(Purchase_Form, text="Total", font=('bold',12))
    pur_tot_qty_label.place(x=1000, y=420)

    pur_discount_label = Label(Purchase_Form, text="Discount", font=('bold', 12))
    pur_discount_label.place(x=1000, y=450)

    pur_cgst_label = Label(Purchase_Form, text="CGST @ 9%", font=('bold', 12))
    pur_cgst_label.place(x=1000, y=480)

    pur_sgst_label = Label(Purchase_Form, text="SGST @ 9%", font=('bold', 12))
    pur_sgst_label.place(x=1000, y=510)

    pur_bill_amt_label = Label(Purchase_Form, text="Bill Amount", font=('bold', 12))
    pur_bill_amt_label.place(x=1000, y=540)

    pur_tot_qty_entry = Entry(Purchase_Form, font=('bold', 12), width=5, state='disable')
    pur_tot_qty_entry.place(x=1100, y=420)

    pur_tot_amount_entry = Entry(Purchase_Form, font=('bold', 12), width=14, state='disable')
    pur_tot_amount_entry.place(x=1155, y=420)

    pur_discount_entry = Entry(Purchase_Form, font=('bold', 12), state='disable')
    pur_discount_entry.place(x=1100, y=450)

    pur_cgst_entry = Entry(Purchase_Form, font=('bold', 12), state='disable')
    pur_cgst_entry.place(x=1100, y=480)

    pur_sgst_entry = Entry(Purchase_Form, font=('bold', 12), state='disable')
    pur_sgst_entry.place(x=1100, y=510)

    pur_bill_amt_entry = Entry(Purchase_Form, font=('bold', 12), state='disable')
    pur_bill_amt_entry.place(x=1100, y=540)

    pur_insert_button = Button(Purchase_Form, text='I N S E R T', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_insert_button.place(x=10, y=520)
    pur_insert_button.focus_set()
    pur_insert_button.bind("<Return>", Purchase_Insert)
    pur_insert_button.bind("<ButtonRelease>", Purchase_Insert)
    pur_insert_button.bind("<FocusIn>", set_focus_insert_button)
    pur_insert_button.bind("<FocusOut>", focus_out_insert_button)

    pur_edit_button = Button(Purchase_Form, text='E D I T', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_edit_button.place(x=185, y=520)
    pur_edit_button.bind("<Return>", Purchase_Edit)
    pur_edit_button.bind("<ButtonRelease>", Purchase_Edit)
    pur_edit_button.bind("<FocusIn>", set_focus_edit_button)
    pur_edit_button.bind("<FocusOut>",  focus_out_edit_button)

    pur_delete_button = Button(Purchase_Form, text='D E L E T E', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_delete_button.place(x=360, y=520)
    pur_delete_button.bind("<Return>", Purchase_Delete)
    pur_delete_button.bind("<ButtonRelease>", Purchase_Delete)
    pur_delete_button.bind("<FocusIn>", set_focus_delete_button)
    pur_delete_button.bind("<FocusOut>", focus_out_delete_button)

    pur_export_button = Button(Purchase_Form, text='R E P O R T', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_export_button.place(x=535, y=520)
    pur_export_button.bind("<ButtonRelease>", Purchase_Export)
    pur_export_button.bind("<Return>", Purchase_Export)
    pur_export_button.bind("<FocusIn>", set_focus_export_button)
    pur_export_button.bind("<FocusOut>", focus_out_export_button)

    pur_quit_button = Button(Purchase_Form, text='Q U I T', bg='Grey35', fg='white', width=15, font=('bold', 14))
    pur_quit_button.place(x=710, y=520)
    pur_quit_button.bind("<Return>", Design_Purchase_Form_Load_destroy)
    pur_quit_button.bind("<ButtonRelease>", Design_Purchase_Form_Load_destroy)
    pur_quit_button.bind("<FocusIn>", set_focus_quit_button)
    pur_quit_button.bind("<FocusOut>", focus_out_quit_button)

    form_bottom_label = Label(Purchase_Form, text="To Insert Purchase Press - [INSERT]       To Edit Purchase Press - [EDIT]       To Delete Purchase Press - [DELETE]       To Export Purchase Press - [REPORT]        To Move Next Button Press - [Tab]", width=1200, bg="#63B8FF", fg="black", font=('copper', 11))
    form_bottom_label.pack(side=BOTTOM)
# *****************************     Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS -  END     ********************************************
