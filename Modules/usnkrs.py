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

def usnkrsconverter():
    print("Welcome to the USNKRS profile converter")
    proceed = str(input("Do you wish to proceed to convert your profiles?(y/n)"))
    if proceed.lower() == "y":
        #extraer rows
        with open(r'Accounts\Toolbox\USNKRS\USNKRSprofiles.csv', 'r') as file:
            csvlist = file.readlines() #returns a list of strings
        rows = len(csvlist)
        print(rows + " profiles detected")

        #convertir el csv a una lista con listas dentro de cada row
        with open(r'Accounts\Toolbox\USNKRS\USNKRSprofiles.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Pass reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)
        bulkprofiles = ""
        i = 1
        while rows > i:
            finalprofile = str(list_of_rows[i])
            finalprofile = finalprofile.replace("', '", "|" )
            finalprofile = finalprofile.replace("['", "")
            finalprofile = finalprofile.replace("']", "")
            finalprofile = finalprofile[:7] + '|' + finalprofile[7:]
            bulkprofiles = bulkprofiles + finalprofile + "\n"
            print(finalprofile)
            i +=1

        with open(r'Accounts\Toolbox\USNKRS\USNKRSbulkprofiles.txt', 'w') as f:
                f.write(bulkprofiles)
        
        print("Profiles converted!")
        #sacar el middle name y ponerlo automatico para que en el csv solo se tenga que poner first y last name.

    elif proceed.lower() == "y":
        print("Proceeding to main menu")
    else:
        print("Error, wrong answer")





