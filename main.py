# Payroll Program: 3/12/2021 Version 2
import ctypes
from tkinter import *
# Setting up window
root = Tk()
root.geometry("400x215")
root.title("Payroll Program")

# Array of pay codes/hourly rates
pay_codes = [10.00, 12.50, 15.00, 17.50, 20.00]


# Puts text inside entry fields
def set_text():
    nameEntry.insert(0, "Enter Name Here")
    socialEntry.insert(0, "Enter Social Here")
    pay_codeEntry.insert(0, "Enter Pay Code Here")
    hours_workedEntry.insert(0, "Enter Hours Here")
    shift_workedEntry.insert(0, "Enter Shift Here")


# Clears any text in entry fields
def clear():
    nameEntry.delete(0, "end")
    socialEntry.delete(0, "end")
    pay_codeEntry.delete(0, "end")
    hours_workedEntry.delete(0, "end")
    shift_workedEntry.delete(0, "end")


# Takes and processes whatever is in the entry fields
def calculate():
    name = nameEntry.get()
    try:
        hours = int(hours_workedEntry.get())
    except ValueError:
        ctypes.windll.user32.MessageBoxW(0, u"Invalid data entry for hours. Make sure input is a number", u"Error", 0)
    try:
        pay_code = int(pay_codeEntry.get())
    except ValueError:
        ctypes.windll.user32.MessageBoxW(0, u"Invalid data entry for pay code. Make sure input is a number", u"Error",
                                         0)
    hourly_wage = (pay_codes[pay_code - 1])
    try:
        social = int(socialEntry.get())
    except ValueError:
        ctypes.windll.user32.MessageBoxW(0, u"Invalid data entry for social. Make sure input is a number", u"Error", 0)
    shift = shift_workedEntry.get()

    if hours > 40:
        overtime = hours - 40
    else:
        overtime = 0

# Calculates pay before taxes and insurance are taken out
    pay_before_tax = (hourly_wage * hours) + ((overtime * hourly_wage) * 1.5)

# Calculates cost of tax
    tax = ("{:,.2f}".format((pay_before_tax * 0.1)))
# Calculates cost of insurance
    insurance = ("{:,.2f}".format((pay_before_tax * 0.05)))

# Calculates pay once taxes are deducted
    pay_after_tax = pay_before_tax - (float(tax) + float(insurance))

# Updates the labels
    take_home_payLabel.configure(text=f"Take home pay  : ${pay_after_tax}")
    taxLabel.configure(text=f"Tax cost       : ${tax}")
    insuranceLabel.configure(text=f"Insurance cost : ${insurance}")
    overtimeLabel.configure(text=f"Overtime worked: {overtime} hours")
    nameLabel.configure(text=f"Name           : {name}")
    socialLabel.configure(text=f"Social         : {social}")
    hours_workedLabel.configure(text=f"Hours worked   : {hours} hours")
    shift_workedLabel.configure(text=f"Shift worked   : {shift}")
    pay_codeLabel.configure(text=f"Pay Code       : {pay_code}")


# Defines all labels
taxLabel = Label(text="Tax cost       :", font="TkFixedFont")
insuranceLabel = Label(text="Insurance cost :", font="TkFixedFont")
overtimeLabel = Label(text="Overtime worked:", font="TkFixedFont")
take_home_payLabel = Label(text="Take home pay  :", font="TkFixedFont")
nameLabel = Label(text="Name           :", font="TkFixedFont")
socialLabel = Label(text="Social         :", font="TkFixedFont")
pay_codeLabel = Label(text="Pay Code       :", font="TkFixedFont")
hours_workedLabel = Label(text="Hours worked   :", font="TkFixedFont")
shift_workedLabel = Label(text="Shift worked   :", font="TkFixedFont")

# Defines all entry fields
nameEntry = Entry()
socialEntry = Entry()
pay_codeEntry = Entry()
hours_workedEntry = Entry()
shift_workedEntry = Entry()

# Puts text inside entry fields
set_text()

# Defines all buttons
clearEntries = Button(text="Clear", width=16, command=clear)
quitButton = Button(text="Quit", width=16, command=quit)
calculateButton = Button(text="Calculate", width=16, command=calculate)

# Places all entry fields
nameEntry.place(x=10, y=10)
socialEntry.place(x=10, y=32)
pay_codeEntry.place(x=10, y=54)
hours_workedEntry.place(x=10, y=76)
shift_workedEntry.place(x=10, y=98)

# Places all buttons
calculateButton.place(x=10, y=120)
clearEntries.place(x=10, y=148)
quitButton.place(x=10, y=176)

# Places all labels
nameLabel.place(x=155, y=10)
socialLabel.place(x=155, y=32)
pay_codeLabel.place(x=155, y=54)
hours_workedLabel.place(x=155, y=76)
shift_workedLabel.place(x=155, y=98)
taxLabel.place(x=155, y=119)
insuranceLabel.place(x=155, y=140)
overtimeLabel.place(x=155, y=162)
take_home_payLabel.place(x=155, y=184)

# Loop that keeps the window open
root.mainloop()
