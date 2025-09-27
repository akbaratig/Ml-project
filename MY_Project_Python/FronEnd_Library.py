from tkinter import *
from tkinter import messagebox
import BackEnd_Library


window = Tk()
window.title('Library')
window.geometry('830x430')
window.resizable(width=FALSE, height=False)
window.config(bg='gray')

# ======================== func ==============================

def view_command():
    list_box.delete(0, END)
    books = BackEnd_Library.view()
    for item in books:
        list_box.insert(END,item)

def search_command():
    list_box.delete(0, END)
    books = BackEnd_Library.search(title_text.get(), Author_text.get(), year_text.get(), isbn_text.get())
    for item in books:
        list_box.insert(END, item)   

def add_command():
    BackEnd_Library.insert(title_text.get(), Author_text.get(), year_text.get(), isbn_text.get())
    view_command()


def delete_command():
    try:
        selection = list_box.curselection()
        if not selection:
            messagebox.showerror("Warning", "Please select an item to delete.")
        selected = list_box.get(selection[0])
        BackEnd_Library.delete(selected[0])
        view_command()
        e_1.delete(0, END)
        e_2.delete(0, END)
        e_3.delete(0, END)
        e_4.delete(0, END)
        
    
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to delete.")
        


def update_command():
    selected = list_box.get(list_box.curselection())
    BackEnd_Library.update(selected[0], title_text.get(), Author_text.get(), year_text.get(), isbn_text.get())
    view_command()
    e_1.delete(0, END)
    e_2.delete(0, END)
    e_3.delete(0, END)
    e_4.delete(0, END)   


def get_selected_row(event):
    global selected_book
    index = list_box.curselection()[0]
    selected_book = list_box.get(index)
        # title
    e_1.delete(0, END)
    e_1.insert(END, selected_book[1])
        # author
    e_2.delete(0, END)
    e_2.insert(END, selected_book[2])
        # year
    e_3.delete(0, END)
    e_3.insert(END, selected_book[3])
        # isbn
    e_4.delete(0, END)
    e_4.insert(END, selected_book[4])
    
    
# ==================== Labels ==============================

l_1 = Label(window, text='Title', bg='black', fg='white', width=6, height=1, font=('Arial', 20))
l_1.grid(row=0, column=0, padx=15, pady=15)
l_2 = Label(window, text='Author', bg='black', fg='white', width=6, height=1, font=('Arial', 20))
l_2.grid(row=0, column=2, padx=15, pady=15)
l_3 = Label(window, text='Year', bg='black', fg='white', width=6, height=1, font=('Arial', 20))
l_3.grid(row=1, column=0, padx=15, pady=15)
l_4 = Label(window, text='ISBN', bg='black', fg='white', width=6, height=1, font=('Arial', 20))
l_4.grid(row=1, column=2, padx=15, pady=15)

# ====================== Entryies ========================

title_text = StringVar()
e_1 = Entry(window,textvariable=title_text,  background='black', foreground='white', width=15, font=('Arial', 24))
e_1.grid(row=0, column=1, padx=0, pady=15)

Author_text = StringVar()
e_2 = Entry(window,textvariable=Author_text,  background='black', foreground='white', width=15, font=('Arial', 24))
e_2.grid(row=0, column=3, padx=0, pady=15)

year_text = StringVar()
e_3 = Entry(window,textvariable=year_text,  background='black', foreground='white', width=15, font=('Arial', 24))
e_3.grid(row=1, column=1, padx=0, pady=15) 

isbn_text = StringVar()
e_4 = Entry(window,textvariable=isbn_text,  background='black', foreground='white', width=15, font=('Arial', 24))
e_4.grid(row=1, column=3, padx=0, pady=15)

list_box = Listbox(window, width=45, height=11, bg='black', foreground='white', font=('Arial', 15))
list_box.grid(row=2, column=0, rowspan=10, columnspan=3)
list_box.bind("<<ListboxSelect>>", get_selected_row) 


Scrol = Scrollbar(window, width=20,background='black')
Scrol.place(x=524, y=143)

# ادغام اسکرول و لیست
list_box.configure(yscrollcommand=Scrol.set)
Scrol.configure(command=list_box.yview)

# ================= Buttons ===============================

b_1 = Button(window, text='View All', bg='black', fg='white', width=13, height=1, font=('Arial', 17),
             cursor='hand2', command=lambda : view_command())
b_1.grid(row=2, column=3)
b_1 = Button(window, text='Search Entry', bg='black', fg='white', width=13, height=1, font=('Arial', 17),
             cursor='hand2', command=lambda : search_command())
b_1.grid(row=3, column=3)
b_1 = Button(window, text='Add Entry', bg='black', fg='white', width=13, height=1, font=('Arial', 17),
             cursor='hand2', command=lambda : add_command())
b_1.grid(row=4, column=3)
b_1 = Button(window, text='Update Selected', bg='black', fg='white', width=13, height=1, font=('Arial', 17),
             cursor='hand2', command=lambda : update_command())
b_1.grid(row=5, column=3)
b_1 = Button(window, text='Delete Selected', bg='black', fg='white', width=13, height=1, font=('Arial', 17),
             cursor='hand2', command=lambda : delete_command())
b_1.grid(row=6, column=3)
b_1 = Button(window, text='Close', bg='black', fg='white', width=13, height=1, font=('Arial', 17),
             cursor='hand2', command=window.destroy)
b_1.grid(row=7, column=3)


view_command()
window.mainloop()