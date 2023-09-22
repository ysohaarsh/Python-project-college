from tkinter import *
import random
import time

# Function to set a modern theme for the application
def set_theme():
    root.tk_setPalette(background="#f3f3f3", foreground="black",
                       activeBackground="#4CAF50", activeForeground="white")
    root.option_add('*TButton*highlightBackground', '#f3f3f3')
    root.option_add('*TButton*highlightColor', '#f3f3f3')
    root.option_add('*TButton*background', '#4CAF50')
    root.option_add('*TButton*foreground', 'white')
    root.option_add('*TButton.padding', [10, 5])
    root.option_add('*TButton.font', ('Helvetica', 12, 'bold'))

root = Tk()
root.geometry("1200x700+0+0")
root.title("Restaurant Management System")
set_theme()

Tops = Frame(root, bg="#4CAF50", width=1200, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=600, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=600, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

# TIME
localtime = time.asctime(time.localtime(time.time()))

# INFO TOP
lblinfo = Label(Tops, font=('roboto', 30, 'bold'),
                text="Restaurant Management System By Harsh Yadav", fg="white", bd=10, anchor='w', bg="#4CAF50")
lblinfo.grid(row=0, column=0)

lblinfo = Label(Tops, font=('roboto', 20), text=localtime, fg="steel blue", anchor=W, bg="#4CAF50")
lblinfo.grid(row=1, column=0)

# CALCULATOR
text_Input = StringVar()
operator = ""

txtdisplay = Entry(f2, font=('ariel', 20, 'bold'), textvariable=text_Input, bd=5, insertwidth=7, bg="white", justify='right')
txtdisplay.grid(columnspan=4)

# Define calculator functions
def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator = ""
    text_Input.set("")

def eqals():
    global operator
    try:
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator = ""
    except Exception:
        text_Input.set("Error")
        operator = ""

# Create calculator buttons
btns = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', 'C', '=', '/'
]

row_val = 2
col_val = 0

for button in btns:
    Button(f2, text=button, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'),
           bg="#4CAF50" if button != '=' and button != 'C' else "#f3f3f3",
           command=lambda b=button: btnclick(b) if b != 'C' else clrdisplay() if b == 'C' else eqals()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create labels and entry fields for order details
order_labels = ['Order No.', 'Fries Meal', 'Lunch Meal', 'Burger Meal', 'Pizza Meal', 'Cheese Burger', 'Drinks']
order_vars = [StringVar() for _ in range(len(order_labels))]

for i in range(len(order_labels)):
    lbl = Label(f1, font=('aria', 16, 'bold'), text=order_labels[i], fg="steel blue", bd=10, anchor='w')
    lbl.grid(row=i, column=0)
    txt = Entry(f1, font=('ariel', 16, 'bold'), textvariable=order_vars[i], bd=6, insertwidth=4, bg="#f3f3f3", justify='right')
    txt.grid(row=i, column=1)

# Define functions for calculations
def calculate_total():
    cof = float(order_vars[1].get())
    colfries = float(order_vars[2].get())
    cob = float(order_vars[3].get())
    cofi = float(order_vars[4].get())
    cochee = float(order_vars[5].get())
    codr = float(order_vars[6].get())

    costoffries = cof * 25
    costoflargefries = colfries * 40
    costofburger = cob * 35
    costoffilet = cofi * 50
    costofcheeseburger = cochee * 30  # Fixed cost for Cheese Burger
    costofdrinks = codr * 35

    subtotal = costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks
    tax = subtotal * 0.05  # Assuming 5% tax rate
    total_cost = subtotal + tax

    order_vars[0].set(str(random.randint(1000, 9999)))
    order_vars[-1].set(f'Rs. {costofdrinks}')
    order_vars[-2].set(f'Rs. {costofcheeseburger}')
    order_vars[-3].set(f'Rs. {total_cost}')
    order_vars[-4].set(f'Rs. {tax}')
    order_vars[-5].set(f'Rs. {subtotal}')

# Calculate button
btnCalculate = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=16,
                      text="CALCULATE TOTAL", bg="#4CAF50", command=calculate_total)
btnCalculate.grid(row=len(order_labels), columnspan=2)

# Price list button
def show_price_list():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
# Price List button
btnPriceList = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10,
                      text="PRICE LIST", bg="#4CAF50", command=show_price_list)
btnPriceList.grid(row=len(order_labels), column=2)

root.mainloop()
