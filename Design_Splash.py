from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
from DB_Connection import*
from Design_User import*

from Design_Purchase_Entry import*
from Design_Sales_Entry import*
from Design_Supplier import*
from Design_Customer import*
from Design_User import*

from Design_Report import*
from Design_About_Us import*

from PIL import Image, ImageTk

Con = DB_Connect()
Cur = Con.cursor()
from Class_Main_Window import*
cls = cls_main_window()

def set_proceed_button_focus(event):
    form_bottom_label.config(text='Press [Enter] Key To Proceed', font = (12))

def set_exit_button_focus(event):
    form_bottom_label.config(text='Press [Enter] Key To Exit', font = (12))

def Set_Focus_User_Name(event):
    wel_user_name_entry.focus_set()
    wel_user_name_entry.selection_range(0, len(str(wel_user_name_entry_tv.get())))

def Set_Focus_Password(event):
    wel_user_password_entry.focus_set()
    wel_user_password_entry.selection_range(0, len(str(wel_user_password_entry_tv.get())))

def exit_form(event):
    exit()

def user_name_entry_lclick_focus(event):
    form_bottom_label.config(text='Enter User Name', font = (12))

def user_password_entry_lclick_focus(event):
    form_bottom_label.config(text='Enter Password', font = (12))

def set_password_entry_focus(event):
    form_bottom_label.config(text='Enter Password', font = (12))
    wel_user_password_entry.focus_set()

def set_login_button_focus(event):
    form_bottom_label.config(text='Press [Enter] Key To Login', font = (12))
    wel_login_button.focus_set()

def set_cancel_button_focus(event):
    form_bottom_label.config(text='Press [Enter] Key To Exit', font = (12))

def set_signup_button_focus(event):
    form_bottom_label.config(text='Press [Enter] Key To Signup New User', font = (12))

def main_window_focus(event):
    user_name = wel_user_name_entry_tv.get()
    cls.set_user(user_name)
    decrypt_pass = ""
    for row in wel_user_password_entry_tv.get():
        decrypt_pass = decrypt_pass+str(ord(row))
    qry = "select  * from user_master where user = '{}' and password = '{}'".format(cls.get_user(), decrypt_pass)
    Cur.execute(qry)
    dum = type(Cur)
    if dum != "<class 'mysql.connector.cursor_text.CMySQLCursor'>":
        for row in Cur:
            dum = row[1]
        Con.commit()
        if decrypt_pass == dum:
            Splash_Form.destroy()
            main_form = Tk()
            main_form.geometry('1350x680+0+0')
            main_form.title(cls.get_com_name())
            main_form.config(bg='#B0E2FF')
            main_form.resizable(False, False)
            main_menu_buttom_frame = Frame(main_form, bg="#63B8FF", width=1350, height=45)
            main_menu_buttom_frame.pack(side=BOTTOM)
            status_bar_label1 = Label(main_menu_buttom_frame, text="Developed By  - ", bg='#63B8FF', fg='black',
                                      font=('bold 9'))
            status_bar_label1.place(x=0, y=8)
            status_bar_label2 = Label(main_menu_buttom_frame, text="Acube Software Technologies", bg='#63B8FF', fg='black',

                                      # font=('Bookman Old Style Italic', 20))
                              font=("Comic Sans MS", 20, 'bold'))
            status_bar_label2.place(x=90, y=0)

            menu_bar = Menu(main_form)
            master_menu = Menu(menu_bar, tearoff=0)
            master_menu.add_command(label="Supplier", command=lambda: Supp_Design_Form_Load())
            master_menu.add_command(label="Customer", command=lambda: cust_Design_Form_Load())
            master_menu.add_separator()
            master_menu.add_command(label="User", command=lambda: User_Design_Form_Load())
            menu_bar.add_cascade(label="Master", menu=master_menu)

            purchase_menu = Menu(menu_bar, tearoff=0)
            purchase_menu.add_command(label="Purchase Entry", command=lambda: Design_Purchase_Form_Load())
            menu_bar.add_cascade(label="Purchase", menu=purchase_menu)

            sales_menu = Menu(menu_bar, tearoff=0)
            sales_menu.add_command(label="Billing", command=lambda: Design_sales_Form_Load())
            menu_bar.add_cascade(label="Sales", menu=sales_menu)

            report_menu = Menu(menu_bar, tearoff=0)
            report_menu.add_command(label="All Reports", command=lambda: Design_Report_Form_Load())
            menu_bar.add_cascade(label="Report", menu=report_menu)

            help_menu = Menu(menu_bar, tearoff=0)
            help_menu.add_command(label="About", command=lambda: Design_About_Us_Form_Load())
            help_menu.add_separator()
            help_menu.add_command(label="Exit", command=lambda: main_form.destroy())
            menu_bar.add_cascade(label="Help", menu=help_menu)
            main_form.config(menu=menu_bar)

            my_image = Image.open(r'C:\Users\SYED\AcubeProjects\Status Plus\Form Photo.png')
            my_image = my_image.resize((1380,680))
            my_photo = ImageTk.PhotoImage(my_image)
            label = Label(main_form, image=my_photo)
            label.pack()
            main_form.mainloop()
        else:
            messagebox.showwarning(cls.get_com_name(), 'UserName Or Password Is Incorrect')
            Splash_Form.focus_set()
            wel_user_name_entry.focus_set()
    else:
        Con.commit()
        messagebox.showwarning(cls.get_com_name(), 'UserName Or Password Is Incorrect')
        Splash_Form.focus_set()
        wel_user_name_entry.focus_set()

def signup_form(event):
    User_Signup_Design_Form_Load()
    user_signup_insert2()

def welcome_screen(event):
    global wel_user_password_entry, wel_user_name_entry, wel_user_name_entry_tv, wel_user_password_entry_tv
    global wel_login_button
    wel_user_name_entry_tv = StringVar()
    wel_user_password_entry_tv = StringVar()
    # *************************************** SPLASH LABEL HIDE SETTINGS - BEGIN *******************************************
    splash_name1.destroy()
    splash_name2.destroy()
    splash_name3.destroy()
    splash_name4.destroy()
    splash_name5.destroy()
    splash_name6.destroy()
    splash_role1.destroy()
    splash_role2.destroy()
    splash_role3.destroy()
    splash_proceed_button.destroy()
    splash_exit_button.destroy()
    # *************************************** SPLASH LABEL HIDE SETTINGS - END *******************************************
    
    # *************************************** COMPANY LABEL SETTINGS - BEGIN *******************************************
    form_top_label.config(text=cls.get_com_name(),height=2)
    wel_com_add= Label(Splash_Form, text=cls.get_com_add(), bg='#B0E2FF', fg='black', font=(12))
    wel_com_add.pack()
    wel_com_loc = Label(Splash_Form, text=cls.get_com_loc(), bg='#B0E2FF', fg='black', font=(12))
    wel_com_loc.pack()
    wel_com_city = Label(Splash_Form, text=cls.get_com_city(), bg='#B0E2FF', fg='black', font=(12))
    wel_com_city.pack()
    wel_com_pin = Label(Splash_Form, text=cls.get_com_pin(), bg='#B0E2FF', fg='black', font=(12))
    wel_com_pin.pack()
    wel_com_state = Label(Splash_Form, text=cls.get_com_state(), bg='#B0E2FF', fg='black', font=(12))
    wel_com_state.pack()
    phone_label = "Phone : "+ str(cls.get_com_phone())
    wel_com_phone = Label(Splash_Form, text=phone_label, bg='#B0E2FF', fg='black', font=(12))
    wel_com_phone.place(x=2,y=200)
    email_label = "Email : " + cls.get_com_email()
    wel_com_email = Label(Splash_Form, text=email_label, bg='#B0E2FF', fg='black', font=(12))
    wel_com_email.place(x=240, y=200)
    gst_label = "GST No. : " + cls.get_com_gst()
    wel_com_gst = Label(Splash_Form, text=gst_label, bg='#B0E2FF', fg='black', font=(12))
    wel_com_gst.place(x=565, y=200)
    # *************************************** COMPANY LABEL SETTINGS - END ********************************************

    # *************************************** USER FRAME & LABEL SETTINGS - BEGIN *******************************************
    wel_frame1 = Frame(Splash_Form, width = 350, height = 150, bg='#63B8FF')
    wel_frame1.pack(side=LEFT, padx=250,ipadx=20)
    wel_user_name = Label(wel_frame1, text="User Name", bg='#63B8FF', fg='black', font=("bold",12))
    wel_user_name.place(x=20, y=30)
    wel_user_password = Label(wel_frame1, text="Password", bg='#63B8FF', fg='black', font=("bold",12))
    wel_user_password.place(x=20, y=60)
    # *************************************** USER FRAME & LABEL SETTINGS - END ********************************************

    # *************************************** USER ENTRY SETTINGS - BEGIN *******************************************
    wel_user_name_entry = Entry(wel_frame1, width=24, textvariable=wel_user_name_entry_tv, bg="white")
    wel_user_name_entry.place(x=120, y=30)
    form_bottom_label.config(text="Enter User Name",font=(12))
    wel_user_name_entry.focus_set()
    wel_user_name_entry.bind("<FocusIn>", Set_Focus_User_Name)
    wel_user_name_entry.bind("<Return>", set_password_entry_focus)
    wel_user_name_entry.bind("<ButtonRelease>", user_name_entry_lclick_focus)

    wel_user_password_entry = Entry(wel_frame1, width=24,textvariable=wel_user_password_entry_tv, bg="white", show = ("*"))
    wel_user_password_entry.place(x=120, y=60)
    wel_user_password_entry.bind("<FocusIn>", Set_Focus_Password)
    wel_user_password_entry.bind("<Return>", set_login_button_focus)
    wel_user_password_entry.bind("<ButtonRelease>",user_password_entry_lclick_focus)
    # *************************************** USER ENTRY SETTINGS - END ********************************************

    # *************************************** USER BUTTON SETTINGS - BEGIN ******************************************
    global welcome_button
    wel_login_button = Button(wel_frame1, text="Login", width=9, bg='white')
    wel_login_button.place(x=120, y=90)
    # wel_login_button.focus_set()
    wel_login_button.bind("<ButtonRelease>", main_window_focus)
    wel_login_button.bind("<Return>", main_window_focus)
    wel_login_button.bind("<Tab>", set_cancel_button_focus)
    wel_login_button.bind("<FocusIn>", set_login_button_focus)

    wel_cancel_button = Button(wel_frame1, text="Cancel", width=9, bg='white')
    wel_cancel_button.place(x=195, y=90)
    wel_cancel_button.bind("<ButtonRelease>", exit_form)
    wel_cancel_button.bind("<Return>", exit_form)
    wel_cancel_button.bind("<FocusIn>", set_cancel_button_focus)

    # wel_signup_button = Button(wel_frame1, text="S i g n u p", width=20, bg='white')
    # wel_signup_button.place(x=120, y=120)
    # wel_signup_button.bind("<ButtonRelease>", signup_form)
    # wel_signup_button.bind("<Return>", signup_form)
    # wel_signup_button.bind("<FocusIn>", set_signup_button_focus)
    # *************************************** USER BUTTON SETTINGS - END ********************************************

def company_details():
    Cur.execute("select * from company_master")
    for com_data in Cur:
        cls.set_com_name(com_data[0])
        cls.set_com_add(com_data[1])
        cls.set_com_loc(com_data[2])
        cls.set_com_city(com_data[3])
        cls.set_com_pin(com_data[4])
        cls.set_com_state(com_data[5])
        cls.set_com_phone(com_data[6])
        cls.set_com_email(com_data[7])
        cls.set_com_gst(com_data[8])
        cls.set_com_crt_date(com_data[9])
        cls.set_com_id(com_data[10])

def Splash_Design_Form_Load():
    global Splash_Form
    global form_top_label, form_bottom_label, splash_name1, splash_name2, splash_name3, splash_name4
    global splash_name5, splash_name6, splash_name7
    global splash_role1, splash_role2, splash_role3
    Splash_Form = Tk()
    Splash_Form.title("")
    Splash_Form.geometry('800x600+300+70')
    Splash_Form.config(bg='#B0E2FF')
    Splash_Form.resizable(False, False)
    Splash_Form.focus_set()

    form_top_label=Label(Splash_Form, text='I N V E N T O R Y   S O F T W A R E   F O R   R E T A I L   S H O P',fg="black", bg="#63B8FF", width=500, font=('copper', 18, 'bold'),heigh=2)
    form_top_label.pack(side=TOP)
    form_bottom_label=Label(Splash_Form,text="",bg="#63B8FF", width=500, height=2)
    form_bottom_label.pack(side=BOTTOM)

    # *************************************** LABEL SETTINGS - BEGIN *******************************************
    splash_name1 = Label(Splash_Form, text="A L P H A   A R T S   &   S C I E N C E   C O L L E G E", bg='#B0E2FF', fg='black', font=('bold', 18))
    splash_name1.place(x=110, y=90)
    splash_name2 = Label(Splash_Form, text="B. S c ( C S )   -   F I N A L   Y E A R   M I N I   P R O J E C T", bg='#B0E2FF', fg='black', font=('bold', 14))
    splash_name2.place(x=150, y=150)
    splash_name3 = Label(Splash_Form, text="D o n e   B y", bg='#B0E2FF', fg='black', font=(12))
    splash_name3.place(x=360, y=210)
    splash_name4 = Label(Splash_Form, text="J.  A L T H A F   H U S S A I N ", bg='#B0E2FF', fg='black', font=('bold',14))
    splash_name4.place(x=30, y=300)
    splash_role1 = Label(Splash_Form, text="(T e a m  L e a d)", bg='#B0E2FF', fg='black',
                         font=('bold', 12))
    splash_role1.place(x=100, y=330)

    splash_name5 = Label(Splash_Form, text="K. A A K A S H", bg='#B0E2FF', fg='black',
                         font=('bold', 14))
    splash_name5.place(x=380, y=300)

    splash_role2 = Label(Splash_Form, text="(M e m b e r)", bg='#B0E2FF', fg='black',
                         font=('bold', 12))
    splash_role2.place(x=400, y=330)

    splash_name6 = Label(Splash_Form, text="S.  A B I N A S H ", bg='#B0E2FF', fg='black',
                         font=('bold', 14))
    splash_name6.place(x=600, y=300)
    splash_role3 = Label(Splash_Form, text="(M e m b e r)", bg='#B0E2FF', fg='black',
                         font=('bold', 12))
    splash_role3.place(x=630, y=330)


    splash_name7 = Label(Splash_Form, text="Python & MySQL", bg="#63B8FF", fg="black", font=('bold',10))
    splash_name7.place(x=0, y=568)
    # *************************************** LABEL SETTINGS - END ********************************************

    # *************************************** BUTTON SETTINGS - BEGIN ******************************************
    cls.set_login_entry(0)
    company_details()
    global splash_proceed_button, splash_exit_button
    splash_proceed_button = Button(Splash_Form, text="Proceed", width=15, height=1, font=('bold',20), bg="white")
    splash_proceed_button.place(x=140, y= 440)
    splash_proceed_button.focus_set()
    splash_proceed_button.bind("<ButtonRelease>", welcome_screen)
    splash_proceed_button.bind("<Return>", welcome_screen)
    splash_proceed_button.bind("<Tab>", set_exit_button_focus)

    splash_exit_button = Button(Splash_Form, text="Exit", width=15, height=1, font=('bold', 20), bg="white")
    splash_exit_button.place(x=400, y=440)
    splash_exit_button.bind("<ButtonRelease>", exit_form)
    splash_exit_button.bind("<Return>", exit_form)
    splash_exit_button.bind("<Tab>", set_proceed_button_focus)

    form_bottom_label.configure(text="Press [Enter] Key To Proceed", font = (12))
    # *************************************** BUTTON SETTINGS - END ********************************************

    Splash_Form.mainloop()
