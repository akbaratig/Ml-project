from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('XO Game')
window.resizable(width=FALSE, height=FALSE)
window.geometry('460x560')
window.config(bg='white')

# =================== functions =====================
clicked = True
count = 0   

def b_click(b):
    global clicked, count
    
    if b['text'] == ' ' and clicked == True:
        b['text'] = 'X'
        clicked = False
        count += 1
    elif b['text'] == ' ' and clicked == False:
        b['text'] = 'O'
        clicked = True
        count += 1
    else:
        messagebox.showerror('TIC TAC TOE', 'Hey That Box Has Already Been Selected')
    check_if_won()
    
    
def reset_game():
    global clicked, count 
    clicked = True
    count = 0

    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    
    for b in buttons:
        b['text'] = ' '
    for b in buttons:
        b['bg'] = 'white'


def check_if_won():
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1['bg'] = ('chartreuse3')
        b2['bg'] = ('chartreuse3')
        b3['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player X is Winner................')
        reset_game()
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        b4['bg'] = ('chartreuse3')
        b5['bg'] = ('chartreuse3')
        b6['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player X is Winner................')
        reset_game()
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        b7['bg'] = ('chartreuse3')
        b8['bg'] = ('chartreuse3')
        b9['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player X is Winner................')
        reset_game()
    if b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b1['bg'] = ('chartreuse3')
        b4['bg'] = ('chartreuse3')
        b7['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player X is Winner................')
        reset_game()
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        b2['bg'] = ('chartreuse3')
        b5['bg'] = ('chartreuse3')
        b8['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player X is Winner................')
        reset_game()
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        b3['bg'] = ('chartreuse3')
        b6['bg'] = ('chartreuse3')
        b9['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player X is Winner................')
        reset_game()
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1['bg'] = ('chartreuse3')
        b2['bg'] = ('chartreuse3')
        b3['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player X is Winner................')
        reset_game()
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b1['bg'] = ('chartreuse3')
        b4['bg'] = ('chartreuse3')
        b7['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player X is Winner................')
        reset_game()
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b1['bg'] = ('chartreuse3')
        b5['bg'] = ('chartreuse3')
        b9['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player X is Winner................')
        reset_game()
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b1['bg'] = ('chartreuse3')
        b5['bg'] = ('chartreuse3')
        b9['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player X is Winner................')
        reset_game()
    elif b7['text'] == 'X' and b5['text'] == 'X' and b3['text'] == 'X':
        b7['bg'] = ('chartreuse3')
        b5['bg'] = ('chartreuse3')
        b3['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player X is Winner................')
        reset_game()
    
    if b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        b1['bg'] = ('chartreuse3')
        b2['bg'] = ('chartreuse3')
        b3['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player O is Winner................')
        reset_game()
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        b4['bg'] = ('chartreuse3')
        b5['bg'] = ('chartreuse3')
        b6['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player O is Winner................')
        reset_game()
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        b7['bg'] = ('chartreuse3')
        b8['bg'] = ('chartreuse3')
        b9['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player O is Winner................')
        reset_game()
    if b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b1['bg'] = ('chartreuse3')
        b4['bg'] = ('chartreuse3')
        b7['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player O is Winner................')
        reset_game()
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        b2['bg'] = ('chartreuse3')
        b5['bg'] = ('chartreuse3')
        b8['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player O is Winner................')
        reset_game()
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        b3['bg'] = ('chartreuse3')
        b6['bg'] = ('chartreuse3')
        b9['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player O is Winner................')
        reset_game()
    if b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        b1['bg'] = ('chartreuse3')
        b2['bg'] = ('chartreuse3')
        b3['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player O is Winner................')
        reset_game()
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b1['bg'] = ('chartreuse3')
        b4['bg'] = ('chartreuse3')
        b7['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player O is Winner................')
        reset_game()
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b1['bg'] = ('chartreuse3')
        b5['bg'] = ('chartreuse3')
        b9['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player O is Winner................')
        reset_game()
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b1['bg'] = ('chartreuse3')
        b5['bg'] = ('chartreuse3')
        b9['bg'] = ('chartreuse3')
        messagebox.showerror('Show Winner', 'Player O is Winner................')
        reset_game()
    elif b7['text'] == 'O' and b5['text'] == 'O' and b3['text'] == 'O':
        b7['bg'] = ('chartreuse3')
        b5['bg'] = ('chartreuse3')
        b3['bg'] = ('rechartreuse3d')
        messagebox.showerror('Show Winner', 'Player O is Winner................')
        reset_game()
    
    if count == 9:
        messagebox.showerror('TIC TAC TOE', 'TIHS GAME IS TIE....')
        reset_game()
        
               
         
# =================== Buttons =======================

b1 = Button(window, text=' ', font=('', 20), height=4, width=9, command=lambda : b_click(b1), bg='white', fg='black')
b2 = Button(window, text=' ', font=('', 20), height=4, width=9, command=lambda : b_click(b2), bg='white', fg='black')
b3 = Button(window, text=' ', font=('', 20), height=4, width=9, command=lambda : b_click(b3), bg='white', fg='black')

b4 = Button(window, text=' ', font=('', 20), height=4, width=9, command=lambda : b_click(b4), bg='white', fg='black')
b5 = Button(window, text=' ', font=('', 20), height=4, width=9, command=lambda : b_click(b5), bg='white', fg='black')
b6 = Button(window, text=' ', font=('', 20), height=4, width=9, command=lambda : b_click(b6), bg='white', fg='black')

b7 = Button(window, text=' ', font=('', 20), height=4, width=9, command=lambda : b_click(b7), bg='white', fg='black')
b8 = Button(window, text=' ', font=('', 20), height=4, width=9, command=lambda : b_click(b8), bg='white', fg='black')
b9 = Button(window, text=' ', font=('', 20), height=4, width=9, command=lambda : b_click(b9), bg='white', fg='black')

b_reset = Button(window, text='Reset', font=('', 17), width=7, height=1, bg='black', fg='white',command=lambda : reset_game())
b_close = Button(window, text='Close', font=('', 17), bg='black', fg='white', command=window.destroy)

# ======================= locations with grids ======================

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

b_reset.place(x=100, y=480)
b_close.place(x=270, y=480)



window.mainloop()