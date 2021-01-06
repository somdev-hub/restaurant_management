"""

Restaurant management System is a genuine project developed by Somdev Behera and Soumya Ranjan Barik for
their academic year computer science project. This project is aimed to be used for the betterment of the targeted
audience. Restaurant management system is developed using python and MySql date bases. This project collects information
from the user and stores the same in the MySql database. This project is also equipped with a calculator developed by
Somdev Behera. This project is completely opensource and is not subjected to earn any amount.

"""

# Importing modules

from tkinter import *
import tkinter.font as font
import datetime as calender
from resmag import resmanag_system_backend as res
from tkinter import messagebox
from tkinter import ttk
from math import *

# Setting up tkinter window

root = Tk()
root.geometry('1750x700')
root.title('Restaurant management system')
root.config(bg="wheat1")
root.iconbitmap(r'C:\Users\hello\Downloads\favicon_io\favicon.ico')

# String variables

data1 = StringVar()
data2 = StringVar()
data3 = StringVar()
data4 = StringVar()
data5 = StringVar()
data6 = StringVar()
data7 = StringVar()

# Important setups

current_date = calender.date.today()
data4.set(current_date)
total_list = []
grand_total = 0
earning_list = []
earning_total = 0
early_value = res.data_all()
early_list = []
for bill_data in early_value:
    early_list.append(bill_data[0])

# Dishes in form of list

dishes = ["French Fries", "Burger", "Pizza", "Coffee", "Sandwich", "Noodles", "Rice", "Soup", "Curry", "Hot Dog"]


# Defining functions

def text_insert():
    """This method inserts the default data into the bill area."""

    text_area.insert(END, '\t\t\t\tProgrammer Foundation Restaurant')
    text_area.insert(END, '\n\t\t\t\t Mountain view, California')
    text_area.insert(END, '\n\t\t\t\t     contact:- 1234567890')
    text_area.insert(END, '\n'
                          '==========================================================='
                          '=================================')


def value_generate():
    """This functions generates the bill of the customer"""

    ph_no = len(data3.get())
    if data1.get() == '' or data2.get() == '' or ph_no != 10:
        messagebox.showerror("Error!", "Please enter all the fields correctly.")
    else:
        text_area.insert(END, f'Bill Number:-{data1.get()}')
        text_area.insert(END, f'\nCustomer Name:- {data2.get()}')
        text_area.insert(END, f'\nCustomer Contact:- {data3.get()}')
        text_area.insert(END, f'\nDate:- {data4.get()}')
        text_area.insert(END, '\n'
                              '======================================================================'
                              '======================')

        text_area.insert(END, 'Product Name\t\t     Quantity\t\t\t     per cost\t\t\t     Total')

        text_area.insert(END, '\n'
                              '===================================================================='
                              '========================')


def value_clear():
    """This method deletes all the data from the entry boxes"""

    data1.set('')
    data2.set('')
    data3.set('')
    data4.set('')
    data5.set('')
    data6.set('')
    data7.set('')


def value_reset():
    """This function resets the bill area"""

    global grand_total
    total_list.clear()
    grand_total = 0
    text_area.delete('1.0', END)
    text_insert()


def value_add():
    """This method adds up the order and shows in the bill area in the format of a table"""

    if data6.get() == '' or data7.get() == '':
        messagebox.showerror("Error", "Please enter all the details.")
    else:
        no_qtn = int(data6.get())
        no_cost = int(data7.get())
        total_cost = no_qtn * no_cost
        total_list.append(total_cost)
        text_area.insert(END,
                         f'\n{data5.get()}\t\t     {data6.get()}\t\t\t     {data7.get()}\t\t             {total_cost}')


def value_total():
    """This function makes a total of all the order"""

    global grand_total
    for items in total_list:
        grand_total += items
    text_area.insert(END, '\n'
                          '==============================================================='
                          '=============================')
    text_area.insert(END, f'\t\t\t\t\t   Grand Total:- {grand_total}')
    text_area.insert(END, '\n'
                          '=============================================================='
                          '==============================')


def value_save():
    """This function saves the user data into the MySql database"""

    ask_confirm = messagebox.askyesno("Confirm", "Do you really want to save?")
    if ask_confirm > 0:
        if data1.get() == '' or data4.get() == '' or data2.get() == '' or data5.get() == '' or data6.get() == '' or \
                data7.get() == '':
            messagebox.showerror("Error", "Please enter all the details.")
        else:
            try:
                val_date = data4.get().split('-')
                val_sql_date = int(val_date[0] + val_date[1] + val_date[2])
                exact_value = res.data_insert(data1.get(), data2.get(), data3.get(), val_sql_date, data5.get(),
                                              data6.get(),
                                              data7.get())

                if exact_value == "successful":
                    messagebox.showinfo("Message", "Data has been saved successfully")
                else:
                    messagebox.showerror("error", exact_value)

            except Exception as error:
                messagebox.showerror("Error", error)

    else:
        return


def value_restore():
    """This method takes the bill no as key and restores the respective records in the entry widgets from the
    database"""

    if data1.get() == '':
        messagebox.showerror("error", "please enter the bill number!")
    else:
        key = data1.get()
        try:
            restore_val = res.data_search(key)
            if restore_val is None:
                messagebox.showerror("error", "Details not found on this bill number!")
            else:
                print(restore_val)
                data2.set(restore_val[1])
                data3.set(restore_val[2])
                data4.set(restore_val[3])
                data5.set(restore_val[4])
                data6.set(restore_val[5])
                data7.set(restore_val[6])

        except Exception as error:
            messagebox.showerror("error",error)
            print(error)


def value_delete():
    """This method takes the bill number as key and deletes the respective record from the database."""

    if data1.get() == '':
        messagebox.showerror("error", "please enter the bill number!")
    else:
        del_confirm = messagebox.askyesno("Warning", "Do you really want to delete this record!")
        if del_confirm > 0:
            try:
                key = int(data1.get())
                if key in early_list:
                    res.data_delete(key)
                    messagebox.showinfo("message", "Record has been successfully deleted.")
                else:
                    messagebox.showwarning("Not Found", "Bill number not found! Enter a valid one.")

            except Exception as error:
                messagebox.showerror("error", error)
                print(error)
        else:
            return


def value_show_all():
    """This method inserts all the records from the database into the bill area in a tabular format"""

    global earning_total
    fetcher_value = res.data_all()
    text_area.insert(END, '\n'
                          '======================================================='
                          '=====================================')

    text_area.insert(END, 'bill no\t    Cust Name\t     Cust contact\t     date\t     item\t    '
                          'quantity\t    per cost')

    text_area.insert(END, '\n'
                          '===================================================='
                          '========================================')

    for data in fetcher_value:
        earn_multiple = data[5] * data[6]
        earning_list.append(earn_multiple)
        text_area.insert(END, f'\n{data[0]}\t    {data[1]}\t     {data[2]}\t     {data[3]}\t     {data[4]}\t    '
                              f'{data[5]}\t\t\t       {data[6]}  ')

    for items in earning_list:
        earning_total += items

    text_area.insert(END, '\n'
                          '========================================================'
                          '====================================')
    text_area.insert(END, f'\t\t\t\t\t   Total Earning:- ₹{earning_total}')
    text_area.insert(END, '\n'
                          '========================================================'
                          '====================================')


def all_exit():
    wish1 = messagebox.askyesno("Confirm", "Do you want to exit?")
    if wish1 > 0:
        if data1.get() != '' or data2.get() != '' or data3.get() != '':
            wish2 = messagebox.askyesno("Confirm", "Would you like to save the data before exiting?")
            if wish2 > 0:
                return
            else:
                root.destroy()
        else:
            root.destroy()
    else:
        return


# Creating frames and widgets

title_label = Label(root, text='Restaurant management system', font=('Ariel', 35, 'bold'), bg='light gray', bd=8,
                    relief=GROOVE)
title_label.pack(side=TOP, fill=X)

bill_frame = LabelFrame(root, text='Enter Details', bg='light gray', font=("Ariel", 15), bd=7, relief=GROOVE)
bill_frame.place(x=20, y=80, width=500, height=620)

# Input area labels

label_data1 = Label(bill_frame, text='Bill no.', font=('Ariel', 15), bg='light gray')
label_data1.grid(row=0, column=0, sticky=W)
label_data2 = Label(bill_frame, text='Customer name', font=('Ariel', 15), bg='light gray')
label_data2.grid(row=1, column=0, sticky=W)
label_data3 = Label(bill_frame, text='Customer contact', font=('Ariel', 15), bg='light gray')
label_data3.grid(row=2, column=0, sticky=W)
label_data4 = Label(bill_frame, text='Date', font=('Ariel', 15), bg='light gray')
label_data4.grid(row=3, column=0, sticky=W)
label_data5 = Label(bill_frame, text='Item purchased', font=('Ariel', 15), bg='light gray')
label_data5.grid(row=4, column=0, sticky=W)
label_data6 = Label(bill_frame, text='Item quantity', font=('Ariel', 15), bg='light gray')
label_data6.grid(row=5, column=0, sticky=W)
label_data7 = Label(bill_frame, text='cost of one', font=('Ariel', 15), bg='light gray')
label_data7.grid(row=6, column=0, sticky=W)

# Entry widgets

entry_data1 = Entry(bill_frame, font=('Ariel', 15), bd=5, textvar=data1, bg="AntiqueWhite1")
entry_data1.grid(row=0, column=1, padx=2, pady=2)
entry_data2 = Entry(bill_frame, font=('Ariel', 15), bd=5, textvar=data2, bg="AntiqueWhite1")
entry_data2.grid(row=1, column=1, padx=2, pady=2)
entry_data3 = Entry(bill_frame, font=('Ariel', 15), bd=5, textvar=data3, bg="AntiqueWhite1")
entry_data3.grid(row=2, column=1, padx=2, pady=2)
entry_data4 = Entry(bill_frame, font=('Ariel', 15), bd=5, textvar=data4, bg="AntiqueWhite1")
entry_data4.grid(row=3, column=1, padx=2, pady=2)
combo_data5 = ttk.Combobox(bill_frame, values=dishes, width=23, font=('Ariel', 13), textvariable=data5)
combo_data5.grid(row=4, column=1, padx=2, pady=2)
entry_data6 = Entry(bill_frame, font=('Ariel', 15), bd=5, textvar=data6, bg="AntiqueWhite1")
entry_data6.grid(row=5, column=1, padx=2, pady=2)
entry_data7 = Entry(bill_frame, font=('Ariel', 15), bd=5, textvar=data7, bg="AntiqueWhite1")
entry_data7.grid(row=6, column=1, padx=2, pady=2)

# Options area frame and buttons

button_frame = LabelFrame(bill_frame, bd=5, text='Options', bg='light gray', font=('Ariel', 15))
button_frame.place(x=20, y=275, width=390, height=305)

button1 = Button(button_frame, bd=2, text='Add', font=('Ariel', 12), width=12, height=3, command=value_add,
                 bg="bisque2")
button1.grid(row=0, column=0, padx=4, pady=2)
button2 = Button(button_frame, bd=2, text='Generate', font=('Ariel', 12), width=12, height=3, command=value_generate,
                 bg="bisque2")
button2.grid(row=0, column=1, padx=4, pady=2)
button3 = Button(button_frame, bd=2, text='Clear', font=('Ariel', 12), width=12, height=3, command=value_clear,
                 bg="bisque2")
button3.grid(row=0, column=2, padx=4, pady=2)
button4 = Button(button_frame, bd=2, text='Total', font=('Ariel', 12), width=12, height=3, command=value_total,
                 bg="bisque2")
button4.grid(row=1, column=0, padx=4, pady=2)
button5 = Button(button_frame, bd=2, text='Reset', font=('Ariel', 12), width=12, height=3, command=value_reset,
                 bg="bisque2")
button5.grid(row=1, column=1, padx=4, pady=2)
button6 = Button(button_frame, bd=2, text='Save', font=('Ariel', 12), width=12, height=3, command=value_save,
                 bg="bisque2")
button6.grid(row=1, column=2, padx=4, pady=2)
button7 = Button(button_frame, bd=2, text='Restore', font=('Ariel', 12), width=12, height=3, command=value_restore,
                 bg="bisque2")
button7.grid(row=2, column=0, padx=4, pady=2)
button8 = Button(button_frame, bd=2, text='Delete', font=('Ariel', 12), width=12, height=3, command=value_delete,
                 bg="bisque2")
button8.grid(row=2, column=1, padx=4, pady=2)
button9 = Button(button_frame, bd=2, text='Show all', font=('Ariel', 12), width=12, height=3, command=value_show_all,
                 bg="bisque2")
button9.grid(row=2, column=2, padx=4, pady=2)
button10 = Button(button_frame, bd=2, text='Exit', font=('Ariel', 12), width=40, height=2, command=all_exit,
                  bg="bisque2")
button10.grid(row=3, column=0, padx=4, pady=2, columnspan=3)

# Creating calculator

calc_frame = Frame(root, bd=3, bg='light gray', relief=GROOVE)
calc_frame.place(x=550, y=80, width=780, height=400)


# defining applicable function

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        """when = is pressed the expression will be evaluated """

        if f_value.get().isdigit():
            value = int(f_value.get())
        else:
            try:
                value = eval(input_field.get())
            except Exception as error:
                print(error)
                value = "Error"

        text_area.insert(END, f"\n{f_value.get()} = {value}")
        f_value.set(value)
        input_field.update()

    elif text == "clear":
        """when clear is pressed the input field will be reset """

        f_value.set("")
        input_field.update()
    else:
        f_value.set(f_value.get() + text)
        input_field.update()


Font1 = font.Font(family="Times", size=15, weight="bold")
f_value = StringVar()
f_value.set("")
input_field = Entry(calc_frame, textvar=f_value, width=20, borderwidth=5, bg="AntiqueWhite1", font=Font1)
input_field.grid(row=0, column=2, columnspan=3, padx=20, pady=10)

# numeral buttons

button1 = Button(calc_frame, text="1", padx=40, pady=20, bg="MistyRose2", font=Font1)
button2 = Button(calc_frame, text="2", padx=55, pady=20, bg="MistyRose2", font=Font1)
button3 = Button(calc_frame, text="3", padx=45, pady=20, bg="MistyRose2", font=Font1)
button4 = Button(calc_frame, text="4", padx=40, pady=20, bg="MistyRose2", font=Font1)
button5 = Button(calc_frame, text="5", padx=55, pady=20, bg="MistyRose2", font=Font1)
button6 = Button(calc_frame, text="6", padx=45, pady=20, bg="MistyRose2", font=Font1)
button7 = Button(calc_frame, text="7", padx=40, pady=20, bg="MistyRose2", font=Font1)
button8 = Button(calc_frame, text="8", padx=55, pady=20, bg="MistyRose2", font=Font1)
button9 = Button(calc_frame, text="9", padx=45, pady=20, bg="MistyRose2", font=Font1)
button0 = Button(calc_frame, text="0", padx=55, pady=20, bg="MistyRose2", font=Font1)

# Operator buttons

button_plus = Button(calc_frame, text="+", padx=50, pady=20, bg="MistyRose2", font=Font1)
button_minus = Button(calc_frame, text="-", padx=50, pady=20, bg="MistyRose2", font=Font1)
button_into = Button(calc_frame, text="*", padx=50, pady=20, bg="MistyRose2", font=Font1)
button_divide = Button(calc_frame, text="/", padx=50, pady=20, bg="MistyRose2", font=Font1)
button_equal = Button(calc_frame, text="=", padx=40, pady=20, bg="MistyRose2", font=Font1)
button_clear = Button(calc_frame, text="clear", padx=25, pady=20, bg="MistyRose2", font=Font1)
button_point = Button(calc_frame, text=".", padx=45, pady=20, bg="MistyRose2", font=Font1)
button_two_zero = Button(calc_frame, text="00", padx=45, pady=20, bg="MistyRose2", font=Font1)

button_sin = Button(calc_frame, text="sin", padx=55, pady=20, bg="MistyRose2", font=Font1)
button_cos = Button(calc_frame, text="cos", padx=55, pady=20, bg="MistyRose2", font=Font1)
button_tan = Button(calc_frame, text="tan", padx=55, pady=20, bg="MistyRose2", font=Font1)
button_br1 = Button(calc_frame, text="(", padx=65, pady=20, bg="MistyRose2", font=Font1)
button_br2 = Button(calc_frame, text=")", padx=65, pady=20, bg="MistyRose2", font=Font1)

button_sqrt = Button(calc_frame, text="sqrt", padx=41, pady=20, bg="MistyRose2", font=Font1)
button_exp = Button(calc_frame, text="exp", padx=43, pady=20, bg="MistyRose2", font=Font1)
button_log10 = Button(calc_frame, text="log10", padx=35, pady=20, bg="MistyRose2", font=Font1)
button_pi = Button(calc_frame, text="pi", padx=50, pady=20, bg="MistyRose2", font=Font1)
button_fac = Button(calc_frame, text="factorial", padx=21, pady=20, bg="MistyRose2", font=Font1)

# __binding buttons__

button1.grid(row=1, column=1)
button1.bind("<Button-1>", click)
button2.grid(row=1, column=2)
button2.bind("<Button-1>", click)
button3.grid(row=1, column=3)
button3.bind("<Button-1>", click)

button4.grid(row=2, column=1)
button4.bind("<Button-1>", click)
button5.grid(row=2, column=2)
button5.bind("<Button-1>", click)
button6.grid(row=2, column=3)
button6.bind("<Button-1>", click)

button7.grid(row=3, column=1)
button7.bind("<Button-1>", click)
button8.grid(row=3, column=2)
button8.bind("<Button-1>", click)
button9.grid(row=3, column=3)
button9.bind("<Button-1>", click)

button0.grid(row=4, column=2)
button0.bind("<Button-1>", click)

button_plus.grid(row=0, column=5)
button_plus.bind("<Button-1>", click)
button_minus.grid(row=1, column=5)
button_minus.bind("<Button-1>", click)
button_into.grid(row=2, column=5)
button_into.bind("<Button-1>", click)
button_divide.grid(row=3, column=5)
button_divide.bind("<Button-1>", click)
button_two_zero.grid(row=4, column=5)
button_two_zero.bind("<Button-1>", click)

button_equal.grid(row=4, column=1)
button_equal.bind("<Button-1>", click)
button_clear.grid(row=0, column=1)
button_clear.bind("<Button-1>", click)
button_point.grid(row=4, column=3)
button_point.bind("<Button-1>", click)

button_sin.grid(row=0, column=6)
button_sin.bind("<Button-1>", click)
button_cos.grid(row=1, column=6)
button_cos.bind("<Button-1>", click)
button_tan.grid(row=2, column=6)
button_tan.bind("<Button-1>", click)
button_br1.grid(row=3, column=6)
button_br1.bind("<Button-1>", click)
button_br2.grid(row=4, column=6)
button_br2.bind("<Button-1>", click)

button_sqrt.grid(row=0, column=0)
button_sqrt.bind("<Button-1>", click)
button_exp.grid(row=1, column=0)
button_exp.bind("<Button-1>", click)
button_log10.grid(row=2, column=0)
button_log10.bind("<Button-1>", click)
button_pi.grid(row=3, column=0)
button_pi.bind("<Button-1>", click)
button_fac.grid(row=4, column=0)
button_fac.bind("<Button-1>", click)

# Creating text area

text_frame = LabelFrame(root, text='Bill Area', font=('Ariel', 15), bg='light gray', bd=8, relief=GROOVE)
text_frame.place(x=550, y=485, width=778, height=210)

y_scroll = Scrollbar(text_frame, orient=VERTICAL)
text_area = Text(text_frame, bg='white', yscrollcommand=y_scroll.set)
y_scroll.config(command=text_area.yview)
y_scroll.pack(side=RIGHT, fill=Y)
text_area.pack(fill=BOTH, expand=TRUE)
text_insert()

root.mainloop()
