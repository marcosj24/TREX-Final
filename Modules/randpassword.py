#imports
import random
import names
#imports
import random
import names
import re
import csv
import itertools
from itertools import permutations
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored

def randpass():
    numofpass = int(input("How many passwrod do you want to generate:"))
    letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    p = ""
    i = 0
    while numofpass > i:
        k = 0
        Password = ""
        while random.randint(6, 8) > k:
            Password = Password + letterlist[random.randint(0, 25)]
            k += 1
        Password = Password.capitalize()
        Password = Password + str(random.randint(0, 9)) + str(random.randint(0, 9)) + "!"
        print(Password)
        p = p + "\n" + Password
        i += 1

    with open(r'Accounts\Toolbox\Passwords\Randpasswords.csv', 'a') as f:
        f.write(p)

    print(str(numofpass) + " passwords generated. You can find your passwords in Randpasswords.csv")




