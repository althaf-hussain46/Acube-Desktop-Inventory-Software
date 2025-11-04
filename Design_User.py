from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
from Show_Data import*
from Class_Login import*
from DB_Connection import*
from Class_Main_Window import*
cls3 = cls_main_window()
cls2 = cls_Login()
Con = DB_Connect()
Cur = Con.cursor()

def login_user_lclick_focus(event):
    form_bottom.configure(text='Press [F1] To List User Name     Maximum Allowed Characters - 20')
    login_user_entry.focus_set()

def login_user_signup_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Characters - 20')
    login_user_entry.focus_set()

def login_password_lclick_focus(event):
    form_bottom.configure(text='Maximum Allowed Characters - 20')
    login_password_entry.focus_set()

def login_password_set_focus(event):
    if len(login_user_entry.get()) >= 1 and len(login_user_entry.get()) <= 20:
        form_bottom.configure(text='Maximum Allowed Characters - 20')
        form_name.focus_set()
        login_password_entry.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 20')
        form_name.focus_set()
        login_user_entry.focus_set()

def login_save_button_set_focus(event):
    if len(login_password_entry.get()) >= 1 and len(login_password_entry.get()) <= 20:
        form_bottom.configure(text='Press [Enter] To Save')
        save_button.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 20')
        form_name.focus_set()
        login_password_entry.focus_set()

def login_update_button_set_focus(event):
    if len(login_password_entry.get()) >= 1 and len(login_password_entry.get()) <= 20:
        form_bottom.configure(text='Press [Enter] To Save')
        update_button.focus_set()
    else:
        messagebox.showinfo('', 'Maximum Allowed Characters - 20')
        form_name.focus_set()
        login_password_entry.focus_set()

def login_delete_button_set_focus(event):
    update_button.focus_set()

def tree_focus(event):
    form_bottom.configure(text='')

def save_get_focus(event):
    form_bottom.configure(text='Press This Button To Create User')

def update_get_focus(event):
    form_bottom.configure(text='Press This Button To Modify User')

def delete_user_get_focus(event):
    form_bottom.configure(text='Press This Button To Remove User')

def cancel_get_focus(event):
    form_bottom.configure(text='Press This Button To Cancel')

def DML_BUTTONS_FOCUS(event):
    form_bottom.configure(text="[Insert] - Create User     [Edit] - Update User     [Delete]- Remove User", font=('bold', 10))

def user_insert(event):
    global login_user_entry, login_password_entry
    global login_user_entry_tv, login_password_entry_tv
    global save_button
    form_name.configure(text="User - I N S E R T")

    cls2.set_login_record_found('0')
    login_user_entry_tv = tk.StringVar()
    login_password_entry_tv = tk.StringVar()

    insert_button.destroy()
    edit_button.destroy()
    quit_button.destroy()

    login_user_entry = Entry(login_form, textvariable=login_user_entry_tv)
    login_user_entry.place(x=120, y=50, width=275)
    login_user_entry.focus_set()
    form_bottom.configure(text="Press [F1] To List User Names     Maximum Allowed Characters - 20")
    login_user_entry.config(bg='#87CEFA')
    login_user_entry.bind("<F1>", user_serarch)
    login_user_entry.bind("<Return>", login_password_set_focus)
    login_user_entry.bind("<ButtonRelease>", login_user_lclick_focus)
    login_user_entry.bind("<FocusIn>", login_user_lclick_focus)

    login_password_entry = Entry(login_form,textvariable=login_password_entry_tv)
    login_password_entry.place(x=120, y=85, width=275)
    login_password_entry.config(show='*')
    login_password_entry.bind("<Return>",login_save_button_set_focus)
    login_password_entry.bind("<ButtonRelease>", login_password_lclick_focus)
    login_password_entry.bind("<FocusIn>", login_password_lclick_focus)
    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN *****************************************
    save_button = Button(login_form, text="Save", font=(14))
    save_button.place(x=260, y=130, width=64)
    save_button.bind("<ButtonRelease>", Save_Button_Click)
    save_button.bind("<Return>",Save_Button_Click)
    save_button.bind('<FocusIn>', save_get_focus)

    cancel_button = Button(login_form, text="Cancel", font=(14))
    cancel_button.place(x=330, y=130, width=64)
    cancel_button.bind("<ButtonRelease>",Cancel_Button_Click)
    cancel_button.bind("<Return>",Cancel_Button_Click)
    cancel_button.bind('<FocusIn>', cancel_get_focus)

    # *************************************** BUTTON SETTINGS - END *****************************************

def user_signup_insert(event):
    global login_user_entry, login_password_entry
    global login_user_entry_tv, login_password_entry_tv
    global save_button
    form_name.configure(text="User - I N S E R T")

    cls2.set_login_record_found('0')
    login_user_entry_tv = tk.StringVar()
    login_password_entry_tv = tk.StringVar()


    insert_button.destroy()
    quit_button.destroy()

    login_user_entry = Entry(login_form, textvariable=login_user_entry_tv)
    login_user_entry.place(x=120, y=50, width=275)
    login_user_entry.focus_set()
    form_bottom.configure(text="Maximum Allowed Characters - 20")
    login_user_entry.bind("<Return>", login_password_set_focus)
    login_user_entry.bind("<FocusIn>", login_user_signup_lclick_focus)


    login_password_entry = Entry(login_form,textvariable=login_password_entry_tv)
    login_password_entry.place(x=120, y=85, width=275)
    login_password_entry.config(show='*')
    login_password_entry.bind("<Return>", login_save_button_set_focus)
    login_password_entry.bind("<ButtonRelease>", login_password_lclick_focus)
    login_password_entry.bind("<FocusIn>", login_password_lclick_focus)
    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN *****************************************
    save_button = Button(login_form, text="Save", font=(14))
    save_button.place(x=260, y=115, width=64)
    save_button.bind("<ButtonRelease>", Save_Signup_Button_Click)
    save_button.bind("<Return>", Save_Signup_Button_Click)
    save_button.bind('<FocusIn>', save_get_focus)

    cancel_button = Button(login_form, text="Cancel", font=(14))
    cancel_button.place(x=330, y=115, width=64)
    cancel_button.bind("<ButtonRelease>", Cancel_Signup_Button_Click)
    cancel_button.bind("<Return>", Cancel_Signup_Button_Click)
    cancel_button.bind('<FocusIn>', cancel_get_focus)

    # *************************************** BUTTON SETTINGS - END *****************************************

def user_signup_insert2():
    global login_user_entry, login_password_entry
    global login_user_entry_tv, login_password_entry_tv
    global save_button
    form_name.configure(text="U S E R - S I G N   U P")

    cls2.set_login_record_found('0')
    login_user_entry_tv = tk.StringVar()
    login_password_entry_tv = tk.StringVar()


    insert_button.destroy()
    quit_button.destroy()

    login_user_entry = Entry(login_form, textvariable=login_user_entry_tv)
    login_user_entry.place(x=120, y=50, width=275)
    login_user_entry.focus_set()
    form_bottom.configure(text="Maximum Allowed Characters - 20")
    login_user_entry.bind("<Return>", login_password_set_focus)
    login_user_entry.bind("<FocusIn>", login_user_signup_lclick_focus)


    login_password_entry = Entry(login_form,textvariable=login_password_entry_tv)
    login_password_entry.place(x=120, y=85, width=275)
    login_password_entry.config(show='*')
    login_password_entry.bind("<Return>", login_save_button_set_focus)
    login_password_entry.bind("<ButtonRelease>", login_password_lclick_focus)
    login_password_entry.bind("<FocusIn>", login_password_lclick_focus)
    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN *****************************************
    save_button = Button(login_form, text="Save", font=(14))
    save_button.place(x=260, y=115, width=64)
    save_button.bind("<ButtonRelease>", Save_Signup_Button_Click)
    save_button.bind("<Return>", Save_Signup_Button_Click)
    save_button.bind('<FocusIn>', save_get_focus)

    cancel_button = Button(login_form, text="Cancel", font=(14))
    cancel_button.place(x=330, y=115, width=64)
    cancel_button.bind("<ButtonRelease>", Cancel_Signup_Button_Click)
    cancel_button.bind("<Return>", Cancel_Signup_Button_Click)
    cancel_button.bind('<FocusIn>', cancel_get_focus)

    # *************************************** BUTTON SETTINGS - END *****************************************

def user_edit(event):
    global login_user_entry, login_password_entry
    global login_user_entry_tv, login_password_entry_tv
    global update_button
    form_name.configure(text="User - E D I T")

    cls2.set_user_id('')
    login_user_entry_tv = tk.StringVar()
    login_password_entry_tv = tk.StringVar()

    insert_button.destroy()
    edit_button.destroy()
    delete_button.destroy()
    quit_button.destroy()

    login_user_entry = Entry(login_form, textvariable=login_user_entry_tv)
    login_user_entry.place(x=120, y=50, width=275)
    login_user_entry.focus_set()
    form_bottom.configure(text="Press [F1] To List User Names     Maximum Allowed Characters - 20")
    login_user_entry.config(bg='#87CEFA')
    login_user_entry.bind("<F1>", user_serarch)
    login_user_entry.bind("<Return>", login_password_set_focus)
    login_user_entry.bind("<ButtonRelease>", login_user_lclick_focus)
    login_user_entry.bind("<FocusIn>", login_user_lclick_focus)

    login_password_entry = Entry(login_form,textvariable=login_password_entry_tv)
    login_password_entry.place(x=120, y=85, width=275)
    login_password_entry.config(show='*')
    login_password_entry.bind("<Return>",login_update_button_set_focus)
    login_password_entry.bind("<ButtonRelease>", login_password_lclick_focus)
    login_password_entry.bind("<FocusIn>", login_password_lclick_focus)

    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN *****************************************
    update_button = Button(login_form, text="Update", font=(14))
    update_button.place(x=260, y=130, width=64)
    update_button.bind("<ButtonRelease>", Update_Button_Click)
    update_button.bind("<Return>", Update_Button_Click)
    update_button.bind('<FocusIn>', update_get_focus)

    cancel_button = Button(login_form, text="Cancel", font=(14))
    cancel_button.place(x=330, y=130, width=64)
    cancel_button.bind("<ButtonRelease>", Cancel_Button_Click)
    cancel_button.bind("<Return>", Cancel_Button_Click)
    cancel_button.bind('<FocusIn>', cancel_get_focus)
    # *************************************** BUTTON SETTINGS - END *****************************************

def user_delete(event):
    global login_user_entry, login_password_entry
    global login_user_entry_tv, login_password_entry_tv
    global update_button
    form_name.configure(text="User - D E L E T E")

    cls2.set_user_id('')
    login_user_entry_tv = tk.StringVar()
    login_password_entry_tv = tk.StringVar()

    insert_button.destroy()
    edit_button.destroy()
    delete_button.destroy()
    quit_button.destroy()

    login_user_entry = Entry(login_form, textvariable=login_user_entry_tv)
    login_user_entry.place(x=120, y=50, width=275)
    login_user_entry.config(bg='#87CEFA')
    login_user_entry.focus_set()
    login_user_entry.bind("<F1>", user_serarch)
    login_user_entry.bind("<Return>", login_delete_button_set_focus)
    login_user_entry.bind("<FocusIn>", login_user_lclick_focus)

    login_password_entry = Entry(login_form,textvariable=login_password_entry_tv)
    login_password_entry.place(x=120, y=85, width=275)
    login_password_entry.config(show='*')
    login_password_entry.config(state='disable')
    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN *****************************************
    update_button = Button(login_form, text="Delete", font=(14))
    update_button.place(x=260, y=130, width=64)
    update_button.bind("<Return>", Update_For_Delete_Button_Click)
    update_button.bind("<ButtonRelease>", Update_For_Delete_Button_Click)
    update_button.bind('<FocusIn>', delete_user_get_focus)

    cancel_button = Button(login_form, text="Cancel", font=(14))
    cancel_button.place(x=330, y=130, width=64)
    cancel_button.bind("<Return>", Cancel_Button_Click)
    cancel_button.bind("<ButtonRelease>", Cancel_Button_Click)
    cancel_button.bind('<FocusIn>', cancel_get_focus)
    # *************************************** BUTTON SETTINGS - END *****************************************


def user_quit(event):
    login_form.withdraw()

def Save_Button_Click(event):
    user = login_user_entry_tv.get()
    password = login_password_entry_tv.get()
    c_date = datetime.datetime.now()

    if len(user.strip()) > 0 and len(password.strip()) > 0:
        if len(user.strip()) <= 20 and len(password.strip()) <= 20:

                Cur.execute("select max(id) as id_no from user_master")
                for row in Cur:
                    id_no = row[0]

                if id_no == None:
                    id_no = 1
                else:
                    id_no = id_no + 1

                enc_pass = ""
                for v1 in password:
                    dum_asc =  ord(v1)
                    enc_pass = enc_pass+str(dum_asc)

                Cur.execute("insert into user_master (user,password,crt_date,id) values('{}','{}','{}',{})".format(user,enc_pass,c_date,id_no))
                Con.commit()
                messagebox.showinfo('', 'User Created')
                login_form.destroy()
                User_Design_Form_Load()
        else:
            messagebox.showwarning('', 'Enter Details As Per The Limitations')
            Con.commit()
            form_name.focus_set()
            login_user_entry.focus_set()
    else:
        messagebox.showwarning('', 'Enter Data In All Fields')
        Con.commit()
        form_name.focus_set()
        login_user_entry.focus_set()

def Save_Signup_Button_Click(event):
    user = login_user_entry_tv.get()
    password = login_password_entry_tv.get()
    c_date = datetime.datetime.now()

    if len(user.strip()) > 0 and len(password.strip()) > 0:
        if len(user.strip()) <= 20 and len(password.strip()) <= 20:

                Cur.execute("select max(id) as id_no from user_master")
                for row in Cur:
                    id_no = row[0]
                Con.commit()

                if id_no == None:
                    id_no = 1
                else:
                    id_no = id_no + 1

                enc_pass = ""
                for v1 in password:
                    dum_asc = ord(v1)
                    enc_pass = enc_pass+str(dum_asc)

                Cur.execute("insert into user_master (user,password,crt_date,id) values('{}','{}','{}',{})".format(user,enc_pass,c_date,id_no))
                Con.commit()
                messagebox.showinfo('', "User Created")
                login_form.destroy()

        else:
            messagebox.showwarning("", 'Enter Details As Per The Limitations')
            form_name.focus_set()
            login_user_entry.focus_set()
    else:
        messagebox.showwarning("", 'Enter Data In All Fields')
        form_name.focus_set()
        login_user_entry.focus_set()


def user_entry_clear():
     login_user_entry_tv.set('')
     login_password_entry_tv.set('')
     login_user_entry.focus_set()

def show_str_in_star(value):
    dum_str = value
    return

def Update_Button_Click(event):
    user = login_user_entry_tv.get()
    password = login_password_entry_tv.get()
    c_date = datetime.datetime.now()
    s_id = cls2.get_user_id()
    encrypt_password = ""
    for row in password:
        encrypt_password = encrypt_password+str(ord(row))

    if len(user.strip()) > 0 and len(password.strip()) > 0:
            qry ="update user_master set user= '{}', password= '{}',crt_date= '{}' where id={}".format(user, encrypt_password, c_date, s_id)
            Cur.execute(qry)
            Con.commit()
            messagebox.showinfo("", "User Updated")
            user_entry_clear()
            refresh_user_data()
    else:
       messagebox.showwarning("", 'Enter Data In All Fields')
       form_name.focus_set()
       login_password_entry.focus_set()


def Update_For_Delete_Button_Click(event):
    user = login_user_entry_tv.get()
    password = login_password_entry_tv.get()
    c_date = datetime.datetime.now()
    s_id = cls2.get_user_id()

    if len(user.strip()) > 0 :
        qry ="delete from  user_master where id= {}".format(s_id)
        Cur.execute(qry)
        Con.commit()
        tree.delete(item)
        messagebox.showinfo('', "User Deleted")
        user_entry_clear()
        refresh_user_data()
    else:
        messagebox.showwarning('', 'Select User From List')
        form_name.focus_set()
        login_user_entry.focus_set()

def Cancel_Button_Click(event):
    result = messagebox.askquestion(message='Do You Want To Cancel')

    if result == 'yes':
        login_form.destroy()
        User_Design_Form_Load()
    else:
        form_name.focus_set()
        login_user_entry.focus_set()

def Cancel_Signup_Button_Click(event):
    result = messagebox.askquestion(message='Do You Want To Cancel')

    if result == 'yes':
        login_form.destroy()

    else:
        form_name.focus_set()
        login_user_entry.focus_set()

def refresh_user_data():
    for item in tree.get_children():
        tree.delete(item)

    Cur.execute("select * from user_master order by user")
    i = 0
    for row in Cur:
        tree.insert('', i, text="", values=(row[0], row [1], row[2], row[3]))
        i = i + 1

def refresh_user_data2(records):
    for item in tree.get_children():
        tree.delete(item)
    i = 0
    for row in records:
        tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3]))
        i = i + 1

def user_serarch(event):
    qry = "select * from user_master where user LIKE '"+login_user_entry.get()+"%' order by user"
    Cur.execute(qry)
    records = Cur.fetchall()
    refresh_user_data2(records)

def select_user_data(event):
    global item
    item=tree.selection()
    global cur_user
    for i in item:
        if len(tree.item(i, 'values')[0]) > 0:
            login_user_entry_tv.set(tree.item(i,'values')[0])
            login_pass_decrypt = tree.item(i,'values')[1]
            login_password_entry_tv.set(())
            cls2.set_user_id(tree.item(i,'values')[3])
        else:
            pass

def User_Signup_Design_Form_Load():
    global login_form, form_name
    global form_bottom
    cls2.set_login_record_found(0)
    login_form = tk.Toplevel()
    login_form.geometry('440x200+500+340')
    login_form.config(bg='#B0E2FF')
    login_form.focus_set()
    login_form.title('USER')
    login_form.resizable(False,False)

    form_name=Label(login_form,text="U S E R", fg="black", bg="#63B8FF", width=500, font=('copper', 20, 'bold'))
    form_name.pack(side=TOP)
    form_bottom=Label(login_form,text="",bg="#63B8FF", width=500, height=2)
    form_bottom.pack(side=BOTTOM)

    # *************************************** LABEL SETTINGS - BEGIN *******************************************
    login_user = Label(login_form, text="User Name", bg='#B0E2FF', fg='black', font=(12))
    login_user.place(x=30, y=45)
    login_password = Label(login_form, text="Password", bg='#B0E2FF', fg='black', font=(12))
    login_password.place(x=30, y=80)
    # *************************************** LABEL SETTINGS - END ********************************************

    # *************************************** ENTRY BOX SETTINGS - BEGIN **************************************

    login_user_entry = Entry(login_form)
    login_user_entry.place(x=120, y=50, width=275)
    login_user_entry.config(state='disable')

    login_password_entry = Entry(login_form)
    login_password_entry.place(x=120, y=85, width=275)
    login_password_entry.config(state='disable', show='*')
    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN ******************************************
    global insert_button, quit_button

    insert_button = Button(login_form,text="Insert", font=(14))
    insert_button.place(x=260, y=115, width=64)
    insert_button.focus_set()
    insert_button.bind('<Return>',user_signup_insert)
    insert_button.bind('<ButtonRelease>', user_signup_insert)
    form_bottom.configure(text="[Insert] - Create User     [Quit] - Close", font=('bold', 10))

    quit_button = Button(login_form, text="Quit", font=(14))
    quit_button.place(x=330, y=115, width=64)
    quit_button.bind("<Return>", user_quit)
    quit_button.bind("<ButtonRelease>", user_quit)
    # *************************************** BUTTON SETTINGS - END ********************************************


def User_Design_Form_Load():
    global login_form, form_name
    global form_bottom
    cls2.set_login_record_found(0)
    login_form = tk.Toplevel()
    login_form.geometry('440x400+350+100')
    login_form.config(bg='#B0E2FF')
    login_form.focus_set()
    login_form.title('USER')
    login_form.resizable(False,False)

    form_name=Label(login_form,text="U S E R", fg="black", bg="#63B8FF", width=500, font=('copper', 20, 'bold'))
    form_name.pack(side=TOP)
    form_bottom=Label(login_form,text="",bg="#63B8FF", width=500, height=2)
    form_bottom.pack(side=BOTTOM)

    # *************************************** LABEL SETTINGS - BEGIN *******************************************
    login_user = Label(login_form, text="User Name", bg='#B0E2FF', fg='black', font=(12))
    login_user.place(x=30, y=45)
    login_password = Label(login_form, text="Password", bg='#B0E2FF', fg='black', font=(12))
    login_password.place(x=30, y=80)
    # *************************************** LABEL SETTINGS - END ********************************************

    # *************************************** ENTRY BOX SETTINGS - BEGIN **************************************

    login_user_entry = Entry(login_form)
    login_user_entry.place(x=120, y=50, width=275)
    login_user_entry.config(state='disable')

    login_password_entry = Entry(login_form)
    login_password_entry.place(x=120, y=85, width=275)
    login_password_entry.config(state='disable', show='*')
    # *************************************** ENTRY BOX SETTINGS - END *****************************************

    # *************************************** BUTTON SETTINGS - BEGIN ******************************************
    global insert_button, edit_button, delete_button, quit_button

    insert_button = Button(login_form,text="Insert", font=(14))
    insert_button.place(x=120, y=130, width=64)
    insert_button.focus_set()
    insert_button.bind('<Return>',user_insert)
    insert_button.bind('<ButtonRelease>', user_insert)
    insert_button.bind('<FocusIn>', DML_BUTTONS_FOCUS)

    edit_button = Button(login_form, text="Edit", font=(14))
    edit_button.place(x=190, y=130, width=64)
    edit_button.bind('<Return>', user_edit)
    edit_button.bind('<ButtonRelease>', user_edit)
    edit_button.bind('<FocusIn>', DML_BUTTONS_FOCUS)

    delete_button = Button(login_form, text="Delete", font=(14))
    delete_button.place(x=260, y=130, width=64)
    delete_button.bind("<Return>", user_delete)
    delete_button.bind("<ButtonRelease>", user_delete)
    delete_button.bind('<FocusIn>', DML_BUTTONS_FOCUS)

    quit_button = Button(login_form, text="Quit", font=(14))
    quit_button.place(x=330, y=130, width=64)
    quit_button.bind("<Return>", user_quit)
    quit_button.bind("<ButtonRelease>", user_quit)
    quit_button.bind('<FocusIn>', DML_BUTTONS_FOCUS)
    # *************************************** BUTTON SETTINGS - END ********************************************
    # *************************************** TREE VIEW  - BEGIN *******************************************
    global tree
    user_frame = Frame(login_form)
    user_frame.pack(pady=5)
    user_frame.place(x=10, y=180)
    user_frame.pack_propagate(False)
    user_frame.configure(width=420, height=135, bg='#63B8FF')

    Cur.execute('select * from user_master  order by user')
    col = ('user', 'password', 'crt_date', 'id')
    tree = ttk.Treeview(user_frame, height=5, show='headings', columns=col)
    tree.pack(fill=tk.X, pady=5)
    style1 = ttk.Style(user_frame)

    style1.theme_use('clam')
    style1.configure(".", font=('times new roman', 12))
    style1.configure("Treeview.Heading",foreground='#63B8FF', background='grey18', font='14')
    style1.configure("Treeview", foreground='black', background='white', fieldbackground='white',
                     font=('times new roman', 12))
    style1.map('Treeview', background=[('selected', '#63B8FF')])

    tree.column("user", width=820, minwidth=200, anchor=tk.W)
    tree.column("password", width=1, minwidth=0, anchor=tk.W)
    tree.column("crt_date", width=1, minwidth= 1, anchor=tk.CENTER)
    tree.column("id", width=80, minwidth=10, anchor=tk.CENTER)

    tree.heading("user", text="USER NAME", anchor=tk.W)
    tree.heading("password", text="PASSWORD", anchor=tk.W)
    tree.heading("crt_date", text="CREATED ON", anchor=tk.W)
    tree.heading("id", text="ID", anchor=tk.CENTER)

    i = 0
    for row in Cur:
        show_str_in_star(row[1])
        i = i + 1

    vsb = ttk .Scrollbar(user_frame, orient="vertical")
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)

    hsb = ttk.Scrollbar(user_frame, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)

    tree.pack()
    tree.bind("<Return>", select_user_data)
    tree.bind("<ButtonRelease>", select_user_data)
    tree.bind('<FocusIn>', tree_focus)
    # *************************************** TREE VIEW  - END *******************************************
