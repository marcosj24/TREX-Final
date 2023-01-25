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


def phonenumgen():

    def genphone(numbers, start, prefix):
        i = 0
        phone = ""
        while int(numbers) > i:
            phone = phone + str(random.randint(0,9))
            i += 1
        phone = prefix + start + phone  
        return phone
        
        


    print("Welcome to the phone number generator")
    start = str(input("input the number/s you want all phone numbers to start with:"))
    numbers = int(input("input the amount of digits the phone number has after those numbers:"))
    prexif = str(input("input your prefix, press enter if you dont want:"))
    amount = int(input("how many phone numbers do you want to generate:"))

    print(genphone(numbers,start,prexif))

    k = 0 
    while amount > k:
        phone = genphone(numbers,start,prexif)
        print(phone)
        f = open('Accounts\ToolBox\Phones\Randomphones.csv','a')
        f.write("\n" + str(phone))
        k += 1
    print("Phone numbers succefully saved in Randomphones.csv")
    f.close()


    









