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


def clear():
    os.system('cls')



def randomnames():
    print("Welcome to the random name generator")
    numbnames = int(input("How many names would you like to generate:"))
    finalnames = []
    if numbnames == 0:
        print("Back to main men")
    
    i = 0
    while i < numbnames:
        randname = names.get_full_name()
        finalnames.append(randname)
        i += 1
        

    k = "\n"
    i = 0
#poner los names a formato csv
    while len(finalnames) > i: 
        print(finalnames[i])
        namedivided = str(finalnames[i]).split(" ")
        k = k + finalnames[i] + ", " +  namedivided[0] + ", " +  namedivided[1] + "\n"
        i += 1


    #insertar a csv ya en ese formato
    f = open(r'Accounts\ToolBox\Names\Randomnames.csv','a')
    f.write(k)
    f.close()
    print("Names succefully saved in Randomnames.csv")

