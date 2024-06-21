from tkinter import *
import ast

root = Tk()
root.title("Calculator")
root.resizable(False, False)

# Calculator display
display = Entry(root, font=("Arial", 24), width=18)
display.grid(row=0, columnspan=6, sticky=W+E, pady= 10)
display.bind("<Key>", lambda e: "break")

i = 0

# Input and calculation functions
def get_number(n):
    global i
    display_state = display.get()
    if display_state == "0":
        clear_display()
    if display_state == "" or (display_state.startswith("0") and len(display_state) == 1):
        display.delete(0, END)
    display.insert(i, n)
    i += 1

def get_operator(operator):
    global i
    display_state = display.get()
    if display_state and display_state[-1] not in "+-*/":
        operator_length = len(operator)
        display.insert(i, operator)
        i += operator_length
        
def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()

def safe_eval(expr):
    try:
        parsed_expr = ast.parse(expr, mode='eval')
        return eval(compile(parsed_expr, '<string>', mode='eval'))
    except Exception:
        root.after(500, clear_display)
        return "error"


    
def calculate():
    display_state = display.get()
    result = safe_eval(display_state)
    clear_display()
    display.insert(0, result)

button_font = ("Arial", 18)

# Numeric buttons
Button(root, text="1", command=lambda:get_number(1), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda:get_number(2), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda:get_number(3), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", command=lambda:get_number(4), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda:get_number(5), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda:get_number(6), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", command=lambda:get_number(7), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda:get_number(8), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", command=lambda:get_number(9), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=4, column=2, sticky=W+E)

# Operators buttons
Button(root, text="AC", command=lambda:clear_display(), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=5, column=0, sticky=W+E)
Button(root, text="0", command=lambda:get_number(0), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=5, column=1, sticky=W+E)
Button(root, text="%", command=lambda:get_operator("%"), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=5, column=2, sticky=W+E)

Button(root, text="+", command=lambda:get_operator("+"), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", command=lambda:get_operator("-"), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=3, column=3, sticky=W+E)
Button(root, text="/", command=lambda:get_operator("/"), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=4, column=3, sticky=W+E)
Button(root, text="X", command=lambda:get_operator("*"), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=5, column=3, sticky=W+E)

Button(root, text="←", command=lambda:undo(), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text="exp", command=lambda:get_operator("**"), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=3, column=4, sticky=W+E)
Button(root, text="x²", command=lambda:get_operator("**2"), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=3, column=5, sticky=W+E)
Button(root, text="=", command=lambda:calculate(), font=button_font, height=2, width=4, bg="#bababa", fg="black", bd=1, padx=5, pady=5).grid(row=4, column=4, sticky="NSEW", columnspan=2, rowspan=2)

root.mainloop()
