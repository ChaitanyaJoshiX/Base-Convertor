"""
4 number systems convertor w GUI
@ChaitanyaJoshiX
"""
# Importing built-in and user-def libs
import sys
from customtkinter import *
from PIL import Image
from conversions import *
from auxiliary import *

# Global vars definitions and some inits
global dec_output_label, bin_output_label, oct_output_label, hex_output_label
global submit_button, again_button, end_button
global dec_entry, bin_entry, oct_entry, hex_entry
global error_flag, mode_flag
dec_output_label=bin_output_label=oct_output_label=hex_output_label=None
error_flag=0
mode_flag=0

# Dark and Light Mode Definition
def ModeSwitch():
    global mode_flag
    if mode_flag == 0:
        mode_flag = 1
        light()
    else:
        mode_flag = 0
        dark()

# Error definitions
def DecError():
    global dec_entry, error_flag
    dec_entry.configure(border_color="red")
    dec_entry.grid(row=1, column=0, padx=40, pady=40)
    error_flag=1

def BinError():
    global bin_entry, error_flag
    bin_entry.configure(border_color="red")
    bin_entry.grid(row=1, column=1, padx=40, pady=40)
    error_flag=2

def OctError():
    global oct_entry, error_flag
    oct_entry.configure(border_color="red")
    oct_entry.grid(row=3, column=0, padx=40, pady=40)
    error_flag=3

def HexError():
    global hex_entry, error_flag
    hex_entry.configure(border_color="red")
    hex_entry.grid(row=3, column=1, padx=40, pady=40)
    error_flag=4

# GUI output definition
def Output(dec, bin, oct, hex):
    global dec_output_label, bin_output_label, oct_output_label, hex_output_label
    global dec_entry, bin_entry, oct_entry, hex_entry

    # Additional output onto terminal
    print("Decimal: ",dec)
    print("Binary: ",bin)
    print("Octal: ",oct)
    print("Hexadecimal: ",hex)
    print("*"*50)

    # GUI output label definitions
    dec_output_label = CTkLabel(main_frame, text=dec, font=("Quicksand", 40, "bold"), text_color="#E9FF97")
    bin_output_label = CTkLabel(main_frame, text=bin, font=("Quicksand", 40, "bold"), text_color="#E9FF97")
    oct_output_label = CTkLabel(main_frame, text=oct, font=("Quicksand", 40, "bold"), text_color="#E9FF97")
    hex_output_label = CTkLabel(main_frame, text=hex, font=("Quicksand", 40, "bold"), text_color="#E9FF97")

    # GUI entry box removal
    dec_entry.grid_remove()
    dec_output_label.grid(row=1, column=0, padx=5, pady=5)
    bin_entry.grid_remove()
    bin_output_label.grid(row=1, column=1, padx=5, pady=5)
    oct_entry.grid_remove()
    oct_output_label.grid(row=3, column=0, padx=5, pady=5)
    hex_entry.grid_remove()
    hex_output_label.grid(row=3, column=1, padx=5, pady=5)

# GUI submit definition
def SubmitEvent():
    global dec_entry, bin_entry, oct_entry, hex_entry
    global submit_button, again_button, end_button

    # Fetching user input from entry box
    dec_inp = dec_entry.get()
    bin_inp = bin_entry.get()
    oct_inp = oct_entry.get()
    hex_inp = hex_entry.get()

    # In case of input as 0
    if dec_inp == '0' or bin_inp == '0' or oct_inp == '0' or hex_inp == '0':
        Output('0', '0', '0', '0')

    # Decimal as input
    elif dec_inp != "":
        dec_inp = DecErrorCheck(dec_inp) # Decimal error handling
        if dec_inp != -1:
            dec_inp = ZeroCheck(dec_inp)
            bin = ZeroCheck(DecToBin(dec_inp))
            oct = DecToOct(dec_inp)
            hex = DecToHex(dec_inp)
            Output(dec_inp, bin, oct, hex)
        else:
            DecError()

    elif bin_inp != "":
        bin_inp = BinErrorCheck(bin_inp) # Binary error handling
        if bin_inp != -1:
            bin_inp = ZeroCheck(bin_inp)
            dec = BinToDec(bin_inp)
            oct = BinToOct(bin_inp)
            hex = BinToHex(bin_inp)
            Output(dec, bin_inp, oct, hex)
        else:
            BinError()

    elif oct_inp != "":
        oct_inp = OctErrorCheck(oct_inp) # Octal error handling
        if oct_inp != -1:
            oct_inp = ZeroCheck(oct_inp)
            dec = OctToDec(oct_inp)
            bin = ZeroCheck(OctToBin(oct_inp))
            hex = OctToHex(oct_inp)
            Output(dec, bin, oct_inp, hex)
        else:
            OctError()

    elif hex_inp != "":
        hex_inp = HexErrorCheck(hex_inp) # Hexadecimal error handling
        if hex_inp != -1:
            hex_inp = ZeroCheck(hex_inp)
            dec = HexToDec(hex_inp)
            bin = ZeroCheck(HexToBin(hex_inp))
            oct = HexToOct(hex_inp)
            Output(dec, bin, oct, hex_inp)
        else:
            HexError()
    # Empty input
    else:
        print("No Input")
    # End button definition
    end_button = CTkButton(main_frame, text="End", fg_color="#E72929", command=EndEvent)
    submit_button.grid_remove()
    end_button.grid(row=4, column=0, padx=20, pady=20)

    # Repeat button definition
    again_button = CTkButton(main_frame, text="Again", fg_color="#0C359E", command=AgainEvent)
    again_button.grid(row=4, column=1, padx=20, pady=20)

def EndEvent():
    # End Program
    exit()

def AgainEvent():
    # Accessing all global vars
    global dec_output_label, bin_output_label, oct_output_label, hex_output_label
    global submit_button, again_button, end_button
    global dec_entry, bin_entry, oct_entry, hex_entry
    global error_flag

    # Removal of any exisiting GUI output labels
    output_labels = [dec_output_label, bin_output_label, oct_output_label, hex_output_label]
    for label in output_labels:
        if label is not None:
            label.grid_remove()
    dec_output_label=bin_output_label=oct_output_label=hex_output_label=None

    # Removal of End and Repeat buttons
    again_button.grid_remove()
    end_button.grid_remove()

    # Entry box error handling
    if error_flag != 0:
        if error_flag == 1: # Decimal input error
            dec_entry.grid_remove()
            dec_entry = CTkEntry(main_frame, placeholder_text="", width=120, height=40)

        elif error_flag == 2: # Binary input error
            bin_entry.grid_remove()
            bin_entry = CTkEntry(main_frame, placeholder_text="", width=120, height=40)

        elif error_flag == 3: # Octal input error
            oct_entry.grid_remove()
            oct_entry = CTkEntry(main_frame, placeholder_text="", width=120, height=40)

        else: # Hexadecimal input error
            hex_entry.grid_remove()
            hex_entry = CTkEntry(main_frame, placeholder_text="", width=120, height=40)
        error_flag = 0 # Reinitializing error flag var

    # Re-placement of GUI entry boxes
    dec_entry.grid(row=1, column=0, padx=40, pady=40)
    bin_entry.grid(row=1, column=1, padx=40, pady=40)
    oct_entry.grid(row=3, column=0, padx=40, pady=40)
    hex_entry.grid(row=3, column=1, padx=40, pady=40)
    submit_button.grid(row=4, column=0, padx=20, pady=20)

# Main function
# Basic GUI Setup
root = CTk()
root.title("PyRunner")
root.geometry("1280x720")
dark() # Dark mode by default

# Dark and light mode Setup
dark_pic = Image.open("E:\Atom Programs\Base Convertor\dark.png")
light_pic = Image.open("E:\Atom Programs\Base Convertor\light.png")
button_image = CTkImage(light_image=light_pic, dark_image=dark_pic, size=(30, 30))
mode_button = CTkButton(root, text="", command=ModeSwitch, image=button_image, width=30, height=30, fg_color="transparent", bg_color="transparent", hover="FALSE")
mode_button.place(relx=1.0, rely=0.0, x=-20, y=20, anchor=NE)

title_label = CTkLabel(root, text="Case Convertor", font=("Quicksand", 50, "bold"), text_color="#3AA6B9")
title_label.place(relx=0.5, rely=0.0002, anchor='n')

# Frame creation
main_frame = CTkFrame(root, width=800, height=600, fg_color="#FFA38F")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Decimal label and entry box
dec_label = CTkLabel(main_frame, text="Decimal", font=("Quicksand", 40, "bold"), text_color="#E9FF97")
dec_entry = CTkEntry(main_frame, placeholder_text="", width=120, height=40)
dec_label.grid(row=0, column=0, padx=40, pady=40)
dec_entry.grid(row=1, column=0, padx=40, pady=40)

# Binary label and entry box
bin_label = CTkLabel(main_frame, text="Binary", font=("Quicksand", 40, "bold"), text_color="#E9FF97")
bin_entry = CTkEntry(main_frame, placeholder_text="", width=120, height=40)
bin_label.grid(row=0, column=1, padx=40, pady=40)
bin_entry.grid(row=1, column=1, padx=40, pady=40)

# Octal label and entry box
oct_label = CTkLabel(main_frame, text="Octal", font=("Quicksand", 40, "bold"), text_color="#E9FF97")
oct_entry = CTkEntry(main_frame, placeholder_text="", width=120, height=40)
oct_label.grid(row=2, column=0, padx=40, pady=40)
oct_entry.grid(row=3, column=0, padx=40, pady=40)

# Hexadecimal label and entry box
hex_label = CTkLabel(main_frame, text="Hexadecimal", font=("Quicksand", 40, "bold"), text_color="#E9FF97")
hex_entry = CTkEntry(main_frame, placeholder_text="", width=120, height=40)
hex_label.grid(row=2, column=1, padx=40, pady=40)
hex_entry.grid(row=3, column=1, padx=40, pady=40)

# Submit button definition
submit_button = CTkButton(main_frame, text="Submit", command=SubmitEvent, fg_color="#A3D8FF", text_color="black")
submit_button.grid(row=4, column=0, padx=20, pady=20)

root.mainloop()
