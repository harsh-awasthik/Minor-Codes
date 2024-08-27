from tkinter import *

root = Tk()
root.title("Calculator")
global lbl
lbl = ""

box = Entry(root, width = 45,text = "Press any button to start")
box.grid(row = 0, column = 0, columnspan = 4)

label = Label(root, anchor = "w", text = "")
label.grid(row = 1, column = 0, columnspan = 4)

def pressed(num):
    current = box.get()
    box.delete(0, END)
    box.insert(0, current + str(num))

def add():
    global first_num, fxn, lbl
    first_num = box.get()
    fxn = "add"
    lbl = box.get() + "+"
    label.config(text = lbl)
    box.delete(0, END)

def subtract():
    global first_num, fxn, lbl
    first_num = box.get()
    fxn = "subtract"
    lbl = box.get() + "-"
    label.config(text = lbl)
    box.delete(0, END)

def multiply():
    global first_num, fxn, lbl
    first_num = box.get()
    fxn = "multiply"
    lbl = box.get() + "x"
    label.config(text = lbl)
    box.delete(0, END)

def divide():
    global first_num, fxn, lbl
    first_num = box.get()
    fxn = "divide"
    lbl = box.get() + "/"
    label.config(text = lbl)
    box.delete(0, END)

def equals():
    second_num = box.get()
    global lbl
    lbl += second_num
    label.config(text = lbl)
    box.delete(0, END)
    try:
        match fxn:
            case "add":
                 ans = round(float(first_num) + float(second_num), 3)
            case "multiply":
                ans = round(float(first_num) * float(second_num), 3)
            case "divide":
                ans = round(float(first_num) / float(second_num), 3)
            case "subtract":
                ans = round(float(first_num) - float(second_num), 3)

        if int(ans) == ans:
            ans = int(ans)

        box.insert(0, ans)

    except ZeroDivisionError:
        label.config(text = "Even I can't do It!!")
        box.delete(0, END)
    except ValueError:
        label.config(text = "ValueError")
        box.delete(0, END)
    except NameError:
        label.config(text = "DO NOT DO useless things")
        box.delete(0, END)


def clear():
    label.config(text = "")
    box.delete(0, END)

button7 = Button(root, text = "7",bg = "#D3D3D3", padx = 30, pady = 20, command = lambda: pressed(7)).grid(row = 2, column = 0, rowspan = 2)
button8 = Button(root, text = "8",bg = "#D3D3D3", padx = 30, pady = 20, command = lambda: pressed(8)).grid(row = 2, column = 1, rowspan = 2)
button9 = Button(root, text = "9",bg = "#D3D3D3", padx = 30, pady = 20, command = lambda: pressed(9)).grid(row = 2, column = 2, rowspan = 2)
multiply = Button(root, text = "x", padx = 30, command = multiply).grid(row = 2, column = 3)
divide = Button(root, text = "/", padx = 30, command = divide).grid(row = 3, column = 3)

button4 = Button(root, text = "4",bg = "#D3D3D3", padx = 30, pady = 20, command = lambda: pressed(4)).grid(row = 4, column = 0, rowspan = 2)
button5 = Button(root, text = "5",bg = "#D3D3D3", padx = 30, pady = 20, command = lambda: pressed(5)).grid(row = 4, column = 1, rowspan = 2)
button6 = Button(root, text = "6",bg = "#D3D3D3", padx = 30, pady = 20, command = lambda: pressed(6)).grid(row = 4, column = 2, rowspan = 2)
subtract = Button(root, text = "-", padx = 30, pady = 20, command = subtract).grid(row = 4, column = 3, rowspan = 2)

button1 = Button(root, text = "1",bg = "#D3D3D3", padx = 30, pady = 20, command = lambda: pressed(1)).grid(row = 6, column = 0, rowspan = 2)
button2 = Button(root, text = "2",bg = "#D3D3D3", padx = 30, pady = 20, command = lambda: pressed(2)).grid(row = 6, column = 1, rowspan = 2)
button3 = Button(root, text = "3",bg = "#D3D3D3", padx = 30, pady = 20, command = lambda: pressed(3)).grid(row = 6, column = 2, rowspan = 2)
add = Button(root, text = "+", padx = 30, pady = 20, command = add).grid(row = 6, column = 3, rowspan = 2)

buttondot = Button(root, text = ".", padx = 33, pady = 18, command = lambda: pressed(".")).grid(row = 8, column = 0, rowspan = 2)
button0 = Button(root, text = "0",bg = "#D3D3D3", padx = 30, pady = 20, command = lambda: pressed(0)).grid(row = 8, column = 1, rowspan = 2)
equal = Button(root, text = "=", padx = 70, pady = 20, command = equals).grid(row = 8, column = 2, rowspan = 2, columnspan = 2)

clear = Button(root, text = "Clear Everything", padx = 100, pady = 20, command = clear).grid(row = 10, column = 0, rowspan = 2, columnspan = 4)

root.mainloop()
