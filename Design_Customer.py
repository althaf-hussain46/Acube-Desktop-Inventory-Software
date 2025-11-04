import os
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
from Show_Data import*
from Class_Customer import*
from Class_Main_Window import*
from Class_Report import*
from DB_Connection import*

cls2 = Cls_Customer_Master()
cls3 = cls_main_window()
cls_rep = cls_report()
Con = DB_Connect()
Cur = Con.cursor()

#*************     L E F T   C L I C K  - B E G I N     *****************
def cust_name_lclick_focus(event):
    form_bottom.configure(text='Press [F1] To List Customer     Maximum Allowed Characters - 50')
    cust_name_entry.focus_set()

def cust_add_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Characters - 100')
    cust_address1_entry.focus_set()

def cust_loc_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Characters - 25')
    cust_locality_entry.focus_set()

def cust_city_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Characters - 20')
    cust_city_entry.focus_set()

def cust_pin_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Numbers - 6')
    cust_pincode_entry.focus_set()

def cust_state_lclick_focus(event):
    form_bottom.configure(text='Select From Dropdown Box')
    cust_state_combo.focus_set()

def cust_phone_lclick_focus(event):
    form_bottom.configure(text='Must Be 10 Numbers')
    cust_phone_entry.focus_set()

def cust_email_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Characters - 100')
    cust_email_entry.focus_set()

def cust_gst_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Characters - 15')
    cust_gst_no_entry.focus_set()
#***********     L E F T   C L I C K  -  E N D     ************

#***********        R E T U R N   K E Y   P R E S S E D  -  B E G I N     ********
def cus_add_set_focus(event):
    if len(cust_name_entry.get()) >= 1 and len(cust_name_entry.get()) <= 50:
        form_bottom.configure(text='Maximum Allowed Characters - 100')
        cust_address1_entry.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 50')
        cust_form.focus_set()
        cust_name_entry.focus_set()

def cus_loc_set_focus(event):
    if len(cust_address1_entry.get()) >= 1 and len(cust_address1_entry.get()) <= 100:
        form_bottom.configure(text='Maximum Allowed Characters - 25')
        cust_locality_entry.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 100')
        cust_form.focus_set()
        cust_address1_entry.focus_set()

def cus_city_set_focus(event):
    if len(cust_locality_entry.get()) >= 1 and len(cust_locality_entry.get()) <= 25:
        form_bottom.configure(text='Maximum Allowed Characters - 20')
        cust_city_entry.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 25')
        cust_form.focus_set()
        cust_locality_entry.focus_set()

def cus_pin_set_focus(event):
    if len(cust_city_entry.get()) >= 1 and len(cust_city_entry.get()) <= 20:
        form_bottom.configure(text='Maximum Allowed Numbers - 6')
        cust_pincode_entry.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 20')
        cust_form.focus_set()
        cust_city_entry.focus_set()

def cus_state_set_focus(event):
    if len(cust_pincode_entry.get()) >= 1 and len(cust_pincode_entry.get()) <= 6:
        form_bottom.configure(text='Select State From Dropdown List')
        cust_state_combo.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Numbers  - 6')
        cust_form.focus_set()
        cust_pincode_entry.focus_set()

def cus_phone_set_focus(event):
    if len(cust_state_combo.get()) > 0:
        form_bottom.configure(text='Must Be 10 Numbers')
        cust_phone_entry.focus_set()
    else:
        messagebox.showinfo('', 'Select State From Dropdown List')
        cust_form.focus_set()
        cust_state_combo.focus_set()

def cus_email_set_focus(event):
    if len(cust_phone_entry.get()) == 10:
        form_bottom.configure(text='Maximum Allowed Characters - 100')
        cust_email_entry.focus_set()
    else:
        messagebox.showinfo('', 'Must Be 10 Numbers')
        cust_form.focus_set()
        cust_phone_entry.focus_set()

def cus_gst_set_focus(event):
    if len(cust_email_entry.get()) >= 1 and len(cust_email_entry.get()) <= 100:
        form_bottom.configure(text='Maximum Allowed Characters - 15')
        cust_gst_no_entry.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 100')
        cust_form.focus_set()
        cust_email_entry.focus_set()

#********        R E T U R N   K E Y   P R E S S E D  -  E N D      ********

def Main_Button_FocusIn(event):
    form_bottom.configure(text="To Create CUSTOMER Press - [Insert]     To Update CUSTOMER Press - [Edit]     To Remove CUSTOMER Press - [Delete]     To Report CUSTOMER Press - [Report]     Press [Tab] - Key To Move To Next Button")

def Save_Button_FocusIn(event):
    form_bottom.configure(text='Press [Enter] To Save CUSTOMER Details')

def Update_Button_FocusIn(event):
    form_bottom.configure(text='Press [Enter] To Update The Changes You Have Made')

def Cancel_Button_FocusIn(event):
    form_bottom.configure(text='Press [Enter] To Cancel The Changes You Have Made')

def Delete_Button_FocusIn(event):
    form_bottom.configure(text='Press [Enter] To Delete The CUSTOMER Details')

def Export_Button_FocusIn(event):
    form_bottom.configure(text='Press [Enter] To Export The CUSTOMER Details')

def Tree_FocusIn(event):
    form_bottom.configure(text='Select From The List To Insert Or Edit Or Delete Or Export The CUSTOMER Details')
    tree.focus_set()

def cus_save_button_set_focus(event):
    if len(cust_gst_no_entry.get()) >= 1 and len(cust_gst_no_entry.get()) <= 15:
        form_bottom.configure(text='Press [Enter] To Save')
        save_button.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 15')
        cust_form.focus_set()
        cust_gst_no_entry.focus_set()

def cus_update_button_set_focus(event):
    if len(cust_gst_no_entry.get()) >= 1 and len(cust_gst_no_entry.get()) <= 15:
        form_bottom.configure(text='Press [Enter] To Save')
        update_button.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 15')
        cust_form.focus_set()
        cust_gst_no_entry.focus_set()

def cus_delete_button_set_focus(event):
    update_button.focus_set()

def cus_report_button_set_focus(event):
    report_button.focus_set()

def Customer_Insert(event):
    global cust_name_entry, cust_address1_entry, cust_locality_entry, cust_city_entry, cust_pincode_entry
    global cust_phone_entry, cust_email_entry, cust_gst_no_entry
    global cust_name_entry_tv, cust_address1_entry_tv, cust_locality_entry_tv, cust_city_entry_tv, cust_pincode_entry_tv
    global cust_state_combo, cust_phone_entry_tv, cust_email_entry_tv, cust_gst_no_entry_tv
    global save_button
    form_name.configure(text="Customer - I N S E R T")

    cls2.set_cust_record_found('0')
    cust_name_entry_tv = tk.StringVar()
    cust_address1_entry_tv = tk.StringVar()
    cust_locality_entry_tv = tk.StringVar()
    cust_city_entry_tv = tk.StringVar()
    cust_pincode_entry_tv = tk.StringVar()
    cust_phone_entry_tv = tk.StringVar()
    cust_email_entry_tv = tk.StringVar()
    cust_gst_no_entry_tv = tk.StringVar()

    insert_button.destroy()
    edit_button.destroy()
    delete_button.destroy()
    report_button.destroy()
    quit_button.destroy()

    cust_name_entry = Entry(cust_form, textvariable=cust_name_entry_tv)
    cust_name_entry.place(x=130, y=50, width=340)
    cust_name_entry.focus_set()
    form_bottom.configure(text="Press [F1] To List Customer     Maximum Allowed Characters - 50")
    cust_name_entry.config(bg='#B0E2FF')
    cust_name_entry.bind("<F1>", Customer_Search)
    cust_name_entry.bind("<Return>", cus_add_set_focus)
    cust_name_entry.bind("<ButtonRelease>", cust_name_lclick_focus)
    cust_name_entry.bind("<FocusIn>", cust_name_lclick_focus)

    cust_address1_entry = Entry(cust_form,textvariable=cust_address1_entry_tv)
    cust_address1_entry.place(x=130, y=80, width=340)
    cust_address1_entry.bind("<Return>",cus_loc_set_focus)
    cust_address1_entry.bind("<ButtonRelease>", cust_add_lclick_focus)
    cust_address1_entry.bind("<FocusIn>", cust_add_lclick_focus)

    cust_locality_entry = Entry(cust_form,textvariable=cust_locality_entry_tv)
    cust_locality_entry.place(x=130, y=110, width=340)
    cust_locality_entry.bind("<Return>",cus_city_set_focus)
    cust_locality_entry.bind("<ButtonRelease>", cust_loc_lclick_focus)
    cust_locality_entry.bind("<FocusIn>", cust_loc_lclick_focus)

    cust_city_entry = Entry(cust_form,textvariable=cust_city_entry_tv)
    cust_city_entry.place(x=130, y=140, width=100)
    cust_city_entry.bind("<Return>",cus_pin_set_focus)
    cust_city_entry.bind("<ButtonRelease>", cust_city_lclick_focus)
    cust_city_entry.bind("<FocusIn>", cust_city_lclick_focus)

    cust_pincode_entry = Entry(cust_form,textvariable=cust_pincode_entry_tv)
    cust_pincode_entry.place(x=130, y=170, width=100)
    reg = cust_form.register(Validate_Number)
    cust_pincode_entry.config(validate="key",validatecommand=(reg,'%P'))
    cust_pincode_entry.bind("<Return>",cus_state_set_focus)
    cust_pincode_entry.bind("<ButtonRelease>", cust_pin_lclick_focus)
    cust_pincode_entry.bind("<FocusIn>", cust_pin_lclick_focus)

    states_name = ['Tamil Nadu', 'Kerala', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Delhi']
    cust_state_combo = ttk.Combobox(cust_form,value=states_name, state='readonly')
    cust_state_combo.current(0)
    cust_state_combo.place(x=130, y=200)
    cust_state_combo.bind("<Return>",cus_phone_set_focus)
    cust_state_combo.bind("<ButtonRelease>", cust_state_lclick_focus)
    cust_state_combo.bind("<FocusIn>", cust_state_lclick_focus)

    cust_phone_entry = Entry(cust_form,textvariable=cust_phone_entry_tv)
    cust_phone_entry.place(x=130, y=230, width=100)
    reg = cust_form.register(Validate_Number)
    cust_phone_entry.config(validate="key", validatecommand=(reg, '%P'))
    cust_phone_entry.bind("<Return>",cus_email_set_focus)
    cust_phone_entry.bind("<ButtonRelease>", cust_phone_lclick_focus)
    cust_phone_entry.bind("<FocusIn>", cust_phone_lclick_focus)

    cust_email_entry = Entry(cust_form,textvariable=cust_email_entry_tv)
    cust_email_entry.place(x=130, y=260, width=230)
    cust_email_entry.bind("<Return>",cus_gst_set_focus)
    cust_email_entry.bind("<ButtonRelease>", cust_email_lclick_focus)
    cust_email_entry.bind("<FocusIn>", cust_email_lclick_focus)

    cust_gst_no_entry = Entry(cust_form,textvariable=cust_gst_no_entry_tv)
    cust_gst_no_entry.place(x=130, y=290, width=230)
    cust_gst_no_entry.bind("<Return>",cus_save_button_set_focus)
    cust_gst_no_entry.bind("<ButtonRelease>", cust_gst_lclick_focus)
    cust_gst_no_entry.bind("<FocusIn>", cust_gst_lclick_focus)
    # *************** ENTRY BOX SETTINGS - END ****************

    # ************ BUTTON SETTINGS - BEGIN *******************
    save_button = Button(cust_form, text="Save", font=(14))
    save_button.place(x=340, y=350, width=64)
    save_button.bind("<ButtonRelease>", Save_Button_Click)
    save_button.bind("<Return>",Save_Button_Click)
    save_button.bind("<FocusIn>", Save_Button_FocusIn)

    cancel_button = Button(cust_form, text="Cancel", font=(14))
    cancel_button.place(x=410, y=350, width=64)
    cancel_button.bind("<ButtonRelease>",Cancel_Button_Click)
    cancel_button.bind("<Return>",Cancel_Button_Click)
    cancel_button.bind("<FocusIn>", Cancel_Button_FocusIn)

    # *************** BUTTON SETTINGS - END *************


def Customer_Edit(event):
    global cust_name_entry, cust_address1_entry, cust_locality_entry, cust_city_entry, cust_pincode_entry
    global cust_phone_entry, cust_email_entry, cust_gst_no_entry
    global cust_name_entry_tv, cust_address1_entry_tv, cust_locality_entry_tv, cust_city_entry_tv, cust_pincode_entry_tv
    global cust_state_combo, cust_phone_entry_tv, cust_email_entry_tv, cust_gst_no_entry_tv
    global update_button
    form_name.configure(text="Customer - E D I T")

    cls2.set_cust_id('')
    cust_name_entry_tv = tk.StringVar()
    cust_address1_entry_tv = tk.StringVar()
    cust_locality_entry_tv = tk.StringVar()
    cust_city_entry_tv = tk.StringVar()
    cust_pincode_entry_tv = tk.StringVar()
    cust_phone_entry_tv = tk.StringVar()
    cust_email_entry_tv = tk.StringVar()
    cust_gst_no_entry_tv = tk.StringVar()

    insert_button.destroy()
    edit_button.destroy()
    delete_button.destroy()
    report_button.destroy()
    quit_button.destroy()

    cust_name_entry = Entry(cust_form, textvariable=cust_name_entry_tv)
    cust_name_entry.place(x=130, y=50, width=340)
    cust_name_entry.focus_set()
    form_bottom.configure(text="Press [F1] To List Customer     Maximum Allowed Characters - 50")
    cust_name_entry.config(bg='#B0E2FF')
    cust_name_entry.bind("<F1>", Customer_Search)
    cust_name_entry.bind("<Return>", cus_add_set_focus)
    cust_name_entry.bind("<ButtonRelease>", cust_name_lclick_focus)
    cust_name_entry.bind("<FocusIn>", cust_name_lclick_focus)

    cust_address1_entry = Entry(cust_form,textvariable=cust_address1_entry_tv)
    cust_address1_entry.place(x=130, y=80, width=340)
    cust_address1_entry.bind("<Return>", cus_loc_set_focus)
    cust_address1_entry.bind("<ButtonRelease>", cust_add_lclick_focus)
    cust_address1_entry.bind("<FocusIn>", cust_add_lclick_focus)

    cust_locality_entry = Entry(cust_form,textvariable=cust_locality_entry_tv)
    cust_locality_entry.place(x=130, y=110, width=340)
    cust_locality_entry.bind("<Return>", cus_city_set_focus)
    cust_locality_entry.bind("<ButtonRelease>", cust_loc_lclick_focus)
    cust_locality_entry.bind("<FocusIn>", cust_loc_lclick_focus)

    cust_city_entry = Entry(cust_form,textvariable=cust_city_entry_tv)
    cust_city_entry.place(x=130, y=140, width=100)
    cust_city_entry.bind("<Return>", cus_pin_set_focus)
    cust_city_entry.bind("<ButtonRelease>", cust_city_lclick_focus)
    cust_city_entry.bind("<FocusIn>", cust_city_lclick_focus)

    cust_pincode_entry = Entry(cust_form,textvariable=cust_pincode_entry_tv)
    cust_pincode_entry.place(x=130, y=170, width=100)
    reg = cust_form.register(Validate_Number)
    cust_pincode_entry.config(validate="key", validatecommand=(reg, '%P'))
    cust_pincode_entry.bind("<Return>", cus_state_set_focus)
    cust_pincode_entry.bind("<ButtonRelease>", cust_pin_lclick_focus)
    cust_pincode_entry.bind("<FocusIn>", cust_pin_lclick_focus)

    states_name = ['Tamil Nadu', 'Kerala', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Delhi']
    cust_state_combo = ttk.Combobox(cust_form,value=states_name, state='readonly')
    cust_state_combo.current(0)
    cust_state_combo.place(x=130, y=200)
    cust_state_combo.bind("<Return>", cus_phone_set_focus)
    cust_state_combo.bind("<ButtonRelease>", cust_state_lclick_focus)
    cust_state_combo.bind("<FocusIn>", cust_state_lclick_focus)

    cust_phone_entry = Entry(cust_form,textvariable=cust_phone_entry_tv)
    cust_phone_entry.place(x=130, y=230, width=100)
    reg = cust_form.register(Validate_Number)
    cust_phone_entry.config(validate="key", validatecommand=(reg, '%P'))
    cust_phone_entry.bind("<Return>", cus_email_set_focus)
    cust_phone_entry.bind("<ButtonRelease>", cust_phone_lclick_focus)
    cust_phone_entry.bind("<FocusIn>", cust_phone_lclick_focus)

    cust_email_entry = Entry(cust_form,textvariable=cust_email_entry_tv)
    cust_email_entry.place(x=130, y=260, width=230)
    cust_email_entry.bind("<Return>", cus_gst_set_focus)
    cust_email_entry.bind("<ButtonRelease>", cust_email_lclick_focus)
    cust_email_entry.bind("<FocusIn>", cust_email_lclick_focus)

    cust_gst_no_entry = Entry(cust_form,textvariable=cust_gst_no_entry_tv)
    cust_gst_no_entry.place(x=130, y=290, width=230)
    cust_gst_no_entry.bind("<Return>",cus_update_button_set_focus)
    cust_gst_no_entry.bind("<ButtonRelease>", cust_gst_lclick_focus)
    cust_gst_no_entry.bind("<FocusIn>", cust_gst_lclick_focus)

    # ************** ENTRY BOX SETTINGS - END **************

    # ************* BUTTON SETTINGS - BEGIN ************
    update_button = Button(cust_form, text="Update", font=(14))
    update_button.place(x=340, y=350, width=64)
    update_button.bind("<ButtonRelease>", Update_Button_Click)
    update_button.bind("<Return>", Update_Button_Click)
    update_button.bind("<FocusIn>", Update_Button_FocusIn)

    cancel_button = Button(cust_form, text="Cancel", font=(14))
    cancel_button.place(x=410, y=350, width=64)
    cancel_button.bind("<ButtonRelease>", Cancel_Button_Click)
    cancel_button.bind("<Return>", Cancel_Button_Click)
    cancel_button.bind("<FocusIn>", Cancel_Button_FocusIn)

    # *********** BUTTON SETTINGS - END ********

def Customer_Delete(event):
    global cust_name_entry, cust_address1_entry, cust_locality_entry, cust_city_entry, cust_pincode_entry
    global cust_phone_entry, cust_email_entry, cust_gst_no_entry
    global cust_name_entry_tv, cust_address1_entry_tv, cust_locality_entry_tv, cust_city_entry_tv, cust_pincode_entry_tv
    global cust_state_combo, cust_phone_entry_tv, cust_email_entry_tv, cust_gst_no_entry_tv
    global update_button
    form_name.configure(text="Customer - D E L E T E")
    form_bottom.configure(text="Press [F1] To List Supplier & Select From The List")

    cls2.set_cust_id('')
    cust_name_entry_tv = tk.StringVar()
    cust_address1_entry_tv = tk.StringVar()
    cust_locality_entry_tv = tk.StringVar()
    cust_city_entry_tv = tk.StringVar()
    cust_pincode_entry_tv = tk.StringVar()
    cust_phone_entry_tv = tk.StringVar()
    cust_email_entry_tv = tk.StringVar()
    cust_gst_no_entry_tv = tk.StringVar()

    insert_button.destroy()
    edit_button.destroy()
    delete_button.destroy()
    report_button.destroy()
    quit_button.destroy()

    tabcontrol = ttk.Notebook()

    cust_name_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_name_entry)
    cust_name_entry = Entry(cust_form, textvariable=cust_name_entry_tv)
    cust_name_entry.place(x=130, y=50, width=340)
    cust_name_entry.config(bg='#B0E2FF')
    cust_name_entry.focus_set()
    cust_name_entry.bind("<F1>", Customer_Search)
    cust_name_entry.bind("<Return>", cus_delete_button_set_focus)
    cust_name_entry.bind("<FocusIn>", cust_name_lclick_focus)

    cust_address1_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_address1_entry)
    cust_address1_entry = Entry(cust_form,textvariable=cust_address1_entry_tv)
    cust_address1_entry.place(x=130, y=80, width=340)
    cust_address1_entry.config(state='disable')

    cust_locality_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_locality_entry)
    cust_locality_entry = Entry(cust_form,textvariable=cust_locality_entry_tv)
    cust_locality_entry.place(x=130, y=110, width=340)
    cust_locality_entry.config(state='disable')

    cust_city_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_city_entry)
    cust_city_entry = Entry(cust_form,textvariable=cust_city_entry_tv)
    cust_city_entry.place(x=130, y=140, width=100)
    cust_city_entry.config(state='disable')

    cust_pincode_entry = ttk.Frame(tabcontrol)
    tabcontrol.add((cust_pincode_entry))
    cust_pincode_entry = Entry(cust_form,textvariable=cust_pincode_entry_tv)
    cust_pincode_entry.place(x=130, y=170, width=100)
    cust_pincode_entry.config(state='disable')

    cust_state_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_state_entry)
    states_name = ['Tamil Nadu', 'Kerala', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Delhi']
    cust_state_combo = ttk.Combobox(cust_form,value=states_name, state='disable')
    #combo_box.set('')
    cust_state_combo.current(0)
    cust_state_combo.place(x=130, y=200)

    cust_phone_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_phone_entry)
    cust_phone_entry = Entry(cust_form,textvariable=cust_phone_entry_tv)
    cust_phone_entry.place(x=130, y=230, width=100)
    cust_phone_entry.config(state='disable')

    cust_email_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_email_entry)
    cust_email_entry = Entry(cust_form,textvariable=cust_email_entry_tv)
    cust_email_entry.place(x=130, y=260, width=230)
    cust_email_entry.config(state='disable')

    cust_gst_no_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_gst_no_entry)
    cust_gst_no_entry = Entry(cust_form,textvariable=cust_gst_no_entry_tv)
    cust_gst_no_entry.place(x=130, y=290, width=230)
    cust_gst_no_entry.config(state='disable')

    # ************ ENTRY BOX SETTINGS - END ******************

    # ************ BUTTON SETTINGS - BEGIN ************
    update_button = Button(cust_form, text="Delete", font=(14))
    update_button.place(x=340, y=350, width=64)
    update_button.bind("<Return>", Update_For_Delete_Button_Click)
    update_button.bind("<ButtonRelease>", Update_For_Delete_Button_Click)
    update_button.bind("<FocusIn>", Delete_Button_FocusIn)

    cancel_button = Button(cust_form, text="Cancel", font=(14))
    cancel_button.place(x=410, y=350, width=64)
    cancel_button.bind("<Return>", Cancel_Button_Click)
    cancel_button.bind("<ButtonRelease>", Cancel_Button_Click)
    cancel_button.bind("<FocusIn>", Cancel_Button_FocusIn)

    # ************** BUTTON SETTINGS - END *********

def Customer_report(event):
    global cust_name_entry, cust_address1_entry, cust_locality_entry, cust_city_entry, cust_pincode_entry
    global cust_phone_entry, cust_email_entry, cust_gst_no_entry
    global cust_name_entry_tv, cust_address1_entry_tv, cust_locality_entry_tv, cust_city_entry_tv, cust_pincode_entry_tv
    global cust_state_combo, cust_phone_entry_tv, cust_email_entry_tv, cust_gst_no_entry_tv
    global report_button
    form_name.configure(text="Customer - E X P O R T")
    form_bottom.configure(text="Press [F1] To List Supplier & Select From The List")

    cls2.set_cust_id('')
    cust_name_entry_tv = tk.StringVar()
    cust_address1_entry_tv = tk.StringVar()
    cust_locality_entry_tv = tk.StringVar()
    cust_city_entry_tv = tk.StringVar()
    cust_pincode_entry_tv = tk.StringVar()
    cust_phone_entry_tv = tk.StringVar()
    cust_email_entry_tv = tk.StringVar()
    cust_gst_no_entry_tv = tk.StringVar()

    insert_button.destroy()
    edit_button.destroy()
    delete_button.destroy()
    report_button.destroy()
    quit_button.destroy()

    tabcontrol = ttk.Notebook()

    cust_name_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_name_entry)
    cust_name_entry = Entry(cust_form, textvariable=cust_name_entry_tv)
    cust_name_entry.place(x=130, y=50, width=340)
    cust_name_entry.focus_set()
    cust_name_entry.bind("<F1>", Customer_Search)
    cust_name_entry.bind("<Return>", cus_report_button_set_focus)
    cust_name_entry.bind("<FocusIn>", cust_name_lclick_focus)

    cust_address1_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_address1_entry)
    cust_address1_entry = Entry(cust_form,textvariable=cust_address1_entry_tv)
    cust_address1_entry.place(x=130, y=80, width=340)
    cust_address1_entry.config(state='disable')

    cust_locality_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_locality_entry)
    cust_locality_entry = Entry(cust_form,textvariable=cust_locality_entry_tv)
    cust_locality_entry.place(x=130, y=110, width=340)
    cust_locality_entry.config(state='disable')

    cust_city_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_city_entry)
    cust_city_entry = Entry(cust_form,textvariable=cust_city_entry_tv)
    cust_city_entry.place(x=130, y=140, width=100)
    cust_city_entry.config(state='disable')

    cust_pincode_entry = ttk.Frame(tabcontrol)
    tabcontrol.add((cust_pincode_entry))
    cust_pincode_entry = Entry(cust_form,textvariable=cust_pincode_entry_tv)
    cust_pincode_entry.place(x=130, y=170, width=100)
    cust_pincode_entry.config(state='disable')

    cust_state_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_state_entry)
    states_name = ['Tamil Nadu', 'Kerala', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Delhi']
    cust_state_combo = ttk.Combobox(cust_form,value=states_name, state='disable')
    cust_state_combo.current(0)
    cust_state_combo.place(x=130, y=200)

    cust_phone_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_phone_entry)
    cust_phone_entry = Entry(cust_form,textvariable=cust_phone_entry_tv)
    cust_phone_entry.place(x=130, y=230, width=100)
    cust_phone_entry.config(state='disable')

    cust_email_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_email_entry)
    cust_email_entry = Entry(cust_form,textvariable=cust_email_entry_tv)
    cust_email_entry.place(x=130, y=260, width=230)
    cust_email_entry.config(state='disable')

    cust_gst_no_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(cust_gst_no_entry)
    cust_gst_no_entry = Entry(cust_form,textvariable=cust_gst_no_entry_tv)
    cust_gst_no_entry.place(x=130, y=290, width=230)
    cust_gst_no_entry.config(state='disable')

    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN *****************************************
    report_button = Button(cust_form, text="Export To Excel", font=(14))
    report_button.place(x=220, y=350, width=120)
    report_button.bind("<Return>", Customer_Export_To_Click)
    report_button.bind("<ButtonRelease>", Customer_Export_To_Click)
    report_button.bind("<FocusIn>", Export_Button_FocusIn)

    cancel_button = Button(cust_form, text="Cancel", font=(14))
    cancel_button.place(x=350, y=350, width=120)
    cancel_button.bind("<Return>", Cancel_Button_Click)
    cancel_button.bind("<ButtonRelease>", Cancel_Button_Click)
    cancel_button.bind("<FocusIn>", Cancel_Button_FocusIn)

    # *************************************** BUTTON SETTINGS - END *****************************************

def Customer_Quit(event):
    cust_form.withdraw()

def Save_Button_Click(event):
    name = cust_name_entry_tv.get()
    address = cust_address1_entry_tv.get()
    locality = cust_locality_entry_tv.get()
    city = cust_city_entry_tv.get()
    pincode = cust_pincode_entry_tv.get()
    state = cust_state_combo.get()
    phone = cust_phone_entry_tv.get()
    email = cust_email_entry_tv.get()
    gst_no = cust_gst_no_entry_tv.get()
    c_date = datetime.datetime.now()

    if len(name.strip()) > 0 and len(address.strip()) > 0 and len(locality.strip()) > 0 and len(city.strip()) > 0 \
            and len(pincode.strip()) > 0 and len(state.strip()) > 0 and len(phone.strip()) > 0 and len(email.strip()) > 0 \
            and len(gst_no.strip()) > 0:
        if len(name.strip()) <= 50 and len(address.strip()) <= 100 and len(locality.strip()) <= 25 and len(city.strip()) <=20 \
                and len(pincode.strip()) <= 6 and len(state.strip()) <= 25 and len(phone.strip()) == 10 and len(email.strip()) <= 100 \
                and len(gst_no.strip()) <= 15:

                Cur.execute("select max(id) as id_no from Customer_master")
                for row in Cur:
                    id_no = row[0]

                if id_no == None:
                    id_no = 1
                else:
                    id_no = id_no + 1

                Cur.execute("insert into Customer_master (name,address,locality,city,pincode,state,phone,email,gst,crt_date,id) values('{}','{}','{}','{}',{},'{}',{},'{}','{}','{}',{})".format(name,address,locality,city,pincode,state,phone,email,gst_no,c_date,id_no))
                Con.commit()
                messagebox.showinfo('', "CUSTOMER Details Added Successfully")
                cust_form.destroy()
                cust_Design_Form_Load()
        else:
            messagebox.showwarning('', 'Enter Details As Per The Limitations')
            cust_form.focus_set()
            save_button.focus_set()

    else:
        messagebox.showwarning('', 'Enter Data In All Fields')
        cust_form.focus_set()
        save_button.focus_set()

def cust_entry_clear():
     cust_name_entry_tv.set('')
     cust_address1_entry_tv.set('')
     cust_locality_entry_tv.set('')
     cust_city_entry_tv.set('')
     cust_pincode_entry_tv.set('')
     cust_state_combo.set('')
     cust_phone_entry_tv.set('')
     cust_email_entry_tv.set('')
     cust_gst_no_entry_tv.set('')
     cust_state_combo.current(0)
     cust_name_entry.focus_set()

def Refresh_cust_Data():
    for item in tree.get_children():
        tree.delete(item)

    Cur.execute("select * from Customer_master order by name")

    i = 0
    for row in Cur:
        tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        i = i + 1

def Refresh_cust_Data2(records):
    for item in tree.get_children():
        tree.delete(item)

    i = 0
    for row in records:
        tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        i = i + 1


def Customer_Export_To_Click(event):
    customer_header = ["Name", "Address", "Locality", "City", "Pincode", "State", "Phone", "Email", "GST"]
    Cur.execute("select name, address, locality, city, pincode, state, phone, email, gst from customer_master  where name like '%{}%' order by name".format(cust_name_entry.get()))
    customer_data = []
    for row in Cur.fetchall():
        customer_data.append(row)

    cls_rep.export_to_excel("Customer List.xlsx", "List", customer_header, customer_data, "C U S T O M E R    L I S T")
    filepath = r'C:\Users\SYED\AcubeProjects\Status Plus\Customer List.xlsx'
    os.startfile(filepath)
    cust_form.focus_set()
    cust_name_entry.focus_set()


def Update_Button_Click(event):
    name = cust_name_entry_tv.get()
    address = cust_address1_entry_tv.get()
    locality = cust_locality_entry_tv.get()
    city = cust_city_entry_tv.get()
    pincode = cust_pincode_entry_tv.get()
    state = cust_state_combo.get()
    phone = cust_phone_entry_tv.get()
    email = cust_email_entry_tv.get()
    gst_no = cust_gst_no_entry_tv.get()
    c_date = datetime.datetime.now()
    s_id = cls2.get_cust_id()

    if len(name.strip()) > 0 and len(address.strip()) > 0 and len(locality.strip()) > 0 and len(city.strip()) > 0 \
        and len(pincode.strip()) > 0 and len(state.strip()) > 0 and len(phone.strip()) > 0 and len(email.strip()) > 0 \
        and len(gst_no.strip()) > 0:

            #Cur.execute("update Customer_master set (name,address,locality,city,pincode,state,phone,email,gst,crt_date) values('{}','{}','{}','{}',{},'{}',{},'{}','{}','{}') where id={}".format(name,address,locality,city,pincode,state,phone,email,gst_no,c_date,s_id))
            qry ="update Customer_master set name= '{}',address= '{}',locality= '{}',city= '{}',pincode={}, \
                 state='{}',phone={},email='{}',gst= '{}',crt_date= '{}' where id={}".format(name, address,
                 locality,city,pincode, state, phone, email, gst_no, c_date, s_id)

            Cur.execute(qry)
            Con.commit()
            messagebox.showinfo('', "CUSTOMER Details Updated Successfully")
            cust_entry_clear()
            Refresh_cust_Data()
    else:
       messagebox.showwarning('', 'Enter Data In All Fields')
       cust_form.focus_set()
       update_button.focus_set()


def Update_For_Delete_Button_Click(event):
    name = cust_name_entry_tv.get()
    address = cust_address1_entry_tv.get()
    locality = cust_locality_entry_tv.get()
    city = cust_city_entry_tv.get()
    pincode = cust_pincode_entry_tv.get()
    state = cust_state_combo.get()
    phone = cust_phone_entry_tv.get()
    email = cust_email_entry_tv.get()
    gst_no = cust_gst_no_entry_tv.get()
    c_date = datetime.datetime.now()
    s_id = cls2.get_cust_id()

    if len(name.strip()) > 0 and len(address.strip()) > 0 and len(locality.strip()) > 0 and len(city.strip()) > 0 \
        and len(pincode.strip()) > 0 and len(state.strip()) > 0 and len(phone.strip()) > 0 and len(email.strip()) > 0 \
        and len(gst_no.strip()) > 0:

            qry ="delete from  Customer_master where id= {}".format(s_id)
            Cur.execute(qry)
            Con.commit()
            tree.delete(item)
            messagebox.showinfo('', "CUSTOMER Details Deleted Successfully")
            cust_entry_clear()
            Refresh_cust_Data()
    else:
        messagebox.showwarning('', 'Select CUSTOMER From List')
        cust_form.focus_set()
        update_button.focus_set()

def Cancel_Button_Click(event):

    result = messagebox.askquestion('', message='Do You Want To Cancel')
    if result == 'yes':
        cust_form.destroy()
        cust_Design_Form_Load()
    else:
        cust_form.focus_set()
        cust_name_entry.focus_set()

def Customer_Search(event):
    qry = "select * from Customer_master where name LIKE '"+cust_name_entry.get()+"%' order by name"
    Cur.execute(qry)
    records = Cur.fetchall()
    Refresh_cust_Data2(records)

def Validate_Number(inp):
    if inp.isdigit():
        return True
    elif inp == "":
        return True
    else:
        return False


def Select_Customer_Data(event):
    global item
    item=tree.selection()
    global cur_name
    for i in item:
        if len(tree.item(i, 'values')[0]) > 0:
            cust_name_entry_tv.set(tree.item(i,'values')[0])
            cust_address1_entry_tv.set(tree.item(i,'values')[1])
            cust_locality_entry_tv.set(tree.item(i,'values')[2])
            cust_city_entry_tv.set(tree.item(i,'values')[3])
            cust_pincode_entry_tv.set(tree.item(i,'values')[4])
            cust_state_combo.set(tree.item(i,'values')[5])
            cust_phone_entry_tv.set(tree.item(i,'values')[6])
            cust_email_entry_tv.set(tree.item(i,'values')[7])
            cust_gst_no_entry_tv.set(tree.item(i,'values')[8])
            cls2.set_cust_id(tree.item(i,'values')[10])
        else:
            pass

def cust_Design_Form_Load():
    global cust_form, form_name
    global form_bottom
    cls2.set_cust_record_found(0)
    cust_form = tk.Toplevel()
    cust_form.geometry('1300x450+25+100')
    cust_form.config(bg='white')
    cust_form.focus_set()
    cust_form.title('Customer')
    cust_form.resizable(False,False)

    form_name=Label(cust_form,text="C U S T O M E R", fg="black", bg="#63B8FF", width=500, font=('copper', 20, 'bold'))
    form_name.pack(side=TOP)
    form_bottom=Label(cust_form,text="",bg="#63B8FF", width=500, height=2, font=('bold',10))
    form_bottom.pack(side=BOTTOM)

    # *************************************** LABEL SETTINGS - BEGIN *******************************************
    cust_name = Label(cust_form, text="Customer Name", bg='white', fg='black', font=(12))
    cust_name.place(x=12, y=50)
    cust_address = Label(cust_form, text="Address", bg='white', fg='black', font=(12))
    cust_address.place(x=12, y=80)
    cust_locality = Label(cust_form, text="Locality", bg='white', fg='black', font=(12))
    cust_locality.place(x=12, y=110)
    cust_city = Label(cust_form, text="City", bg='white', fg='black', font=(12))
    cust_city.place(x=12, y=140)
    cust_pincode = Label(cust_form, text="Pincode", bg='white', fg='black', font=(12))
    cust_pincode.place(x=12, y=170)
    cust_state = Label(cust_form, text="State", bg='white', fg='black', font=(12))
    cust_state.place(x=12, y=200)
    cust_phone = Label(cust_form, text="Phone", bg='white', fg='black', font=(12))
    cust_phone.place(x=12, y=230)
    cust_email = Label(cust_form, text="Email", bg='white', fg='black', font=(12))
    cust_email.place(x=12, y=260)
    cust_gst_no = Label(cust_form, text="GST No.", bg='white', fg='black', font=(12))
    cust_gst_no.place(x=12, y=290)
    # *************************************** LABEL SETTINGS - END ********************************************

    # *************************************** ENTRY BOX SETTINGS - BEGIN **************************************

    cust_name_entry = Entry(cust_form)
    cust_name_entry.place(x=130, y=50, width=340)
    cust_name_entry.config(state='disable')

    cust_address1_entry = Entry(cust_form)
    cust_address1_entry.place(x=130, y=80, width=340)
    cust_address1_entry.config(state='disable')

    cust_locality_entry = Entry(cust_form)
    cust_locality_entry.place(x=130, y=110, width=340)
    cust_locality_entry.config(state='disable')

    cust_city_entry = Entry(cust_form)
    cust_city_entry.place(x=130, y=140, width=100)
    cust_city_entry.config(state='disable')

    cust_pincode_entry = Entry(cust_form)
    cust_pincode_entry.place(x=130, y=170, width=100)
    cust_pincode_entry.config(state='disable')

    states_name = ['Tamil Nadu', 'Kerala', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Delhi']
    combo_box = ttk.Combobox(cust_form,value=states_name, state='disable')
    combo_box.set('')
    #combo_box.current(0)
    combo_box.place(x=130, y=200)

    cust_phone_entry = Entry(cust_form)
    cust_phone_entry.place(x=130, y=230, width=100)
    cust_phone_entry.config(state='disable')

    cust_email_entry = Entry(cust_form)
    cust_email_entry.place(x=130, y=260, width=230)
    cust_email_entry.config(state='disable')

    cust_gst_no_entry = Entry(cust_form)
    cust_gst_no_entry.place(x=130, y=290, width=230)
    cust_gst_no_entry.config(state='disable')
    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN ******************************************
    global insert_button, edit_button, delete_button, report_button, quit_button


    insert_button = Button(cust_form,text="Insert", font=(14))
    insert_button.place(x=130, y=350, width=64)
    insert_button.focus_set()
    insert_button.bind('<Return>',Customer_Insert)
    insert_button.bind('<ButtonRelease>', Customer_Insert)
    insert_button.bind('<FocusIn>', Main_Button_FocusIn)

    edit_button = Button(cust_form, text="Edit", font=(14))
    edit_button.place(x=200, y=350, width=64)
    edit_button.bind('<Return>', Customer_Edit)
    edit_button.bind('<ButtonRelease>', Customer_Edit)
    edit_button.bind('<FocusIn>', Main_Button_FocusIn)

    delete_button = Button(cust_form, text="Delete", font=(14))
    delete_button.place(x=270, y=350, width=64)
    delete_button.bind("<Return>", Customer_Delete)
    delete_button.bind("<ButtonRelease>", Customer_Delete)
    delete_button.bind('<FocusIn>', Main_Button_FocusIn)

    report_button = Button(cust_form, text="Report", font=(14))
    report_button.place(x=340, y=350, width=64)
    report_button.bind("<Return>", Customer_report)
    report_button.bind("<ButtonRelease>", Customer_report)
    report_button.bind('<FocusIn>', Main_Button_FocusIn)

    quit_button = Button(cust_form, text="Quit", font=(14))
    quit_button.place(x=410, y=350, width=64)
    quit_button.bind("<Return>", Customer_Quit)
    quit_button.bind("<ButtonRelease>", Customer_Quit)
    quit_button.bind('<FocusIn>', Main_Button_FocusIn)

    # *************************************** BUTTON SETTINGS - END ********************************************
    # *************************************** TREE VIEW  - BEGIN *******************************************
    global tree
    cust_frame = Frame(cust_form)
    cust_frame.pack(pady=5)
    cust_frame.place(x=480, y=50)
    cust_frame.pack_propagate(False)
    cust_frame.configure(width=800, height=335, bg='#63B8FF')

    Cur.execute('select * from Customer_master order by name')
    col = ('name', 'address', 'locality', 'city', 'pincode', 'state', 'phone', 'email', 'gst_no', 'crt_date', 'id')
    tree = ttk.Treeview(cust_frame, height=14, show='headings', columns=col)
    # tree['show']='headings'
    tree.pack(fill=tk.X,pady=5)
    style1 = ttk.Style(cust_frame)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading",foreground='#63B8FF', background='grey18', font='14')
    style1.configure("Treeview", foreground='black', background='white', fieldbackground='white',
                     font=('times new roman', 12))
    style1.map('Treeview', background=[('selected', '#63B8FF')])

    tree.column("name", width=200, minwidth=50, anchor=tk.W)
    tree.column("address", width=350, minwidth=50, anchor=tk.W)
    tree.column("locality", width=125, minwidth=50, anchor=tk.W)
    tree.column("city", width=121, minwidth=50, anchor=tk.W)
    tree.column("pincode", width=80, minwidth=50, anchor=tk.W)
    tree.column("state", width=150, minwidth=50, anchor=tk.W)
    tree.column("phone", width=100, minwidth=50, anchor=tk.W)
    tree.column("email", width=200, minwidth=50, anchor=tk.W)
    tree.column("gst_no", width=150, minwidth=50, anchor=tk.W)
    tree.column("crt_date", width=0, minwidth=0, anchor=tk.CENTER)
    tree.column("id", width=80, minwidth=10, anchor=tk.CENTER)

    tree.heading("name", text="Customer NAME", anchor=tk.W)
    tree.heading("address", text="ADDRESS", anchor=tk.W)
    tree.heading("locality", text="LOCALITY", anchor=tk.W)
    tree.heading("city", text="CITY", anchor=tk.W)
    tree.heading("pincode", text="PINCODE", anchor=tk.W)
    tree.heading("state", text="STATE", anchor=tk.W)
    tree.heading("phone", text="PHONE", anchor=tk.W)
    tree.heading("email", text="EMAIL", anchor=tk.W)
    tree.heading("gst_no", text="GST NO.", anchor=tk.W)
    tree.heading("crt_date", text="CREATED ON", anchor=tk.CENTER)
    tree.heading("id", text="ID", anchor=tk.CENTER)

    i = 0
    for row in Cur:
        i = i + 1

    vsb = ttk.Scrollbar(cust_frame, orient="vertical")
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(cust_frame, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)

    tree.pack()
    tree.bind("<Return>", Select_Customer_Data)
    tree.bind("<ButtonRelease>", Select_Customer_Data)
    tree.bind("<FocusIn>", Tree_FocusIn)

    # *************************************** TREE VIEW  - END *******************************************
