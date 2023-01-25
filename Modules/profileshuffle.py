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

def shuffleprofiles():
    proceed = str(input("Do you wish to proceed to shuffle your profiles?(y/n)"))
    if proceed.lower() == "y":
# opening the file in read mode
        profilefile = open(r"Accounts\Toolbox\Profiles\profilestoshuffle.csv", "r")
  
# reading the file
        profiles = profilefile.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
        profilelist = profiles.split("\n")
        profilefile.close()
        
        profilelist.pop(0)
        profilelist.pop(len(profilelist) - 1)
        random.shuffle(profilelist)


        i = 0
        with open('Accounts\Toolbox\Profiles\Profilesshuffled.csv', 'w') as f:
            f.write(" ," + " ," + "\n")

        with open('Accounts\Toolbox\Profiles\Profilesshuffled.csv', 'a') as f:
            while len(profilelist) > i:
                profile = profilelist[i]
                f.write("\n")
                f.write(profile)
                i += 1
    elif proceed.lower() == "n":
        print("Proceeding to main menu")
    else:
        print("Error: Wrong answer")

    print(str(len(profilelist)) + " profiles shuffled! You can now find your profiles in a new order in: Profilesshuffled.csv")









