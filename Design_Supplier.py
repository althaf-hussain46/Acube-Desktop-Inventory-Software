import os
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
from Show_Data import*
from Class_Supplier import*
from Class_Main_Window import*
from Class_Report import*
from DB_Connection import*


cls2 = Cls_Supplier_Master()
cls_sup = cls_main_window()
cls_rep = cls_report()
Con = DB_Connect()
Cur = Con.cursor()

def supp_name_lclick_focus(event):
    form_bottom.configure(text='Press [F1] To List Supplier     Maximum Allowed Characters - 50')
    supp_name_entry.focus_set()

def supp_add_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Characters - 100')
    supp_address1_entry.focus_set()

def supp_loc_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Characters - 25')
    supp_locality_entry.focus_set()

def supp_city_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Characters - 20')
    supp_city_entry.focus_set()

def supp_pin_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Numbers - 6')
    supp_pincode_entry.focus_set()

def supp_state_lclick_focus(event):
    form_bottom.configure(text='Select From Dropdown Box')
    supp_state_combo.focus_set()

def supp_phone_lclick_focus(event):
    form_bottom.configure(text='Must Be 10 Numbers')
    supp_phone_entry.focus_set()

def supp_email_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Characters - 100')
    supp_email_entry.focus_set()

def supp_gst_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Characters - 15')
    supp_gst_no_entry.focus_set()

def sup_add_set_focus(event):
    if len(supp_name_entry.get()) >= 1 and len(supp_name_entry.get()) <= 50:
        form_bottom.configure(text='Maximum Allowed Characters - 100')
        supp_address1_entry.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 50')
        supp_form.focus_set()
        supp_name_entry.focus_set()

def sup_loc_set_focus(event):
    if len(supp_address1_entry.get()) >= 1 and len(supp_address1_entry.get()) <= 100:
        form_bottom.configure(text='Maximum Allowed Characters - 25')
        supp_locality_entry.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 100')
        supp_form.focus_set()
        supp_address1_entry.focus_set()

def sup_city_set_focus(event):
    if len(supp_locality_entry.get()) >= 1 and len(supp_locality_entry.get()) <= 25:
        form_bottom.configure(text='Maximum Allowed Characters - 20')
        supp_city_entry.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 25')
        supp_form.focus_set()
        supp_locality_entry.focus_set()

def sup_pin_set_focus(event):
    if len(supp_city_entry.get()) >= 1 and len(supp_city_entry.get()) <= 20:
        form_bottom.configure(text='Maximum Allowed Numbers - 6')
        supp_pincode_entry.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 20')
        supp_form.focus_set()
        supp_city_entry.focus_set()

def sup_state_set_focus(event):
    if len(supp_pincode_entry.get()) >= 1 and len(supp_pincode_entry.get()) <= 6:
        form_bottom.configure(text='Select State From Dropdown List')
        supp_state_combo.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Numbers  - 6')
        supp_form.focus_set()
        supp_pincode_entry.focus_set()

def sup_phone_set_focus(event):
    if len(supp_state_combo.get()) > 0:
        form_bottom.configure(text='Must Be 10 Numbers')
        supp_phone_entry.focus_set()
    else:
        messagebox.showinfo('', 'Select State From Dropdown List')
        supp_form.focus_set()
        supp_state_combo.focus_set()

def sup_email_set_focus(event):
    if len(supp_phone_entry.get()) == 10:
        form_bottom.configure(text='Maximum Allowed Characters - 100')
        supp_email_entry.focus_set()
    else:
        messagebox.showinfo('', 'Must Be 10 Numbers')
        supp_form.focus_set()
        supp_phone_entry.focus_set()

def sup_gst_set_focus(event):
    if len(supp_email_entry.get()) >= 1 and len(supp_email_entry.get()) <= 100:
        form_bottom.configure(text='Maximum Allowed Characters - 15')
        supp_gst_no_entry.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 100')
        supp_form.focus_set()
        supp_email_entry.focus_set()

def Main_Button_FocusIn(event):
    form_bottom.configure(text="To Create SUPPLIER Press - [Insert]     To Update SUPPLIER Press - [Edit]     To Remove SUPPLIER Press - [Delete]     To Report SUPPLIER Press - [Report]     Press [Tab] - Key To Move To Next Button")

def Save_Button_FocusIn(event):
    form_bottom.configure(text='Press [Enter] To Save SUPPLIER Details')

def Update_Button_FocusIn(event):
    form_bottom.configure(text='Press [Enter] To Update The Changes You Have Made')

def Cancel_Button_FocusIn(event):
    form_bottom.configure(text='Press [Enter] To Cancel The Changes You Have Made')

def Delete_Button_FocusIn(event):
    form_bottom.configure(text='Press [Enter] To Delete The SUPPLIER Details')

def Export_Button_FocusIn(event):
    form_bottom.configure(text='Press [Enter] To Export The SUPPLIER Details')

def Tree_FocusIn(event):
    form_bottom.configure(text='Select From The List To Insert Or Edit Or Delete Or Export The SUPPLIER Details')
    tree.focus_set()

def sup_save_button_set_focus(event):
    if len(supp_gst_no_entry.get()) >= 1 and len(supp_gst_no_entry.get()) <= 15:
        form_bottom.configure(text='Press [Enter] To Save')
        save_button.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 15')
        supp_form.focus_set()
        supp_gst_no_entry.focus_set()

def sup_update_button_set_focus(event):
    if len(supp_gst_no_entry.get()) >= 1 and len(supp_gst_no_entry.get()) <= 15:
        form_bottom.configure(text='Press [Enter] To Save')
        update_button.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 15')
        supp_form.focus_set()
        supp_gst_no_entry.focus_set()

def sup_delete_button_set_focus(event):
    update_button.focus_set()

def sup_report_button_set_focus(event):
    report_button.focus_set()

def Supplier_Insert(event):
    global supp_name_entry, supp_address1_entry, supp_locality_entry, supp_city_entry, supp_pincode_entry
    global supp_phone_entry, supp_email_entry, supp_gst_no_entry
    global supp_name_entry_tv, supp_address1_entry_tv, supp_locality_entry_tv, supp_city_entry_tv, supp_pincode_entry_tv
    global supp_state_combo, supp_phone_entry_tv, supp_email_entry_tv, supp_gst_no_entry_tv
    global save_button
    form_name.configure(text="Supplier - I N S E R T")

    cls2.set_supp_record_found('0')
    supp_name_entry_tv = tk.StringVar()
    supp_address1_entry_tv = tk.StringVar()
    supp_locality_entry_tv = tk.StringVar()
    supp_city_entry_tv = tk.StringVar()
    supp_pincode_entry_tv = tk.StringVar()
    supp_phone_entry_tv = tk.StringVar()
    supp_email_entry_tv = tk.StringVar()
    supp_gst_no_entry_tv = tk.StringVar()

    insert_button.destroy()
    edit_button.destroy()
    delete_button.destroy()
    report_button.destroy()
    quit_button.destroy()

    supp_name_entry = Entry(supp_form, textvariable=supp_name_entry_tv)
    supp_name_entry.place(x=130, y=50, width=340)
    supp_name_entry.focus_set()
    form_bottom.configure(text="Press [F1] To List Supplier     Maximum Allowed Characters - 50")
    supp_name_entry.config(bg='#87CEFA')
    supp_name_entry.bind("<F1>", Supplier_Search)
    supp_name_entry.bind("<Return>", sup_add_set_focus)
    supp_name_entry.bind("<ButtonRelease>", supp_name_lclick_focus)
    supp_name_entry.bind("<FocusIn>", supp_name_lclick_focus)

    supp_address1_entry = Entry(supp_form,textvariable=supp_address1_entry_tv)
    supp_address1_entry.place(x=130, y=80, width=340)
    supp_address1_entry.bind("<Return>",sup_loc_set_focus)
    supp_address1_entry.bind("<ButtonRelease>", supp_add_lclick_focus)
    supp_address1_entry.bind("<FocusIn>", supp_add_lclick_focus)

    supp_locality_entry = Entry(supp_form,textvariable=supp_locality_entry_tv)
    supp_locality_entry.place(x=130, y=110, width=340)
    supp_locality_entry.bind("<Return>",sup_city_set_focus)
    supp_locality_entry.bind("<ButtonRelease>", supp_loc_lclick_focus)
    supp_locality_entry.bind("<FocusIn>", supp_loc_lclick_focus)

    supp_city_entry = Entry(supp_form,textvariable=supp_city_entry_tv)
    supp_city_entry.place(x=130, y=140, width=100)
    supp_city_entry.bind("<Return>",sup_pin_set_focus)
    supp_city_entry.bind("<ButtonRelease>", supp_city_lclick_focus)
    supp_city_entry.bind("<FocusIn>", supp_city_lclick_focus)

    supp_pincode_entry = Entry(supp_form,textvariable=supp_pincode_entry_tv)
    supp_pincode_entry.place(x=130, y=170, width=100)
    reg = supp_form.register(Validate_Number)
    supp_pincode_entry.config(validate="key",validatecommand=(reg,'%P'))
    supp_pincode_entry.bind("<Return>",sup_state_set_focus)
    supp_pincode_entry.bind("<ButtonRelease>", supp_pin_lclick_focus)
    supp_pincode_entry.bind("<FocusIn>", supp_pin_lclick_focus)

    states_name = ['Tamil Nadu', 'Kerala', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Delhi']
    supp_state_combo = ttk.Combobox(supp_form,value=states_name, state='readonly')
    supp_state_combo.current(0)
    supp_state_combo.place(x=130, y=200)
    supp_state_combo.bind("<Return>",sup_phone_set_focus)
    supp_state_combo.bind("<ButtonRelease>", supp_state_lclick_focus)
    supp_state_combo.bind("<FocusIn>", supp_state_lclick_focus)

    supp_phone_entry = Entry(supp_form,textvariable=supp_phone_entry_tv)
    supp_phone_entry.place(x=130, y=230, width=100)
    reg = supp_form.register(Validate_Number)
    supp_phone_entry.config(validate="key", validatecommand=(reg, '%P'))
    supp_phone_entry.bind("<Return>",sup_email_set_focus)
    supp_phone_entry.bind("<ButtonRelease>", supp_phone_lclick_focus)
    supp_phone_entry.bind("<FocusIn>", supp_phone_lclick_focus)

    supp_email_entry = Entry(supp_form,textvariable=supp_email_entry_tv)
    supp_email_entry.place(x=130, y=260, width=230)
    supp_email_entry.bind("<Return>",sup_gst_set_focus)
    supp_email_entry.bind("<ButtonRelease>", supp_email_lclick_focus)
    supp_email_entry.bind("<FocusIn>", supp_email_lclick_focus)

    supp_gst_no_entry = Entry(supp_form,textvariable=supp_gst_no_entry_tv)
    supp_gst_no_entry.place(x=130, y=290, width=230)
    supp_gst_no_entry.bind("<Return>",sup_save_button_set_focus)
    supp_gst_no_entry.bind("<ButtonRelease>", supp_gst_lclick_focus)
    supp_gst_no_entry.bind("<FocusIn>", supp_gst_lclick_focus)
    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN *****************************************
    save_button = Button(supp_form, text="Save", font=(14))
    save_button.place(x=340, y=350, width=64)
    save_button.bind("<ButtonRelease>", Save_Button_Click)
    save_button.bind("<Return>",Save_Button_Click)
    save_button.bind("<FocusIn>", Save_Button_FocusIn)

    cancel_button = Button(supp_form, text="Cancel", font=(14))
    cancel_button.place(x=410, y=350, width=64)
    cancel_button.bind("<ButtonRelease>",Cancel_Button_Click)
    cancel_button.bind("<Return>",Cancel_Button_Click)
    cancel_button.bind("<FocusIn>", Cancel_Button_FocusIn)
    # *************************************** BUTTON SETTINGS - END *****************************************


def Supplier_Edit(event):
    global supp_name_entry, supp_address1_entry, supp_locality_entry, supp_city_entry, supp_pincode_entry
    global supp_phone_entry, supp_email_entry, supp_gst_no_entry
    global supp_name_entry_tv, supp_address1_entry_tv, supp_locality_entry_tv, supp_city_entry_tv, supp_pincode_entry_tv
    global supp_state_combo, supp_phone_entry_tv, supp_email_entry_tv, supp_gst_no_entry_tv
    global update_button
    form_name.configure(text="Supplier - E D I T")

    cls2.set_supp_id('')
    supp_name_entry_tv = tk.StringVar()
    supp_address1_entry_tv = tk.StringVar()
    supp_locality_entry_tv = tk.StringVar()
    supp_city_entry_tv = tk.StringVar()
    supp_pincode_entry_tv = tk.StringVar()
    supp_phone_entry_tv = tk.StringVar()
    supp_email_entry_tv = tk.StringVar()
    supp_gst_no_entry_tv = tk.StringVar()

    insert_button.destroy()
    edit_button.destroy()
    delete_button.destroy()
    report_button.destroy()
    quit_button.destroy()

    supp_name_entry = Entry(supp_form, textvariable=supp_name_entry_tv)
    supp_name_entry.place(x=130, y=50, width=340)
    supp_name_entry.focus_set()
    form_bottom.configure(text="Press [F1] To List Supplier     Maximum Allowed Characters - 50")
    supp_name_entry.config(bg='#87CEFA')
    supp_name_entry.bind("<F1>", Supplier_Search)
    supp_name_entry.bind("<Return>", sup_add_set_focus)
    supp_name_entry.bind("<ButtonRelease>", supp_name_lclick_focus)
    supp_name_entry.bind("<FocusIn>", supp_name_lclick_focus)

    supp_address1_entry = Entry(supp_form,textvariable=supp_address1_entry_tv)
    supp_address1_entry.place(x=130, y=80, width=340)
    supp_address1_entry.bind("<Return>", sup_loc_set_focus)
    supp_address1_entry.bind("<ButtonRelease>", supp_add_lclick_focus)
    supp_address1_entry.bind("<FocusIn>", supp_add_lclick_focus)

    supp_locality_entry = Entry(supp_form,textvariable=supp_locality_entry_tv)
    supp_locality_entry.place(x=130, y=110, width=340)
    supp_locality_entry.bind("<Return>", sup_city_set_focus)
    supp_locality_entry.bind("<ButtonRelease>", supp_loc_lclick_focus)

    supp_city_entry = Entry(supp_form,textvariable=supp_city_entry_tv)
    supp_city_entry.place(x=130, y=140, width=100)
    supp_city_entry.bind("<Return>", sup_pin_set_focus)
    supp_city_entry.bind("<ButtonRelease>", supp_city_lclick_focus)
    supp_city_entry.bind("<FocusIn>", supp_city_lclick_focus)

    supp_pincode_entry = Entry(supp_form,textvariable=supp_pincode_entry_tv)
    supp_pincode_entry.place(x=130, y=170, width=100)
    reg = supp_form.register(Validate_Number)
    supp_pincode_entry.config(validate="key", validatecommand=(reg, '%P'))
    supp_pincode_entry.bind("<Return>", sup_state_set_focus)
    supp_pincode_entry.bind("<ButtonRelease>", supp_pin_lclick_focus)
    supp_pincode_entry.bind("<FocusIn>", supp_pin_lclick_focus)

    states_name = ['Tamil Nadu', 'Kerala', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Delhi']
    supp_state_combo = ttk.Combobox(supp_form,value=states_name, state='readonly')
    supp_state_combo.current(0)
    supp_state_combo.place(x=130, y=200)
    supp_state_combo.bind("<Return>", sup_phone_set_focus)
    supp_state_combo.bind("<ButtonRelease>", supp_state_lclick_focus)
    supp_state_combo.bind("<FocusIn>", supp_state_lclick_focus)

    supp_phone_entry = Entry(supp_form,textvariable=supp_phone_entry_tv)
    supp_phone_entry.place(x=130, y=230, width=100)
    reg = supp_form.register(Validate_Number)
    supp_phone_entry.config(validate="key", validatecommand=(reg, '%P'))
    supp_phone_entry.bind("<Return>", sup_email_set_focus)
    supp_phone_entry.bind("<ButtonRelease>", supp_phone_lclick_focus)
    supp_phone_entry.bind("<FocusIn>", supp_phone_lclick_focus)


    supp_email_entry = Entry(supp_form,textvariable=supp_email_entry_tv)
    supp_email_entry.place(x=130, y=260, width=230)
    supp_email_entry.bind("<Return>", sup_gst_set_focus)
    supp_email_entry.bind("<ButtonRelease>", supp_email_lclick_focus)
    supp_email_entry.bind("<FocusIn>", supp_email_lclick_focus)

    supp_gst_no_entry = Entry(supp_form,textvariable=supp_gst_no_entry_tv)
    supp_gst_no_entry.place(x=130, y=290, width=230)
    supp_gst_no_entry.bind("<Return>",sup_update_button_set_focus)
    supp_gst_no_entry.bind("<ButtonRelease>", supp_gst_lclick_focus)
    supp_gst_no_entry.bind("<FocusIn>", supp_gst_lclick_focus)


    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN *****************************************
    update_button = Button(supp_form, text="Update", font=(14))
    update_button.place(x=340, y=350, width=64)
    update_button.bind("<ButtonRelease>", Update_Button_Click)
    update_button.bind("<Return>", Update_Button_Click)
    update_button.bind("<FocusIn>", Update_Button_FocusIn)

    cancel_button = Button(supp_form, text="Cancel", font=(14))
    cancel_button.place(x=410, y=350, width=64)
    cancel_button.bind("<ButtonRelease>", Cancel_Button_Click)
    cancel_button.bind("<Return>", Cancel_Button_Click)
    cancel_button.bind("<FocusIn>", Cancel_Button_FocusIn)

    # *************************************** BUTTON SETTINGS - END *****************************************

def Supplier_Delete(event):
    global supp_name_entry, supp_address1_entry, supp_locality_entry, supp_city_entry, supp_pincode_entry
    global supp_phone_entry, supp_email_entry, supp_gst_no_entry
    global supp_name_entry_tv, supp_address1_entry_tv, supp_locality_entry_tv, supp_city_entry_tv, supp_pincode_entry_tv
    global supp_state_combo, supp_phone_entry_tv, supp_email_entry_tv, supp_gst_no_entry_tv
    global update_button
    form_name.configure(text="Supplier - D E L E T E")
    form_bottom.configure(text="Press [F1] To List Supplier & Select From The List")

    cls2.set_supp_id('')
    supp_name_entry_tv = tk.StringVar()
    supp_address1_entry_tv = tk.StringVar()
    supp_locality_entry_tv = tk.StringVar()
    supp_city_entry_tv = tk.StringVar()
    supp_pincode_entry_tv = tk.StringVar()
    supp_phone_entry_tv = tk.StringVar()
    supp_email_entry_tv = tk.StringVar()
    supp_gst_no_entry_tv = tk.StringVar()

    insert_button.destroy()
    edit_button.destroy()
    delete_button.destroy()
    report_button.destroy()
    quit_button.destroy()

    tabcontrol = ttk.Notebook()

    supp_name_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_name_entry)
    supp_name_entry = Entry(supp_form, textvariable=supp_name_entry_tv, bg='#87CEFA')
    supp_name_entry.place(x=130, y=50, width=340)
    supp_name_entry.focus_set()
    supp_name_entry.bind("<F1>", Supplier_Search)
    supp_name_entry.bind("<Return>", sup_delete_button_set_focus)
    supp_name_entry.bind("<FocusIn>", supp_name_lclick_focus)

    supp_address1_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_address1_entry)
    supp_address1_entry = Entry(supp_form,textvariable=supp_address1_entry_tv)
    supp_address1_entry.place(x=130, y=80, width=340)
    supp_address1_entry.config(state='disable')

    supp_locality_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_locality_entry)
    supp_locality_entry = Entry(supp_form,textvariable=supp_locality_entry_tv)
    supp_locality_entry.place(x=130, y=110, width=340)
    supp_locality_entry.config(state='disable')

    supp_city_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_city_entry)
    supp_city_entry = Entry(supp_form,textvariable=supp_city_entry_tv)
    supp_city_entry.place(x=130, y=140, width=100)
    supp_city_entry.config(state='disable')

    supp_pincode_entry = ttk.Frame(tabcontrol)
    tabcontrol.add((supp_pincode_entry))
    supp_pincode_entry = Entry(supp_form,textvariable=supp_pincode_entry_tv)
    supp_pincode_entry.place(x=130, y=170, width=100)
    supp_pincode_entry.config(state='disable')

    supp_state_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_state_entry)
    states_name = ['Tamil Nadu', 'Kerala', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Delhi']
    supp_state_combo = ttk.Combobox(supp_form,value=states_name, state='disable')
    #combo_box.set('')
    supp_state_combo.current(0)
    supp_state_combo.place(x=130, y=200)

    supp_phone_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_phone_entry)
    supp_phone_entry = Entry(supp_form,textvariable=supp_phone_entry_tv)
    supp_phone_entry.place(x=130, y=230, width=100)
    supp_phone_entry.config(state='disable')

    supp_email_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_email_entry)
    supp_email_entry = Entry(supp_form,textvariable=supp_email_entry_tv)
    supp_email_entry.place(x=130, y=260, width=230)
    supp_email_entry.config(state='disable')

    supp_gst_no_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_gst_no_entry)
    supp_gst_no_entry = Entry(supp_form,textvariable=supp_gst_no_entry_tv)
    supp_gst_no_entry.place(x=130, y=290, width=230)
    supp_gst_no_entry.config(state='disable')

    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN *****************************************
    update_button = Button(supp_form, text="Delete", font=(14))
    update_button.place(x=340, y=350, width=64)
    update_button.bind("<Return>", Update_For_Delete_Button_Click)
    update_button.bind("<ButtonRelease>", Update_For_Delete_Button_Click)
    update_button.bind("<FocusIn>", Delete_Button_FocusIn)

    cancel_button = Button(supp_form, text="Cancel", font=(14))
    cancel_button.place(x=410, y=350, width=64)
    cancel_button.bind("<Return>", Cancel_Button_Click)
    cancel_button.bind("<ButtonRelease>", Cancel_Button_Click)
    cancel_button.bind("<FocusIn>", Cancel_Button_FocusIn)

    # *************************************** BUTTON SETTINGS - END *****************************************

def Supplier_Report(event):
    global supp_name_entry, supp_address1_entry, supp_locality_entry, supp_city_entry, supp_pincode_entry
    global supp_phone_entry, supp_email_entry, supp_gst_no_entry
    global supp_name_entry_tv, supp_address1_entry_tv, supp_locality_entry_tv, supp_city_entry_tv, supp_pincode_entry_tv
    global supp_state_combo, supp_phone_entry_tv, supp_email_entry_tv, supp_gst_no_entry_tv
    global report_button
    form_name.configure(text="Supplier - E X P O R T")
    form_bottom.configure(text="Press [F1] To List Supplier & Select From The List")

    cls2.set_supp_id('')
    supp_name_entry_tv = tk.StringVar()
    supp_address1_entry_tv = tk.StringVar()
    supp_locality_entry_tv = tk.StringVar()
    supp_city_entry_tv = tk.StringVar()
    supp_pincode_entry_tv = tk.StringVar()
    supp_phone_entry_tv = tk.StringVar()
    supp_email_entry_tv = tk.StringVar()
    supp_gst_no_entry_tv = tk.StringVar()

    insert_button.destroy()
    edit_button.destroy()
    delete_button.destroy()
    report_button.destroy()
    quit_button.destroy()

    tabcontrol = ttk.Notebook()

    supp_name_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_name_entry)
    supp_name_entry = Entry(supp_form, textvariable=supp_name_entry_tv)
    supp_name_entry.place(x=130, y=50, width=340)
    supp_name_entry.focus_set()
    supp_name_entry.bind("<F1>", Supplier_Search)
    supp_name_entry.bind("<Return>", sup_report_button_set_focus)
    supp_name_entry.bind("<FocusIn>", supp_name_lclick_focus)

    supp_address1_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_address1_entry)
    supp_address1_entry = Entry(supp_form,textvariable=supp_address1_entry_tv)
    supp_address1_entry.place(x=130, y=80, width=340)
    supp_address1_entry.config(state='disable')

    supp_locality_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_locality_entry)
    supp_locality_entry = Entry(supp_form,textvariable=supp_locality_entry_tv)
    supp_locality_entry.place(x=130, y=110, width=340)
    supp_locality_entry.config(state='disable')

    supp_city_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_city_entry)
    supp_city_entry = Entry(supp_form,textvariable=supp_city_entry_tv)
    supp_city_entry.place(x=130, y=140, width=100)
    supp_city_entry.config(state='disable')

    supp_pincode_entry = ttk.Frame(tabcontrol)
    tabcontrol.add((supp_pincode_entry))
    supp_pincode_entry = Entry(supp_form,textvariable=supp_pincode_entry_tv)
    supp_pincode_entry.place(x=130, y=170, width=100)
    supp_pincode_entry.config(state='disable')

    supp_state_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_state_entry)
    states_name = ['Tamil Nadu', 'Kerala', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Delhi']
    supp_state_combo = ttk.Combobox(supp_form,value=states_name, state='disable')
    #combo_box.set('')
    supp_state_combo.current(0)
    supp_state_combo.place(x=130, y=200)

    supp_phone_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_phone_entry)
    supp_phone_entry = Entry(supp_form,textvariable=supp_phone_entry_tv)
    supp_phone_entry.place(x=130, y=230, width=100)
    supp_phone_entry.config(state='disable')

    supp_email_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_email_entry)
    supp_email_entry = Entry(supp_form,textvariable=supp_email_entry_tv)
    supp_email_entry.place(x=130, y=260, width=230)
    supp_email_entry.config(state='disable')

    supp_gst_no_entry = ttk.Frame(tabcontrol)
    tabcontrol.add(supp_gst_no_entry)
    supp_gst_no_entry = Entry(supp_form,textvariable=supp_gst_no_entry_tv)
    supp_gst_no_entry.place(x=130, y=290, width=230)
    supp_gst_no_entry.config(state='disable')

    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN *****************************************
    report_button = Button(supp_form, text="Export To Excel", font=(14))
    report_button.place(x=220, y=350, width=120)
    report_button.bind("<Return>", Supplier_Export_To_Excel_Click)
    report_button.bind("<ButtonRelease>", Supplier_Export_To_Excel_Click)
    report_button.bind("<FocusIn>", Export_Button_FocusIn)

    cancel_button = Button(supp_form, text="Cancel", font=(14))
    cancel_button.place(x=350, y=350, width=120)
    cancel_button.bind("<Return>", Cancel_Button_Click)
    cancel_button.bind("<ButtonRelease>", Cancel_Button_Click)
    cancel_button.bind("<FocusIn>", Cancel_Button_FocusIn)

    # *************************************** BUTTON SETTINGS - END *****************************************

def Supplier_Quit(event):
    supp_form.withdraw()

def Save_Button_Click(event):
    name = supp_name_entry_tv.get()
    address = supp_address1_entry_tv.get()
    locality = supp_locality_entry_tv.get()
    city = supp_city_entry_tv.get()
    pincode = supp_pincode_entry_tv.get()
    state = supp_state_combo.get()
    phone = supp_phone_entry_tv.get()
    email = supp_email_entry_tv.get()
    gst_no = supp_gst_no_entry_tv.get()
    c_date = datetime.datetime.now()

    if len(name.strip()) > 0 and len(address.strip()) > 0 and len(locality.strip()) > 0 and len(city.strip()) > 0 \
            and len(pincode.strip()) > 0 and len(state.strip()) > 0 and len(phone.strip()) > 0 and len(email.strip()) > 0 \
            and len(gst_no.strip()) > 0:
        if len(name.strip()) <= 50 and len(address.strip()) <= 100 and len(locality.strip()) <= 25 and len(city.strip()) <=20 \
                and len(pincode.strip()) <= 6 and len(state.strip()) <= 25 and len(phone.strip()) == 10 and len(email.strip()) <= 100 \
                and len(gst_no.strip()) <= 15:

                Cur.execute("select max(id) as id_no from supplier_master")
                for row in Cur:
                    id_no = row[0]

                if id_no == None:
                    id_no = 1
                else:
                    id_no = id_no + 1

                Cur.execute("insert into supplier_master (name,address,locality,city,pincode,state,phone,email,gst,crt_date,id) values('{}','{}','{}','{}',{},'{}',{},'{}','{}','{}',{})".format(name,address,locality,city,pincode,state,phone,email,gst_no,c_date,id_no))
                Con.commit()
                messagebox.showinfo('', "SUPPLIER Details Added Successfully")
                supp_form.destroy()
                Supp_Design_Form_Load()
        else:
            messagebox.showwarning('', 'Enter Details As Per The Limitations')
            supp_form.focus_set()
            save_button.focus_set()
    else:
        messagebox.showwarning('', 'Enter Data In All Fields')
        supp_form.focus_set()
        save_button.focus_set()

def supp_entry_clear():
     supp_name_entry_tv.set('')
     supp_address1_entry_tv.set('')
     supp_locality_entry_tv.set('')
     supp_city_entry_tv.set('')
     supp_pincode_entry_tv.set('')
     supp_state_combo.set('')
     supp_phone_entry_tv.set('')
     supp_email_entry_tv.set('')
     supp_gst_no_entry_tv.set('')
     supp_state_combo.current(0)
     supp_name_entry.focus_set()

def Refresh_Supp_Data():
    for item in tree.get_children():
        tree.delete(item)

    Cur.execute("select * from supplier_master order by name")

    i = 0
    for row in Cur:
        tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        # tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        i = i + 1

def Refresh_Supp_Data2(records):
    for item in tree.get_children():
        tree.delete(item)

    i = 0
    for row in records:
        tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        i = i + 1


def Supplier_Export_To_Excel_Click(event):
    supplier_header = ["Name", "Address", "Locality", "City", "Pincode", "State", "Phone", "Email", "GST"]
    Cur.execute("select name, address, locality, city, pincode, state, phone, email, gst from supplier_master  where name like '%{}%' order by name".format(supp_name_entry.get()))
    supplier_data = []
    for row in Cur.fetchall():
        supplier_data.append(row)

    cls_rep.export_to_excel("Supplier List.xlsx", "List", supplier_header, supplier_data, "S U P P L I E R   L I S T")
    filepath = r'C:\Users\SYED\AcubeProjects\Status Plus\Supplier List.xlsx'
    os.startfile(filepath)
    supp_form.focus_set()
    supp_name_entry.focus_set()


def Update_Button_Click(event):
    name = supp_name_entry_tv.get()
    address = supp_address1_entry_tv.get()
    locality = supp_locality_entry_tv.get()
    city = supp_city_entry_tv.get()
    pincode = supp_pincode_entry_tv.get()
    state = supp_state_combo.get()
    phone = supp_phone_entry_tv.get()
    email = supp_email_entry_tv.get()
    gst_no = supp_gst_no_entry_tv.get()
    c_date = datetime.datetime.now()
    s_id = cls2.get_supp_id()

    if len(name.strip()) > 0 and len(address.strip()) > 0 and len(locality.strip()) > 0 and len(city.strip()) > 0 \
        and len(pincode.strip()) > 0 and len(state.strip()) > 0 and len(phone.strip()) > 0 and len(email.strip()) > 0 \
        and len(gst_no.strip()) > 0:

            #Cur.execute("update supplier_master set (name,address,locality,city,pincode,state,phone,email,gst,crt_date) values('{}','{}','{}','{}',{},'{}',{},'{}','{}','{}') where id={}".format(name,address,locality,city,pincode,state,phone,email,gst_no,c_date,s_id))
            qry ="update supplier_master set name= '{}',address= '{}',locality= '{}',city= '{}',pincode={}, \
                 state='{}',phone={},email='{}',gst= '{}',crt_date= '{}' where id={}".format(name, address,
                 locality,city,pincode, state, phone, email, gst_no, c_date, s_id)

            Cur.execute(qry)
            Con.commit()
            messagebox.showinfo('', "SUPPLIER Details Updated Successfully")
            supp_entry_clear()
            Refresh_Supp_Data()
    else:
       messagebox.showwarning('', 'Enter Data In All Fields')
       supp_form.focus_set()
       update_button.focus_set()

def Update_For_Delete_Button_Click(event):
    name = supp_name_entry_tv.get()
    address = supp_address1_entry_tv.get()
    locality = supp_locality_entry_tv.get()
    city = supp_city_entry_tv.get()
    pincode = supp_pincode_entry_tv.get()
    state = supp_state_combo.get()
    phone = supp_phone_entry_tv.get()
    email = supp_email_entry_tv.get()
    gst_no = supp_gst_no_entry_tv.get()
    c_date = datetime.datetime.now()
    s_id = cls2.get_supp_id()

    if len(name.strip()) > 0 and len(address.strip()) > 0 and len(locality.strip()) > 0 and len(city.strip()) > 0 \
        and len(pincode.strip()) > 0 and len(state.strip()) > 0 and len(phone.strip()) > 0 and len(email.strip()) > 0 \
        and len(gst_no.strip()) > 0:

            qry ="delete from  supplier_master where id= {}".format(s_id)
            Cur.execute(qry)
            Con.commit()
            tree.delete(item)
            messagebox.showinfo('', "SUPPLIER Details Deleted Successfully")
            supp_entry_clear()
            Refresh_Supp_Data()
    else:
        messagebox.showwarning('', 'Select SUPPLIER From List')
        supp_form.focus_set()
        update_button.focus_set()

def Cancel_Button_Click(event):

    result = messagebox.askquestion('', message='Do You Want To Cancel')
    if result == 'yes':
        supp_form.destroy()
        Supp_Design_Form_Load()
    else:
        supp_form.focus_set()
        supp_name_entry.focus_set()

def Supplier_Search(event):
    qry = "select * from supplier_master where name LIKE '"+supp_name_entry.get()+"%' order by name"
    Cur.execute(qry)
    records = Cur.fetchall()
    Refresh_Supp_Data2(records)

def Validate_Number(inp):
    if inp.isdigit():
        return True
    elif inp == "":
        return True
    else:
        return False


def Select_Supplier_Data(event):
    global item
    item = tree.selection()
    global cur_name
    for i in item:
        if len(tree.item(i, 'values')[0]) > 0:
            supp_name_entry_tv.set(tree.item(i,'values')[0])
            supp_address1_entry_tv.set(tree.item(i,'values')[1])
            supp_locality_entry_tv.set(tree.item(i,'values')[2])
            supp_city_entry_tv.set(tree.item(i,'values')[3])
            supp_pincode_entry_tv.set(tree.item(i,'values')[4])
            supp_state_combo.set(tree.item(i,'values')[5])
            supp_phone_entry_tv.set(tree.item(i,'values')[6])
            supp_email_entry_tv.set(tree.item(i,'values')[7])
            supp_gst_no_entry_tv.set(tree.item(i,'values')[8])
            cls2.set_supp_id(tree.item(i,'values')[10])
        else:
            pass

def Supp_Design_Form_Load():
    global supp_form, form_name
    global form_bottom
    global insert_button, edit_button, delete_button, report_button, quit_button
    global tree
    cls2.set_supp_record_found(0)
    supp_form = tk.Toplevel()
    supp_form.geometry('1300x450+25+100')
    supp_form.config(bg='white')
    supp_form.focus_set()
    supp_form.title('SUPPLIER')
    supp_form.resizable(False,False)

    form_name=Label(supp_form,text="S U P P L I E R", fg="black", bg="#63B8FF", width=500, font=('copper', 20, 'bold'))
    form_name.pack(side=TOP)
    form_bottom=Label(supp_form,text="",bg="#63B8FF", width=500, height=2, font=('bold',11))
    form_bottom.pack(side=BOTTOM)

    # *************************************** LABEL SETTINGS - BEGIN *******************************************
    supp_name = Label(supp_form, text="Supplier Name", bg='white', fg='black', font=(12))
    supp_name.place(x=20, y=50)
    supp_address = Label(supp_form, text="Address", bg='white', fg='black', font=(12))
    supp_address.place(x=20, y=80)
    supp_locality = Label(supp_form, text="Locality", bg='white', fg='black', font=(12))
    supp_locality.place(x=20, y=110)
    supp_city = Label(supp_form, text="City", bg='white', fg='black', font=(12))
    supp_city.place(x=20, y=140)
    supp_pincode = Label(supp_form, text="Pincode", bg='white', fg='black', font=(12))
    supp_pincode.place(x=20, y=170)
    supp_state = Label(supp_form, text="State", bg='white', fg='black', font=(12))
    supp_state.place(x=20, y=200)
    supp_phone = Label(supp_form, text="Phone", bg='white', fg='black', font=(12))
    supp_phone.place(x=20, y=230)
    supp_email = Label(supp_form, text="Email", bg='white', fg='black', font=(12))
    supp_email.place(x=20, y=260)
    supp_gst_no = Label(supp_form, text="GST No.", bg='white', fg='black', font=(12))
    supp_gst_no.place(x=20, y=290)
    # *************************************** LABEL SETTINGS - END ********************************************

    # *************************************** ENTRY BOX SETTINGS - BEGIN **************************************

    supp_name_entry = Entry(supp_form)
    supp_name_entry.place(x=130, y=50, width=340)
    supp_name_entry.config(state='disable')

    supp_address1_entry = Entry(supp_form)
    supp_address1_entry.place(x=130, y=80, width=340)
    supp_address1_entry.config(state='disable')

    supp_locality_entry = Entry(supp_form)
    supp_locality_entry.place(x=130, y=110, width=340)
    supp_locality_entry.config(state='disable')

    supp_city_entry = Entry(supp_form)
    supp_city_entry.place(x=130, y=140, width=100)
    supp_city_entry.config(state='disable')

    supp_pincode_entry = Entry(supp_form)
    supp_pincode_entry.place(x=130, y=170, width=100)
    supp_pincode_entry.config(state='disable')

    states_name = ['Tamil Nadu', 'Kerala', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Delhi']
    combo_box = ttk.Combobox(supp_form,value=states_name, state='disable')
    combo_box.set('')
    #combo_box.current(0)
    combo_box.place(x=130, y=200)

    supp_phone_entry = Entry(supp_form)
    supp_phone_entry.place(x=130, y=230, width=100)
    supp_phone_entry.config(state='disable')

    supp_email_entry = Entry(supp_form)
    supp_email_entry.place(x=130, y=260, width=230)
    supp_email_entry.config(state='disable')

    supp_gst_no_entry = Entry(supp_form)
    supp_gst_no_entry.place(x=130, y=290, width=230)
    supp_gst_no_entry.config(state='disable')
    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN ******************************************


    insert_button = Button(supp_form,text="Insert", font=(14))
    insert_button.place(x=130, y=350, width=64)
    insert_button.focus_set()
    insert_button.bind('<Return>',Supplier_Insert)
    insert_button.bind('<ButtonRelease>', Supplier_Insert)
    insert_button.bind('<FocusIn>', Main_Button_FocusIn)

    edit_button = Button(supp_form, text="Edit", font=(14))
    edit_button.place(x=200, y=350, width=64)
    edit_button.bind('<Return>', Supplier_Edit)
    edit_button.bind('<ButtonRelease>', Supplier_Edit)
    edit_button.bind('<FocusIn>', Main_Button_FocusIn)

    delete_button = Button(supp_form, text="Delete", font=(14))
    delete_button.place(x=270, y=350, width=64)
    delete_button.bind("<Return>", Supplier_Delete)
    delete_button.bind("<ButtonRelease>", Supplier_Delete)
    delete_button.bind('<FocusIn>', Main_Button_FocusIn)

    report_button = Button(supp_form, text="Report", font=(14))
    report_button.place(x=340, y=350, width=64)
    report_button.bind("<Return>", Supplier_Report)
    report_button.bind("<ButtonRelease>", Supplier_Report)
    report_button.bind('<FocusIn>', Main_Button_FocusIn)

    quit_button = Button(supp_form, text="Quit", font=(14))
    quit_button.place(x=410, y=350, width=64)
    quit_button.bind("<Return>", Supplier_Quit)
    quit_button.bind("<ButtonRelease>", Supplier_Quit)
    quit_button.bind('<FocusIn>', Main_Button_FocusIn)

    # *************************************** BUTTON SETTINGS - END ********************************************
    # *************************************** TREE VIEW  - BEGIN *******************************************

    supp_frame = Frame(supp_form)
    supp_frame.pack(pady=5)
    supp_frame.place(x=480, y=50)
    supp_frame.pack_propagate(False)
    supp_frame.configure(width=800, height=335, bg='#63B8FF')

    Cur.execute('select * from supplier_master order by name')
    col = ('name', 'address', 'locality', 'city', 'pincode', 'state', 'phone', 'email', 'gst_no', 'crt_date', 'id')
    #col = ('name', 'address', 'locality', 'city', 'pincode', 'state', 'phone', 'email', 'gst_no')
    tree = ttk.Treeview(supp_frame, height=14, show='headings', columns=col)
    # tree['show']='headings'
    tree.pack(fill=tk.X,pady=5)
    style1 = ttk.Style(supp_frame)

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

    tree.heading("name", text="SUPPLIER NAME", anchor=tk.W)
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

    vsb = ttk.Scrollbar(supp_frame, orient="vertical")
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(supp_frame, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)

    tree.pack()
    tree.bind("<Return>", Select_Supplier_Data)
    tree.bind("<ButtonRelease>", Select_Supplier_Data)
    tree.bind("<FocusIn>", Tree_FocusIn)
    # *************************************** TREE VIEW  - END *******************************************
