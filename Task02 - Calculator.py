# IMPORTING MODULE -
from tkinter import *
interface = Tk()

# INTERFACE SECTION -
interface.title("Python Simple Calculator")
interface["bg"]="#232423" 

# INPUT SECTION - 
input = Entry(interface,width=30,font=("Helvetica",12,"bold"),borderwidth=5)
input.grid(row=0,column=0,columnspan=2000,rowspan=1,padx=15,pady=30)

# DEFINING BUTTONS -

def button_click(number):
    current = input.get()
    input.delete(0,END)
    input.insert(0,int(str(current)+str(number)))

def button_clr():
    input.delete(0,END)    

def button_addition():
    current_number = input.get()
    global first_number
    first_number = int(current_number) 
    global Math
    Math = "addition"   
    input.delete(0,END)


def button_subtraction():
    current_number = input.get()
    global first_number
    first_number = int(current_number) 
    global Math
    Math = "subtract"   
    input.delete(0,END)    

def button_multiplication():
    current_number = input.get()
    global first_number
    first_number = int(current_number) 
    global Math
    Math = "multiply"   
    input.delete(0,END)    

def button_division():
    current_number = input.get()
    global first_number
    first_number = int(current_number) 
    global Math
    Math = "divide"   
    input.delete(0,END)

def button_equal():
    second_number = input.get()
    input.delete(0,END)

    if Math == "addition":
        input.insert(0,first_number+int(second_number))

    if Math == "subtract":
        input.insert(0,first_number-int(second_number))

    if Math == "multiply":
        input.insert(0,first_number*int(second_number))

    if Math == "divide":
        input.insert(0,first_number/int(second_number))            


# CREATING BUTTON -

button1 = Button(interface,text="1",padx=28,pady=15,command=lambda: button_click(1),bg="#161716",fg="#fcfafa",font="bold")
button2 = Button(interface,text="2",padx=32,pady=15,command=lambda: button_click(2),bg="#161716",fg="#fcfafa",font="bold")
button3 = Button(interface,text="3",padx=30,pady=15,command=lambda: button_click(3),bg="#161716",fg="#fcfafa",font="bold")
button4 = Button(interface,text="4",padx=28,pady=15,command=lambda: button_click(4),bg="#161716",fg="#fcfafa",font="bold")
button5 = Button(interface,text="5",padx=32,pady=15,command=lambda: button_click(5),bg="#161716",fg="#fcfafa",font="bold")
button6 = Button(interface,text="6",padx=30,pady=15,command=lambda: button_click(6),bg="#161716",fg="#fcfafa",font="bold")
button7 = Button(interface,text="7",padx=28,pady=15,command=lambda: button_click(7),bg="#161716",fg="#fcfafa",font="bold")
button8 = Button(interface,text="8",padx=32,pady=15,command=lambda: button_click(8),bg="#161716",fg="#fcfafa",font="bold")
button9 = Button(interface,text="9",padx=30,pady=15,command=lambda: button_click(9),bg="#161716",fg="#fcfafa",font="bold")
button0 = Button(interface,text="0",padx=32,pady=15,command=lambda: button_click(0),bg="#161716",fg="#fcfafa",font="bold")

button_add = Button(interface,text="+",padx=31,pady=15,command=button_addition,bg="#ebc507",fg="black",font=("Arial",15,"bold"))
button_subtract = Button(interface,text="_",padx=31,pady=15,command=button_subtraction,bg="#ebc507",fg="black",font=("Arial",15,"bold"))
button_multiply = Button(interface,text="X",padx=31,pady=15,command=button_multiplication,bg="#ebc507",fg="black",font=("Arial",15,"bold"))
button_divide = Button(interface,text="╱",padx=31,pady=15,command=button_division,bg="#ebc507",fg="black",font=("Arial",15,"bold"))
button_equality = Button(interface,text="=",padx=29,pady=15,command=button_equal,bg="#706f6f",fg="black",font="bold")

button_clear = Button(interface,text="CLEAR",padx=1,pady=15,command=button_clr,bg="#706f6f",fg="black",font="bold")

# POSITIONING BUTTON -

#1 Row No. 02 
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
button_divide.grid(row=2,column=3)

#2 Row No. 03
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
button_multiply.grid(row=3,column=3)

#3 Row No. 04
button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)
button_subtract.grid(row=4,column=3)

#4 Row No. 05
button_clear.grid(row=5,column=0)
button0.grid(row=5,column=1)
button_add.grid(row=5,column=3)
button_equality.grid(row=5,column=2)

# RUNNING THE INTERFACE -
interface.mainloop()