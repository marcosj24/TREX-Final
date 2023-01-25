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
def yahoo():
#test proxies
  def log(message, color, task):
      now = datetime.now()
      now = now.strftime("  [%b %d @ %H:%M:%S.%f")[:-3]+("] ")
      print(color + f"{now}TASK {str(task)}: {message}" + Fore.WHITE)

  def goodproxy(task):
    proxyraw = getproxy()
    ip=proxyraw.split(":")[0]
    port=proxyraw.split(":")[1]
    user=proxyraw.split(":")[2]
    pwd=proxyraw.split(":")[3]
    try:
        proxy = {
        "http": f"http://{user}:{pwd}@{ip}:{port}",
        "https": f"http://{user}:{pwd}@{ip}:{port}",
        }
        # ip = get('https://api.ipify.org').text
        # print('My public IP address is: {}'.format(ip))

    except:
        proxy = {
        "http": f"http://{user}:{pwd}@{ip}:{port}",
        # "https": f"https://{user}:{pwd}@{ip}:{port}",
        }

    #first request(get some values that will be used in the secodn request)
    headers = {
        'authority': 'login.yahoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en;q=0.9',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    try:
      response = requests.get('https://login.yahoo.com/account/create', headers=headers, proxies=proxy)
      return proxyraw
    except:
      log("Proxy flagged, retrying...", Fore.RED, task)
      return False




  #add webhooks and add to file
  #try with oxylabs
  def genyahoo(task):
    with open("Settings\Personal Settings.csv", 'r') as f:
      csvlist = f.readlines()
      smskey = csvlist[6].replace("\n","").split(",")[1]
    letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    firstname = names.get_first_name()
    lastname = names.get_last_name()
    randomelements = ["",".","_"]
    mail = firstname.lower() + random.choice(randomelements) + lastname.lower() + str(random.randint(100, 999))
    password = random.choice(letterlist).upper() + random.choice(letterlist) + random.choice(letterlist) + random.choice(letterlist) + random.choice(letterlist) + random.choice(letterlist) + random.choice(letterlist) + random.choice(letterlist) + str(random.randint(10,99)) + "!"
    year = str(random.randint(1970,2002))
    headless = True
    with sync_playwright() as p:
      start_time = time.time()
      while True:
        try:
          log("Rotating proxies...", Fore.WHITE, task)
          proxy = goodproxy(task)
          while proxy == False:
            proxy = goodproxy(task)
          log("Launching proxy...", Fore.WHITE, task)
          proxyInfo = {}
          if proxy == "localhost":
              log("running on localhost", Fore.WHITE, task)
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
          #cookies = [{'name': 'WMF-Last-Access', 'value': '17-Jan-2023', 'domain': 'www.wikipedia.org', 'path': '/', 'expires': 1676721600, 'httpOnly': True, 'secure': True, 'sameSite': 'None'},{'name': 'WMF-Last-Access-Global', 'value': '17-Jan-2023', 'domain': '.wikipedia.org', 'path': '/', 'expires': 1676721600, 'httpOnly': True, 'secure': True, 'sameSite': 'None'}, {'name': 'GeoIP', 'value': 'GB:ENG:London:51.51:-0.10:v4', 'domain': '.wikipedia.org', 'path': '/', 'expires': -1, 'httpOnly': False, 'secure': True, 'sameSite': 'None'}, {'name': 'guest_id', 'value': 'v1%3A167397504994623864', 'domain': '.twitter.com', 'path': '/', 'expires': 1708189450, 'httpOnly': False, 'secure': True, 'sameSite': 'None'}, {'name': 'ct0', 'value': 'ea24051a1d177a451bb8be5f4dbe7ad6', 'domain': '.twitter.com', 'path': '/', 'expires': 1673996650, 'httpOnly': False, 'secure': True, 'sameSite': 'None'}, {'name': 'gt', 'value': '1615394563568304237', 'domain': '.twitter.com', 'path': '/', 'expires': 1673985851, 'httpOnly': False, 'secure': True, 'sameSite': 'None'}]
          #context.add_cookies(cookies=cookies)
          page.goto("https://login.yahoo.com/account/create")
          log("Loaded generation URL...", Fore.WHITE, task)
          break
        except:
          browser.close()
          log("Bad proxy, rotating...", Fore.RED, task)
      log("Mail to be generated: " + mail + "@yahoo.com", Fore.WHITE, task)
      log("Filling informations...", Fore.WHITE, task)
      while True:
        try:
          page.type('//*[@id="usernamereg-firstName"]', firstname, delay=100)
          page.type('//*[@id="usernamereg-lastName"]', lastname, delay=100)
          page.type('//*[@id="usernamereg-userId"]', mail, delay=100)
          page.type('//*[@id="usernamereg-password"]', password, delay=100)
          page.type('//*[@id="usernamereg-birthYear"]', year, delay=100)
          page.locator('//*[@id="reg-submit-button"]').click()
          time.sleep(2)
          break
        except:
          pass
      time.sleep(10)
      try:
        s = page.locator('//*[@id="contact-countrycode-dropdown"]/div[2]/div/select/option').text_content()
        log("Informations filled", Fore.WHITE, task)
      except:
        log("Mail allready exsists", Fore.RED, task)
        time.sleep(2)
        return False
      log("Getting proxy region...", Fore.WHITE, task)
      try:
        s = page.locator('//*[@id="contact-countrycode-dropdown"]/div[2]/div/select/option').text_content()
        prefix = (s[s.find('(')+len('('):s.rfind(')')])
        prefix = prefix.replace("+","")
        phoneinput = True
      except:
        page.type('//input[@id="usernamereg-contact"]', str(random.randint(1,9)), delay=100)
        s = page.locator('//*[@id="contact-countrycode-dropdown"]/div[2]/div/select/option').text_content()
        prefix = (s[s.find('(')+len('('):s.rfind(')')])
        prefix = prefix.replace("+","")
        page.fill('//input[@id="usernamereg-contact"]',"")
        phoneinput = False

      region = prefix2code(prefix)
      log("Region: " + region, Fore.WHITE, task)
      try:
        number,id = getphone(region,smskey,"mb")
        log("Got phone number: " + number, Fore.WHITE, task)
      except:
        log("Retrying...", Fore.RED, task)
        return False

      try:
        log("Inputing phone number...", Fore.WHITE, task)
        page.type('//*[@id="usernamereg-phone"]', number, delay=100)
        page.locator('//*[@id="reg-submit-button"]').click()
      except:
        log("Inputing account phone number...", Fore.WHITE, task)
        page.type('//*[@id="usernamereg-contact"]', number, delay=100)
        page.locator('//*[@id="reg-submit-button"]').click()

      #if statement si captcha en html
      time.sleep(3)
      if "phone-verify" not in page.url: 
        if "captcha" in page.url:
          log("Captcha detected, retrying...", Fore.RED, task)
          return False
        else:
          log("Invalid phone number, retrying...", Fore.RED, task)
          return False
      else:
        log("verification code sent!", Fore.MAGENTA, task)
      
      log("Waiting for code...", Fore.WHITE, task)
      code = getCode(8,smskey,id)
      if code == False:
        log("could not get code, retrying...", Fore.RED, task)
        return False
      else:
            log("Verification code: " + code, Fore.MAGENTA, task)
      while True:
        try:
          log("Submiting code...", Fore.WHITE, task)
          page.type('//input[@id="verification-code-field"]', code, delay=100)
          page.locator('//button[@class="pure-button puree-button-primary puree-spinner-button challenge-button"]').click()
          break
        except:
          pass
      while True:
        try:
          page.locator('//input[@class="subscription-checkbox  pure-u-1-8"]')
          break
        except:
          pass
      #print("--- %s seconds ---" % (time.time() - start_time))
      log("Account generated and verified succesfully!", Fore.GREEN, task)
      f = open('Accounts\Account Generators\Yahoo\GeneratedYahoo.csv','a')
      f.write("\n"+mail+"@yahoo.com"+","+password+","+firstname+","+lastname)
      f.close()
      log("Mail saved to file!", Fore.GREEN, task)
      yahoopersonal(firstname + " " + lastname,mail+"@yahoo.com", password, region)
      log("Webhook sent!", Fore.GREEN, task)
      time.sleep(3)
      browser.close()
      return True

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

  def mailchecker():
    yahoolist = []
    with open("Accounts\Account Generators\Yahoo\YahooChecker.csv", 'r') as file:
        csvlist = file.readlines()
        csvlist.remove(csvlist[0])
        for i in range(len(csvlist)):
            mail = csvlist[i].split(",")[0]
            yahoolist.append(mail)
    def checkmail(email_address,task):
      url = f"https://dev.me/api/module-app/v1-get-email-details?email={email_address}&verifyMx=true&verifySmtp=true"

      # Set up the request payload and headers
      payload = {}
      headers = {
          'x-api-key': 'demo-key'
      }

      # Make the API request
      response = requests.get(url, headers=headers, data=payload)

      # Get the JSON response
      rsp = response.json()
      response = requests.get(
          "https://isitarealemail.com/api/email/validate",
          params = {'email': email_address})
      status = response.json()['status']

      if status == "valid":
          log(Fore.WHITE + email_address + Fore.GREEN + " Account Active",Fore.WHITE,task)
          return True
      else:
          log(Fore.WHITE + email_address + Fore.RED + " Account Clipped/Doesn't Exsist",Fore.WHITE,task)
          return False
    deletespaces("Accounts\Account Generators\Yahoo\YahooChecker.csv")
    for i in range(len(yahoolist)):
        response = checkmail(yahoolist[i],i+1)
        changecell("Accounts\Account Generators\Yahoo\YahooChecker.csv",i+1,1,str(response))
        time.sleep(0.5)

  print("Welcome to the Yahoo Module")
  spaces = ""
  print()
  print(spaces + "1. Yahoo Mail Generator")
  print(spaces + "2. Yahoo Mail Checker")
  print()             
  module = input("select an option(1-2)")
  if module == "1":
    if validate() == True:
        clear()
        num = input("input the amount of yahoo accounts you would like to generate")
        clear()
        for i in range(1,int(num) + 1):
          while genyahoo(i) == False:
            pass
        print("All tasks completed succesfully")
  elif module == "2":
    clear()
    confirmation = input("Press enter to proceed to check your mails in YahooChecker.csv")
    clear()
    mailchecker()

  else:
    print("Error:Wrong Answer")