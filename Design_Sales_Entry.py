import datetime
import os
from Class_Main_Window import*
from tkinter import *
import tkinter as tk
from tkinter import ttk
from DB_Connection import *
from datetime import *
from datetime import datetime
from tkinter import messagebox
from Class_Sales_Entry import *
from Class_Sales_Report import *

cls_rep = cls_sales_report()
obj_com_details = cls_main_window()
obj_cls_sal_entry = cls_sales_entry()

Con = DB_Connect()
Cur = Con.cursor()
Cur1 = Con.cursor()
Cur2 = Con.cursor()
global field1
s_no = 0
total_qty1 = 0
total_amount1 = 0.00
dt = datetime.today()
newdate = dt.strftime("%d-%m-%Y")

def Show_Calendar(event):
    sal_bill_date_entry.config(text=sal_bill_date_entry_tv.get())

def set_focus_sal_bill_no(event):
    form_bottom_label.config(text="To List Bill No.'s Type 2 & Press [F1] Key")

def lost_focus_sal_bill_no(event):
    form_bottom_label.config(text="")

def set_focus_sal_cust_list(event):
    form_bottom_label.config(text="Choose Customer Name From The List")
    
def set_focus_sal_brand(event):
    sal_brand_entry.focus_set()
    obj_cls_sal_entry.set_sal_field_focus("Brand")
    sal_brand_entry.selection_range(0, len(str(sal_brand_entry_tv.get())))
    form_bottom_label.config(text="To List Stock Balance Of All The Item Press [F1]     or     Type Design Name And Press [F1]")

def lost_focus_sal_brand(event):
    form_bottom_label.config(text="")

def set_focus_sal_qty():
    sal_qty_entry.focus_set()
    sal_qty_entry.selection_range(0, len(str(sal_qty_entry_tv.get())))

def set_focus_sal_qty1(event):
    sal_qty_entry.focus_set()
    sal_qty_entry.selection_range(0, len(str(sal_qty_entry_tv.get())))
    form_bottom_label.config(text="Enter Qty        Integer Numbers Only")

def set_focus_sal_discount(event):
    form_bottom_label.config(text="Enter Discount Amount        Maximum Allowed Number Including Decimal - 10")

def set_focus_insert_button(event):
    form_bottom_label.config(text="To Add Sales Press - [INSERT]")
    sal_insert_button.config(bg="#87CEFA", fg="black")

def set_focus_edit_button(event):
    form_bottom_label.config(text="To Modify Sales Press - [EDIT]")
    sal_edit_button.config(bg="#87CEFA", fg="black")

def set_focus_delete_button(event):
    form_bottom_label.config(text="To Remove Sales Press - [DELETE]")
    sal_delete_button.config(bg="#87CEFA", fg="black")

def set_focus_export_button(event):
    form_bottom_label.config(text="To Export Sales Press - [REPORT]")
    sal_export_button.config(bg="#87CEFA", fg="black")

def set_focus_quit_button(event):
    form_bottom_label.config(text="To Exit This Form Press - [QUIT]")
    sal_quit_button.config(bg="#87CEFA", fg="black")

def set_focus_save_button(event):
    sal_save_button.focus_set()
    form_bottom_label.config(text="To Save This Sales Entries Press [Enter] Key")
    sal_save_button.config(bg="#87CEFA", fg="black" )

def set_focus_update_button(event):
    sal_save_button.config(bg="#87CEFA", fg="black")
    form_bottom_label.config(text="To Update This Sales Entries Press [Enter] Key")

def set_focus_delete2_button(event):
    sal_delete_button.focus_set()
    sal_delete_button.config(bg="#87CEFA", fg="black")
    form_bottom_label.config(text="To Delete This Sales Entries Press [Enter] Key")

def set_focus_cancel_button(event):
    sal_cancel_button.config(bg="#87CEFA", fg="black")
    form_bottom_label.config(text="To Undo The Changes Made To This Sales Entries Press [Enter] Key")

def set_focus_export_to_excel_button(event):
    sal_export_to_excel_button.config(bg="#87CEFA", fg="black")
    form_bottom_label.config(text="To View Sales Bill In Excel Press [ENTER]")

def lost_focus_export_to_excel_button(event):
    sal_export_to_excel_button.config(bg="Grey28", fg="white")
    form_bottom_label.config(text="")

def set_focus_export_to_excel_cancel_button(event):
    sal_cancel_button.config(bg="#87CEFA", fg="black")
    form_bottom_label.config(text="To Go Back Press [ENTER]")

def focus_out_insert_button(evcnt):
    form_bottom_label.config(text="To Insert Sales Press - [INSERT]       To Edit Sales Press - [EDIT]       To Delete Sales Press - [DELETE]       To Export Sales Press - [REPORT]        To Move Next Button Press - [Tab]")
    sal_insert_button.config(bg="Grey28", fg="white")

def focus_out_edit_button(event):
    form_bottom_label.config(text="To Insert Sales Press - [INSERT]       To Edit Sales Press - [EDIT]       To Delete Sales Press - [DELETE]       To Export Sales Press - [REPORT]        To Move Next Button Press - [Tab]")
    sal_edit_button.config(bg="Grey28", fg="white")

def focus_out_delete_button(event):
    form_bottom_label.config(text="To Insert Sales Press - [INSERT]       To Edit Sales Press - [EDIT]       To Delete Sales Press - [DELETE]       To Export Sales Press - [REPORT]        To Move Next Button Press - [Tab]")
    sal_delete_button.config(bg="Grey28", fg="white")

def focus_out_export_button(event):
    form_bottom_label.config(text="To Insert Sales Press - [INSERT]       To Edit Sales Press - [EDIT]       To Delete Sales Press - [DELETE]       To Export Sales Press - [REPORT]        To Move Next Button Press - [Tab]")
    sal_export_button.config(bg="Grey28", fg="white")

def focus_out_quit_button(event):
    form_bottom_label.config(text="To Insert Sales Press - [INSERT]       To Edit Sales Press - [EDIT]       To Delete Sales Press - [DELETE]       To Export Sales Press - [REPORT]        To Move Next Button Press - [Tab]")
    sal_quit_button.config(bg="Grey28", fg="white")

def focus_out_save_button(event):
    sal_save_button.config(bg="Grey28", fg="white")

def focus_out_update_button(event):
    sal_save_button.config(bg="Grey28", fg="white")

def focus_out_delete2_button(event):
    sal_delete_button.config(bg="Grey28", fg="white")

def focus_out_export_to_excel(event):
    sal_export_button.config(bg="Grey28", fg="white")

def focus_out_cancel_button(event):
    sal_cancel_button.config(bg="Grey28", fg="white")
    form_bottom_label.config(text="")

def set_focus_treeview(event):
    if obj_cls_sal_entry.get_sal_button_clicked() == "insert" or obj_cls_sal_entry.get_sal_button_clicked() == "edit":
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

def Customer_Name_Fetching():
    name = list()
    Cur.execute("select name from customer_master order by name")
    for customer_name in Cur:
        name.append(customer_name[0])

    return name

def Refresh_cust_Data2(records):
    for item in tree.get_children():
        tree.delete(item)

    i = 0
    for row in records:
        tree.insert('', i, text="",
                    values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        i = i + 1

def Select_Item_Data(event):
    if obj_cls_sal_entry.get_sal_button_clicked() == "insert" or obj_cls_sal_entry.get_sal_button_clicked() == "edit":
        dum1 = tree.selection()

        for row4 in dum1:
            sal_brand_entry_tv.set(tree.item(row4, 'values')[0])
            sal_product_entry_tv.set(tree.item(row4, 'values')[1])
            sal_design_name_entry_tv.set(tree.item(row4, 'values')[2])
            sal_color_entry_tv.set(tree.item(row4, 'values')[3])
            sal_size_entry_tv.set(tree.item(row4, 'values')[4])
            sal_mrp_entry_tv.set(tree.item(row4, 'values')[5])
            sal_rate_entry_tv.set(tree.item(row4, 'values')[6])
            sal_gst_entry_tv.set(tree.item(row4, 'values')[7])
            sal_id_entry_tv.set(tree.item(row4, 'values')[8])
            sal_qty_entry_tv.set(tree.item(row4, 'values')[9])
            sal_amount_entry_tv.set(tree.item(row4, 'values')[10])

def Add_sales_Items_In_Treeview(event):
    global total_qty1, total_amount1
    Cur1.execute("select * from stock_balance where item_id = {}".format(sal_id_entry_tv.get()))
    for row1 in Cur1.fetchall():
        if sal_qty_entry_tv.get() <= row1[8]:
            Cur.execute("select*from item_master where item_id = {}".format(sal_id_entry_tv.get()))
            for row in Cur:
                dum_amount = row[5]
                sal_amount_entry_tv.set(round(dum_amount, 2) * sal_qty_entry_tv.get())
                tree.insert("", "end", text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                                        row[9], sal_qty_entry_tv.get(), sal_amount_entry_tv.get()))
            total_qty1 = obj_cls_sal_entry.get_sal_tot_qty() + sal_qty_entry_tv.get()
            total_amount1 = obj_cls_sal_entry.get_sal_tot_amount() + sal_amount_entry_tv.get()
            obj_cls_sal_entry.set_sal_tot_qty(total_qty1)
            obj_cls_sal_entry.set_sal_tot_amount(round(total_amount1, 2))
            sal_tot_qty_entry_tv.set(total_qty1)
            sal_tot_amount_entry_tv.set(round(total_amount1, 2))
            sales_Bill_Amt_Calculate(total_amount1)
            sal_qty_entry.config(state="disable")
            form_bottom_label.config(text="To List Stock Balance Of All The Item Press [F1]     or     Type Design Name And Press [F1]")
            sal_brand_entry_tv.set("")
            sal_product_entry_tv.set("")
            sal_design_name_entry_tv.set("")
            sal_color_entry_tv.set("")
            sal_size_entry_tv.set("")
            sal_mrp_entry_tv.set("")
            sal_rate_entry_tv.set("")
            sal_gst_entry_tv.set("")
            sal_id_entry_tv.set("")
            sal_qty_entry_tv.set("")
            sal_brand_label.config(text="Select Item")
            sal_brand_entry.focus_set()
            sal_brand_entry.selection_range(0, len(sal_brand_entry_tv.get()))
        else:
            messagebox.showinfo("Warning", "Available Stock Is "+str(row1[8]))
            sales_Form.focus_set()
            sal_qty_entry.focus_set()

def sales_Bill_Amt_Calculate(n):
    dum_net_amt = n - sal_discount_entry_tv.get()
    n2 = float(dum_net_amt/118)*100
    dum_cgst = (n2 * 9) / 100
    dum_sgst = (n2 * 9) / 100
    obj_cls_sal_entry.set_sal_discount(float(sal_discount_entry_tv.get()))
    obj_cls_sal_entry.set_sal_taxable(round(n2,2))
    obj_cls_sal_entry.set_sal_cgst(round(dum_cgst, 2))
    obj_cls_sal_entry.set_sal_sgst(round(dum_sgst, 2))
    tot_amt = dum_net_amt
    obj_cls_sal_entry.set_sal_bill_amount(round(tot_amt, 2))
    sal_taxable_entry_tv.set(obj_cls_sal_entry.get_sal_taxable())
    sal_cgst_entry_tv.set(obj_cls_sal_entry.get_sal_cgst())
    sal_sgst_entry_tv.set(obj_cls_sal_entry.get_sal_sgst())
    sal_bill_amt_entry_tv.set(round(obj_cls_sal_entry.get_sal_bill_amount(), 0))

def sales_Bill_Amt_Calculate2(event):
    sales_Bill_Amt_Calculate(obj_cls_sal_entry.get_sal_tot_amount())

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
    if event.keycode >= 48 and event.keycode <= 57:
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
        sales_Bill_Amt_Calculate(obj_cls_sal_entry.get_sal_tot_amount())

def Delete_sales_Items_In_Treeview(event):
    global total_qty2, total_amount2
    if obj_cls_sal_entry.get_sal_button_clicked() == "insert" or obj_cls_sal_entry.get_sal_button_clicked() == "edit":
        item = tree.selection()
        for i in item:
            total_qty2 = obj_cls_sal_entry.get_sal_tot_qty() - int(tree.item(i, 'values')[9])
            total_amount2 = obj_cls_sal_entry.get_sal_tot_amount() - float(tree.item(i, 'values')[10])
        obj_cls_sal_entry.set_sal_tot_qty(total_qty2)
        obj_cls_sal_entry.set_sal_tot_amount(total_amount2)
        sal_tot_qty_entry_tv.set(total_qty2)
        sal_tot_amount_entry_tv.set(total_amount2)
        tree.delete(item)
        sales_Bill_Amt_Calculate(total_amount2)
        sal_cgst_entry_tv.set(obj_cls_sal_entry.get_sal_cgst())
        sal_sgst_entry_tv.set(obj_cls_sal_entry.get_sal_sgst())
        sal_bill_amt_entry_tv.set(obj_cls_sal_entry.get_sal_bill_amount())
        if len(tree.selection()) == 0:
            child_id = tree.get_children()[0]
            tree.focus(child_id)
            tree.selection_set(child_id)

def item_id_creation(event):
    brand1 = sal_brand_entry_tv.get()
    product1 = sal_product_entry_tv.get()
    design1 = sal_design_name_entry_tv.get()
    color1 = sal_color_entry_tv.get()
    size1 = sal_size_entry_tv.get()
    mrp1 = sal_mrp_entry_tv.get()
    rate1 = sal_rate_entry_tv.get()
    gst1 = sal_gst_entry_tv.get()
    crt_date1 = date.today().strftime("%Y-%m-%d")

    d_mrp = str(sal_mrp_entry_tv.get())
    d_rate = str(sal_rate_entry_tv.get())
    if len(sal_brand_entry_tv.get().strip()) > 0 and len(sal_product_entry_tv.get().strip()) > 0 and \
            len(sal_design_name_entry_tv.get().strip()) > 0 and len(sal_color_entry_tv.get().strip()) > 0 and \
            len(sal_size_entry_tv.get().strip()) > 0 and len(d_mrp.strip()) > 0 and len(d_rate.strip()) > 0:
        Cur.execute("select max(item_id) as dum_id from item_master")
        data = Cur.fetchall()
        for row in data:
            i = row[0]
        i = str(i)
        if i == 'None':
            sal_id_entry_tv.set(1)
            Cur.execute(
                "insert into item_master (brand,product,design,color,size,mrp,rate,gst,crt_date,item_id) "
                "values('{}','{}','{}','{}','{}',{},{},{},'{}',{})"
                .format(brand1, product1, design1, color1, size1, mrp1, rate1, gst1, crt_date1, sal_id_entry_tv.get()))
            Con.commit()
            sal_qty_entry.config(state="normal")
        else:
            sal_id_entry_tv.set(int(i) + 1)
            sal_qty_entry.config(state="normal")
            Cur.execute("select brand, product, design, color, size, mrp, rate, gst, crt_date, item_id from item_master"
                        " where brand='{}' and product ='{}' and design ='{}' and color = '{}' and size = '{}'  "
                        "and mrp = {} and rate = {} and gst = {}"
                        .format(brand1, product1, design1, color1, size1, mrp1, rate1, gst1))
            data1 = Cur.fetchall()
            if not data1:
                Cur.execute("insert into item_master (brand,product,design,color,size,mrp,rate,gst,crt_date,item_id)"
                            " values('{}','{}','{}','{}','{}',{},{},{},'{}',{})"
                            .format(brand1, product1, design1, color1, size1, mrp1, rate1, gst1, crt_date1,
                            sal_id_entry_tv.get()))
                Con.commit()
            else:
                for row2 in data1:
                    dum_data2 = row2[9]

                sal_id_entry_tv.set(dum_data2)
        set_focus_sal_qty()
        form_bottom_label.config(text="Enter Qty        Integer Numbers Only")

    else:
        messagebox.showinfo('', "Enter All Fields")
        form_bottom_label.config(
            text="Enter Brand Name To Create       Maximum Allowed Characters - 25        To List Brand Press [F1]"
                 "        To List ITEMS Press [F2]")
        sal_brand_entry.focus_set()

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
    style1.configure("Treeview.Heading", foreground='orange', background='grey18', font='14')
    style1.configure("Treeview", foreground='black', background='orange', fieldbackground='orange',
                     font=('times new roman', 10))
    style1.map('Treeview', background=[('selected', 'grey28')])

    field_treeview.column("field_name", width=150, minwidth=150, anchor=tk.W)

    field_treeview.heading("field_name", text=obj_cls_sal_entry.get_sal_field_focus(), anchor=tk.W)

    vsb = ttk.Scrollbar(field_form, orient="vertical")
    vsb.configure(command=field_treeview.yview)
    field_treeview.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    field_treeview.pack()

    if obj_cls_sal_entry.get_sal_field_focus() == "Brand":
        Cur.execute(
            "select distinct(brand) from item_master where brand like '" + sal_brand_entry_tv.get() + "%' order by brand")
    elif obj_cls_sal_entry.get_sal_field_focus() == "Product":
        Cur.execute(
            "select distinct(product) from item_master where product like '" + sal_product_entry_tv.get() + "%' order by product")
    elif obj_cls_sal_entry.get_sal_field_focus() == "Design":
        Cur.execute(
            "select distinct(design) from item_master where design like '" + sal_design_name_entry_tv.get() + "%' order by design")
    elif obj_cls_sal_entry.get_sal_field_focus() == "Color":
        Cur.execute(
            "select distinct(color) from item_master where color like '" + sal_color_entry_tv.get() + "%' order by color")
    elif obj_cls_sal_entry.get_sal_field_focus() == "Size":
        Cur.execute(
            "select distinct(size) from item_master where size like '" + sal_size_entry_tv.get() + "%' order by size")

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
        if obj_cls_sal_entry.get_sal_field_focus() == "Brand":
            sal_brand_entry_tv.set(field_treeview.item(row, 'values')[0])
        elif obj_cls_sal_entry.get_sal_field_focus() == "Product":
            sal_product_entry_tv.set(field_treeview.item(row, 'values')[0])
        elif obj_cls_sal_entry.get_sal_field_focus() == "Design":
            sal_design_name_entry_tv.set(field_treeview.item(row, 'values')[0])
        elif obj_cls_sal_entry.get_sal_field_focus() == "Color":
            sal_color_entry_tv.set(field_treeview.item(row, 'values')[0])
        elif obj_cls_sal_entry.get_sal_field_focus() == "Size":
            sal_size_entry_tv.set(field_treeview.item(row, 'values')[0])

    field_form.destroy()
    if obj_cls_sal_entry.get_sal_field_focus() == "Brand":
        sal_product_entry.focus_set()
    elif obj_cls_sal_entry.get_sal_field_focus() == "Product":
        sal_design_name_entry.focus_set()
    elif obj_cls_sal_entry.get_sal_field_focus() == "Design":
        sal_color_entry.focus_set()
    elif obj_cls_sal_entry.get_sal_field_focus() == "Color":
        sal_size_entry.focus_set()
    elif obj_cls_sal_entry.get_sal_field_focus() == "Size":
        sal_mrp_entry.focus_set()

def Close_Field_Treeview(event):
    obj_cls_sal_entry.set_sal_field_focus("")
    field_form.destroy()

def Show_Stock_Balance(event):
    global item_form, item_treeview

    item_form = tk.Toplevel()
    item_form.title('STOCK BALANCE List')
    item_form.resizable(False, False)
    item_form.geometry("640x148+672+300")
    col = ('brand', 'product', 'design', 'color', 'size', 'mrp', 'rate', 'qty', 'id')
    item_treeview = ttk.Treeview(item_form, height=6, show='headings', columns=col)
    item_treeview.pack(fill=tk.X, pady=5)
    style1 = ttk.Style(item_form)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading", foreground='white', background='grey28', font='14')
    style1.configure("Treeview", foreground='black', background='#87CEFA', fieldbackground='#B0E2FF',
                     font=('times new roman', 10))
    style1.map('Treeview', background=[('selected', 'grey28')])

    item_treeview.column("brand", width=80, minwidth=50, anchor=tk.W)
    item_treeview.column("product", width=90, minwidth=50, anchor=tk.W)
    item_treeview.column("design", width=130, minwidth=50, anchor=tk.W)
    item_treeview.column("color", width=70, minwidth=50, anchor=tk.W)
    item_treeview.column("size", width=50, minwidth=50, anchor=tk.W)
    item_treeview.column("mrp", width=60, minwidth=50, anchor=tk.E)
    item_treeview.column("rate", width=60, minwidth=50, anchor=tk.E)
    item_treeview.column("qty", width=40, minwidth=40, anchor=tk.S)
    item_treeview.column("id", width=40, minwidth=40, anchor=tk.E)

    item_treeview.heading("brand", text="BRAND", anchor=tk.W)
    item_treeview.heading("product", text="PRODUCT", anchor=tk.W)
    item_treeview.heading("design", text="DESIGN NAME", anchor=tk.W)
    item_treeview.heading("color", text="COLOR", anchor=tk.W)
    item_treeview.heading("size", text="SIZE", anchor=tk.W)
    item_treeview.heading("mrp", text="MRP", anchor=tk.E)
    item_treeview.heading("rate", text="RATE", anchor=tk.E)
    item_treeview.heading("qty", text="QTY", anchor=tk.S)
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

    Cur.execute("select*from stock_balance where bal_qty > 0 and design like '%" + sal_brand_entry_tv.get() + "%' order by design, brand, product")

    i = 0
    for row in Cur:
        item_treeview.insert('', i, text="", values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[0]))
        i = i + 1

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
        sal_brand_entry_tv.set(item_treeview.item(row, 'values')[0])
        sal_product_entry_tv.set(item_treeview.item(row, 'values')[1])
        sal_design_name_entry_tv.set(item_treeview.item(row, 'values')[2])
        sal_color_entry_tv.set(item_treeview.item(row, 'values')[3])
        sal_size_entry_tv.set(item_treeview.item(row, 'values')[4])
        sal_mrp_entry_tv.set(item_treeview.item(row, 'values')[5])
        sal_rate_entry_tv.set(item_treeview.item(row, 'values')[6])
        sal_qty_entry_tv.set(item_treeview.item(row, 'values')[7])
        sal_id_entry_tv.set(item_treeview.item(row, 'values')[8])

    item_form.destroy()
    if sal_id_entry_tv.get() > 0:
        sal_qty_entry.config(state='normal')
        sal_brand_label.config(text="Brand")
        sal_qty_entry.focus_set()
        sal_qty_entry.selection_range(0, len(str(sal_qty_entry_tv.get())))

def String_To_Date(get_str):
    date_format = datetime.strptime(get_str, "%Y-%m-%d")
    return date_format.strftime("%d-%m-%Y")

def Save_Button_Click(event):
    bill_no1 = sal_bill_no_entry_tv.get()
    bill_date1 = date.today().strftime("%Y-%m-%d")

    cust_name1 = sal_cust_list_combo.get()
    bill_qty1 = sal_tot_qty_entry_tv.get()
    item_total1 = round(sal_tot_amount_entry_tv.get(),2)
    less_amt1 = round(sal_discount_entry_tv.get(),2)
    taxable_amt1 = round(sal_taxable_entry_tv.get(),2)
    cgst_amt1 = round(sal_cgst_entry_tv.get(),2)
    sgst_amt1 = round(sal_sgst_entry_tv.get(),2)
    bill_amt1 = round(sal_bill_amt_entry_tv.get(),0)

    if len(cust_name1.strip()) > 0 and len(bill_no1.strip()) > 0 and bill_qty1 > 0 and less_amt1 >= 0:
        if len(bill_no1.strip()) <= 25 and len(str(less_amt1).strip()) <= 10:
            Cur.execute("select max(bill_no) as bill_nos from sales_master")
            for row in Cur:
                id_no = row[0]

            if id_no == None:
                id_no = 20230001
            else:
                id_no = id_no + 1

            Cur.execute("insert into sales_master (bill_no,bill_date,cust_name,bill_qty,"
                        "item_total,less_amt,cgst_amt,sgst_amt,bill_amt) "
                        "values({},'{}','{}',{},{},{},{},{},{})"
                        .format(bill_no1, bill_date1, cust_name1, bill_qty1,
                                item_total1, less_amt1, cgst_amt1, sgst_amt1, bill_amt1))
            Con.commit()
            k = 0
            for k in tree.get_children():
                Cur.execute("insert into sales_item (bill_no,bill_date,item_id,brand, product, design, color, sizes,"
                            " mrp, rate,item_qty,item_amount) "
                            "values({},'{}',{},'{}','{}', '{}', '{}', '{}', {}, {}, {}, {})"
                            .format(bill_no1, bill_date1, tree.item(k, 'value')[8], tree.item(k,'value')[0],
                            tree.item(k, 'value')[1], tree.item(k, 'value')[2], tree.item(k, 'value')[3],
                            tree.item(k, 'value')[4], tree.item(k, 'value')[5], tree.item(k, 'value')[6],
                            tree.item(k, 'value')[9], tree.item(k, 'value')[10]))
                Con.commit()
                dum_item_id = int(tree.item(k, 'value')[8])
                print('id ',dum_item_id)
                qry2 = "select * from stock_balance where item_id = {}".format(dum_item_id)
                Cur.execute(qry2)
                check_item_id = Cur.fetchall()
                if not check_item_id:
                    pass
                else:
                    for m in check_item_id:
                        dum_tot_qty = int(m[8]) - int(tree.item(k, 'value')[9])
                        dum_tot_amt = float(m[9]) - float(tree.item(k, 'value')[6]) * int(tree.item(k, 'value')[9])
                        qry3 = "update stock_balance set bal_qty = {}, bal_amount = {} where item_id = {}" \
                            .format(dum_tot_qty, dum_tot_amt, dum_item_id)
                        Cur.execute(qry3)
                        Con.commit()

            messagebox.showinfo('', "SALES BILL Added Successfully")
            sales_Form.destroy()
            Design_sales_Form_Load()
        else:
            messagebox.showwarning('', 'Enter Details As Per The Limitations')
    else:
        messagebox.showwarning('', 'Enter Data In All Fields')
        sales_Form.focus_set()
        sal_save_button.focus_set()

def sales_Insert(event):
    global sal_bill_no_entry, sal_bill_date_entry, sal_cust_list_combo, sal_bill_no_entry, sal_bill_date_entry, \
        sal_brand_entry, sal_product_entry, sal_design_name_entry, sal_color_entry, sal_size_entry, \
        sal_mrp_entry, sal_rate_entry, sal_gst_entry, sal_id_entry, sal_qty_entry, sal_amount_entry
    global sal_tot_qty_entry, sal_tot_amount_entry, sal_discount_entry, sal_taxable_entry, sal_cgst_entry, sal_sgst_entry, sal_bill_amt_entry

    global a3, sal_frame3, sal_save_button, sal_brand_label, sal_cancel_button
    global sal_bill_no_entry_tv, sal_bill_date_entry_tv, sal_cust_list_combo_tv, sal_bill_no_entry_tv, sal_bill_date_entry_tv, \
        sal_brand_entry_tv, sal_product_entry_tv, sal_design_name_entry_tv, sal_color_entry_tv, sal_size_entry_tv, \
        sal_mrp_entry_tv, sal_rate_entry_tv, sal_gst_entry_tv, sal_id_entry_tv, sal_qty_entry_tv, sal_amount_entry_tv, \
        sal_tot_qty_entry_tv, sal_tot_amount_entry_tv, sal_discount_entry_tv, sal_taxable_entry_tv, sal_cgst_entry_tv, sal_sgst_entry_tv, \
        sal_bill_amt_entry_tv

    form_top_label.configure(text="S A L E S     I N S E R T")
    obj_cls_sal_entry.set_sal_button_clicked("insert")
    sal_bill_no_entry_tv = tk.IntVar()
    sal_bill_date_entry_tv = tk.StringVar()
    sal_bill_no_entry_tv = tk.StringVar()
    sal_bill_date_entry_tv = tk.StringVar()
    sal_brand_entry_tv = tk.StringVar()
    sal_product_entry_tv = tk.StringVar()
    sal_design_name_entry_tv = tk.StringVar()
    sal_color_entry_tv = tk.StringVar()
    sal_size_entry_tv = tk.StringVar()
    sal_mrp_entry_tv = tk.DoubleVar()
    sal_rate_entry_tv = tk.DoubleVar()
    sal_gst_entry_tv = tk.IntVar()
    sal_id_entry_tv = tk.IntVar()
    sal_qty_entry_tv = tk.IntVar()
    sal_amount_entry_tv = tk.DoubleVar()
    sal_tot_qty_entry_tv = tk.IntVar()
    sal_tot_amount_entry_tv = tk.DoubleVar()
    sal_discount_entry_tv = tk.DoubleVar()
    sal_taxable_entry_tv = tk.DoubleVar()
    sal_cgst_entry_tv = tk.DoubleVar()
    sal_sgst_entry_tv = tk.DoubleVar()
    sal_bill_amt_entry_tv = tk.DoubleVar()

    obj_cls_sal_entry.set_sal_tot_qty(0)
    obj_cls_sal_entry.set_sal_tot_amount(0.00)

    sal_rate_entry_tv.set(0.00)
    sal_id_entry_tv.set('')
    sal_qty_entry_tv.set(0)
    sal_discount_entry_tv.set(0.00)
    sal_taxable_entry_tv.set(0.00)
    sal_cgst_entry_tv.set(0.00)
    sal_sgst_entry_tv.set(0.00)
    sal_bill_amt_entry_tv.set(0.00)

    sal_insert_button.destroy()
    sal_edit_button.destroy()
    sal_delete_button.destroy()
    sal_export_button.destroy()
    sal_quit_button.destroy()

    # *****************************    Frame1 - LABEL & ENTRY BOX SETTINGS - BEGIN     ********************************************
    sal_frame1 = Frame(sales_Form, width=380, height=40, bg='#B0E2FF')
    sal_frame1.place(x=10, y=48)

    sal_bill_no_label = Label(sal_frame1, text="Bill No.", bg='#B0E2FF', font=('bold'))
    sal_bill_no_label.place(x=5, y=10)

    sal_bill_date_label = Label(sal_frame1, text="Date", bg='#B0E2FF', font=('bold'))
    sal_bill_date_label.place(x=200, y=10)

    sal_bill_no_entry = Entry(sal_frame1, textvariable=sal_bill_no_entry_tv)
    sal_bill_no_entry.place(x=75, y=10)
    sal_bill_no_entry.config(state='disable')

    sal_bill_date_entry = Entry(sal_frame1, textvariable=sal_bill_date_entry_tv)
    sal_bill_date_entry.place(x=250, y=10)
    sal_bill_date_entry.config(state='disable')

    Cur.execute("select max(bill_no) as m_bill_no from sales_master")
    data = Cur.fetchall()
    for row in data:
        i = row[0]
    i = str(i)
    if i == 'None':
        sal_bill_no_entry_tv.set(20230001)
    else:
        i = int(i)
        i += 1
        sal_bill_no_entry_tv.set(i)

    sal_bill_date_entry_tv.set(newdate)
    # *****************************   Frame1 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************   Frame2 - LABEL &  ENTRY BOX SETTINGS - BEGIN     ********************************************
    sal_frame2 = Frame(sales_Form, width=380, height=100, bg='#B0E2FF')
    sal_frame2.place(x=10, y=95)

    customer_list_label = Label(sal_frame2, text="Customer List", bg='#B0E2FF', font=('bold'))
    customer_list_label.place(x=5, y=10)

    customer_list = Customer_Name_Fetching()
    sal_cust_list_combo = ttk.Combobox(sal_frame2, value=customer_list, width=40, state='readonly')
    sal_cust_list_combo.set("Cash")
    sal_cust_list_combo.place(x=110, y=10)
    sal_cust_list_combo.bind("<FocusIn>", set_focus_sal_cust_list)
    sal_cust_list_combo.bind("<Return>",  set_focus_sal_brand)
    sal_cust_list_combo.focus_set()

    # *****************************   Frame2 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************   Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    sal_frame3 = LabelFrame(sales_Form, text="ITEM SELECTION", width=640, height=148, bg='#B0E2FF', font=('bold', 10))
    sal_frame3.place(x=650, y=48)

    sal_brand_label = Label(sal_frame3, text="Select Item", font=('bold'), bg='#B0E2FF')
    sal_brand_label.place(x=10, y=0)

    sal_product_label = Label(sal_frame3, text="Product", font=('bold'), bg='#B0E2FF')
    sal_product_label.place(x=10, y=27)

    sal_design_name_label = Label(sal_frame3, text="Design Name", font=('bold'), bg='#B0E2FF')
    sal_design_name_label.place(x=10, y=52)

    sal_color_label = Label(sal_frame3, text="Color", font=('bold'), bg='#B0E2FF')
    sal_color_label.place(x=10, y=77)

    sal_size_label = Label(sal_frame3, text="Size", font=('bold'), bg='#B0E2FF')
    sal_size_label.place(x=10, y=102)

    sal_mrp_label = Label(sal_frame3, text="Mrp", font=('bold'), bg='#B0E2FF')
    sal_mrp_label.place(x=250, y=102)

    sal_qty_label = Label(sal_frame3, text="Qty", font=('bold'), bg='#B0E2FF')
    sal_qty_label.place(x=250, y=0)

    sal_rate_label = Label(sal_frame3, text="Rate", font=('bold'), bg='#B0E2FF')
    sal_rate_label.place(x=250, y=27)

    sal_gst_label = Label(sal_frame3, text="GST", font=('bold'), bg='#B0E2FF')
    sal_gst_label.place(x=250, y=52)

    sal_id_label = Label(sal_frame3, text="ID", font=('bold'), bg='#B0E2FF')
    sal_id_label.place(x=250, y=77)

    sal_amount_label = Label(sal_frame3, text="Amount", font=('bold'), bg='#B0E2FF')
    sal_amount_label.place(x=430, y=0)

    sal_brand_entry = Entry(sal_frame3, text=sal_brand_entry_tv, state="normal")
    sal_brand_entry.place(x=120, y=1)
    sal_brand_entry.bind("<F1>", Show_Stock_Balance)
    sal_brand_entry.bind("<FocusIn>", set_focus_sal_brand)
    sal_brand_entry.bind("<FocusOut>", lost_focus_sal_brand)

    sal_product_entry = Entry(sal_frame3, textvariable=sal_product_entry_tv)
    sal_product_entry.place(x=120, y=30)
    sal_product_entry.config(state="disable")

    sal_design_name_entry = Entry(sal_frame3, textvariable=sal_design_name_entry_tv)
    sal_design_name_entry.place(x=120, y=55)
    sal_design_name_entry.config(state="disable")

    sal_color_entry = Entry(sal_frame3, textvariable=sal_color_entry_tv)
    sal_color_entry.place(x=120, y=80)
    sal_color_entry.config(state="disable")

    sal_size_entry = Entry(sal_frame3, textvariable=sal_size_entry_tv)
    sal_size_entry.place(x=120, y=105)
    sal_size_entry.config(state="disable")

    sal_mrp_entry = Entry(sal_frame3, textvariable=sal_mrp_entry_tv, justify="right")
    sal_mrp_entry.place(x=300, y=105)
    sal_mrp_entry.config(state="disable")

    sal_rate_entry = Entry(sal_frame3, textvariable=sal_rate_entry_tv, justify="right")
    sal_rate_entry.place(x=300, y=30)
    sal_rate_entry.config(state="disable")

    sal_gst_entry = Entry(sal_frame3, state="disable", textvariable=sal_gst_entry_tv, justify='right')
    sal_gst_entry_tv.set(18)
    sal_gst_entry.place(x=300, y=55)

    sal_id_entry = Entry(sal_frame3, state="disable", textvariable=sal_id_entry_tv, justify='right', font=(9), width=5)
    sal_id_entry.place(x=300, y=80)

    sal_qty_entry = Entry(sal_frame3, textvariable=sal_qty_entry_tv,  justify="right", width=5)
    sal_qty_entry.place(x=300, y=1)
    sal_qty_entry.config(state="disable")
    reg = sal_qty_entry.register(Validate_Number)
    sal_qty_entry.config(validate="key", validatecommand=(reg, '%P'))

    sal_qty_entry.bind("<FocusIn>", set_focus_sal_qty1)
    sal_qty_entry.bind("<Return>", Add_sales_Items_In_Treeview)

    sal_amount_entry = Entry(sal_frame3, state="disable", textvariable=sal_amount_entry_tv, justify='right')
    sal_amount_entry.place(x=500, y=0)
    # *****************************   Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - END     ********************************************

    # *****************************     Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    sal_tot_qty_label = Label(sales_Form, text="Total", font=('bold', 12))
    sal_tot_qty_label.place(x=1000, y=420)

    sal_discount_label = Label(sales_Form, text="Discount", font=('bold', 12))
    sal_discount_label.place(x=1000, y=450)

    sal_bill_amt_label = Label(sales_Form, text="Bill Amount", font=('bold', 12))
    sal_bill_amt_label.place(x=1000, y=480)

    sal_taxable_label = Label(sales_Form, text="Taxable", font=('bold', 12))
    sal_taxable_label.place(x=1000, y=510)

    sal_cgst_label = Label(sales_Form, text="CGST @ 9%", font=('bold', 12))
    sal_cgst_label.place(x=1100, y=510)

    sal_sgst_label = Label(sales_Form, text="SGST @ 9%", font=('bold', 12))
    sal_sgst_label.place(x=1200, y=510)

    sal_tot_qty_entry = Entry(sales_Form, font=('bold', 12), width=5, state='disable', textvariable=sal_tot_qty_entry_tv, justify='right')
    sal_tot_qty_entry.place(x=1100, y=420)

    sal_tot_amount_entry = Entry(sales_Form, font=('bold', 12), width=14, state='disable', textvariable=sal_tot_amount_entry_tv, justify='right')
    sal_tot_amount_entry.place(x=1155, y=420)

    sal_discount_entry = Entry(sales_Form, font=('bold', 12), textvariable=sal_discount_entry_tv, justify='right')
    sal_discount_entry.place(x=1100, y=450)
    reg3 = sal_discount_entry.register(Validate_Number2)
    sal_discount_entry.config(validate="key", validatecommand=(reg3, '%P'))
    sal_discount_entry.bind("<Return>", set_focus_save_button)
    sal_discount_entry.bind("<KeyRelease>", sales_Bill_Amt_Calculate2)
    sal_discount_entry.bind("<Tab>", sales_Bill_Amt_Calculate2)
    sal_discount_entry.bind("<FocusIn>", set_focus_sal_discount)
    sal_discount_entry.bind("<FocusOut>", Set_Zero)

    sal_bill_amt_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_bill_amt_entry_tv, justify='right')
    sal_bill_amt_entry.place(x=1100, y=480)

    sal_taxable_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_taxable_entry_tv, justify='right', width=10)
    sal_taxable_entry.place(x=1003, y=540)

    sal_cgst_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_cgst_entry_tv, justify='right', width=10)
    sal_cgst_entry.place(x=1103, y=540)

    sal_sgst_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_sgst_entry_tv, justify='right', width=10)
    sal_sgst_entry.place(x=1203, y=540)

    sal_save_button = Button(sales_Form, text='S A V E', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_save_button.place(x=535, y=520)
    sal_save_button.bind('<Return>', Save_Button_Click)
    sal_save_button.bind("<ButtonRelease>", Save_Button_Click)
    sal_save_button.bind("<FocusIn>", set_focus_save_button)
    sal_save_button.bind("<FocusOut>", focus_out_save_button)

    sal_cancel_button = Button(sales_Form, text='C A N C E L', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_cancel_button.place(x=710, y=520)
    sal_cancel_button.bind("<Return>", Design_sales_Form_Load_destroy2)
    sal_cancel_button.bind("<ButtonRelease>", Design_sales_Form_Load_destroy2)
    sal_cancel_button.bind("<FocusIn>", set_focus_cancel_button)
    sal_cancel_button.bind("<FocusOut>", focus_out_cancel_button)
# *****************************     Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS -  END     ********************************************

def Design_sales_Form_Load_destroy2(event):
    sales_Form.destroy()
    Design_sales_Form_Load()

def Design_sales_Form_Load_destroy(event):
    sales_Form.destroy()

def Update_Button_Click(event):

    bill_no1 = sal_bill_no_entry_tv.get()
    bill_date11 = str(sal_bill_date_entry_tv.get())
    bill_date1 = datetime.strptime(bill_date11, "%d-%m-%Y")
    cust_name1 = sal_cust_list_combo.get()
    bill_qty1 = sal_tot_qty_entry_tv.get()
    item_total1 = round(sal_tot_amount_entry_tv.get(),2)
    taxable_amt1 = round(sal_taxable_entry_tv.get(),2)
    less_amt1 = round(sal_discount_entry_tv.get(),2)
    cgst_amt1 = round(sal_cgst_entry_tv.get(),2)
    sgst_amt1 = round(sal_sgst_entry_tv.get(),2)
    bill_amt1 = round(sal_bill_amt_entry_tv.get(),0)
    if len(cust_name1.strip()) > 0 and len(bill_no1.strip()) > 0 and bill_qty1 > 0 and less_amt1 >= 0:
        if len(bill_no1.strip()) <= 25 and len(str(less_amt1).strip()) <= 10:
            Cur.execute("delete from sales_item where bill_no = {}".format(sal_bill_no_entry_tv.get()))
            Con.commit()

            for row in obj_cls_sal_entry.get_sal_original_data():
                Cur.execute("update stock_balance set bal_qty = bal_qty + {}, bal_amount = bal_amount + {} "
                            "where item_id = {}".format(row[10], row[9] * row[10], row[2]))
                Con.commit()

            Cur.execute("Update sales_master set  cust_name = '{}', bill_qty = {},"
                        " item_total = {}, less_amt = {}, cgst_amt = {}, sgst_amt = {}, bill_amt = {} where bill_no = {}"
                        .format(cust_name1, bill_qty1, item_total1, less_amt1, cgst_amt1, sgst_amt1, bill_amt1, bill_no1))
            Con.commit()

            k = 0
            for k in tree.get_children():
                Cur.execute("insert into sales_item (bill_no,bill_date,item_id,brand, product, design, color, sizes, "
                            "mrp, rate, item_qty, item_amount) "
                            "values({},'{}',{},'{}','{}', '{}', '{}', '{}', {}, {}, {}, {})"
                            .format(bill_no1, bill_date1, tree.item(k, 'value')[8], tree.item(k, 'value')[0],
                            tree.item(k, 'value')[1], tree.item(k, 'value')[2], tree.item(k, 'value')[3],
                            tree.item(k, 'value')[4], tree.item(k, 'value')[5], tree.item(k, 'value')[6],
                            tree.item(k, 'value')[9], tree.item(k, 'value')[10]))
                Con.commit()
                dum_item_id = int(tree.item(k, 'value')[8])
                qry2 = "select * from stock_balance where item_id = {}".format(dum_item_id)
                Cur.execute(qry2)
                check_item_id = Cur.fetchall()
                if not check_item_id:
                    pass
                else:
                    for m in check_item_id:
                        dum_tot_qty = int(m[8]) - int(tree.item(k, 'value')[9])
                        dum_tot_amt = float(m[9]) - float(tree.item(k, 'value')[6]) * int(tree.item(k, 'value')[9])
                        print(dum_tot_qty)
                        print(dum_tot_amt)
                        qry3 = "update stock_balance set bal_qty = {}, bal_amount = {} where item_id = {}" \
                            .format(dum_tot_qty, dum_tot_amt, dum_item_id)
                        Cur.execute(qry3)
                        Con.commit()

            messagebox.showinfo('', "SALES BILL Updated Successfully")
            sales_Form.destroy()
            Design_sales_Form_Load()
        else:
            messagebox.showwarning('', 'Enter Details As Per The Limitations')
    else:
        messagebox.showwarning('', 'Enter Data In All Fields')
        sales_Form.focus_set()
        sal_save_button.focus_set()


def sales_Edit(event):
    global sal_bill_no_entry, sal_bill_date_entry, sal_cust_list_combo, sal_bill_no_entry, sal_bill_date_entry, \
        sal_brand_entry, sal_product_entry, sal_design_name_entry, sal_color_entry, sal_size_entry, \
        sal_mrp_entry, sal_rate_entry, sal_gst_entry, sal_id_entry, sal_qty_entry, sal_amount_entry
    global sal_tot_qty_entry, sal_tot_amount_entry, sal_discount_entry, sal_taxable_entry, sal_cgst_entry, sal_sgst_entry, sal_bill_amt_entry

    global a3, sal_frame3, sal_save_button, sal_brand_label, sal_cancel_button
    global sal_bill_no_entry_tv, sal_bill_date_entry_tv, sal_cust_list_combo_tv, sal_bill_no_entry_tv, sal_bill_date_entry_tv, \
        sal_brand_entry_tv, sal_product_entry_tv, sal_design_name_entry_tv, sal_color_entry_tv, sal_size_entry_tv, \
        sal_mrp_entry_tv, sal_rate_entry_tv, sal_gst_entry_tv, sal_id_entry_tv, sal_qty_entry_tv, sal_amount_entry_tv, \
        sal_tot_qty_entry_tv, sal_tot_amount_entry_tv, sal_discount_entry_tv, sal_taxable_entry_tv, sal_cgst_entry_tv, sal_sgst_entry_tv, \
        sal_bill_amt_entry_tv

    form_top_label.configure(text="S A L E S      E D I T")
    obj_cls_sal_entry.set_sal_button_clicked("edit")
    sal_bill_no_entry_tv = tk.IntVar()
    sal_bill_date_entry_tv = tk.StringVar()
    sal_bill_no_entry_tv = tk.StringVar()
    sal_bill_date_entry_tv = tk.StringVar()
    sal_brand_entry_tv = tk.StringVar()
    sal_product_entry_tv = tk.StringVar()
    sal_design_name_entry_tv = tk.StringVar()
    sal_color_entry_tv = tk.StringVar()
    sal_size_entry_tv = tk.StringVar()
    sal_mrp_entry_tv = tk.DoubleVar()
    sal_rate_entry_tv = tk.DoubleVar()
    sal_gst_entry_tv = tk.IntVar()
    sal_id_entry_tv = tk.IntVar()
    sal_qty_entry_tv = tk.IntVar()
    sal_amount_entry_tv = tk.DoubleVar()
    sal_tot_qty_entry_tv = tk.IntVar()
    sal_tot_amount_entry_tv = tk.DoubleVar()
    sal_discount_entry_tv = tk.DoubleVar()
    sal_taxable_entry_tv = tk.DoubleVar()
    sal_cgst_entry_tv = tk.DoubleVar()
    sal_sgst_entry_tv = tk.DoubleVar()
    sal_bill_amt_entry_tv = tk.DoubleVar()

    sal_mrp_entry_tv.set(0.00)
    sal_rate_entry_tv.set(0.00)
    sal_id_entry_tv.set('')
    sal_qty_entry_tv.set(0)
    sal_discount_entry_tv.set(0.00)
    sal_taxable_entry_tv.set(0.00)
    sal_cgst_entry_tv.set(0.00)
    sal_sgst_entry_tv.set(0.00)
    sal_bill_amt_entry_tv.set(0.00)

    sal_insert_button.destroy()
    sal_edit_button.destroy()
    sal_delete_button.destroy()
    sal_export_button.destroy()
    sal_quit_button.destroy()

    # *****************************   EDIT - Frame1 - LABEL & ENTRY BOX SETTINGS - BEGIN     ********************************************
    sal_frame1 = Frame(sales_Form, width=380, height=40, bg='#B0E2FF')
    sal_frame1.place(x=10, y=48)

    sal_bill_no_label = Label(sal_frame1, text="Bill No.", bg='#B0E2FF', font=('bold'))
    sal_bill_no_label.place(x=5, y=10)

    sal_bill_date_label = Label(sal_frame1, text="Date", bg='#B0E2FF', font=('bold'))
    sal_bill_date_label.place(x=200, y=10)

    sal_bill_no_entry = Entry(sal_frame1, textvariable=sal_bill_no_entry_tv)
    sal_bill_no_entry.place(x=75, y=10)
    sal_bill_no_entry.config(state='normal')
    sal_bill_no_entry_tv.set("")
    sal_bill_no_entry.focus_set()
    sal_bill_no_entry.bind("<FocusIn>", set_focus_sal_bill_no)
    sal_bill_no_entry.bind("<FocusOut>", lost_focus_sal_bill_no)
    sal_bill_no_entry.bind("<F1>", Show_sales_Master)

    sal_bill_date_entry = Entry(sal_frame1, textvariable=sal_bill_date_entry_tv)
    sal_bill_date_entry.place(x=250, y=10)
    sal_bill_date_entry.config(state='disable')

    # *****************************  EDIT - Frame1 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************  EDIT - Frame2 - LABEL &  ENTRY BOX SETTINGS - BEGIN     ********************************************
    sal_frame2 = Frame(sales_Form, width=380, height=100, bg='#B0E2FF')
    sal_frame2.place(x=10, y=95)

    customer_list_label = Label(sal_frame2, text="Customer List", bg='#B0E2FF', font=('bold'))
    customer_list_label.place(x=5, y=10)



    customer_list = Customer_Name_Fetching()
    sal_cust_list_combo = ttk.Combobox(sal_frame2, value=customer_list, width=40, state='disable')
    sal_cust_list_combo.set('Cash')
    sal_cust_list_combo.place(x=110, y=10)
    sal_cust_list_combo.bind("<FocusIn>", set_focus_sal_cust_list)
    sal_cust_list_combo.bind("<Return>", set_focus_sal_brand)



    # *****************************   EDIT - Frame2 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************   EDIT - Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    sal_frame3 = LabelFrame(sales_Form, text="ITEM SELECTION", width=640, height=148, bg='#B0E2FF', font=('bold', 10))
    sal_frame3.place(x=650, y=48)

    sal_brand_label = Label(sal_frame3, text="Select Item", font=('bold'), bg='#B0E2FF')
    sal_brand_label.place(x=10, y=0)

    sal_product_label = Label(sal_frame3, text="Product", font=('bold'), bg='#B0E2FF')
    sal_product_label.place(x=10, y=27)

    sal_design_name_label = Label(sal_frame3, text="Design Name", font=('bold'), bg='#B0E2FF')
    sal_design_name_label.place(x=10, y=52)

    sal_color_label = Label(sal_frame3, text="Color", font=('bold'), bg='#B0E2FF')
    sal_color_label.place(x=10, y=77)

    sal_size_label = Label(sal_frame3, text="Size", font=('bold'), bg='#B0E2FF')
    sal_size_label.place(x=10, y=102)

    sal_mrp_label = Label(sal_frame3, text="Mrp", font=('bold'), bg='#B0E2FF')
    sal_mrp_label.place(x=250, y=102)

    sal_qty_label = Label(sal_frame3, text="Qty", font=('bold'), bg='#B0E2FF')
    sal_qty_label.place(x=250, y=0)

    sal_rate_label = Label(sal_frame3, text="Rate", font=('bold'), bg='#B0E2FF')
    sal_rate_label.place(x=250, y=27)

    sal_gst_label = Label(sal_frame3, text="GST", font=('bold'), bg='#B0E2FF')
    sal_gst_label.place(x=250, y=52)

    sal_id_label = Label(sal_frame3, text="ID", font=('bold'), bg='#B0E2FF')
    sal_id_label.place(x=250, y=77)

    sal_amount_label = Label(sal_frame3, text="Amount", font=('bold'), bg='#B0E2FF')
    sal_amount_label.place(x=430, y=0)

    sal_brand_entry = Entry(sal_frame3, textvariable=sal_brand_entry_tv)
    sal_brand_entry.place(x=120, y=1)
    sal_brand_entry.config(state="disable")
    sal_brand_entry.bind("<F1>", Show_Stock_Balance)
    sal_brand_entry.bind("<FocusIn>", set_focus_sal_brand)
    sal_brand_entry.bind("<FocusOut>", lost_focus_sal_brand)

    sal_product_entry = Entry(sal_frame3, textvariable=sal_product_entry_tv)
    sal_product_entry.place(x=120, y=30)
    sal_product_entry.config(state="disable")

    sal_design_name_entry = Entry(sal_frame3, textvariable=sal_design_name_entry_tv)
    sal_design_name_entry.place(x=120, y=55)
    sal_design_name_entry.config(state="disable")

    sal_color_entry = Entry(sal_frame3, textvariable=sal_color_entry_tv)
    sal_color_entry.place(x=120, y=80)
    sal_color_entry.config(state="disable")

    sal_size_entry = Entry(sal_frame3, textvariable=sal_size_entry_tv)
    sal_size_entry.place(x=120, y=105)
    sal_size_entry.config(state="disable")

    sal_mrp_entry = Entry(sal_frame3, textvariable=sal_mrp_entry_tv, justify='right')
    sal_mrp_entry.place(x=300, y=105)
    sal_mrp_entry.config(state="disable")

    sal_rate_entry = Entry(sal_frame3, textvariable=sal_rate_entry_tv, justify='right')
    sal_rate_entry.place(x=300, y=30)
    sal_rate_entry.config(state="disable")

    sal_gst_entry = Entry(sal_frame3, state="disable", textvariable=sal_gst_entry_tv, justify='right')
    sal_gst_entry_tv.set(18)
    sal_gst_entry.place(x=300, y=55)

    sal_id_entry = Entry(sal_frame3, state="disable", textvariable=sal_id_entry_tv, justify='right', font=(9), width=5)
    sal_id_entry.place(x=300, y=80)

    sal_qty_entry = Entry(sal_frame3, textvariable=sal_qty_entry_tv, justify='right', width=5)
    sal_qty_entry.place(x=300, y=1)
    sal_qty_entry.config(width=5, state="disable")
    reg = sal_qty_entry.register(Validate_Number)
    sal_qty_entry.config(validate="key", validatecommand=(reg, '%P'))

    sal_qty_entry.bind("<FocusIn>", set_focus_sal_qty1)
    sal_qty_entry.bind("<Return>", Add_sales_Items_In_Treeview)

    sal_amount_entry = Entry(sal_frame3, state="disable", textvariable=sal_amount_entry_tv, justify='right')
    sal_amount_entry.place(x=500, y=0)
    # *****************************   EDIT - Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - END     ********************************************

    # *****************************     EDIT - Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    sal_tot_qty_label = Label(sales_Form, text="Total", font=('bold', 12))
    sal_tot_qty_label.place(x=1000, y=420)

    sal_discount_label = Label(sales_Form, text="Discount", font=('bold', 12))
    sal_discount_label.place(x=1000, y=450)

    sal_bill_amt_label = Label(sales_Form, text="Bill Amount", font=('bold', 12))
    sal_bill_amt_label.place(x=1000, y=480)

    sal_taxable_label = Label(sales_Form, text="Taxable", font=('bold', 12))
    sal_taxable_label.place(x=1000, y=510)

    sal_cgst_label = Label(sales_Form, text="CGST @ 9%", font=('bold', 12))
    sal_cgst_label.place(x=1100, y=510)

    sal_sgst_label = Label(sales_Form, text="SGST @ 9%", font=('bold', 12))
    sal_sgst_label.place(x=1200, y=540)

    sal_tot_qty_entry = Entry(sales_Form, font=('bold', 12), width=5, state='disable',
                              textvariable=sal_tot_qty_entry_tv, justify='right')
    sal_tot_qty_entry.place(x=1100, y=420)

    sal_tot_amount_entry = Entry(sales_Form, font=('bold', 12), width=14, state='disable',
                                 textvariable=sal_tot_amount_entry_tv, justify='right')
    sal_tot_amount_entry.place(x=1155, y=420)

    sal_discount_entry = Entry(sales_Form, font=('bold', 12), textvariable=sal_discount_entry_tv, justify='right')
    sal_discount_entry.place(x=1100, y=450)
    sal_discount_entry.config(state="disable")
    reg3 = sal_discount_entry.register(Validate_Number2)
    sal_discount_entry.config(validate="key", validatecommand=(reg3, '%P'))
    sal_discount_entry.bind("<Return>", set_focus_save_button)
    sal_discount_entry.bind("<KeyRelease>", sales_Bill_Amt_Calculate2)
    sal_discount_entry.bind("<Tab>", sales_Bill_Amt_Calculate2)
    sal_discount_entry.bind("<FocusIn>", set_focus_sal_discount)
    sal_discount_entry.bind("<FocusOut>", Set_Zero)

    sal_bill_amt_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_bill_amt_entry_tv, justify='right')
    sal_bill_amt_entry.place(x=1100, y=480)

    sal_taxable_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_taxable_entry_tv, justify='right', width=10)
    sal_taxable_entry.place(x=1003, y=540)

    sal_cgst_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_cgst_entry_tv, justify='right', width=10)
    sal_cgst_entry.place(x=1103, y=540)

    sal_sgst_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_sgst_entry_tv, justify='right', width=10)
    sal_sgst_entry.place(x=1203, y=540)


    sal_save_button = Button(sales_Form, text='U P D A T E', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_save_button.place(x=535, y=520)
    sal_save_button.bind('<Return>', Update_Button_Click)
    sal_save_button.bind("<ButtonRelease>", Update_Button_Click)
    sal_save_button.bind("<FocusIn>", set_focus_update_button)
    sal_save_button.bind("<FocusOut>", focus_out_update_button)

    sal_cancel_button = Button(sales_Form, text='C A N C E L', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_cancel_button.place(x=710, y=520)
    sal_cancel_button.bind("<Return>", Design_sales_Form_Load_destroy2)
    sal_cancel_button.bind("<ButtonRelease>", Design_sales_Form_Load_destroy2)
    sal_cancel_button.bind("<FocusIn>", set_focus_cancel_button)
    sal_cancel_button.bind("<FocusOut>", focus_out_cancel_button)


# *****************************     EDIT - Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS -  END     ********************************************


def sales_Delete(event):
    global sal_bill_no_entry, sal_bill_date_entry, sal_cust_list_combo, sal_bill_no_entry, sal_bill_date_entry, \
        sal_brand_entry, sal_product_entry, sal_design_name_entry, sal_color_entry, sal_size_entry, \
        sal_mrp_entry, sal_rate_entry, sal_gst_entry, sal_id_entry, sal_qty_entry, sal_amount_entry
    global sal_tot_qty_entry, sal_tot_amount_entry, sal_discount_entry, sal_taxable_entry, sal_cgst_entry, sal_sgst_entry, sal_bill_amt_entry

    global a3, sal_frame3, sal_delete_button, sal_cancel_button
    global sal_bill_no_entry_tv, sal_bill_date_entry_tv, sal_cust_list_combo_tv, sal_bill_no_entry_tv, sal_bill_date_entry_tv, \
        sal_brand_entry_tv, sal_product_entry_tv, sal_design_name_entry_tv, sal_color_entry_tv, sal_size_entry_tv, \
        sal_mrp_entry_tv, sal_rate_entry_tv, sal_gst_entry_tv, sal_id_entry_tv, sal_qty_entry_tv, sal_amount_entry_tv, \
        sal_tot_qty_entry_tv, sal_tot_amount_entry_tv, sal_discount_entry_tv, sal_taxable_entry_tv, sal_cgst_entry_tv, sal_sgst_entry_tv, \
        sal_bill_amt_entry_tv

    form_top_label.configure(text="S A L E S      D E L E T E")
    obj_cls_sal_entry.set_sal_button_clicked("delete")
    sal_bill_no_entry_tv = tk.IntVar()
    sal_bill_date_entry_tv = tk.StringVar()
    sal_bill_no_entry_tv = tk.StringVar()
    sal_bill_date_entry_tv = tk.StringVar()
    sal_brand_entry_tv = tk.StringVar()
    sal_product_entry_tv = tk.StringVar()
    sal_design_name_entry_tv = tk.StringVar()
    sal_color_entry_tv = tk.StringVar()
    sal_size_entry_tv = tk.StringVar()
    sal_mrp_entry_tv = tk.DoubleVar()
    sal_rate_entry_tv = tk.DoubleVar()
    sal_gst_entry_tv = tk.IntVar()
    sal_id_entry_tv = tk.IntVar()
    sal_qty_entry_tv = tk.IntVar()
    sal_amount_entry_tv = tk.DoubleVar()
    sal_tot_qty_entry_tv = tk.IntVar()
    sal_tot_amount_entry_tv = tk.DoubleVar()
    sal_discount_entry_tv = tk.DoubleVar()
    sal_taxable_entry_tv = tk.DoubleVar()
    sal_cgst_entry_tv = tk.DoubleVar()
    sal_sgst_entry_tv = tk.DoubleVar()
    sal_bill_amt_entry_tv = tk.DoubleVar()

    sal_mrp_entry_tv.set(0.00)
    sal_rate_entry_tv.set(0.00)
    sal_id_entry_tv.set('')
    sal_qty_entry_tv.set(0)
    sal_discount_entry_tv.set(0.00)
    sal_taxable_entry_tv.set(0.00)
    sal_cgst_entry_tv.set(0.00)
    sal_sgst_entry_tv.set(0.00)
    sal_bill_amt_entry_tv.set(0.00)

    sal_insert_button.destroy()
    sal_edit_button.destroy()
    sal_delete_button.destroy()
    sal_export_button.destroy()
    sal_quit_button.destroy()

    # *****************************   DELETE - Frame1 - LABEL & ENTRY BOX SETTINGS - BEGIN     ********************************************
    sal_frame1 = Frame(sales_Form, width=380, height=40, bg='#B0E2FF')
    sal_frame1.place(x=10, y=48)

    sal_bill_no_label = Label(sal_frame1, text="Bill No.", bg='#B0E2FF', font=('bold'))
    sal_bill_no_label.place(x=5, y=10)

    sal_bill_date_label = Label(sal_frame1, text="Date", bg='#B0E2FF', font=('bold'))
    sal_bill_date_label.place(x=200, y=10)

    sal_bill_no_entry = Entry(sal_frame1, textvariable=sal_bill_no_entry_tv)
    sal_bill_no_entry.place(x=75, y=10)
    sal_bill_no_entry.config(state='normal')
    sal_bill_no_entry_tv.set("")
    sal_bill_no_entry.bind("<F1>", Show_sales_Master)
    sal_bill_no_entry.bind("<FocusIn>", set_focus_sal_bill_no)
    sal_bill_no_entry.bind("<FocusOut>", lost_focus_sal_bill_no)
    sal_bill_no_entry.focus_set()

    sal_bill_date_entry = Entry(sal_frame1, textvariable=sal_bill_date_entry_tv)
    sal_bill_date_entry.place(x=250, y=10)
    sal_bill_date_entry.config(state='disable')

    # *****************************  DELETE - Frame1 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************  DELETE - Frame2 - LABEL &  ENTRY BOX SETTINGS - BEGIN     ********************************************
    sal_frame2 = Frame(sales_Form, width=380, height=100, bg='#B0E2FF')
    sal_frame2.place(x=10, y=95)

    customer_list_label = Label(sal_frame2, text="Customer List", bg='#B0E2FF', font=('bold'))
    customer_list_label.place(x=5, y=10)



    customer_list = Customer_Name_Fetching()
    sal_cust_list_combo = ttk.Combobox(sal_frame2, value=customer_list, width=40, state='disable')
    sal_cust_list_combo.set('')
    sal_cust_list_combo.place(x=110, y=10)
    sal_cust_list_combo.bind("<Return>", set_focus_sal_bill_no)



    # *****************************   DELETE - Frame2 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************   DELETE - Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    sal_frame3 = LabelFrame(sales_Form, text="ITEM SELECTION", width=640, height=148, bg='#B0E2FF', font=('bold', 10))
    sal_frame3.place(x=650, y=48)

    sal_brand_label = Label(sal_frame3, text="Select Item", font=('bold'), bg='#B0E2FF')
    sal_brand_label.place(x=10, y=0)

    sal_product_label = Label(sal_frame3, text="Product", font=('bold'), bg='#B0E2FF')
    sal_product_label.place(x=10, y=27)

    sal_design_name_label = Label(sal_frame3, text="Design Name", font=('bold'), bg='#B0E2FF')
    sal_design_name_label.place(x=10, y=52)

    sal_color_label = Label(sal_frame3, text="Color", font=('bold'), bg='#B0E2FF')
    sal_color_label.place(x=10, y=77)

    sal_size_label = Label(sal_frame3, text="Size", font=('bold'), bg='#B0E2FF')
    sal_size_label.place(x=10, y=102)

    sal_mrp_label = Label(sal_frame3, text="Mrp", font=('bold'), bg='#B0E2FF')
    sal_mrp_label.place(x=250, y=102)

    sal_qty_label = Label(sal_frame3, text="Qty", font=('bold'), bg='#B0E2FF')
    sal_qty_label.place(x=250, y=0)

    sal_rate_label = Label(sal_frame3, text="Rate", font=('bold'), bg='#B0E2FF')
    sal_rate_label.place(x=250, y=27)

    sal_gst_label = Label(sal_frame3, text="GST", font=('bold'), bg='#B0E2FF')
    sal_gst_label.place(x=250, y=52)

    sal_id_label = Label(sal_frame3, text="ID", font=('bold'), bg='#B0E2FF')
    sal_id_label.place(x=250, y=77)

    sal_amount_label = Label(sal_frame3, text="Amount", font=('bold'), bg='#B0E2FF')
    sal_amount_label.place(x=430, y=0)

    sal_brand_entry = Entry(sal_frame3, textvariable=sal_brand_entry_tv)
    sal_brand_entry.place(x=120, y=1)
    sal_brand_entry.config(state="disable")

    sal_product_entry = Entry(sal_frame3, textvariable=sal_product_entry_tv)
    sal_product_entry.place(x=120, y=30)
    sal_product_entry.config(state="disable")

    sal_design_name_entry = Entry(sal_frame3, textvariable=sal_design_name_entry_tv)
    sal_design_name_entry.place(x=120, y=55)
    sal_design_name_entry.config(state="disable")

    sal_color_entry = Entry(sal_frame3, textvariable=sal_color_entry_tv)
    sal_color_entry.place(x=120, y=80)
    sal_color_entry.config(state="disable")

    sal_size_entry = Entry(sal_frame3, textvariable=sal_size_entry_tv)
    sal_size_entry.place(x=120, y=105)
    sal_size_entry.config(state="disable")

    sal_mrp_entry = Entry(sal_frame3, textvariable=sal_mrp_entry_tv, justify='right')
    sal_mrp_entry.place(x=300, y=105)
    sal_mrp_entry.config(state="disable")

    sal_rate_entry = Entry(sal_frame3, textvariable=sal_rate_entry_tv, justify='right')
    sal_rate_entry.place(x=300, y=30)
    sal_rate_entry.config(state="disable")

    sal_gst_entry = Entry(sal_frame3, state="disable", textvariable=sal_gst_entry_tv, justify='right')
    sal_gst_entry_tv.set(18)
    sal_gst_entry.place(x=300, y=55)

    sal_id_entry = Entry(sal_frame3, state="disable", textvariable=sal_id_entry_tv, justify='right', font=(9), width=5)
    sal_id_entry.place(x=300, y=80)

    sal_qty_entry = Entry(sal_frame3, textvariable=sal_qty_entry_tv, justify='right', width=5)
    sal_qty_entry.place(x=300, y=11)
    sal_qty_entry.config(width=5, state="disable")

    sal_amount_entry = Entry(sal_frame3, state="disable", textvariable=sal_amount_entry_tv, justify='right')
    sal_amount_entry.place(x=500, y=0)
    # *****************************   DELETE - Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - END     ********************************************

    # *****************************     DELETE - Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    sal_tot_qty_label = Label(sales_Form, text="Total", font=('bold', 12))
    sal_tot_qty_label.place(x=1000, y=420)

    sal_discount_label = Label(sales_Form, text="Discount", font=('bold', 12))
    sal_discount_label.place(x=1000, y=450)

    sal_bill_amt_label = Label(sales_Form, text="Bill Amount", font=('bold', 12))
    sal_bill_amt_label.place(x=1000, y=480)

    sal_taxable_label = Label(sales_Form, text="Taxable", font=('bold', 12))
    sal_taxable_label.place(x=1000, y=510)

    sal_cgst_label = Label(sales_Form, text="CGST @ 9%", font=('bold', 12))
    sal_cgst_label.place(x=1100, y=510)

    sal_sgst_label = Label(sales_Form, text="SGST @ 9%", font=('bold', 12))
    sal_sgst_label.place(x=1200, y=510)


    sal_tot_qty_entry = Entry(sales_Form, font=('bold', 12), width=5, state='disable',
                              textvariable=sal_tot_qty_entry_tv, justify='right')
    sal_tot_qty_entry.place(x=1100, y=420)

    sal_tot_amount_entry = Entry(sales_Form, font=('bold', 12), width=14, state='disable',
                                 textvariable=sal_tot_amount_entry_tv, justify='right')
    sal_tot_amount_entry.place(x=1155, y=420)

    sal_discount_entry = Entry(sales_Form, font=('bold', 12), textvariable=sal_discount_entry_tv, justify='right')
    sal_discount_entry.place(x=1100, y=450)
    sal_discount_entry.config(state="disable")

    sal_bill_amt_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_bill_amt_entry_tv,
                               justify='right')
    sal_bill_amt_entry.place(x=1100, y=480)

    sal_taxable_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_taxable_entry_tv, justify='right', width=10)
    sal_taxable_entry.place(x=1003, y=540)

    sal_cgst_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_cgst_entry_tv, justify='right', width=10)
    sal_cgst_entry.place(x=1103, y=540)

    sal_sgst_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_sgst_entry_tv, justify='right', width=10)
    sal_sgst_entry.place(x=1203, y=540)

    sal_delete_button = Button(sales_Form, text='D E L E T E', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_delete_button.place(x=535, y=520)
    sal_delete_button.bind('<Return>', Delete_Button_Click)
    sal_delete_button.bind("<ButtonRelease>", Delete_Button_Click)
    sal_delete_button.bind("<FocusIn>", set_focus_delete2_button)
    sal_delete_button.bind("<FocusOut>", focus_out_delete2_button)

    sal_cancel_button = Button(sales_Form, text='C A N C E L', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_cancel_button.place(x=710, y=520)
    sal_cancel_button.bind("<Return>", Design_sales_Form_Load_destroy2)
    sal_cancel_button.bind("<ButtonRelease>", Design_sales_Form_Load_destroy2)
    sal_cancel_button.bind("<FocusIn>", set_focus_cancel_button)
    sal_cancel_button.bind("<FocusOut>", focus_out_cancel_button)


# *****************************     DELETE - Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS -  END     ********************************************

def Delete_Button_Click(event):
    bill_no1 = str(sal_bill_no_entry_tv.get())
    delete_confirm = messagebox.askquestion("", "Do You Want To Delete All Items Of This Bill No. " + bill_no1)
    if delete_confirm == "yes":
        Cur.execute("delete from sales_item where bill_no = {}".format(sal_bill_no_entry_tv.get()))
        Con.commit()
        Cur.execute("delete from sales_master where bill_no = {}".format(sal_bill_no_entry_tv.get()))
        Con.commit()

        for row in obj_cls_sal_entry.get_sal_original_data():#orginal data is from sales_item Table
            Cur.execute(
                "update stock_balance set bal_qty = bal_qty + {}, bal_amount = bal_amount + {} where item_id = {}"
                    .format(row[10], row[11], row[2]))
            Con.commit()
        messagebox.showinfo('', "SALES BILL No. " + bill_no1 + " Deleted Successfully")
        sales_Form.destroy()
        Design_sales_Form_Load()
    else:
        sales_Form.focus_set()


def Show_sales_Master(event):
    global sal_mas_form, sal_mas_treeview

    sal_mas_form = tk.Toplevel()
    sal_mas_form.title('SALES ENTRY List')
    sal_mas_form.geometry("1200x200+100+200")
    sal_mas_form.resizable(False, False)
    col = ('bill_no', 'bill_date', 'cust_name','bill_qty', 'item_total', 'less_amt', 'cgst_amt', 'sgst_amt', 'bill_amt')
    sal_mas_treeview = ttk.Treeview(sal_mas_form, height=8, show='headings', columns=col)
    sal_mas_treeview.pack(fill=tk.X, pady=5)
    style1 = ttk.Style(sal_mas_form)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading", foreground='white', background='grey28', font='14')
    style1.configure("Treeview", foreground='black', background='#87CEFA', fieldbackground='#B0E2FF',
                     font=('times new roman', 10))
    style1.map('Treeview', background=[('selected', 'grey28')])

    sal_mas_treeview.column("bill_no", width=80, minwidth=50, anchor=tk.W)
    sal_mas_treeview.column("bill_date", width=90, minwidth=50, anchor=tk.W)
    sal_mas_treeview.column("cust_name", width=200, minwidth=50, anchor=tk.W)
    sal_mas_treeview.column("bill_qty", width=60, minwidth=50, anchor=tk.E)
    sal_mas_treeview.column("item_total", width=100, minwidth=50, anchor=tk.E)
    sal_mas_treeview.column("less_amt", width=100, minwidth=40, anchor=tk.E)
    sal_mas_treeview.column("cgst_amt", width=120, minwidth=50, anchor=tk.E)
    sal_mas_treeview.column("sgst_amt", width=120, minwidth=50, anchor=tk.E)
    sal_mas_treeview.column("bill_amt", width=120, minwidth=50, anchor=tk.E)

    sal_mas_treeview.heading("bill_no", text="Bill No.", anchor=tk.W)
    sal_mas_treeview.heading("bill_date", text="Bill Date", anchor=tk.W)
    sal_mas_treeview.heading("cust_name", text="Customer Name", anchor=tk.W)
    sal_mas_treeview.heading("bill_qty", text="Bill Qty", anchor=tk.E)
    sal_mas_treeview.heading("item_total", text="Item Total", anchor=tk.E)
    sal_mas_treeview.heading("less_amt", text="Less Amount", anchor=tk.E)
    sal_mas_treeview.heading("cgst_amt", text="CGST Amount", anchor=tk.E)
    sal_mas_treeview.heading("sgst_amt", text="SGST Amount", anchor=tk.E)
    sal_mas_treeview.heading("bill_amt", text="Bill Amount", anchor=tk.E)

    vsb = ttk.Scrollbar(sal_mas_form, orient="vertical")
    vsb.configure(command=sal_mas_treeview.yview)
    sal_mas_treeview.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(sal_mas_form, orient="horizontal")
    hsb.configure(command=sal_mas_treeview.xview)
    sal_mas_treeview.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)
    sal_mas_treeview.pack()

    Cur.execute("select*from sales_master  where bill_no like '%" + str(sal_bill_no_entry_tv.get()) + "%' order by bill_no desc")
    i = 0
    for row in Cur:
        sal_mas_treeview.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        i = i + 1

    sal_mas_treeview.focus_set()

    sal_mas_treeview.bind("<Double-1>", Select_Bill_No)
    sal_mas_treeview.bind("<Return>", Select_Bill_No)
    sal_mas_treeview.bind("<Escape>", Close_sal_Mas_Treeview)

    child_id = sal_mas_treeview.get_children()[0]
    sal_mas_treeview.focus(child_id)
    sal_mas_treeview.selection_set(child_id)

    # *****************************   Frame4 - TREEVIEW SETTINGS - END     ********************************************


def Select_Bill_No(event):
    Bill_No_Selected = sal_mas_treeview.selection()
    for row in Bill_No_Selected:
        sal_bill_no_entry_tv.set(sal_mas_treeview.item(row, 'values')[0])
        bill_date1 = sal_mas_treeview.item(row, 'values')[1]
        sal_bill_date_entry_tv.set(String_To_Date(bill_date1))
        sal_cust_list_combo.set(sal_mas_treeview.item(row, 'values')[2])
        sal_tot_qty_entry_tv.set(sal_mas_treeview.item(row, 'values')[3])
        obj_cls_sal_entry.set_sal_tot_qty(sal_tot_qty_entry_tv.get())
        sal_tot_amount_entry_tv.set(sal_mas_treeview.item(row, 'values')[4])
        obj_cls_sal_entry.set_sal_tot_amount(sal_tot_amount_entry_tv.get())
        sal_discount_entry_tv.set(sal_mas_treeview.item(row, 'values')[5])
        dum_taxable = (float(sal_mas_treeview.item(row,'value')[6])/9)*100
        sal_taxable_entry_tv.set(round(dum_taxable,2))
        sal_cgst_entry_tv.set(sal_mas_treeview.item(row, 'values')[6])
        sal_sgst_entry_tv.set(sal_mas_treeview.item(row, 'values')[7])
        sal_bill_amt_entry_tv.set(sal_mas_treeview.item(row, 'values')[8])
    sal_mas_form.destroy()
    sal_bill_no_entry.config(state='disable')
    sal_cust_list_combo.focus_set()
    Cur.execute("select*from sales_item where bill_no = {}".format(sal_bill_no_entry_tv.get()))
    i = 0
    old_data = Cur.fetchall()
    obj_cls_sal_entry.set_sal_original_data(old_data)
    for row2 in old_data:
        Cur.execute("select*from sales_item where item_id = {} and bill_no = {}".format(row2[2], sal_bill_no_entry_tv.get()))

        for row3 in Cur.fetchall():
            tree.insert('', i, text="", values=(row3[3], row3[4], row3[5], row3[6], row3[7], row3[8], row3[9], 18, row3[2], row3[10], row3[11]))
            i = i + 1

    if obj_cls_sal_entry.get_sal_button_clicked() == "edit":
        sal_cust_list_combo.config(state="readonly")
        sal_bill_date_entry.config(state="disable")
        sal_bill_no_entry.config(state="disable")
        sal_brand_entry.config(state="normal")
        sal_product_entry.config(state="disable")
        sal_design_name_entry.config(state="disable")
        sal_color_entry.config(state="disable")
        sal_size_entry.config(state="disable")
        sal_mrp_entry.config(state="disable")
        sal_rate_entry.config(state="disable")
        sal_qty_entry.config(state="disable")
        sal_discount_entry.config(state="normal")
        sal_cust_list_combo.focus_set()
    elif obj_cls_sal_entry.get_sal_button_clicked() == "delete":
        sal_delete_button.focus_set()
    elif obj_cls_sal_entry.get_sal_button_clicked() == "report":
        sal_export_to_excel_button.focus_set()


def Close_sal_Mas_Treeview(event):
    sal_mas_form.destroy()


def sales_Export(event):
    global sal_bill_no_entry, sal_bill_date_entry, sal_cust_list_combo, sal_bill_no_entry, sal_bill_date_entry, \
        sal_brand_entry, sal_product_entry, sal_design_name_entry, sal_color_entry, sal_size_entry, \
        sal_mrp_entry, sal_rate_entry, sal_gst_entry, sal_id_entry, sal_qty_entry, sal_amount_entry
    global sal_tot_qty_entry, sal_tot_amount_entry, sal_discount_entry, sal_taxable_entry, sal_cgst_entry, sal_sgst_entry, sal_bill_amt_entry

    global a3, sal_frame3, sal_export_button, sal_export_to_excel_button, sal_cancel_button
    global sal_bill_no_entry_tv, sal_bill_date_entry_tv, sal_cust_list_combo_tv, sal_bill_no_entry_tv, sal_bill_date_entry_tv, \
        sal_brand_entry_tv, sal_product_entry_tv, sal_design_name_entry_tv, sal_color_entry_tv, sal_size_entry_tv, \
        sal_mrp_entry_tv, sal_rate_entry_tv, sal_gst_entry_tv, sal_id_entry_tv, sal_qty_entry_tv, sal_amount_entry_tv, \
        sal_tot_qty_entry_tv, sal_tot_amount_entry_tv, sal_discount_entry_tv, sal_taxable_entry_tv, sal_cgst_entry_tv, sal_sgst_entry_tv, \
        sal_bill_amt_entry_tv

    form_top_label.configure(text="S A L E S     E X P O R T")
    obj_cls_sal_entry.set_sal_button_clicked("report")
    sal_bill_no_entry_tv = tk.IntVar()
    sal_bill_date_entry_tv = tk.StringVar()
    sal_bill_no_entry_tv = tk.StringVar()
    sal_bill_date_entry_tv = tk.StringVar()
    sal_brand_entry_tv = tk.StringVar()
    sal_product_entry_tv = tk.StringVar()
    sal_design_name_entry_tv = tk.StringVar()
    sal_color_entry_tv = tk.StringVar()
    sal_size_entry_tv = tk.StringVar()
    sal_mrp_entry_tv = tk.DoubleVar()
    sal_rate_entry_tv = tk.DoubleVar()
    sal_gst_entry_tv = tk.IntVar()
    sal_id_entry_tv = tk.IntVar()
    sal_qty_entry_tv = tk.IntVar()
    sal_amount_entry_tv = tk.DoubleVar()
    sal_tot_qty_entry_tv = tk.IntVar()
    sal_tot_amount_entry_tv = tk.DoubleVar()
    sal_discount_entry_tv = tk.DoubleVar()
    sal_taxable_entry_tv = tk.DoubleVar()
    sal_cgst_entry_tv = tk.DoubleVar()
    sal_sgst_entry_tv = tk.DoubleVar()
    sal_bill_amt_entry_tv = tk.DoubleVar()

    sal_mrp_entry_tv.set(0.00)
    sal_rate_entry_tv.set(0.00)
    sal_id_entry_tv.set('')
    sal_qty_entry_tv.set(0)
    sal_discount_entry_tv.set(0.00)
    sal_taxable_entry_tv.set(0.00)
    sal_cgst_entry_tv.set(0.00)
    sal_sgst_entry_tv.set(0.00)
    sal_bill_amt_entry_tv.set(0.00)

    sal_insert_button.destroy()
    sal_edit_button.destroy()
    sal_delete_button.destroy()
    sal_export_button.destroy()
    sal_quit_button.destroy()

    # *****************************   EXPORT - Frame1 - LABEL & ENTRY BOX SETTINGS - BEGIN     ********************************************
    sal_frame1 = Frame(sales_Form, width=380, height=40, bg='#B0E2FF')
    sal_frame1.place(x=10, y=48)

    sal_bill_no_label = Label(sal_frame1, text="Bill No.", bg='#B0E2FF', font=('bold'))
    sal_bill_no_label.place(x=5, y=10)

    sal_bill_date_label = Label(sal_frame1, text="Date", bg='#B0E2FF', font=('bold'))
    sal_bill_date_label.place(x=200, y=10)

    sal_bill_no_entry = Entry(sal_frame1, textvariable=sal_bill_no_entry_tv)
    sal_bill_no_entry.place(x=75, y=10)
    sal_bill_no_entry.config(state='normal')
    sal_bill_no_entry_tv.set("")
    sal_bill_no_entry.bind("<F1>", Show_sales_Master)
    sal_bill_no_entry.bind("<FocusIn>", set_focus_sal_bill_no)
    sal_bill_no_entry.bind("<FocusOut>", lost_focus_sal_bill_no)
    sal_bill_no_entry.focus_set()

    sal_bill_date_entry = Entry(sal_frame1, textvariable=sal_bill_date_entry_tv)
    sal_bill_date_entry.place(x=250, y=10)
    sal_bill_date_entry.config(state='disable')

    # *****************************  EXPORT - Frame1 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************  EXPORT - Frame2 - LABEL &  ENTRY BOX SETTINGS - BEGIN     ********************************************
    sal_frame2 = Frame(sales_Form, width=380, height=100, bg='#B0E2FF')
    sal_frame2.place(x=10, y=95)

    customer_list_label = Label(sal_frame2, text="Customer List", bg='#B0E2FF', font=('bold'))
    customer_list_label.place(x=5, y=10)

    customer_list = Customer_Name_Fetching()
    sal_cust_list_combo = ttk.Combobox(sal_frame2, value=customer_list, width=40, state='disable')
    sal_cust_list_combo.set('')
    sal_cust_list_combo.place(x=110, y=10)
    sal_cust_list_combo.bind("<Return>", set_focus_sal_bill_no)


    # *****************************   EXPORT - Frame2 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************   EXPORT - Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    sal_frame3 = LabelFrame(sales_Form, text="ITEM SELECTION", width=640, height=148, bg='#B0E2FF', font=('bold', 10))
    sal_frame3.place(x=650, y=48)

    sal_brand_label = Label(sal_frame3, text="Select Item", font=('bold'), bg='#B0E2FF')
    sal_brand_label.place(x=10, y=0)

    sal_product_label = Label(sal_frame3, text="Product", font=('bold'), bg='#B0E2FF')
    sal_product_label.place(x=10, y=27)

    sal_design_name_label = Label(sal_frame3, text="Design Name", font=('bold'), bg='#B0E2FF')
    sal_design_name_label.place(x=10, y=52)

    sal_color_label = Label(sal_frame3, text="Color", font=('bold'), bg='#B0E2FF')
    sal_color_label.place(x=10, y=77)

    sal_size_label = Label(sal_frame3, text="Size", font=('bold'), bg='#B0E2FF')
    sal_size_label.place(x=10, y=102)

    sal_mrp_label = Label(sal_frame3, text="Mrp", font=('bold'), bg='#B0E2FF')
    sal_mrp_label.place(x=250, y=102)

    sal_qty_label = Label(sal_frame3, text="Qty", font=('bold'), bg='#B0E2FF')
    sal_qty_label.place(x=250, y=0)

    sal_rate_label = Label(sal_frame3, text="Rate", font=('bold'), bg='#B0E2FF')
    sal_rate_label.place(x=250, y=27)

    sal_gst_label = Label(sal_frame3, text="GST", font=('bold'), bg='#B0E2FF')
    sal_gst_label.place(x=250, y=52)

    sal_id_label = Label(sal_frame3, text="ID", font=('bold'), bg='#B0E2FF')
    sal_id_label.place(x=250, y=77)

    sal_amount_label = Label(sal_frame3, text="Amount", font=('bold'), bg='#B0E2FF')
    sal_amount_label.place(x=430, y=0)

    sal_brand_entry = Entry(sal_frame3, textvariable=sal_brand_entry_tv)
    sal_brand_entry.place(x=120, y=1)
    sal_brand_entry.config(state="disable")

    sal_product_entry = Entry(sal_frame3, textvariable=sal_product_entry_tv)
    sal_product_entry.place(x=120, y=30)
    sal_product_entry.config(state="disable")

    sal_design_name_entry = Entry(sal_frame3, textvariable=sal_design_name_entry_tv)
    sal_design_name_entry.place(x=120, y=55)
    sal_design_name_entry.config(state="disable")

    sal_color_entry = Entry(sal_frame3, textvariable=sal_color_entry_tv)
    sal_color_entry.place(x=120, y=80)
    sal_color_entry.config(state="disable")

    sal_size_entry = Entry(sal_frame3, textvariable=sal_size_entry_tv)
    sal_size_entry.place(x=120, y=105)
    sal_size_entry.config(state="disable")

    sal_mrp_entry = Entry(sal_frame3, textvariable=sal_mrp_entry_tv, justify='right')
    sal_mrp_entry.place(x=300, y=105)
    sal_mrp_entry.config(state="disable")

    sal_rate_entry = Entry(sal_frame3, textvariable=sal_rate_entry_tv, justify='right')
    sal_rate_entry.place(x=300, y=30)
    sal_rate_entry.config(state="disable")

    sal_gst_entry = Entry(sal_frame3, state="disable", textvariable=sal_gst_entry_tv, justify='right')
    sal_gst_entry_tv.set(18)
    sal_gst_entry.place(x=300, y=55)

    sal_id_entry = Entry(sal_frame3, state="disable", textvariable=sal_id_entry_tv, justify='right', font=(9), width=5)
    sal_id_entry.place(x=300, y=80)

    sal_qty_entry = Entry(sal_frame3, textvariable=sal_qty_entry_tv, justify='right', width=5)
    sal_qty_entry.place(x=300, y=1)
    sal_qty_entry.config(width=5, state="disable")

    sal_amount_entry = Entry(sal_frame3, state="disable", textvariable=sal_amount_entry_tv, justify='right')
    sal_amount_entry.place(x=500, y=0)
    # *****************************   DELETE - Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - END     ********************************************

    # *****************************     DELETE - Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    sal_tot_qty_label = Label(sales_Form, text="Total", font=('bold', 12))
    sal_tot_qty_label.place(x=1000, y=420)

    sal_discount_label = Label(sales_Form, text="Discount", font=('bold', 12))
    sal_discount_label.place(x=1000, y=450)

    sal_bill_amt_label = Label(sales_Form, text="Bill Amount", font=('bold', 12))
    sal_bill_amt_label.place(x=1000, y=480)

    sal_taxable_label = Label(sales_Form, text="Taxable", font=('bold', 12))
    sal_taxable_label.place(x=1000, y=510)

    sal_cgst_label = Label(sales_Form, text="CGST @ 9%", font=('bold', 12))
    sal_cgst_label.place(x=1100, y=510)

    sal_sgst_label = Label(sales_Form, text="SGST @ 9%", font=('bold', 12))
    sal_sgst_label.place(x=1200, y=540)

    sal_tot_qty_entry = Entry(sales_Form, font=('bold', 12), width=5, state='disable',
                              textvariable=sal_tot_qty_entry_tv, justify='right')
    sal_tot_qty_entry.place(x=1100, y=420)

    sal_tot_amount_entry = Entry(sales_Form, font=('bold', 12), width=14, state='disable',
                                 textvariable=sal_tot_amount_entry_tv, justify='right')
    sal_tot_amount_entry.place(x=1155, y=420)

    sal_discount_entry = Entry(sales_Form, font=('bold', 12), textvariable=sal_discount_entry_tv, justify='right')
    sal_discount_entry.place(x=1100, y=450)
    sal_discount_entry.config(state="disable")

    sal_bill_amt_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_bill_amt_entry_tv, justify='right')
    sal_bill_amt_entry.place(x=1100, y=480)


    sal_taxable_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_taxable_entry_tv, justify='right', width=10)
    sal_taxable_entry.place(x=1003, y=540)

    sal_cgst_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_cgst_entry_tv, justify='right', width=10)
    sal_cgst_entry.place(x=1103, y=540)

    sal_sgst_entry = Entry(sales_Form, font=('bold', 12), state='disable', textvariable=sal_sgst_entry_tv, justify='right', width=10)
    sal_sgst_entry.place(x=1203, y=540)


    sal_export_to_excel_button = Button(sales_Form, text='Export To Excel', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_export_to_excel_button.place(x=535, y=520)
    sal_export_to_excel_button.bind("<ButtonRelease>", Export_Button_Click)
    sal_export_to_excel_button.bind("<Return>", Export_Button_Click)
    sal_export_to_excel_button.bind("<FocusIn>", set_focus_export_to_excel_button)
    sal_export_to_excel_button.bind("<FocusOut>", lost_focus_export_to_excel_button)

    sal_cancel_button = Button(sales_Form, text='Cancel', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_cancel_button.place(x=710, y=520)
    sal_cancel_button.bind("<Return>", Design_sales_Form_Load_destroy2)
    sal_cancel_button.bind("<ButtonRelease>", Design_sales_Form_Load_destroy2)
    sal_cancel_button.bind("<FocusIn>", set_focus_export_to_excel_cancel_button)
    sal_cancel_button.bind("<FocusOut>", focus_out_cancel_button)

# *****************************     EXPORT  - Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS -  END     ********************************************

def Export_Button_Click(event):
    sales_master_header = ["Bill No.", "Bill Date", "Customer Name", "Bill Qty", "Item Total", "Less Amount",
                              "CGST Amount", "SGST Amount", "Bill Amount"]

    Cur.execute("select * from  sales_master where bill_no = '{}'".format(sal_bill_no_entry.get()))

    for row in Cur.fetchall():
        cls_rep.set_bill_no(row[0])
        cls_rep.set_bill_date(row[1])
        cls_rep.set_cust_name(row[2])
        cls_rep.set_bill_qty(row[3])
        cls_rep.set_item_total(row[4])
        cls_rep.set_less_amount(row[5])
        dum_taxable = round((float(row[6])/9)*100,2)
        cls_rep.set_taxable_amt(dum_taxable)
        cls_rep.set_cgst_amt(row[6])
        cls_rep.set_sgst_amt(row[7])
        cls_rep.set_bill_amount(row[8])

    Cur2.execute("select * from sales_item where bill_no = '{}'".format(sal_bill_no_entry.get()))
    sales_item_data = []
    for row in Cur2.fetchall():
        sales_item_data.append(row)

    file_name1 = "Sales Bill No. " + sal_bill_no_entry.get() + " " + sal_bill_date_entry.get() + ".xlsx"
    sal_report_export_to_excel(file_name1, "Sales", sales_item_data)
    filepath = r"C:\Users\SYED\AcubeProjects\Status Plus\Sales Bill No. " + sal_bill_no_entry.get() + " " + sal_bill_date_entry.get() + ".xlsx"

    os.startfile(filepath)
    sales_Form.focus_set()
    sal_bill_no_entry.focus_set()


def sal_report_export_to_excel(workbookname: str, worksheetname: str, sal_item_data: list):
    item_master_header = ["Brand", "Product", "Design Name", "Color", "Size", "Mrp", "GST", "ID", "Qty",
                          "Amount"]
    workbook = xlsxwriter.Workbook(workbookname)
    worksheet = workbook.add_worksheet(worksheetname)

    worksheet.merge_range('A1:C1', obj_com_details.get_com_name(), workbook.add_format({'bg_color': '#D8FFF8','color': '007396', 'align': 'left', 'font_size': 30, 'bold' : 'True', 'left':1, 'top':1, 'border_color': '007396'}))
    worksheet.merge_range('A2:C2', obj_com_details.get_com_add(), workbook.add_format({'bg_color': '#D8FFF8','color': '007396', 'align': 'left','left':1, 'font_size': 10, 'border_color': '007396'}))
    worksheet.merge_range('A3:C3', obj_com_details.get_com_loc() + ", " + obj_com_details.get_com_city()+" - " +str(obj_com_details.get_com_pin()), workbook.add_format({'bg_color': '#D8FFF8','color': '007396', 'align': 'left', 'left':1, 'font_size': 10, 'border_color': '007396'}))

    worksheet.merge_range('A4:C4', "GST No. : "+obj_com_details.get_com_gst(), workbook.add_format({'bg_color': '#D8FFF8','color': '007396', 'align':'left','left':1, 'font_size': 10, 'border_color': '007396'}))
    worksheet.merge_range('A5:C5', "Email : " + obj_com_details.get_com_email(), workbook.add_format({'bg_color': '#D8FFF8','color': '007396', 'align': 'left','left':1, 'font_size': 10, 'border_color': '007396'}))
    worksheet.merge_range('A6:C6', "Phone : "+str(obj_com_details.get_com_phone()), workbook.add_format({'bg_color': '#D8FFF8','color': '007396', 'align': 'left','left':1, 'font_size': 10, 'border_color': '007396'}))

    worksheet.merge_range('D1:J2', "B  I  L  L", workbook.add_format({'align': 'top', 'valign': 'center', 'font_size': 40, 'top':1, 'right':1, 'bg_color': '007396', 'color': 'white', 'border_color': '007396'}))
    worksheet.merge_range('D3:F4', "Bill No.   :", workbook.add_format({'align': 'left', 'font_size': 20, 'bg_color': '007396', 'color': 'white', 'border_color': '007396'}))
    worksheet.merge_range('D5:F6', "Bill Date :", workbook.add_format({'align': 'left', 'font_size': 20, 'bg_color': '007396', 'color': 'white', 'border_color': '007396'}))

    worksheet.merge_range('G3:J4', str(cls_rep.get_bill_no()), workbook.add_format({'align': 'left', 'font_size': 20, 'right':1, 'bg_color': '007396', 'color': 'white', 'border_color': '007396'}))
    newdate2 = cls_rep.get_bill_date()
    newdate2 = newdate2.strftime("%d-%m-%Y")
    worksheet.merge_range('G5:J6', newdate2, workbook.add_format({'align': 'left', 'font_size': 20, 'right':1, 'bg_color': '007396', 'color': 'white', 'border_color': '007396'}))
    worksheet.merge_range('A7:J7', "", workbook.add_format({'left':1, 'right': 1, 'border_color': '007396'}))

    worksheet.write(7, 0, "Customer:", workbook.add_format({'left':1, 'font_size': 14, 'bold': 'True', 'border_color': '007396'}))
    worksheet.merge_range('A9:A14', "", workbook.add_format({'left': 1, 'border_color': '007396'}))
    worksheet.merge_range('J8:J14', "", workbook.add_format({'right': 1, 'border_color': '007396'}))

    Cur1.execute("select * from  customer_master where name = '{}'".format(cls_rep.get_cust_name()))
    cus_details = []
    for row in Cur1.fetchone():
        cus_details.append(row)
    worksheet.write(7, 1, cls_rep.get_cust_name(), workbook.add_format({'font_size': 14, 'bold': 'True', 'border_color': '007396'}))
    if cls_rep.get_cust_name() == "Cash":
        pass
    else:
        worksheet.write(8, 1, cus_details[1], workbook.add_format({'font_size': 10}))  # address
        worksheet.write(9, 1, cus_details[2]+", "+ cus_details[3] + "-" + str(cus_details[4]), workbook.add_format({'font_size': 10}))  # locality, city & pincode
        worksheet.write(10, 1, "Phone No. : " + str(cus_details[6]), workbook.add_format({'font_size': 10}))
        worksheet.write(11, 1, "Email : " + cus_details[7], workbook.add_format({'font_size': 10}))
        worksheet.write(12, 1, "GST No. :" + cus_details[8], workbook.add_format({'font_size': 10}))
    worksheet.set_column(14, 0, 12)#brand
    worksheet.set_column(14, 1, 10)#product
    worksheet.set_column(14, 2, 18)#design
    worksheet.set_column(14, 3, 10)#color
    worksheet.set_column(14, 4, 4)#size
    worksheet.set_column(14, 5, 7)#mrp
    worksheet.set_column(14, 6, 3)#gst
    worksheet.set_column(14, 7, 4)#id
    worksheet.set_column(14, 8, 3)#qty
    worksheet.set_column(14, 9, 9)#amount

    for index, row in enumerate(item_master_header):
        if index ==0:
            worksheet.write(14, index, row, workbook.add_format({'left':1,'bg_color': '007396', 'color': 'white', 'border_color': '007396'}))
        elif index ==9:
            worksheet.write(14, index, row, workbook.add_format({'right':1,'bg_color': '007396', 'color': 'white', 'border_color': '007396'}))
        else:
            worksheet.write(14, index, row, workbook.add_format({'bg_color': '007396', 'color': 'white', 'border_color': '007396'}))

    row_count = 15
    for index1, row1 in enumerate(sal_item_data):
        row_count = row_count + 1
        if row_count%2 == 0:
            worksheet.write(index1 + 15, 0, row1[3], workbook.add_format({'align':'left', 'left':1, 'bg_color': 'white', 'border_color': '007396'}))  # brand
            worksheet.write(index1 + 15, 1, row1[4],  workbook.add_format({'align':'left', 'bg_color': 'white', 'border_color': '007396'}))  # product
            worksheet.write(index1 + 15, 2, row1[5], workbook.add_format({'align':'left', 'bg_color': 'white', 'border_color': '007396'}))  # design
            worksheet.write(index1 + 15, 3, row1[6], workbook.add_format({'align':'left',  'bg_color': 'white', 'border_color': '007396'}))  # color
            worksheet.write(index1 + 15, 4, row1[7], workbook.add_format({'align':'left',  'bg_color': 'white', 'border_color': '007396'}))  # size
            worksheet.write(index1 + 15, 5, row1[8], workbook.add_format({'align':'right', 'num_format': '####.00', 'bg_color': 'white', 'border_color': '007396'}))  # mrp
            worksheet.write(index1 + 15, 6, "18", workbook.add_format({'align':'right', 'bg_color': 'white', 'border_color': '007396'}))     # gst
            worksheet.write(index1 + 15, 7, row1[2], workbook.add_format({'align':'center', 'bg_color': 'white', 'border_color': '007396'}))  # item_id
            worksheet.write(index1 + 15, 8, row1[10], workbook.add_format({'align': 'right', 'bg_color': 'white', 'border_color': '007396'}))  # item_qty
            worksheet.write(index1 + 15, 9, row1[11], workbook.add_format({'align': 'right', 'right': 1, 'num_format': '####.00', 'bg_color': 'white', 'border_color': '007396'}))  # item_amount
        else:
            worksheet.set_row(index1 +15, 15)
            worksheet.write(index1 + 15, 0, row1[3], workbook.add_format({'align': 'left', 'left': 1, 'bg_color': '#D8FFF8', 'border_color': '007396'}))  # brand
            worksheet.write(index1 + 15, 1, row1[4], workbook.add_format({'align': 'left',  'bg_color': '#D8FFF8', 'border_color': '007396'}))  # product
            worksheet.write(index1 + 15, 2, row1[5], workbook.add_format({'align': 'left',  'bg_color': '#D8FFF8', 'border_color': '007396'}))  # design
            worksheet.write(index1 + 15, 3, row1[6], workbook.add_format({'align': 'left',  'bg_color': '#D8FFF8', 'border_color': '007396'}))  # color
            worksheet.write(index1 + 15, 4, row1[7], workbook.add_format({'align': 'left',  'bg_color': '#D8FFF8', 'border_color': '007396'}))  # size
            worksheet.write(index1 + 15, 5, row1[8], workbook.add_format({'align': 'right', 'num_format': '####.00', 'bg_color': '#D8FFF8', 'border_color': '007396'}))  # mrp
            worksheet.write(index1 + 15, 6, "18", workbook.add_format({'align': 'right', 'bg_color': '#D8FFF8', 'border_color': '007396'}))  # gst
            worksheet.write(index1 + 15, 7, row1[2], workbook.add_format({'align': 'center', 'bg_color': '#D8FFF8', 'border_color': '007396'}))  # item_id
            worksheet.write(index1 + 15, 8, row1[10], workbook.add_format({'align': 'right', 'bg_color': '#D8FFF8', 'border_color': '007396'}))  # item_qty
            worksheet.write(index1 + 15, 9, row1[11], workbook.add_format({'align': 'right', 'right': 1, 'num_format': '####.00', 'bg_color': '#D8FFF8', 'border_color': '007396'}))  # item_amount

    for lc in range(0,11):
        row_count = row_count + 1
        if row_count % 2 == 0:
            rc3 = 'A' + str((row_count)) + ':J' + str((row_count))
            worksheet.merge_range(rc3, "", workbook.add_format({'bg_color': 'white', 'left': 1, 'right': 1, 'border_color': '007396'}))
        else:
            rc3 = 'A' + str((row_count)) + ':J' + str((row_count))
            worksheet.merge_range(rc3, "", workbook.add_format({'bg_color': '#D8FFF8', 'left': 1, 'right': 1, 'border_color': '007396'}))

    row_count = row_count + 1
    rc1 = row_count
    rc3 = 'A' + str((row_count)) + ':J' + str((row_count))
    worksheet.merge_range(rc3, "", workbook.add_format({'left':1, 'right':1, 'bottom': 1, 'border_color': '007396'}))
    worksheet.write(row_count, 0, "", workbook.add_format({'left': 1, 'border_color': '007396'}))
    worksheet.write(row_count, 4, "Total ")
    worksheet.write(row_count, 8, str(cls_rep.get_bill_qty()), workbook.add_format({'align': 'right'}))
    worksheet.write(row_count, 9, str(cls_rep.get_item_total()), workbook.add_format({'align': 'right', 'right':1, 'border_color': '007396'}))
    worksheet.write(row_count + 1, 0, "", workbook.add_format({'left': 1, 'border_color': '007396'}))
    worksheet.write(row_count + 1, 4, "Discount Amount ")
    worksheet.write(row_count + 1, 9, str(cls_rep.get_less_amount()), workbook.add_format({'align': 'right', 'right':1, 'border_color': '007396'}))
    worksheet.write(row_count + 2, 0, "", workbook.add_format({'left': 1, 'border_color': '007396'}))
    worksheet.write(row_count + 2, 4, "Bill Amount ", workbook.add_format({'font_size' :12, 'bold': 'True'}))
    worksheet.write(row_count + 2, 9, str(cls_rep.get_bill_amount()), workbook.add_format({'align': 'right', 'font_size': 12, 'bold' : 'True', 'top':1, 'bottom':1, 'right':1, 'border_color': '007396'}))
    worksheet.write(row_count + 4, 1, "Tax Slab ", workbook.add_format({'align':'center', 'top':1, 'bottom':1, 'left':1, 'right':1, 'border_color': '007396'}))
    worksheet.write(row_count + 4, 2, "Taxable Value", workbook.add_format({'align':'center', 'top':1, 'bottom':1, 'left':1, 'right':1, 'border_color': '007396'}))
    worksheet.write(row_count + 4, 3, "CGST @ 9% ", workbook.add_format({'align':'center', 'top':1, 'bottom':1, 'left':1, 'right':1, 'border_color': '007396'}))

    rc2 = 'J' + str((row_count + 4)) + ':J' + str((row_count + 8))
    worksheet.merge_range(rc2, "", workbook.add_format({'right' : 1, 'border_color': '007396'}))

    rc = 'E' + str((row_count + 5)) + ':F' + str((row_count + 5))
    worksheet.merge_range(rc, "SGST @ 9% ", workbook.add_format({'align':'center', 'top':1, 'bottom':1, 'left':1, 'right':1, 'border_color': '007396'}))

    worksheet.write(row_count + 5, 1, str("GST @ 18%"), workbook.add_format({'align':'center', 'bottom':1, 'left':1, 'right':1, 'border_color': '007396'}))
    worksheet.write(row_count + 5, 2, str(cls_rep.get_taxable_amt()), workbook.add_format({'align':'center', 'bottom':1, 'left':1, 'right':1, 'border_color': '007396'}))
    worksheet.write(row_count + 5, 3, str(cls_rep.get_cgst_amt()), workbook.add_format({'align':'center', 'bottom':1, 'left':1, 'right':1, 'border_color': '007396'}))
    rc = 'E' + str((row_count + 6)) + ':F' + str((row_count + 6))
    worksheet.merge_range(rc, str(cls_rep.get_sgst_amt()), workbook.add_format({'align':'center', 'bottom':1, 'left':1, 'right':1, 'border_color': '007396'}))

    rc = 'A' + str((rc1+1)) + ':A' + str((row_count + 8))
    worksheet.merge_range(rc, "", workbook.add_format({'left': 1, 'border_color': '007396'}))

    rc = 'A' + str((row_count + 9)) + ':J' + str((row_count + 9))
    worksheet.merge_range(rc, "T H A N K   Y O U", workbook.add_format({'align': 'center', 'left': 1, 'right': 1, 'bg_color':'#D8FFF8', 'border_color': '007396', 'color': '007396'}))

    rc = 'A' + str((row_count + 10)) + ':J' + str((row_count + 10))
    worksheet.merge_range(rc, "V I S I T   A G A I N", workbook.add_format({'align': 'center', 'bottom':1, 'left': 1, 'right': 1, 'bg_color':'007396', 'color': 'white', 'border_color': '007396'}))

    rc = 'A' + str((row_count + 11)) + ':J' + str((row_count + 11))
    worksheet.merge_range(rc, "", workbook.add_format({'bottom' : 1, 'left': 1, 'right': 1, 'border_color': '007396'}))

    workbook.close()


def Design_sales_Form_Load():
    global sales_Form, form_top_label, form_bottom_label, sal_frame1, tree, sal_frame4
    global sal_insert_button, sal_edit_button, sal_delete_button, sal_export_button, sal_quit_button

    sales_Form = tk.Toplevel()
    sales_Form.geometry("1300x600+24+51")
    sales_Form.title("")
    form_top_label = Label(sales_Form, text="S A L E S ", width=1200, bg="#63B8FF", fg="black", font=('copper', 20, 'bold'))
    form_top_label.pack()
    Cur.execute("select * from company_master")
    for row in Cur.fetchall():
        obj_com_details.set_com_name(row[0])
        obj_com_details.set_com_add(row[1])
        obj_com_details.set_com_loc(row[2])
        obj_com_details.set_com_city(row[3])
        obj_com_details.set_com_pin(row[4])
        obj_com_details.set_com_state(row[5])
        obj_com_details.set_com_phone(row[6])
        obj_com_details.set_com_email(row[7])
        obj_com_details.set_com_gst(row[8])

    # *****************************    Frame1 - LABEL & ENTRY BOX SETTINGS - BEGIN     ********************************************
    sal_frame1 = Frame(sales_Form, width=380, height=40, bg='#B0E2FF')
    sal_frame1.place(x=10, y=48)

    sal_bill_no_label = Label(sal_frame1, text="Bill No.", bg='#B0E2FF', font=('bold'))
    sal_bill_no_label.place(x=5, y=10)

    sal_bill_date_label = Label(sal_frame1, text="Date", bg='#B0E2FF', font=('bold'))
    sal_bill_date_label.place(x=200, y=10)

    sal_bill_no_entry = Entry(sal_frame1)
    sal_bill_no_entry.place(x=75, y=10)
    sal_bill_no_entry.config(state='disable')

    sal_bill_date_entry = Entry(sal_frame1)
    sal_bill_date_entry.place(x=250, y=10)
    sal_bill_date_entry.config(state='disable')
    # *****************************   Frame1 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************   Frame2 - LABEL &  ENTRY BOX SETTINGS - BEGIN     ********************************************
    sal_frame2 = Frame(sales_Form, width=380, height=100, bg='#B0E2FF')
    sal_frame2.place(x=10, y=95)

    customer_list_label = Label(sal_frame2, text="Customer List", bg='#B0E2FF', font=('bold'))
    customer_list_label.place(x=5, y=10)

    
    customer_list = Customer_Name_Fetching()
    sal_cust_list_combo = ttk.Combobox(sal_frame2, value=customer_list, width=40, state='readonly')
    sal_cust_list_combo.set('')
    sal_cust_list_combo.place(x=110, y=10)
    sal_cust_list_combo.config(state='disable')



    # *****************************   Frame2 - LABEL & ENTRY BOX SETTINGS - END     ********************************************

    # *****************************   Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    sal_frame3 = LabelFrame(sales_Form, text="ITEM SELECTION", width=640, height=148, bg='#B0E2FF', font=('bold', 10))
    sal_frame3.place(x=650, y=48)

    sal_brand_label = Label(sal_frame3, text="Select Item", font=('bold'), bg='#B0E2FF')
    sal_brand_label.place(x=10, y=0)

    sal_product_label = Label(sal_frame3, text="Product", font=('bold'), bg='#B0E2FF')
    sal_product_label.place(x=10, y=30)

    sal_design_name_label = Label(sal_frame3, text="Design Name", font=('bold'), bg='#B0E2FF')
    sal_design_name_label.place(x=10, y=52)

    sal_color_label = Label(sal_frame3, text="Color", font=('bold'), bg='#B0E2FF')
    sal_color_label.place(x=10, y=77)

    sal_size_label = Label(sal_frame3, text="Size", font=('bold'), bg='#B0E2FF')
    sal_size_label.place(x=10, y=102)

    sal_mrp_label = Label(sal_frame3, text="Mrp", font=('bold'), bg='#B0E2FF')
    sal_mrp_label.place(x=250, y=102)


    sal_qty_label = Label(sal_frame3, text="Qty", font=('bold'), bg='#B0E2FF')
    sal_qty_label.place(x=250, y=0)

    sal_rate_label = Label(sal_frame3, text="Rate", font=('bold'), bg='#B0E2FF')
    sal_rate_label.place(x=250, y=30)

    sal_gst_label = Label(sal_frame3, text="GST", font=('bold'), bg='#B0E2FF')
    sal_gst_label.place(x=250, y=52)

    sal_id_label = Label(sal_frame3, text="ID", font=('bold'), bg='#B0E2FF')
    sal_id_label.place(x=250, y=77)


    sal_amount_label = Label(sal_frame3, text="Amount", font=('bold'), bg='#B0E2FF')
    sal_amount_label.place(x=430, y=0)

    sal_brand_entry = Entry(sal_frame3, state="disable")
    sal_brand_entry.place(x=120, y=1)

    sal_product_entry = Entry(sal_frame3, state="disable")
    sal_product_entry.place(x=120, y=30)

    sal_design_name_entry = Entry(sal_frame3, state="disable")
    sal_design_name_entry.place(x=120, y=55)

    sal_color_entry = Entry(sal_frame3, state="disable")
    sal_color_entry.place(x=120, y=80)

    sal_size_entry = Entry(sal_frame3, state="disable")
    sal_size_entry.place(x=120, y=105)

    sal_mrp_entry = Entry(sal_frame3, state="disable")
    sal_mrp_entry.place(x=300, y=105)

    sal_qty_entry = Entry(sal_frame3, state="disable", width=5)
    sal_qty_entry.place(x=300, y=1)

    sal_rate_entry = Entry(sal_frame3, state="disable")
    sal_rate_entry.place(x=300, y=30)

    sal_gst_entry = Entry(sal_frame3, state="disable")
    sal_gst_entry.place(x=300, y=55)

    sal_id_entry = Entry(sal_frame3, state="disable", font=(8), width=5)
    sal_id_entry.place(x=300, y=80)

    sal_amount_entry = Entry(sal_frame3, state="disable")
    sal_amount_entry.place(x=500, y=0)

    # *****************************   Frame3 - LABEL, ENTRY BOX & BUTTON SETTINGS - END     ********************************************

    # *****************************    Frame4 - TREEVIEW SETTINGS - BEGIN     ********************************************

    sal_frame4 = Frame(sales_Form)
    sal_frame4.pack(pady=5)
    sal_frame4.place(x=10, y=210)
    sal_frame4.pack_propagate(False)
    sal_frame4.configure(width=1280, height=196, bg='#B0E2FF')
    global col

    col = ('brand', 'product', 'design', 'color', 'size', 'mrp', 'rate', 'gst', 'id', 'qty', 'amount')
    tree = ttk.Treeview(sal_frame4, height=8, show='headings', columns=col)
    # tree['show']='headings'
    tree.pack(fill=tk.X, pady=5)
    style1 = ttk.Style(sal_frame4)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading", foreground='white', background='grey28', font='14')
    style1.configure("Treeview", foreground='white', background='grey28', fieldbackground='#B0E2FF',
                     font=('times new roman', 10))
    style1.map('Treeview', background=[('selected', '#B0E2FF')])

    tree.column("brand", width=200, minwidth=50, anchor=tk.W)
    tree.column("product", width=200, minwidth=50, anchor=tk.W)
    tree.column("design", width=220, minwidth=50, anchor=tk.W)
    tree.column("color", width=150, minwidth=50, anchor=tk.W)
    tree.column("size", width=100, minwidth=50, anchor=tk.W)
    tree.column("mrp", width=100, minwidth=50, anchor=tk.E)
    tree.column("rate", width=0, minwidth=0, anchor=tk.E)
    tree.column("gst", width=100, minwidth=50, anchor=tk.S)
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

    vsb = ttk.Scrollbar(sal_frame4, orient="vertical")
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(sal_frame4, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)

    tree.pack()
    tree.bind("<Return>", Select_Item_Data)
    tree.bind("<ButtonRelease>", Select_Item_Data)
    tree.bind("<Delete>", Delete_sales_Items_In_Treeview)
    tree.bind("<FocusIn>", set_focus_treeview)

    # *****************************   Frame4 - TREEVIEW SETTINGS - END     ********************************************

    # *****************************     Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS - BEGIN     ********************************************
    sal_tot_qty_label = Label(sales_Form, text="Total", font=('bold', 12))
    sal_tot_qty_label.place(x=1000, y=420)

    sal_discount_label = Label(sales_Form, text="Discount", font=('bold', 12))
    sal_discount_label.place(x=1000, y=450)

    sal_bill_amt_label = Label(sales_Form, text="Bill Amount", font=('bold', 12))
    sal_bill_amt_label.place(x=1000, y=480)

    sal_taxable_label = Label(sales_Form, text="Taxable", font=('bold', 12))
    sal_taxable_label.place(x=1000, y=510)

    sal_cgst_label = Label(sales_Form, text="CGST @ 9%", font=('bold', 12))
    sal_cgst_label.place(x=1100, y=510)

    sal_sgst_label = Label(sales_Form, text="SGST @ 9%", font=('bold', 12))
    sal_sgst_label.place(x=1200, y=510)


    sal_tot_qty_entry = Entry(sales_Form, font=('bold', 12), width=5, state='disable')
    sal_tot_qty_entry.place(x=1100, y=420)

    sal_tot_amount_entry = Entry(sales_Form, font=('bold', 12), width=14, state='disable')
    sal_tot_amount_entry.place(x=1155, y=420)

    sal_discount_entry = Entry(sales_Form, font=('bold', 12), state='disable')
    sal_discount_entry.place(x=1100, y=450)

    sal_bill_amt_entry = Entry(sales_Form, font=('bold', 12), state='disable')
    sal_bill_amt_entry.place(x=1100, y=480)

    sal_taxable_entry = Entry(sales_Form, font=('bold', 12), state='disable', width=10)
    sal_taxable_entry.place(x=1003, y=540)

    sal_cgst_entry = Entry(sales_Form, font=('bold', 12), state='disable', width=10)
    sal_cgst_entry.place(x=1103, y=540)

    sal_sgst_entry = Entry(sales_Form, font=('bold', 12), state='disable', width=10)
    sal_sgst_entry.place(x=1203, y=540)


    sal_insert_button = Button(sales_Form, text='I N S E R T', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_insert_button.place(x=10, y=520)
    sal_insert_button.focus_set()
    sal_insert_button.bind("<Return>", sales_Insert)
    sal_insert_button.bind("<ButtonRelease>", sales_Insert)
    sal_insert_button.bind("<FocusIn>", set_focus_insert_button)
    sal_insert_button.bind("<FocusOut>", focus_out_insert_button)

    sal_edit_button = Button(sales_Form, text='E D I T', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_edit_button.place(x=185, y=520)
    sal_edit_button.bind("<Return>", sales_Edit)
    sal_edit_button.bind("<ButtonRelease>", sales_Edit)
    sal_edit_button.bind("<FocusIn>", set_focus_edit_button)
    sal_edit_button.bind("<FocusOut>", focus_out_edit_button)

    sal_delete_button = Button(sales_Form, text='D E L E T E', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_delete_button.place(x=360, y=520)
    sal_delete_button.bind("<Return>", sales_Delete)
    sal_delete_button.bind("<ButtonRelease>", sales_Delete)
    sal_delete_button.bind("<FocusIn>", set_focus_delete_button)
    sal_delete_button.bind("<FocusOut>", focus_out_delete_button)

    sal_export_button = Button(sales_Form, text='R E P O R T', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_export_button.place(x=535, y=520)
    sal_export_button.bind("<ButtonRelease>", sales_Export)
    sal_export_button.bind("<Return>", sales_Export)
    sal_export_button.bind("<FocusIn>", set_focus_export_button)
    sal_export_button.bind("<FocusOut>", focus_out_export_button)

    sal_quit_button = Button(sales_Form, text='Q U I T', bg='grey28', fg='white', width=15, font=('bold', 14))
    sal_quit_button.place(x=710, y=520)
    sal_quit_button.bind("<Return>", Design_sales_Form_Load_destroy)
    sal_quit_button.bind("<ButtonRelease>", Design_sales_Form_Load_destroy)
    sal_quit_button.bind("<FocusIn>", set_focus_quit_button)
    sal_quit_button.bind("<FocusOut>", focus_out_quit_button)

    form_bottom_label = Label(sales_Form, text="To Insert Sales Press - [INSERT]       To Edit Sales Press - [EDIT]"
                                               "       To Delete Sales Press - [DELETE]       "
                                               "To Export Sales Press - [REPORT]        "
                                               "To Move Next Button Press - [Tab]",
                              width=1200, bg="#B0E2FF", fg="black", font=('copper', 11))
    form_bottom_label.pack(side=BOTTOM)
# *****************************     Bottom - LABEL, ENTRY BOX & BUTTON SETTINGS -  END     ********************************************
