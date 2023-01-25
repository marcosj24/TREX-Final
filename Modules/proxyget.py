#get and delete proxy
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

def getproxy():
    file=open("proxies\proxies.txt")
    proxies=file.read()
    file.close()
    proxies=proxies.split("\n")
    proxy = proxies[0].replace("\n", "")
    del proxies[0]
         #returns a list of strings
    newfile = ""
    for i in range(len(proxies)):
        newfile = newfile + proxies[i] + "\n"
    with open('proxies\proxies.txt', 'w') as f:
        f.write(newfile)
    return proxy
    
