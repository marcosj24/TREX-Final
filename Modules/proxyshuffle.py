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

def shuffle():
    proceed = str(input("Do you wish to proceed to shuffle your proxies?(y/n)"))
    if proceed.lower() == "y":
# opening the file in read mode
        proxyfile = open("Accounts\Toolbox\Proxies\proxiestoshuffle.txt", "r")
  
# reading the file
        data = proxyfile.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
        proxylist = data.split("\n")
        proxyfile.close()
        random.shuffle(proxylist)
        i = 0

        with open('Accounts\Toolbox\Proxies\proxiesshuffled.txt', 'w') as f:
            while len(proxylist) > i:
                proxy = proxylist[i]
                f.write("\n")
                f.write(proxy)
                i += 1
    
        print(str(len(proxylist)) + " proxies shuffled! You can now find your proxies in a new order in: proxiesshuffled.txt")

    elif proceed.lower() == "n":
        print("Proceeding to main menu")
    else:
        print("Error: Wrong answer")





