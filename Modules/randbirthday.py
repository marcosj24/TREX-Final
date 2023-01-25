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

def birthdays():
    birthdaylist = []
    usernumber = int(input("How many birthdays do you want to generate?"))
    usoreu = int(input("In what format do you want your birthdays: 1. day/month/year, 2. month/day/year (1/2):"))
    brithdaymode = int(input("How do you want your birthday year: 1. 2022, 2. 22 (1/2):"))

    if usoreu == 1:
        if brithdaymode == 1:
            i = 0
            while usernumber > i:
                birthdaylist.append(str(random.randint(1, 28)) + "/" + str(random.randint(1, 12)) + "/" + str(random.randint(1970, 2004)))
                i += 1
            #convertir lista a csv mode
            k = "\n"
            i = 0
            while len(birthdaylist) > i: 
                print(birthdaylist[i])
                k = k + birthdaylist[i] + "\n"
                i += 1
                
            #insertar a csv ya en ese formato
            f = open('Accounts\Toolbox\Birthdays\Randombirthdays.csv','a')
            f.write(k)
            f.close()

            print("Birthdays succefully saved in Randombirthdays.csv")

        elif brithdaymode == 2:
            i = 0
            while usernumber > i:
                birthdaylist.append(str(random.randint(1, 28)) + "/" + str(random.randint(1, 12)) + "/" + str(random.randint(70, 99)))
                i += 1
            #convertir lista a csv mode
            k = "\n"
            i = 0
            while len(birthdaylist) > i:
                print(birthdaylist[i]) 
                k = k + birthdaylist[i] + "\n"
                i += 1
                
            #insertar a csv ya en ese formato
            f = open('Accounts\ToolBox\Birthdays\Randombirthdays.csv','a')
            f.write(k)
            f.close()

            print("Birthdays succefully saved in Randombirthdays.csv")

        else:
            print("Error: Wrong answer")

    elif usoreu == 2:
        if brithdaymode == 1:
            i = 0
            while usernumber > i:
                birthdaylist.append(str(random.randint(1, 12)) + "/" + str(random.randint(1, 28)) + "/" + str(random.randint(1970, 2004)))
                i += 1
            #convertir lista a csv mode
            k = "\n"
            i = 0
            while len(birthdaylist) > i: 
                print(birthdaylist[i])
                k = k + birthdaylist[i] + "\n"
                i += 1
                
            #insertar a csv ya en ese formato
            f = open('Accounts\ToolBox\Birthdays\Randombirthdays.csv','a')
            f.write(k)
            f.close()

            print("Birthdays succefully saved in Randombirthdays.csv")

        elif brithdaymode == 2:
            i = 0
            while usernumber > i:
                birthdaylist.append(str(random.randint(1, 12)) + "/" + str(random.randint(1, 28)) + "/" + str(random.randint(70, 99)))
                i += 1
            #convertir lista a csv mode
            k = "\n"
            i = 0
            while len(birthdaylist) > i: 
                print(birthdaylist[i])
                k = k + birthdaylist[i] + "\n"
                i += 1
                
            #insertar a csv ya en ese formato
            f = open('Accounts\ToolBox\Birthdays\Randombirthdays.csv','a')
            f.write(k)
            f.close()

            print("Birthdays succefully saved in Randombirthdays.csv")

        else:
            print("Error: Wrong answer")




