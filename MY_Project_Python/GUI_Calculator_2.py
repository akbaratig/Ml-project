from tkinter import *
from tkinter import messagebox

# ============ Root =====================
root = Tk()
root.title("Calculator")
root.resizable(width=FALSE, height=FALSE)
root.geometry('400x350')
root.config(bg="#343434")

# =============== Variable ====================

num1 = StringVar()
num2 = StringVar()
res_num = StringVar()

# ============ func ========================

def plus():
    try:
        result = float(num1.get()) + float(num2.get())
        res_num.set(result)
    except ValueError:
        messagebox.showerror("خطا", "لطفاً فقط عدد وارد کنید.")

def minus():
    try:
        result = float(num1.get()) - float(num2.get())
        res_num.set(result)
    except ValueError:
        messagebox.showerror("خطا", "لطفاً فقط عدد وارد کنید.")

def mul():
    try:
        result = float(num1.get()) * float(num2.get())
        res_num.set(result)
    except ValueError:
        messagebox.showerror("خطا", "لطفاً فقط عدد وارد کنید.")
     
def divide():
    if num2.get() == '0':
       messagebox.showerror('Error', 'Please not Enter a Zero Number...')
    elif num2.get() != '0':
        try:
            result = float(num1.get()) / float(num2.get())
            res_num.set(result)
        except ValueError:
            messagebox.showerror("خطا", "لطفاً فقط عدد وارد کنید.")
        
# ================== Lable ======================
label_1 = Label(root, text='Number 1 : ', bg='black', fg='white',width=12, height=3)
label_1.place(x=10, y=10)

label_2 = Label(root, text='Number 2 : ', bg='black', fg='white', width=12, height=3)
label_2.place(x=10, y=70)

# ================== Entry =======================
entry_1 = Entry(root, bg='black', fg='white', width=12, font=("Arial", 31), justify=CENTER,
                textvariable=num1)
entry_1.place(x=110, y=10)

entry_2 = Entry(root, bg='black', fg='white', width=12, font=("Arial", 31), justify=CENTER,
                textvariable=num2)
entry_2.place(x=110, y=70)

res = Entry(root, bg='black', fg='white', width=16, font=('Arial', 31), justify=CENTER,
            textvariable=res_num)
res.place(x=14, y=250)

# ================== Button ======================
button_plus = Button(root, text='+', bg='black', fg='white', font=('Arial', 25), width=4,
                     command=lambda : plus())
button_plus.place(x=10, y=135)

button_Minus = Button(root, text='-', bg='black', fg='white', font=('Arial', 25), width=4,
                      command=lambda : minus())
button_Minus.place(x=108, y=135)

button_mul = Button(root, text='*', bg='black', fg='white', font=('Arial', 25), width=4,
                    command=lambda : mul())
button_mul.place(x=208, y=135)

button_res = Button(root, text='/', bg='black', fg='white', font=('Arial', 25), width=4,
                    command=lambda : divide())
button_res.place(x=308, y=135)

root.mainloop()