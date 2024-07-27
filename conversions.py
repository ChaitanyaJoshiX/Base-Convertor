"""
Includes all 12 conversions
@ChaitanyaJoshiX
"""
from auxiliary import *

def BinToDec(num):
    dec=0
    i=0
    rev = num[::-1]
    for ch in rev:
        dig = int(ch)
        dec += dig * (2**i)
        i+=1
    return str(int(dec))

def BinToOct(num):
    oct = ""
    while (len(num)%3) != 0:
        num = '0' + num
    while num != "":
        subs = num[:3]
        temp = (int(subs[0])*4) + (int(subs[1])*2) + (int(subs[2])*1)
        oct += str(temp)
        num = num[3:]
    while oct[0] == '0':
        oct = oct[1:]
    return oct

def BinToHex(num):
    hex = ""
    while (len(num)%4) != 0:
        num = '0' + num
    while num != "":
        subs = num[:4]
        temp = (int(subs[0])*8) + (int(subs[1])*4) + (int(subs[2])*2) + (int(subs[3])*1)
        temp = checkChar(temp)
        hex += str(temp)
        num = num[4:]
    return hex

def DecToBin(num):
    num = int(num)
    bin = ""
    while num != 0:
        bin += str(num % 2)
        num = num // 2
    bin = bin[::-1]
    while len(bin) < 4:
        bin = '0' + bin
    return bin

def DecToOct(num):
    num = int(num)
    oct = ""
    while num != 0:
        oct += str(num % 8)
        num = num // 8
    oct = oct[::-1]
    return oct

def DecToHex(num):
    num = int(num)
    hex = ""
    while num != 0:
        temp = checkChar(str(num % 16))
        hex += temp
        num = num // 16
    hex = hex[::-1]
    return hex

def OctToDec(num):
    num = num[::-1]
    dec = 0
    for i in range(len(num)):
        dec += int(num[i]) * (8**i)
    return str(dec)

def OctToBin(num):
    bin = ""
    for dig in num:
        temp = ""
        dig = int(dig)
        if dig - 4 >= 0:
            temp += '1'
            dig -= 4
        else:
            temp += '0'
        if dig - 2 >= 0:
            temp += '1'
            dig -= 2
        else:
            temp += '0'
        if dig - 1 >= 0:
            temp += '1'
            dig -= 1
        else:
            temp += '0'
        bin += temp
    return bin

def OctToHex(num):
    bin = ""
    for dig in num:
        temp = ""
        dig = int(dig)
        if dig - 4 >= 0:
            temp += '1'
            dig -= 4
        else:
            temp += '0'
        if dig - 2 >= 0:
            temp += '1'
            dig -= 2
        else:
            temp += '0'
        if dig - 1 >= 0:
            temp += '1'
            dig -= 1
        else:
            temp += '0'
        bin += temp
    while bin[0] == '0':
        bin = bin[1:]
    while len(bin) % 4 != 0:
        bin = '0' + bin
    hex = BinToHex(bin)
    return hex

def HexToDec(num):
    dec = 0
    num = num[::-1]
    i = 0
    for dig in num:
        dig = checkNum(dig)
        dec += dig * (16**i)
        i += 1
    return str(dec)

def HexToBin(num):
    bin = ""
    for dig in num:
        dig = checkNum(dig)
        bin += DecToBin(str(dig))
    return bin

def HexToOct(num):
    bin = HexToBin(num)
    oct = BinToOct(bin)
    return oct
