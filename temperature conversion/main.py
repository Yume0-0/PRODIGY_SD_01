import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import pyttsx3

def convert():
    try:
        input_value = float(entry_int.get())
        unit = unit_var.get()

        if unit == "Kelvin":
            to_cel = round(input_value - 273.15 , 3)
            to_fahren = "{:.2f}".format((to_cel * 9 / 5) + 32)
            output_string.set(str(to_cel) + " degree Celsius \n" + to_fahren + " degree Fahrenheit")
        elif unit == "Celsius":
            to_kel = round(input_value + 273.15 , 3)
            to_fahren = "{:.2f}".format((input_value * 9 / 5) + 32)
            output_string.set(str(to_kel) + " Kelvin \n" + to_fahren + " Fahrenheit")
        elif unit == "Fahrenheit":
            to_cel = (input_value - 32) * 5 / 9
            to_kel = to_cel + 273.15
            output_string.set("{:.2f}".format(to_cel) + " Celsius \n" + "{:.2f}".format(to_kel) + " Kelvin")
        else:
            output_string.set("Unsupported unit")
    except ValueError:
        output_string.set("Invalid input")


window = ttk.Window(themename = 'darkly')   #the window
window.title("temperature convertor")
window.geometry('500x300')


#title
title_label = ttk.Label(master = window , text = 'click the button to convert the temperature : ' , font = 'courier' )

#input field
input_frame = ttk.Frame(master= window )
entry_int = tk.StringVar()
entery = ttk.Entry(input_frame , textvariable= entry_int)
unit_var = tk.StringVar(value="Celsius")
unit_menu = ttk.Combobox(master=input_frame, textvariable=unit_var, values=["Celsius", "Kelvin", "Fahrenheit"], state='readonly')
button = ttk.Button(master=input_frame , text= 'convert' , command= convert)

title_label.pack(pady= 20 )
entery.pack(side= 'left' )
input_frame.pack()
unit_menu.pack(side= 'left' )
button.pack(side= 'left' , padx=10)


output_string = tk.StringVar()
outpu_label = ttk.Label(master= window , text='output :' , font='courier', textvariable= output_string)


outpu_label.pack(pady= 10)

window.mainloop()   #run