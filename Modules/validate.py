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




#authentication
def getinfo(row,column):
    with open(r'Settings\Personal Settings.csv', 'r') as file:
        rows = file.readlines() #returns a list of strings
    value = rows[row].split(",")[column].replace("\n", "")
    return value

def auth(license_key):
    Authentication = False
    machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    headers = {
        'Authorization': f'Bearer {"sk_lEwYS7j7x4QMi0hNHjKZYkrpD8lZNUDThfXqcYjz6kKsF73BqHjQrn5pBrqEZt5I"}'
    }
    req = requests.get(f'https://api.hyper.co/v6/licenses/{license_key}', headers=headers)
    if str(req.status_code) == "200":
        license_data = req.json()
        global username
        username = license_data['integrations']['discord']['username']

        if license_data:
            if license_data.get('metadata') == {} or license_data['metadata']['hwid'] == machine_id:
                headers = {
                'Authorization': f'Bearer {"sk_lEwYS7j7x4QMi0hNHjKZYkrpD8lZNUDThfXqcYjz6kKsF73BqHjQrn5pBrqEZt5I"}',
                'Content-Type': 'application/json'
                }

                payload = {
                    'metadata': {
                        'hwid': machine_id
                    }
                }

                req = requests.patch(f'https://api.hyper.co/v6/licenses/{license_key}/metadata', headers=headers, json=payload)
                print('License is good to go!')
                Authentication = True

            else:
                print('License is already in use on another machine!')
                Authentication = False
        else:
            print('License not found!')
            Authentication = False
    else:
        print('License not found!')
        Authentication = False
    return Authentication


def validate():
    if getinfo(1,1) == "":
        key = input("Please insert your license key:")
        if auth(key) == True:
            r = csv.reader(open(r'Settings\Settings.csv')) # Here your csv file
            rows = list(r)
            rows[1][1] = key
            csvready = ""
            for i in range(len(rows)):
                csvready = csvready + rows[i][0] + "," + rows[i][1] + "\n"
            f = open(r'Settings\Settings.csv','w')
            f.write(csvready)
            validation = True
        else:
            validation = False
    else:
        key = getinfo(1,1)
        validation = auth(key)
        if validation != True:
            key = input("Please insert your license key:")
            if auth(key) == True:
                r = csv.reader(open(r'Settings\Settings.csv')) # Here your csv file
                rows = list(r)
                rows[1][1] = key
                csvready = ""
                for i in range(len(rows)):
                    csvready = csvready + rows[i][0] + "," + rows[i][1] + "\n"
                f = open(r'Settings\Settings.csv','w')
                f.write(csvready)
                validation = True
            else:
                validation = False
    return validation

def logout():
    license_key = getinfo(1,1)
    headers = {
        'Authorization': f'Bearer {"sk_lEwYS7j7x4QMi0hNHjKZYkrpD8lZNUDThfXqcYjz6kKsF73BqHjQrn5pBrqEZt5I"}',
        'Content-Type': 'application/json'
    }

    payload = {
        'metadata': {
            'hwid': None
        }
    }

    req = requests.patch(f'https://api.hyper.co/v6/licenses/{license_key}/metadata', headers=headers, json=payload)

def getusername():
    license_key = getinfo(1,1)
    headers = {
        'Authorization': f'Bearer {"sk_lEwYS7j7x4QMi0hNHjKZYkrpD8lZNUDThfXqcYjz6kKsF73BqHjQrn5pBrqEZt5I"}'
    }
    req = requests.get(f'https://api.hyper.co/v6/licenses/{license_key}', headers=headers)
    if str(req.status_code) == "200":
        license_data = req.json()
        username = license_data['integrations']['discord']['username']
        return username


