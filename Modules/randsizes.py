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

def randomsize():
    print("Welcome to the random size generator")
    USsize = ["1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5", "5.5", "6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", "12", "12.5", "13", "14", "15"]
    EUsize = ["32", "33", "33.5", "34", "35", "35.5", "36", "36.5", "37.5", "38", "38.5", "39", "40", "40.5", "41", "42", "42.5", "43", "44", "44.5", "45", "45.5", "46", "47", "47.5", "48.5", "49.5"]

    randlist = []
    def sizerandomizer(sizelist):
        minsize = str(input("Input the minimum value of your size range"))
        while minsize not in sizelist:
            print("Error: Invalid size inputed")
            minsize = str(input("Input the minimum value of your size range"))
            
        maxsize = str(input("Input the maximum value of your size range"))
        while maxsize not in sizelist:
            print("Error: Invalid size inputed")
            maxsize = str(input("Input the maximum value of your size range"))

        sizetimes = int(input("Input how many sizes you want to generate"))
        #listafinal de valores
        i = 0
        while sizetimes > i:
            minvalue = sizelist.index(minsize)
            maxvalue = sizelist.index(maxsize)
            randvalue = random.randint(minvalue, maxvalue)
            randlist.append(sizelist[randvalue])
            i += 1

    print("Size Generators:")
    print("1. EU")
    print("2. US")
    print("3. UK")
    typesize = int(input("What type of shoe size list do you want to generate(1-3):"))
    if typesize == 1:
        sizerandomizer(EUsize)
        print(randlist)
        #convertir lista a csv mode
        k = "\n"
        i = 0
        while len(randlist) > i: 
            print(randlist[i])
            k = k + randlist[i] + "\n"
            i += 1
            
        #insertar a csv ya en ese formato
        f = open('Accounts\ToolBox\Sizes\Randomsize.csv','a')
        f.write(k)
        f.close()
        print("Sizes succefully saved in Randomsize.csv")
    
    elif typesize == 2:
        sizerandomizer(USsize)

        #convertir lista a csv mode
        k = "\n"
        i = 0
        while len(randlist) > i: 
            print(randlist[i])
            k = k + randlist[i] + "\n"
            i += 1
            
        #insertar a csv ya en ese formato
        f = open('Accounts\ToolBox\Sizes\Randomsize.csv','a')
        f.write(k)
        f.close()
        print("Sizes succefully saved in Randomsize.csv")
    elif typesize == 3:
        sizerandomizer(USsize)
        #convertir lista a csv mode
        k = "\n"
        i = 0
        while len(randlist) > i: 
            print(randlist[i])
            k = k + randlist[i] + "\n"
            i += 1
            
        #insertar a csv ya en ese formato
        f = open('Accounts\ToolBox\Sizes\Randomsize.csv','a')
        f.write(k)
        f.close()
        print("Sizes succefully saved in Randomsize.csv")
    else:
        print("Error: Wrong answer")





