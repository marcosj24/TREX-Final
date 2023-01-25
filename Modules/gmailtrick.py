#imports
import random
import names
import re
import csv
from csv import reader
import itertools
from itertools import permutations
import pandas as pd
import time
import os
from selenium import webdriver

def clear():
    os.system('cls')

def unlimitedgmail():
    letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    maillist = []
    mail = str(input('Input your gmail without the "@gmail.com":'))
    times = int(input("Input the amount of gmails you want to generate"))
    t=""
    i = 0 
    while times > i:
        k = 0
        letters = ""
        while random.randint(3, 7) > k:
            letters =letters + letterlist[random.randint(0, 25)]
            k += 1
        finalmail = mail + "+" + letters + "@gmail.com"
        t = t + "\n" + finalmail

        print(finalmail)
        maillist.append(finalmail)
        i += 1
    
    print(t)
    f = open(r'Accounts\Toolbox\Gmailtrick\Gmails.csv','a')
    f.write(t)
    f.close()
    print("Gmails succefully saved in Gmails.csv")



