# Yamkela Mathontsi

from tkinter import *


from tkinter import messagebox
root = Tk()
root.title('Temperature Conversion')
root.configure(bg="cyan")
root.geometry('1000x400')
convert1 = "none"
convert2 = "none"


# defining my cel
def act_entry1():
    if entry1["state"] == "normal":
        entry1.config(state="disabled")
        entry2.delete(0, END)
    else:
        entry1.config(state="normal")
        entry2.config(state="disabled")

        global convert1
        convert1 = "CTF"


# activation of fah
def entry_2():
    if entry2["state"] == "normal":
        entry2.config(state="disabled")
        entry1.delete(0, END)
        results_label["text"] = ""
    else:
        entry2.config(state="normal")
        entry1.config(state="disabled")
        results_label["text"] = ""

        global convert2
        convert2 = "FtC"


# calculating of conversion
def calculating():
    try:
        global convert1
        if entry1["state"] == "normal":
            temp = float(entry1.get())
            answer = str(temp * 9 / 5 + 32)
            results_label["text"] = answer
        elif entry2["state"] == "normal":
            temp = float(entry2.get())
            answer = str((temp - 32) * 5 / 9)
            results_label["text"] = answer

    except ValueError as ex:
        entry1.config(state="normal")
        entry1.delete(0, END)
        entry1.config(state="readonly")

        entry2.config(state="normal")
        entry2.delete(0, END)
        entry2.config(state="readonly")

        messagebox.showerror("ERROR", " Please Enter A Number For Temperature")


# defining the clear button
def clearing():
    entry1.config(state="normal")
    entry1.delete(0, END)
    entry1.config(state="readonly")

    entry2.config(state="normal")
    entry2.delete(0, END)
    entry2.config(state="readonly")

    entry3.config(state="normal")
    entry3.delete(0, END)
    entry3.config(state="readonly")


def button_Exit():
    msg_box = messagebox.askquestion("Terminating Program", "Are you sure you want to exit program", icon="warning")
    if msg_box =="yes":
        root.destroy()
    else:
        messagebox.showinfo("Temperature Converter", "Returning to program", icon="warning")


# code

# label frames
lb1 = LabelFrame(root, text="Celsius to Fahrenheit")
lb2 = LabelFrame(root, text="Fahrenheit to Celsius")

# labels place
lb1.place(x=150, y=50, width=300, height=300)
lb2.place(x=500, y=50, width=300, height=300)

results_label = Label(root, text="", width=20, height=4)
results_label.place(x=350, y=470)

# entry
entry1 = Entry(lb1, width=30, state="readonly")
entry2 = Entry(lb2, width=30, state="readonly")
entry3 = Entry(root, width=25, state="readonly", fg="#65ff00")

# entry place
entry1.place(x=15, y=80)
entry2.place(x=15, y=80)
#entry3.place(x=350, y=470, height=70,)

# button
button1 = Button(root, text="Activate - Celsius to Fahrenheit", command=act_entry1)
button2 = Button(root, text="Activate - Fahrenheit to Celsius", command=entry_2)
button3 = Button(root, text="Calculate Conversion", command=calculating)
button4 = Button(root, text="clear", command=clearing)
button5 = Button(root, text="Exit program", command=exit)

# button place
button1.place(x=150, y=410)
button2.place(x=530, y=410)
button3.place(x=150, y=470)
button4.place(x=600, y=450)
button5.place(x=600, y=500)

root.mainloop()
