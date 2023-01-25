#imports
import random
import names
import re
import csv
from csv import reader
import itertools
from itertools import permutations
import pandas as pd
import os
import time


def catchall():
    def getinfo(row,column):
        with open(r'Settings\Personal Settings.csv', 'r') as file:
            rows = file.readlines() #returns a list of strings
        value = rows[row].split(",")[column]
        return value

    print("Welcome to the catchall generator!")
    domain = getinfo(2,1).replace("\n", "")
    times = input("Please input the amount of catchall mails you want to generate:")
    i = 0
    k = ""
    randomelements = ["","-",".","_"]
    while int(times) > i:
        firstname = names.get_first_name()
        lastname = names.get_last_name()
        mail = firstname.lower() + random.choice(randomelements) + lastname.lower() + str(random.randint(100, 999))
        maildomain = mail + "@" + domain
        print(maildomain)
        k = k + "\n" + maildomain + "," + mail + "," + firstname + "," + lastname
        i += 1


    f = open(r'Accounts\Toolbox\Catchall\Catchalls.csv','a')
    f.write(k)
    f.close()
    print("Mails succefully saved in Catchalls.csv")





