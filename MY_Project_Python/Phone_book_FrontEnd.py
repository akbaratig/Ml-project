from tkinter import *
from tkinter import messagebox
import Phone_Book_BackEnd

window = Tk()
window.title('Phone book')
window.geometry('1280x760')
window.resizable(width=False, height=FALSE)
window.config(bg='white')

# ======================= functions =============================

def view_all():
    list_box.delete(0, END)
    person = Phone_Book_BackEnd.view()
    for item in person:
        list_box.insert(END, item)

def add_command():
    Phone_Book_BackEnd.insert(name_text.get(), email_text.get(), gender_text.get(), mobile_text.get(),
                tel_text.get(), adres_text.get())
    view_all()
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_gender.delete(0, END)
    e_mobile.delete(0, END)
    e_tel.delete(0, END)
    e_address.delete(0, END)


def delete_command():
    try:
        selection = list_box.curselection()
        if not selection:
            messagebox.showerror("Warning", "Please select an item to delete.")
        selected = list_box.get(selection[0])
        Phone_Book_BackEnd.delete(selected[0])
        view_all()
        e_name.delete(0, END)
        e_email.delete(0, END)
        e_gender.delete(0, END)
        e_mobile.delete(0, END)
        e_tel.delete(0, END)
        e_address.delete(0, END)
  
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to delete.")
        

def search_command():
    list_box.delete(0, END)
    persons = Phone_Book_BackEnd.search(name_text.get(), email_text.get(), gender_text.get(),
                              mobile_text.get(), tel_text.get(), adres_text.get())
    for item in persons:
        list_box.insert(END, item)
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_gender.delete(0, END)
    e_mobile.delete(0, END)
    e_tel.delete(0, END)
    e_address.delete(0, END)


def update_command():
    selected = list_box.get(list_box.curselection())
    Phone_Book_BackEnd.update(selected[0], name_text.get(), email_text.get(), gender_text.get(), mobile_text.get(),
                              tel_text.get(), adres_text.get())
    view_all()
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_gender.delete(0, END)
    e_mobile.delete(0, END)   
    e_tel.delete(0, END) 
    e_address.delete(0, END) 


def on_select(event):
    global selected_id
    try:
        index = list_box.curselection()[0]
        selected = list_box.get(index)

        # فرض: selected شکلی مثل (id, name, email, gender, mobile, tel, address) دارد
        selected_id = selected[0]  # این id اصلی در دیتابیس است

        e_name.delete(0, END)
        e_name.insert(END, selected[1])

        e_email.delete(0, END)
        e_email.insert(END, selected[2])

        e_gender.delete(0, END)
        e_gender.insert(END, selected[3])

        e_mobile.delete(0, END)
        e_mobile.insert(END, selected[4])

        e_tel.delete(0, END)
        e_tel.insert(END, selected[5])

        e_address.delete(0, END)
        e_address.insert(END, selected[6])

    except IndexError:
        pass
    
# ================= labels ======================

label_header = Label(window, text='Contacts Book', width=66, height=2, font=('', 25),bg='chartreuse3', fg='white',
                    relief=SOLID)
label_header.place(x=10, y=10)
label_manage = Label(window, text='Mange contacts', bg='white', font=('', 20))
label_manage.place(x=180, y=150)
label_name = Label(window, text='Name', font=('', 15), bg='white')
label_name.place(x=30, y=220)
label_email = Label(window, text='Email', font=('', 15), bg='white')
label_email.place(x=30, y=290)
label_gender = Label(window, text='Gender', font=('', 15), bg='white')
label_gender.place(x=30, y= 360)
label_mobile = Label(window, text='Mobile NO', font=('', 15), bg='white')
label_mobile.place(x=30, y=430)
label_tel = Label(window, text='Tel No', font=('', 15), bg='white')
label_tel.place(x=30, y=510)
label_addres = Label(window, text='Address', font=('', 15), bg='white')
label_addres.place(x=30, y=580)

# =========================== Buttons ============================

but_view = Button(window, text='View', font=('', 22), bg='chartreuse3', fg='white', relief=GROOVE, cursor='hand2',
                  command=lambda : view_all())
but_view.place(x=30, y=660)

but_add = Button(window, text='Add Contact', font=('', 22), bg='chartreuse3', fg='white', relief=GROOVE, cursor='hand2',
                 command=lambda : add_command())
but_add.place(x=130, y=660)

but_up = Button(window, text='Update', font=('', 22), bg='chartreuse3', fg='white', relief=GROOVE, cursor='hand2',
                command=update_command)
but_up.place(x=330, y=660)

but_del = Button(window, text='Delete', font=('', 22), bg='chartreuse3', fg='white', relief=GROOVE, cursor='hand2',
                 command=delete_command)
but_del.place(x=460, y=660)

but_close = Button(window, text='close', font=('', 22), bg='chartreuse3', fg='white', relief=GROOVE, command=window.destroy)
but_close.place(x=1150, y=660)

but_search = Button(window, text='Search', font=('', 22), bg='chartreuse3', fg='white', relief=GROOVE, cursor='hand2',
                    command=search_command)
but_search.place(x=1000, y=660)

# ============================== Entries ==============================

name_text = StringVar()
e_name = Entry(window, textvariable=name_text, font=('', 23), relief='solid', fg='gray')
e_name.place(x=170, y=220)

email_text = StringVar()
e_email = Entry(window, textvariable=email_text, font=('', 23), relief='solid', fg='gray')
e_email.place(x=170, y= 285)

gender_text = StringVar()
e_gender = Entry(window, textvariable=gender_text, font=('', 23), relief='solid', fg='gray')
e_gender.place(x=170, y= 360)
 
mobile_text = StringVar()
e_mobile = Entry(window, textvariable=mobile_text, font=('', 23), relief='solid', fg='gray')
e_mobile.place(x=170, y= 430)

tel_text = StringVar()
e_tel = Entry(window, textvariable=tel_text, font=('', 23), relief='solid', fg='gray')
e_tel.place(x=170, y= 505)

adres_text = StringVar()
e_address = Entry(window, textvariable=adres_text, font=('', 23), relief='solid', fg='gray')
e_address.place(x=170, y= 570)

# ======================= list box ==============================

list_box = Listbox(window, width=40, height=13, bg='white', fg='black', font=('', 22), relief=SOLID,
                   selectbackground='gray', )
list_box.place(x=580, y=170)
list_box.bind('<<ListboxSelect>>', on_select)

Scrol = Scrollbar(window, width=20,background='white')
Scrol.place(x=1230, y=167)

Scrol_2 = Scrollbar(window, width=20,background='white',orient="horizontal")
Scrol_2.place(x=1170, y=620)

# ادغام اسکرول و لیست
list_box.configure(yscrollcommand=Scrol.set)
Scrol.configure(command=list_box.yview)

list_box.configure(xscrollcommand=Scrol_2.set)
Scrol_2.configure(command=list_box.xview)



view_all()
window.mainloop()