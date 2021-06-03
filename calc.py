from tkinter import *
from tkinter.messagebox import *

# Creating the root window
root = Tk()
root.title('Calculator')
root.iconbitmap('calc.ico')
root.geometry("300x450+500+100")
root.resizable(1,1)

# Defining functions and initializing some values
val_before_operator = 0
operator = ""

def btn1_clicked():
    global output
    output.set(output.get()+'1') 

def btn2_clicked():
    global output
    output.set(output.get()+'2') 

def btn3_clicked():
    global output
    output.set(output.get()+'3') 

def btn4_clicked():
    global output
    output.set(output.get()+'4') 

def btn5_clicked():
    global output
    output.set(output.get()+'5') 

def btn6_clicked():
    global output
    output.set(output.get()+'6') 

def btn7_clicked():
    global output
    output.set(output.get()+'7') 

def btn8_clicked():
    global output
    output.set(output.get()+'8') 

def btn9_clicked():
    global output
    output.set(output.get()+'9') 

def btn0_clicked():
    global output
    output.set(output.get()+'0')

def btn_pt_clicked():
    global output
    output.set(output.get()+'.')

def btn_bkspc_clicked():
    global output
    output.set(str(output.get()).strip()[:len(str(output.get()).strip())-1])

def btn_pls_clicked():
    global output, val_before_operator, operator
    if output.get():
        try: 
            val_before_operator= float(output.get())
            operator = '+'
            output.set(output.get()+ ' + ') 
        except ValueError:
            btn_eqs_clicked()
            btn_pls_clicked()
        except Exception:
            btn_cls_clicked()
    else:
        output.set('+')

def btn_mns_clicked():
    global output, val_before_operator, operator
    if output.get():
        try:
            val_before_operator= float(output.get())
            operator = '-'
            output.set(output.get()+ ' - ') 
        except ValueError:
            btn_eqs_clicked()
            btn_mns_clicked()
        except Exception:
            btn_cls_clicked()
    else:
        output.set('-')
    

def btn_mul_clicked():
    global output, val_before_operator, operator
    if output.get():
        try:
            val_before_operator= float(output.get())
            operator = '×'
            output.set(output.get()+ ' × ')
        except ValueError:
            btn_eqs_clicked()
            btn_mul_clicked()
        except Exception:
            btn_cls_clicked()
    else:
        showinfo("Info", 'Please provide a value to multiply with!!!')

def btn_div_clicked():
    global output, val_before_operator, operator
    if output.get():
        try:
            val_before_operator= float(output.get())
            operator = '÷'
            output.set(output.get()+' ÷ ')
        except ValueError:
            btn_eqs_clicked()
            btn_div_clicked()
        except Exception:
            btn_cls_clicked()
    else:
        showinfo("Info", 'Please provide a value to divide with!!!')
def btn_eqs_clicked():
    global output, val_before_operator, operator
    try:
        if operator:
            if len(output.get().split(operator)) == 3:
                val_before_eqs= float(output.get().split(operator)[2].strip())
            else:
                val_before_eqs= float(output.get().split(operator)[1].strip())
            if operator == '+':
                output.set(val_before_operator+val_before_eqs)
            elif operator == '-':
                output.set(val_before_operator-val_before_eqs)
            elif operator == '÷':
                if val_before_eqs == 0:
                    showinfo("Info!", "Division by zero is undefined!!!")
                    output.set(str(int(val_before_operator))+ " "+operator+" ")
                else:
                    output.set(val_before_operator/val_before_eqs)
            elif operator == '×':
                output.set(val_before_operator*val_before_eqs)
        else:
            output.set(output.get())
    except ValueError:
        showerror('Error!',"Multiple operations can't be performed at once!")
        raise Exception
    except Exception:
        btn_cls_clicked()
        

def btn_cls_clicked():
    output.set('')

# Creating the frame and row for output
output = StringVar()
output_row = LabelFrame(root, bg= '#000000', padx=2, pady=2)
output_row.pack(expand=True, fill=BOTH)
lbl = Label(output_row, bg ='#ffffff', anchor=SE, textvariable=output, font=("Verdana", 20))
lbl.pack(expand=True, fill=BOTH)

# Creating frames for buttons
btn_row1 = Frame(root)
btn_row2 = Frame(root)
btn_row3 = Frame(root)
btn_row4 = Frame(root)
btn_row5 = Frame(root)
btn_row1.pack(expand=True, fill='both')
btn_row2.pack(expand=True, fill='both')
btn_row3.pack(expand=True, fill='both')
btn_row4.pack(expand=True, fill='both')
btn_row5.pack(expand=True, fill=BOTH)

# Creating buttons in row 1
btn_1 = Button(btn_row1, text='1', font=("Verdana", 22), border=0, activebackground='#808080', command=btn1_clicked)
btn_2 = Button(btn_row1, text='2', font=("Verdana", 22), border=0, activebackground='#808080', command= btn2_clicked)
btn_3 = Button(btn_row1, text='3', font=("Verdana", 22), border=0, activebackground='#808080', command= btn3_clicked)
btn_pls = Button(btn_row1, text='+', font=("Verdana", 22), border=0, activebackground='#808080',fg='blue', activeforeground='blue', command= btn_pls_clicked)
btn_1.pack(expand=True,fill=BOTH, side=LEFT)
btn_2.pack(expand=True,fill=BOTH, side=LEFT)
btn_3.pack(expand=True,fill=BOTH, side=LEFT)
btn_pls.pack(expand=True,fill=BOTH, side=LEFT)

# Creating buttons in row 2
btn_4 = Button(btn_row2, text='4', font=("Verdana", 22), border=0, activebackground='#808080', command=btn4_clicked)
btn_5 = Button(btn_row2, text='5', font=("Verdana", 22), border=0, activebackground='#808080', command=btn5_clicked)
btn_6 = Button(btn_row2, text='6', font=("Verdana", 22), border=0, activebackground='#808080', command=btn6_clicked)
btn_mns = Button(btn_row2, text='-', font=("Verdana", 22), border=0, activebackground='#808080',fg='blue', activeforeground='blue', command=btn_mns_clicked)
btn_4.pack(expand=True,fill=BOTH, side=LEFT)
btn_5.pack(expand=True,fill=BOTH, side=LEFT)
btn_6.pack(expand=True,fill=BOTH, side=LEFT)
btn_mns.pack(expand=True,fill=BOTH, side=LEFT)

# Creating buttons in row 3
btn_7 = Button(btn_row3, text='7', font=("Verdana", 22), border=0, activebackground='#808080', command=btn7_clicked)
btn_8 = Button(btn_row3, text='8', font=("Verdana", 22), border=0, activebackground='#808080', command=btn8_clicked)
btn_9 = Button(btn_row3, text='9', font=("Verdana", 22), border=0, activebackground='#808080', command=btn9_clicked)
btn_mul = Button(btn_row3, text='×', font=("Verdana", 22), border=0, activebackground='#808080',fg='blue', activeforeground='blue', command=btn_mul_clicked)
btn_7.pack(expand=True,fill=BOTH, side=LEFT)
btn_8.pack(expand=True,fill=BOTH, side=LEFT)
btn_9.pack(expand=True,fill=BOTH, side=LEFT)
btn_mul.pack(expand=True,fill=BOTH, side=LEFT)

# Creating buttons in row 4
btn_0 = Button(btn_row4, text='0', font=("Verdana", 22), border=0, activebackground='#808080', command=btn0_clicked)
btn_pt = Button(btn_row4, text='.', font=("Verdana", 22), border=0, activebackground='#808080', command=btn_pt_clicked)
btn_eqs = Button(btn_row4, text='=', font=("Verdana", 22), border=0, activebackground='#808080',fg='blue', activeforeground='blue', command=btn_eqs_clicked)
btn_div = Button(btn_row4, text='÷', font=("Verdana", 22), border=0, activebackground='#808080',fg='blue', activeforeground='blue', command=btn_div_clicked)
btn_pt.pack(expand=True,fill=BOTH, side=LEFT, padx=4)
btn_0.pack(expand=True,fill=BOTH, side=LEFT)
btn_eqs.pack(expand=True,fill=BOTH, side=LEFT)
btn_div.pack(expand=True,fill=BOTH, side= LEFT)

# Creating buttons in row 5
btn_cls = Button(btn_row5, text='C', font=("Verdana", 22), border=0, fg='red', activebackground='#808080', activeforeground="red", command=btn_cls_clicked)
btn_bkspc = Button(btn_row5, text='⌫', font=("Verdana", 22), border=0, fg='red', activebackground='#808080', activeforeground="red", command=btn_bkspc_clicked)
btn_cls.pack(expand=True,fill=BOTH, side=LEFT)
btn_bkspc.pack(expand=True, fill=BOTH, side=LEFT)


root.mainloop()
