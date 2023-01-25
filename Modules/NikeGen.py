from colorama import Fore, init
from bs4 import BeautifulSoup
from datetime import datetime
import random
import string
import time
import json
import csv
import os
import re
import requests
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
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import pprint
import time
import pyperclip
from sys import exit
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import requests
from discord import SyncWebhook, file, colour, Embed, embeds
from playwright.sync_api import sync_playwright
from proxyget import getproxy
import undetected_chromedriver.v2 as uc
import imaplib
import email
import os
import base64
import email.parser
import os
import pickle
# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from imapclient import IMAPClient
from bs4 import BeautifulSoup as bs4
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type
from bs4 import BeautifulSoup
from getsms import getphone, getselectvalue, getCode
import traceback
from webhooks import nikepersonal
init(convert=True)


def log(message, color, task):
    now = datetime.now()
    now = now.strftime("  [%b %d @ %H:%M:%S.%f")[:-3]+("] ")
    print(color + f"{now}TASK {str(task)}: {message}" + Fore.WHITE)

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

                



def getnikecode(mail):
    with IMAPClient('imap.gmail.com', ssl=True) as server:
        server.login("valluyjunca@gmail.com", "yvsurjrckcswmefp")
        server.select_folder('INBOX')
        messages = server.search(f'TO "{mail}"') #use server.search('UNSEEN FROM "nike@notifications.nike.com"') to only see unseen messages from nike
        try:
            for uid, message_data in server.fetch(messages[-1], 'RFC822').items():
                data = message_data[b'RFC822']
                soup = bs4(str(data.decode()), "html.parser")
                soup = bs4(str(data.decode()),features="lxml")
                code = soup.find_all("p")[2].getText().split(": ")[1].split(".")[0]
                if code == None:
                    return False
                else:
                    return code
        except:
            return False



#look for recall of nike verify function when adding parameters
def nikegenverf(firstname,lastname,gmail,password,region,smskey,task):
    headless = True
    mail = gmail.split("@")[0] + str(random.randint(100, 999)) + "@valluyjunca.com"
    log("Generating: " + gmail, Fore.CYAN,task)
    log("Rotating proxy", Fore.WHITE,task)
    proxy = getproxy()
    #2 sus addLogs missing
    #google search, then access nike
    start_time = time.time()
    with sync_playwright() as p:
        log("Launching proxy", Fore.WHITE,task)
        proxyInfo = {}
        if proxy == "localhost":
            browser = p.firefox.launch(headless=headless)
        else:
            proxyInfo = proxy.split(":")
            proxyInfo = {
                "server": f"http://{proxyInfo[0]}:{proxyInfo[1]}",
                "username": proxyInfo[2],
                "password": proxyInfo[3],
            }
            browser = p.firefox.launch(headless=headless,  proxy=proxyInfo)
        
        context = browser.new_context()
        page = context.new_page()

   
        log("Generating cookies...",Fore.WHITE,task)
        time.sleep(1)

        while True:
            try:
                page.goto("https://twitter.com/")
                break
            except:
                pass
        log("Cookies generated!",Fore.MAGENTA,task)
        '''
        while True:
            try:
                log("Targeting nike URL...",Fore.WHITE,task)
                page.goto("https://www.nike.com/member/profile")
                break
            except:
                pass
        '''
        def fillemailpass():
            while True:
                try:
                    log("Redirecting to generation URL...",Fore.WHITE,task)
                    page.goto("https://www.nike.com/member/profile")
                    break
                except:
                    pass
            try:
                page.wait_for_selector('//*[@id="username"]')
                log("Loggin credentials...",Fore.WHITE,task)
                page.fill('//*[@id="username"]', mail)
                page.locator('//button[@class="css-18y7846 btn-primary-dark  btn-md"]').click()
                page.wait_for_selector('//*[@id="l7r-code-input"]')
                return True
            except:
                log("Failed to log credentials, retrying...",Fore.RED,task)
                return False

        login = fillemailpass()
        while login == False:
            time.sleep(10)
            login = fillemailpass()
        else:
            log("Credentials Logged!",Fore.MAGENTA,task)
        #page.locator('//*[@id="1a8d7baa-6096-418b-889b-1961c680d8ae"]/div/div/div[2]/a').click()
        log("Injecting AKAMAI BYPASS...",Fore.WHITE,task)
        i = 0
        for i in range(120):
            verifcode = getnikecode(mail)
            if verifcode == False:
                time.sleep(1)
                gotcode = False
            else:
                log("BYPASS succesfull!",Fore.MAGENTA,task)
                gotcode = True
                break
            i += 1
        if gotcode == False:
            log("BYPASS failed, retrying...",Fore.RED,task)
            return False
        #get xpaths de name...
        #see if it works
        #email scrape(specific sender)
        #email code: 

        log("Logging informations...",Fore.WHITE,task)
        page.type('//*[@id="l7r-code-input"]', verifcode, delay=100)
        #fname: 
        page.type('//*[@id="l7r-first-name-input"]', firstname, delay=100)
        #lname: 
        page.type('//*[@id="l7r-last-name-input"]', lastname, delay=100)
        #password: 
        page.type('//*[@id="l7r-password-input"]', password, delay=100)
        #shoping pref(click): 
        page.locator('//*[@id="l7r-shopping-preference"]').select_option(index=random.randint(1,2))
        #birthdate: 
        page.type('//*[@id="l7r-date-of-birth-input"]', "10122000", delay=100)
        log("Informations logged...",Fore.MAGENTA,task)
        created = False
        for i in range(3):
        #newsletter 
            try:
                log("Submitting account details for generation...",Fore.WHITE,task)
                page.locator('//input[@aria-describedby="a11y-label-details-marketingOptIn"]').click()
                page.locator('//*[@id="privacyTerms"]').click()
                page.locator('//button[@aria-label="Create Account"]').click()
                created = True
                break
            except:
                pass
        if created == False:
            log("Generation failed, restarting...",Fore.RED,task)
            return False

        #press button instead of reload link(change from loead url to buttons)
        while True:
            log("Getting generation tokens...",Fore.WHITE,task)
            try:
                page.hover('//*[@id="AccountMenu"]/a/div/div/p')
                page.locator('//*[@id="AccountMenu-Menu"]/div/nav/ul/li[6]/a').click()
                break
            except:
                while True:
                    log("Reloading page...",Fore.WHITE,task)
                    try:
                        page.goto("https://www.nike.com/member/profile")
                        break
                    except:
                        pass
        while True:
            try:
                log("Inputting account details...",Fore.WHITE,task)
                page.locator('//*[@id="email"]').fill("")
                page.type('//*[@id="email"]', gmail, delay=100)
                page.locator('//*[@id="settings"]/div[3]/div[2]/div/div/form/div[2]/div[7]/div[2]/div[2]/button').click()
                log("Account details saved!",Fore.MAGENTA,task)
                break
            except:
                while True:
                    try:
                        log("Checking if details have been saved...",Fore.WHITE,task)
                        page.goto("https://www.nike.com/member/settings/")
                        break
                    except:
                        pass
        try:
            log("Generating account...",Fore.WHITE,task)
            page.locator('//button[@class="css-18y7846 btn-primary-dark  btn-md"]').click()
            log("Account generated succesfully!...",Fore.GREEN,task)
        except:
           log("Account generation failed!",Fore.RED,task)

        while True:
            try:
                page.wait_for_selector('//button[@class="nds-btn underline d-sm-ib css-34a37p ex41m6f0 cta-primary-dark underline"]')
                break
            except:
                while True:
                    try:
                        page.goto("https://www.nike.com/member/settings")
                        break
                    except:
                        pass
        
        def sendcode():
        #accept cookies
        #apretar boton de añadir phone number
            try:
                log("Opening phone number settings",Fore.WHITE,task)
                page.locator('//button[@class="nds-btn underline d-sm-ib css-34a37p ex41m6f0 cta-primary-dark underline"]').click()
                log("Oppened",Fore.MAGENTA,task)
            except Exception as e:
                print(e)
                return False
            try:
                log("Opening confirmation field",Fore.WHITE,task)
                page.fill('//*[@id="phoneNumber"]', str(random.randint(1,9)))
                page.fill('//*[@id="phoneNumber"]', "")
            except Exception as e:
                print(e)
                return False

            selectvalue = getselectvalue(region)
            log("Getting phone number from SMS service",Fore.WHITE,task)
            number,id = getphone(region,smskey,"ew")
            while True:
                try:
                    log("Selecting region...",Fore.WHITE,task)
                    page.locator('//*[@id="callingCode"]').select_option(selectvalue)
                    break
                except:
                    pass
            log("Got number: " + number,Fore.WHITE,task)
            while True:
                try:
                    log("Sending verification code to phone number",Fore.WHITE,task)
                    page.type('//*[@id="phoneNumber"]', number, delay=100)
                    break
                except:
                    pass
            while True:
                try:
                    page.locator('//*[@id="agreeToTerms"]').click()
                    page.locator('//button[@class="nds-btn mr-12-sm css-1kvzham ex41m6f0 btn-primary-dark  btn-responsive"]').click()
                    break
                except:
                    pass
            log("Verification code sent!...",Fore.MAGENTA,task)
            log("Waiting for code...",Fore.WHITE,task)
            return id
        id = sendcode()
        while id == False:
            while True:
                try:
                    log("Re submitting phone number",Fore.WHITE,task)
                    page.locator('//button[@class="nds-btn nds-button--icon-only dialog-ui-close egyxy7o0 css-wpekej ex41m6f0 btn-secondary-dark "]').click()
                    break
                except:
                    pass
            id = sendcode()
        code = getCode(15, smskey, id)
        while code == False:
            log("could not get code number, retrying",Fore.RED,task)
            while True:
                try:
                    page.locator('//button[@class="nds-btn nds-button--icon-only dialog-ui-close egyxy7o0 css-wpekej ex41m6f0 btn-secondary-dark "]').click()
                    break
                except:
                    pass
            id = sendcode()
            time.sleep(10)
            code = getCode(15, smskey, id)
        else:
            log("got code: " + code, Fore.MAGENTA, task)
        page.type('//input[@class="nds-input-text-field css-1vpt1v7 e1fiih290"]', code, delay=100)
        while True:
            try:
                page.locator('//button[@class="nds-btn css-278i28 ex41m6f0 btn-primary-dark  btn-responsive"]').click()
                break
            except:
                pass
        while True:
            try:
                page.wait_for_selector('//button[@class="nds-btn underline d-sm-ib css-34a37p ex41m6f0 cta-primary-dark underline"]')
                break
            except:
                pass
        log("Account generated and verified succesfully!", Fore.GREEN, task)
        nikepersonal(gmail, password, region)
        log("Webhook sent!", Fore.GREEN,task)
        browser.close()



amount = input("How many Nike account would you like to generate(dont input more than in CSV):")
with open("Settings\Personal Settings.csv", 'r') as f:
    csvlist = f.readlines()
    smskey = csvlist[6].replace("\n","").split(",")[1]

for i in range(int(amount)):
    try:
        mail,password,fname,lname,region,row = getcsvdata(r"Accounts\Account Generators\Nike\NikeCustom.csv")
    except:
        print(Fore.RED + "There are not more nike accounts to generate" + Fore.WHITE)
        break
    changecell(r"Accounts\Account Generators\Nike\NikeCustom.csv",row,5,"Gen")
    while nikegenverf(fname,lname,mail,password,region,smskey,i+1) == False:
        pass
    changecell(r"Accounts\Account Generators\Nike\NikeCustom.csv",row,5,"True")
    log("Account saved succesfully in CSV!", Fore.GREEN, i+1)