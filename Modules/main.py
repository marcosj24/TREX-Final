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
from sys import exit
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
import pathlib
import requests
import socket
import subprocess

#import modules
from ToolBox import toolbox
from AccountGenerators import accgenerators
from validate import validate,getusername,logout

'''
from phonegen import phonenumgen
from randname import randomnames
from randsizes import randomsize
from randbirthday import birthdays
from namejig import jignames
from addyjig import addressjigger
from usnkrs import usnkrsconverter
from proxyshuffle import shuffle
from catchallgen import catchall
from profileshuffle import shuffleprofiles
from randpassword import randpass
from usnkrslinker import usnkrsprofilelinker
from gmailtrick import unlimitedgmail
from icloudrequests import icloud
from geocoder import geocode
from mailchecker import checkmails
from proxychecker import checkproxy
from prodirectgen import prodirect
'''

#variables
#Variables in use for while loops:
#lists
#functions
#other funcions
def clear():
    os.system('cls')

#error functions

def wronganswer():
    wornganswerinput = int(input("Wrong answer, press 0 to go back"))
    if wornganswerinput == 0:
        start()

def finish():
    finishinput = int(input("Press 0 to continue"))
    if finishinput == 0:
        clear()
        start()


#authentication
def getinfo(row,column):
    with open(r'Settings\Personal Settings.csv', 'r') as file:
        rows = file.readlines() #returns a list of strings
    value = rows[row].split(",")[column].replace("\n", "")
    return value

def getversion():
    f = open(r"Settings\Files\TREXv", "r")
    return f.read().replace(".exe","")
#start function
def start():
    spaces = ""
    spaces2 = ""
    clear()
    print(Fore.GREEN)
    print(spaces2 + " _______              _______          _ _               ")
    print(spaces2 + "|__   __|            |__   __|        | | |              ")
    print(spaces2 + "   | |_ __ _____  __    | | ___   ___ | | |__   _____  __")
    print(spaces2 + "   | | '__/ _ \ \/ /    | |/ _ \ / _ \| | '_ \ / _ \ \/ /")
    print(spaces2 + "   | | | |  __/>  <     | | (_) | (_) | | |_) | (_) >  < ")
    print(spaces2 + '   |_|_|  \___/_/\_\    |_|\___/ \___/|_|_.__/ \___/_/\_\ ')
    print(Fore.WHITE)
    print(spaces + "v" + getversion())
    print(spaces + "Welcome back " + Fore.MAGENTA + getusername() + Fore.WHITE +  "!")
    print(spaces + "Modules:")
    print(spaces + "0. Exit")
    print(spaces + "1. ToolBox")
    print(spaces + "2. Account Generators")
    option = str(input(spaces + "Select an option(1-2):"))
    if option == "1":
        if validate() == True:
            clear()
            toolbox()
            finish()
    elif option == "2":
        if validate() == True:
            clear()
            accgenerators()
            finish()
    elif option == "0":
        logout()
        exit()
    else:
        wronganswer()


clear()
#look for key if key doesnt exsitt, ask for it and store it
if validate() == True:
    start()
else:
    exit()