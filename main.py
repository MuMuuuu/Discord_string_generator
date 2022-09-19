#!/usr/bin/python3

import pyperclip
from string import ascii_lowercase as alpha

regional = ":regional_indicator_{}:"
 
special = {"!" : ":exclamation:", "?" : ":question:", "#" : ":hash:", "*" : ":asterisk:", "0" : ":zero:", "1" : ":one:", "2" : ":two:", "3" : ":three:", "4" : ":four:", "5" : ":five:", "6" : ":six:", "7" : ":seven:", "8" : ":eight:", "9" : ":nine:" , "-" : ":heavy_minus_sign:" , "+" : "heavy_plus_sign" , "$" : ":heavy_dollar_sign" , "=" : ":heavy_equals_sign"}
spoiler = "||{}||"

def regional_wrap(s : str)->str:
    res = [] 
    for i in s.lower():
        if i in special:
            res.append(special[i])
        elif i in alpha:
            res.append(regional.format(i))
        else:
            res.append(i)
    
    return " ".join(res)

def spoiler_wrap(s : str)->str:
    return "".join([spoiler.format(i) for i in s])

def costum_wrap(f : str, s : str)->str:
    return "".join([f.format(i) for i in s])

def main():
    print("""Choose an option:
    1. Regional Indicators
    2. Full of Spoiler
    3. Custom Format ( wrap in {})
    4. Exit""")
    choice = int(input("> : "))
    s = input("string : ")

    if(choice == 4): exit()
    elif(choice == 1) : return regional_wrap(s)
    elif(choice == 2) : return spoiler_wrap(s)
    elif(choice == 3) : return costum_wrap(input("Format : ") , s)

if __name__ == "__main__":
    pyperclip.copy(main())

