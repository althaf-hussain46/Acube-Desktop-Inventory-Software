from tkinter import*
import tkinter as tk
from tkinter import ttk

def Design_About_Us_Form_Load():
    about_us_form = tk.Toplevel()
    about_us_form.geometry('760x520+270+100')
    about_us_form.config(bg='#B0E2FF')
    about_us_form.focus_set()
    about_us_form.title('ABOUT')
    about_us_form.resizable(False, False)

    form_name = Label(about_us_form, text="A B O U T", fg="black", bg="#63B8FF", width=500, font=('copper', 20, 'bold'))
    form_name.pack(side=TOP)
    form_bottom = Label(about_us_form, text="", bg="#63B8FF", width=500, height=2)
    form_bottom.pack(side=BOTTOM)

    # *************************************** LABEL SETTINGS - BEGIN *******************************************
    about_us_text = "\n      I   am   a   final   year   student,  passionate   about   developing   innovative   and   effective solutions\n" \
                    "for   the   retail  industry.  My  project,  the 'Inventory  Software  for  Retail Shop', is aimed at streamlining\n" \
                    "the  inventory  management  process   for   retail   shops.  With   my  combined  skills  and  expertise  in\n" \
                    "software  development,  I  aim  to deliver a  user-friendly  and  efficient software   that  will  help retailers \n" \
                    "to track their stock levels, manage their purchasing, and make informed decisions about their inventory." \
                    "\n\n      My goal  is  to  provide  a  comprehensive  solution  that will save retailers time and money and help \n" \
                    "them   grow  their  businesses.  I  believe  that  my  project  will  make  a  positive  impact  on  the  retail  \n" \
                    "industry    and   I  am   committed    to   delivering    a   high-quality   product   that  exceeds   my  clients\n" \
                    "expectations. \n\n"\
                    "     With  hard   work,  dedication  and  a  commitment  to excellence, I  am  confident  that  my 'Inventory \n" \
                    "Software  for  Retail  Shop'   will   be  a  game-changer  in   the industry.  I  look forward   to  sharing my \n" \
                    "passion and expertise with you and helping you to achieve your business goals."\
                    "\n\n\n\t\t\t\tJ. Althaf Hussain"


    label1 = Label(about_us_form, text=about_us_text, bg='#B0E2FF', fg='black', font=(12), justify=LEFT)
    label1.place(x=30, y=45)
