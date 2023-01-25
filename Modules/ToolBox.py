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
from colorama import Fore, Back, Style, init
import pathlib
import requests
import socket
import subprocess
import os
import sys


from phonegen import phonenumgen
from randname import randomnames
from randsizes import randomsize
from randbirthday import birthdays
from namejig import jignames
from addyjig import addressjigger
from usnkrs import usnkrsconverter
from usnkrslinker import usnkrsprofilelinker
from profileshuffle import shuffleprofiles
from randpassword import randpass
from gmailtrick import unlimitedgmail
from geocoder import geocoder
from proxychecker import checkproxy
from catchallgen import catchall
from proxyshuffle import shuffle
init(convert=True)




def clear():
    os.system('cls')


def toolbox():
    spaces = ""
    print("Welcome to the ToolBox Modules")
    print()
    print(spaces + "0. Exit                                         8. Usnkrs Profile Linker")
    print(spaces + "1. Phone Number Generator                       9. Profile shuffler")
    print(spaces + "2. Name Generator                               10. Password Generator")
    print(spaces + "3. Size Generator                               11. Unlimited gmail trick")
    print(spaces + "4. Birthday Generator                           12. Geocoder")
    print(spaces + "5. Name Jigger                                  13. Proxychecker")
    print(spaces + "6. Addy Jigger                                  14. Catchall Generator")
    print(spaces + "7. Usnkrs Profile Converter                     15. Proxy Shuffler")  
    print()             
    module = input("select the module you want to use(0-15)")

    if module == "1":
        if validate() == True:
            clear()
            phonenumgen()
    elif module == "2":
        if validate() == True:
            clear()
            randomnames()
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

    elif module == "6":
        if validate() == True:
            clear()
            addressjigger()

    elif module == "7":
        if validate() == True:
            clear()
            usnkrsconverter()

    elif module == "8":
        if validate() == True:
            clear()
            usnkrsprofilelinker()

    elif module == "9":
        if validate() == True:
            clear()
            shuffleprofiles()
  
    elif module == "10":
        if validate() == True:
            clear()
            randpass()

    elif module == "11":
        if validate() == True:
            clear()
            unlimitedgmail()

    elif module == "12":
        if validate() == True:
            clear()
            geocoder()
            

    elif module == "13":
        if validate() == True:
            clear()
            checkproxy()
            

    elif module == "14":
        if validate() == True:
            clear()
            catchall()


    elif module == "15":
        if validate() == True:
            clear()
            shuffle()

    elif module == "0":
        pass
    else: 
        print("Wrong answer")



