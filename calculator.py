

#! python3
# calculator.py - A simple Calculator Using Tkinter Python GUI.
# author- Madhuri Patil

from tkinter import *
from tkinter import ttk

# create root object for Tk()
root = Tk()
root.geometry("319x479+300+300")
root.resizable(0,0)
root.title('Calculator')

# create a frame on root.
mainFrame = Frame(root, bg="#222")
mainFrame.grid(column=0, row=0)
mainFrame.columnconfigure([0, 1, 2, 3], minsize=80)
mainFrame.rowconfigure([0, 1, 2, 3, 4, 5], minsize=80)

# button function
val = ''
operator = ''
A = 0
count = 0

def btn1_clicked():
    global val
    val = val + '1'
    data.set(val)

def btn2_clicked():
    global val
    val = val + '2'
    data.set(val)

def btn3_clicked():
    global val
    val = val + '3'
    data.set(val)

def btn4_clicked():
    global val
    val = val + '4'
    data.set(val)

def btn5_clicked():
    global val
    val = val + '5'
    data.set(val)

def btn6_clicked():
    global val
    val = val + '6'
    data.set(val)

def btn7_clicked():
    global val
    val = val + '7'
    data.set(val)

def btn8_clicked():
    global val
    val = val + '8'
    data.set(val)

def btn9_clicked():
    global val
    val = val + '9'
    data.set(val)

def btn0_clicked():
    global val
    val = val + '0'
    data.set(val)


# operator function.
def btnplus_clicked():
    global val, operator, A
    if val[-1] == '+':
        pass
    else:
        try:
            if '.' in val:
                A = float(val)
            else:
                A = int(val)
                operator = '+'
                val = val + '+'
                data.set(val)
        except ValueError:
            pass


def btnminus_clicked():
    global val, operator, A
    if val[-1] == '-':
        pass
    else:
        try:
            if '.' in val:
                A = float(val)
            else:
                A = int(val)
            operator = '-'
            val = val + '-'
            data.set(val)
        except ValueError:
            pass

def btndiv_clicked():
    global val, operator, A
    if val[-1] == '/':
        pass
    else:
        try:
            if '.' in val:
                A = float(val)
            else:
                A = int(val)
            operator = '/'
            val = val + '/'
            data.set(val)
        except ValueError:
            pass

def btnmul_clicked():
    global val, operator, A
    if val[-1] == 'x':
        pass
    else:
        try:
            if '.' in val:
                A = float(val)
            else:
                A = int(val)
            operator = 'x'
            val = val + 'x'
            data.set(val)
        except ValueError:
            pass

def btndot_clicked():
    global val
    if val[-1] == '.':
        pass
    else:
        if val.count('.') < 1:
            val = val + '.'
            data.set(val)

def btnpercent_clicked():
    global val, operator, A
    if len(val) == 0 or val[-1] == '%':
        pass
    else:
        try:
            if '.' in val:
                A = float(val)
            else:
                A = int(val)
            operator = '%'
            if val.count('%') < 1:
                val = val + '%'
                data.set(val)
            else:
                pass
        except ValueError:
            pass

def btnac_clicked():
    global val, operator, A
    val = ''
    operator = ''
    A = ''
    data.set(val)

def btnC_clicked():
    global val, operator, A
    val = val[:len(val)-1]
    data.set(val)

# result function.
def equal_pressed():
    global val, operator, A
    val2 = val
    result = 0
    if operator == '+':
        x = val2.split('+')[1]
        if '.' in x:
            x = float(x)
            val = str(A + x)
            data.set(str(val))
        else:
            x = int(x)
            val = str(A + x)
            data.set(str(val))

    if operator == '-':
        x = val2.split('-')[1]
        if '.' in x:
            x = float(x)
            val = str(A - x)
            data.set(str(val))

        else:
            x = int(x)
            val = str(A - x)
            data.set(str(val))

    if operator == 'x':
        x = val2.split('x')[1]
        if '.' in x:
            x = float(x)
            val = str(A * x)
            data.set(str(val))

        else:
            x = int(x)
            val = str(A * x)
            data.set(str(val))

    if operator == '/':
        x = val2.split('/')[1]
        if x == '0':
            data.set('Infinite')
        elif '.' in x:
            x = float(x)
            val = str(A / x)
            data.set(str(val))
        else:
            x = int(x)
            val = str(A / x)
            data.set(str(val))

    if operator == '%':
        x = val2.split('%')[1]
        if x == '':
            val = str(A/100)
            data.set(str(val))

        elif '.' in x:
            x = float(x)
            val = str((A / 100) * x)
            data.set(val)
        else:
            x = int(x)
            val = str((A / 100) * x)
            data.set(val)



# create a display label.

data = StringVar()
display_data = Label(
    mainFrame,
    text = 'Label',
    anchor = SE,
    font= ('San Serif',22),
    textvariable = data,
    bg = '#fafaff',
    fg = '#222',
    highlightthickness=0,
)
display_data.grid(columnspan=4, row=0, sticky=('nsew'),)
display_data.config(width=1, height=2)

# second row
btn_ac = Button(
    mainFrame,
    text='ac',
    font=("San Serif", 16),
    border=0,
    bg = '#1e1e1f',
    fg = '#faffaf',
    highlightthickness=0,
    command = btnac_clicked,
)
btn_ac.grid(column=0, row=1, sticky=('nsew'),)

btn_percent = Button(
    mainFrame,
    text='%',
    font=("San Serif", 16),
    border=0,
    bg = '#1e1e1f',
    fg = '#faffaf',
    highlightthickness=0,
    command = btnpercent_clicked,
)
btn_percent.grid(column=1, row=1, sticky=('nsew'))

btn_div = Button(
    mainFrame,
    text='/',
    font=("San Serif", 16),
    border=0,
    bg = '#1e1e1f',
    fg = '#faffaf',
    highlightthickness=0,
    command= btndiv_clicked,
)
btn_div.grid(column=2, row=1, sticky=('nsew'))

btn_mul = Button(
    mainFrame,
    text='x',
    font=("San Serif", 16),
    border=0,
    bg = '#1e1e1f',
    fg = '#faffaf',
    highlightthickness=0,
    command= btnmul_clicked,
)
btn_mul.grid(column=3, row=1, sticky=('nsew'))

# third row
btn_7 = Button(
    mainFrame,
    text='7',
    font=("San Serif", 16),
    border=0,
    bg = '#222',
    fg = '#faffaf',
    highlightthickness=0,
    command = btn7_clicked,
)
btn_7.grid(column=0, row=2, sticky=('nsew'))

btn_8 = Button(
    mainFrame,
    text='8',
    font=("San Serif", 16),
    border=0,
    bg = '#222',
    fg = '#faffaf',
    highlightthickness=0,
    command=btn8_clicked,

)
btn_8.grid(column=1, row=2, sticky=('nsew'))

btn_9 = Button(
    mainFrame,
    text='9',
    font=("San Serif", 16),
    border=0,
    bg = '#222',
    fg = '#faffaf',
    highlightthickness=0,
    command=btn9_clicked,
)
btn_9.grid(column=2, row=2, sticky=('nsew'))

btn_minus = Button(
    mainFrame,
    text='-',
    font=("San Serif", 16),
    border=0,
    bg = '#1e1e1f',
    fg = '#faffaf',
    highlightthickness=0,
    command=btnminus_clicked,
)
btn_minus.grid(column=3, row=2, sticky=('nsew'))

# fourth row
btn_4 = Button(
    mainFrame,
    text='4',
    font=("San Serif", 16),
    border=0,
    bg = '#222',
    fg = '#faffaf',
    highlightthickness=0,
    command=btn4_clicked,
)
btn_4.grid(column=0, row=3, sticky=('nsew'))

btn_5 = Button(
    mainFrame,
    text='5',
    font=("San Serif", 16),
    border=0,
    bg = '#222',
    fg = '#faffaf',
    highlightthickness=0,
    command=btn5_clicked,
)
btn_5.grid(column=1, row=3, sticky=('nsew'))

btn_6 = Button(
    mainFrame,
    text='6',
    font=("San Serif", 16),
    border=0,
    bg = '#222',
    fg = '#faffaf',
    highlightthickness=0,
    command=btn6_clicked,
)
btn_6.grid(column=2, row=3, sticky=('nsew'))

btn_plus = Button(
    mainFrame,
    text='+',
    font=("San Serif", 16),
    border=0,
    bg = '#1e1e1f',
    fg = '#faffaf',
    highlightthickness=0,
    command=btnplus_clicked,
)
btn_plus.grid(column=3, row=3, sticky=('nsew'))

# fifth row
btn_1 = Button(
    mainFrame,
    text='1',
    font=("San Serif", 16),
    border=0,
    bg = '#222',
    fg = '#faffaf',
    highlightthickness=0,
    command=btn1_clicked,
)
btn_1.grid(column=0, row=4, sticky=('nsew'))

btn_2 = Button(
    mainFrame,
    text='2',
    font=("San Serif", 16),
    border=0,
    bg = '#222',
    fg = '#faffaf',
    highlightthickness=0,
    command=btn2_clicked,
)
btn_2.grid(column=1, row=4, sticky=('nsew'))

btn_3 = Button(
    mainFrame,
    text='3',
    font=("San Serif", 16),
    border=0,
    bg = '#222',
    fg = '#faffaf',
    highlightthickness=0,
    command = btn3_clicked,
)
btn_3.grid(column=2, row=4, sticky=('nsew'))


btn_equal = Button(
    mainFrame,
    text='=',
    font=("San Serif", 20),
    border=0,
    bg="#ff6b08",
    fg = '#faffaf',
    highlightthickness=0,
    command=equal_pressed,
)
btn_equal.grid(column=3, row=4, sticky=('nsew'), rowspan=2)

# sixth row
btn_c = Button(
    mainFrame,
    text='C',
    font=("San Serif", 16),
    border=0,
    bg = '#1e1e1f',
    fg = '#faffaf',
    highlightthickness=0,
    command= btnC_clicked,
)
btn_c.grid(column=0, row=5, sticky=('nsew'))

btn_0 = Button(
    mainFrame,
    text='0',
    font=("San Serif", 16),
    border=0,
    bg = '#222',
    fg = '#faffaf',
    highlightthickness=0,
    command=btn0_clicked,
)
btn_0.grid(column=1, row=5, sticky=('nsew'))

btn_dot = Button(
    mainFrame,
    text='.',
    font=("San Serif", 16),
    border=0,
    bg = '#1e1e1f',
    fg = '#faffaf',
    highlightthickness=0,
    command=btndot_clicked,
)
btn_dot.grid(column=2, row=5, sticky=('nsew'))

# close root.
root.mainloop()
