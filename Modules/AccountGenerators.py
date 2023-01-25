from validate import validate
import random
import names
import re
import csv
from csv import reader
import itertools
from itertools import permutations
import pandas as pd
import time
from sys import exit
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
import pathlib
import requests
import socket
import subprocess
import os
import sys


from icloudrequests import icloud
from yahooplaywrt import yahoo

def clear():
    os.system('cls')

init(convert=True)

def accgenerators():
    print("Welcome to the Account Generator Modules")
    spaces = ""
    print()
    print(spaces + "0. Exit                                          3. Outlook")
    print(spaces + "1. iCloud                                        4. Nike")
    print(spaces + "2. Yahoo                                         5. Prodirect")
    print(spaces + "6. Gmail                                         7. Asos(under dev)")
    print()             
    module = input("select the module you want to use(0-15)")

    if module == "1":
        if validate() == True:
            clear()
            icloud()
    elif module == "2":
        if validate() == True:
            clear()
            #Add yahoo checker
            yahoo()
    elif module == "3":
        if validate() == True:
            clear()
            randomsize()

    elif module == "4":
        if validate() == True:
            clear()
            birthdays()
   
    elif module == "5":
        if validate() == True:
            clear()
            jignames()

    elif module == "0":
        pass
    else: 
        print("Wrong answer")

