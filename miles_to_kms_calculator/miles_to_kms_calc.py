import tkinter
from tkinter import END

window = tkinter.Tk()
window.title("Miles to KM Calculator")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


def convert_to_kms():
    miles = float(input.get())
    km = miles * 1.689
    ans = round(km, 2)
    answer.config(text=ans)


# entry 0x1

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)
input.insert(END, string="0")


# is equal to label 0x1

is_equal = tkinter.Label(text="is equal to")
is_equal.grid(column=0, row=1)

# answer label 1x1

answer = tkinter.Label(text="0")
answer.grid(column=1, row=1)

# miles 0x2

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

# kms 1x2

kms = tkinter.Label(text="Kms")
kms.grid(column=2, row=1)


# button calculate
calculate = tkinter.Button(text="caclulate", command=convert_to_kms)
calculate.grid(column=1, row=2)










window.mainloop()