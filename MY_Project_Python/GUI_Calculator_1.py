from tkinter import *
from tkinter import messagebox

# Root ---------------------------------------------------
root = Tk()
root.title('Calculator')
root.geometry('440x400')
root.resizable(height=False, width=False)
root.config(bg="#343434")

# Flag to check if '=' was pressed
calculated = False

# Func ---------------------------------------------------
def show(value):
    global calculated

    if calculated:
        # If last action was '=', clear everything
        entry_1.config(state="normal")
        entry_1.delete(0, END)
        entry_1.config(state="disabled")

        entry_2.config(state="normal")
        entry_2.delete(0, END)
        entry_2.config(state="disabled")

        calculated = False  # Reset flag

    entry_1.config(state="normal")
    entry_1.insert(END, value)
    entry_1.config(state="disabled")


def calculate_result():
    global calculated
    expression = entry_1.get()

    try:
        result = eval(expression)
    except:
        result = "خطا!"

    entry_2.config(state="normal")
    entry_2.delete(0, END)
    entry_2.insert(0, str(result))
    entry_2.config(state="disabled")

    calculated = True  # Set flag to indicate calculation done


def clear_all():
    global calculated
    calculated = False

    entry_1.config(state="normal")
    entry_1.delete(0, END)
    entry_1.config(state="disabled")

    entry_2.config(state="normal")
    entry_2.delete(0, END)
    entry_2.config(state="disabled")


# Entry--------------------------------------------------
entry_1 = Entry(root, font=("Arial", 20), width=27, relief=FLAT, background='black', foreground='white', justify=CENTER, 
                state="disabled", disabledbackground='#343434', disabledforeground='white') 
entry_1.place(x = 10, y = 10)

entry_2 = Entry(root, font=("Arial", 20), width=27, relief=FLAT, background='black', foreground='white', justify=CENTER,
                state="disabled", disabledbackground="#343434", disabledforeground='white') 
entry_2.place(x = 10, y = 50)

# Button-------------------------------------------------
button_7 = Button(root, text='7',  width=10, height=3, background='black', foreground='white', 
                font=20,cursor='hand2', command=lambda : show('7'))
button_7.place(x=10, y=95)
button_8 = Button(root, text='8', width=10, height=3, background='black', foreground='white',
                font=20,cursor='hand2', command=lambda : show('8'))
button_8.place(x=115, y=95)
button_9 = Button(root, text='9', width=10, height=3, background='black', foreground='white',
                font=20,cursor='hand2', command=lambda : show('9'))
button_9.place(x=220, y=95)
button_Plus = Button(root, text='+', width=10, height=3, background='black', foreground='white',
                font=20,cursor='hand2', command=lambda : show('+'))
button_Plus.place(x=325, y=95)

button_4 = Button(root, text='4', width=10, height=3, background='black', foreground='white',
                  font=20,cursor='hand2', command=lambda : show('4'))
button_4.place(x=10, y=170)
button_5 = Button(root, text='5', width=10, height=3, background='black', foreground='white', 
                  font=20,cursor='hand2', command=lambda : show('5'))
button_5.place(x=115, y=170)
button_6 = Button(root, text='6', width=10, height=3, background='black', foreground='white', 
                  font=20,cursor='hand2', command=lambda : show('6'))
button_6.place(x=220, y=170)
button_minus = Button(root, text='-', width=10, height=3, background='black', foreground='white', 
                      font=20,cursor='hand2', command=lambda : show('-'))
button_minus.place(x=325, y=170)

button_1 = Button(root, text='1', width=10, height=3, background='black', foreground='white', 
                  font=20,cursor='hand2', command=lambda : show('1'))
button_1.place(x=10, y=245)
button_2 = Button(root, text='2', width=10, height=3, background='black', foreground='white', 
                  font=20,cursor='hand2', command=lambda : show('2'))
button_2.place(x=115, y=245)
button_3 = Button(root, text='3', width=10, height=3, background='black', foreground='white', 
                  font=20,cursor='hand2', command=lambda : show('3'))
button_3.place(x=220, y=245)
button_Mul = Button(root, text='*', width=10, height=3, background='black', foreground='white', 
                    font=20,cursor='hand2', command=lambda : show('*'))
button_Mul.place(x=325, y=245)

button_0 = Button(root, text='0', width=10, height=3, background='black', foreground='white', 
                  font=20,cursor='hand2', command=lambda : show('0'))
button_0.place(x=10, y=320)
button_c = Button(root, text='c', width=10, height=3, background='black', foreground='white', 
                  font=20,cursor='hand2', command=clear_all)
button_c.place(x=115, y=320)
button_res = Button(root, text='=', width=10, height=3, background='black', foreground='white', 
                    font=20,cursor='hand2', command=calculate_result)
button_res.place(x=220, y=320)
button_div = Button(root, text='/', width=10, height=3, background='black', foreground='white', 
                    font=20,cursor='hand2', command=lambda : show('/'))
button_div.place(x=325, y=320)

root.mainloop()

