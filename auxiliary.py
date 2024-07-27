"""
Includes supplementary functions
@ChaitanyaJoshiX
"""
from customtkinter import *

def dark():
    set_appearance_mode("dark")
def light():
    set_appearance_mode("light")

def checkChar(temp):
    dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    if int(temp) >= 10:
        temp = dic[int(temp)]
    return temp

def checkNum(temp):
    temp = temp.upper()
    dic = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    if temp in dic:
        return dic[temp]
    return int(temp)

def ZeroCheck(num):
    while num[0] == '0':
        num = num[1:]
    return num

def DecErrorCheck(num):
    for ch in num:
        if ch.isdigit():
            continue
        else:
            return -1
    return num

def BinErrorCheck(num):
    for ch in num:
        if ch.isdigit():
            if ch == '0' or ch == '1':
                continue
            else:
                return -1
        else:
            return -1
    return num

def OctErrorCheck(num):
    for ch in num:
        if ch.isdigit():
            if ch == '8' or ch == '9':
                return -1
            else:
                continue
        else:
            return -1
    return num

def HexErrorCheck(num):
    alphas = ['A', 'B', 'C', 'D', 'E', 'F']
    for ch in num:
        if ch.isalpha():
            ch = ch.upper()
            if ch not in alphas:
                return -1
            else:
                continue
        elif ch.isdigit():
            continue
        else:
            return -1
    return num
