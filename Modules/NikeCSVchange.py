import random
import names
import re
import csv
from csv import reader
import itertools
from itertools import permutations
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import pprint
import time
import pyperclip
from sys import exit
from colorama import init, Fore, Back, Style
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import requests
from discord import SyncWebhook, file, colour, Embed, embeds
from bs4 import BeautifulSoup
from datetime import datetime
from validate import validate
from playwright.sync_api import sync_playwright
from proxyget import getproxy
import names
from getsms import prefix2code,getphone,getCode
from webhooks import yahoopersonal
init(convert=True)



def clear():
    os.system('cls')
#function that gets, tests proxies, extracts a good one for the site, new module
def changecell(path,row,column,content):
  with open(path, 'r') as file:
      csvlist = file.readlines()
  line = csvlist[row]
  line = line.replace("\n","")
  lineslist = line.split(",")
  lineslist[column] = content
  line = ",".join(lineslist)
  line = line + "\n"
  csvlist[row] = line
  csvdata = ""
  for i in range(len(csvlist)):
      csvdata = csvdata + csvlist[i]
  with open(path, 'w') as file:
      file.write(csvdata)

def deletespaces(path):
  with open(path, 'r') as file:
      csvlist = file.readlines() #returns a list of strings
  rows = len(csvlist)
  while('\n' in csvlist):
      csvlist.remove('\n')
  csvdata = ""
  for i in range(len(csvlist)):
      csvdata = csvdata + csvlist[i]
  with open(path, 'w') as file:
      file.write(csvdata)

def getcsvdata(path):
  acclist = []
  deletespaces(path)
  with open(path, 'r') as f:
      csvlist = f.readlines()
      csvlist.remove(csvlist[0])
      for i in range(len(csvlist)):
        if "True" in csvlist[i]:
          pass
        elif  "Gen" in csvlist[i]:
          pass
        else:
          mail = csvlist[i].replace("\n","").split(",")[0]
          password = csvlist[i].replace("\n","").split(",")[1]
          fname = csvlist[i].replace("\n","").split(",")[2]
          lname = csvlist[i].replace("\n","").split(",")[3]
          region = csvlist[i].replace("\n","").split(",")[4]
          row = i + 1
          break
  return mail,password,fname,lname,region,row


def getsmskey():
with open("Settings\Personal Settings.csv", 'r') as f:
    csvlist = f.readlines()
    smskey = csvlist[6].replace("\n","").split(",")[1])


#get a list of account that dont have True