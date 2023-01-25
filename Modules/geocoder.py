import csv
import requests
import time
from colorama import init, Fore, Back, Style
import socket
import subprocess
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import random
import datetime
import math
import numpy as np
import matplotlib.pyplot as plt
from lxml import etree
import re
import json
import os

def clear():
    os.system('cls')

def getinfo(row,column):
    with open(r'Settings\Personal Settings.csv', 'r') as file:
        rows = file.readlines() #returns a list of strings
    value = rows[row].split(",")[column].replace("\n", "")
    return value

global googleAPI
googleAPI = getinfo(4,1)



def geocoder():
    def geocodeexpand():
        addy = input("please input your original address")
        city = input("please input the city where the addy belongs")
        country = input("please input the country where the addy belongs")
        proximitylevel = int(input("please input the proximity level between addys(1-20,20 far, 1 near)"))
        addyamount = int(input("please input the amount of addys youw would like to generate"))

        def addy2cord(addy,city,country):
            response = requests.get(
                f"https://maps.googleapis.com/maps/api/geocode/json?address={addy},{city},{country}&key={googleAPI}"
            )
            location = response.json()["results"][0]["geometry"]["location"]
            return [location["lng"], location["lat"]]


        def expandcoords(org,coords,proximitylevel):
            long = float(org[0])
            lat = float(org[1])
            times = int(np.ceil(coords/4))
            dif = proximitylevel * 0.0001
            coordlist = []
            for i in range(1,times+1):
                coordlist.append([format(long + dif*i, '.7f'),format(lat + dif*i, '.7f')])
                coordlist.append([format(long + dif*i, '.7f'),format(lat - dif*i, '.7f')])
                coordlist.append([format(long - dif*i, '.7f'),format(lat + dif*i, '.7f')])
                coordlist.append([format(long - dif*i, '.7f'),format(lat - dif*i, '.7f')])
            return coordlist[:coords]

        org = addy2cord(addy,city,country)
        coords = expandcoords(org,addyamount,proximitylevel)
        addylist = []
        replacementnumb = len(coords)
        for i in range(len(coords)):
            long = coords[i][0]
            lat = coords[i][1]
            response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{long}&key={googleAPI}")
            addy = response.json()['results'][0]['formatted_address']
            while "+" in addy: 
                replacementnumb = replacementnumb + 1
                replacementcoords = expandcoords(org,replacementnumb,proximitylevel)[replacementnumb-1]
                response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?latlng={replacementcoords[1]},{replacementcoords[0]}&key={googleAPI}")
                addy = response.json()['results'][0]['formatted_address']
                print(addy + " found, replacing")
            else:
                print(addy)
                addylist.append(addy)
        k = "\n"
        i = 0
        while len(addylist) > i: 
            print(addylist[i])
            k = k + addylist[i] + "\n"
            i += 1
            
        #insertar a csv ya en ese formato
        f = open('Accounts\ToolBox\Geocoder\Addresses.csv','a')
        f.write(k)
        f.close()
        print(str(len(addylist)) + " addys geocoded and saved in Addresses.csv!")
        return addylist





    def geocodepostal():
        postal = input("please input the postal code you want to goecode")
        city = input("please input the city where the postal code belongs")
        country = input("please input the country where the postal code belongs")
        addynumb = int(input("please input the amount of addys youw would like to generate"))
        def postal2cord(postal,city,country):
            response = requests.get(
                f"https://maps.googleapis.com/maps/api/geocode/json?address={postal},{city},{country}&key={googleAPI}"
            )
            location = response.json()["results"][0]["geometry"]["location"]
            return [location["lng"], location["lat"]]

        def coordtoaddynvalidate(coords,postal):
            lat = coords[0]
            long = coords[1]
            response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?latlng={long},{lat}&key={googleAPI}")
            addy = response.json()['results'][0]['formatted_address']
            addyinfo = response.json()['results'][0]['address_components']
            respostal = addyinfo[len(addyinfo)-1]["long_name"]
            if postal == respostal:
                return addy
            else:
                return False
        orgcoords = postal2cord(postal,city,country)
        long = orgcoords[0]
        lat = orgcoords[1]
        addylist = []
    #return addys, while len addys is mas bajo, empezar por 5 de proximidad y ir bajando 0.1 cada vez
        dif = 0.0002
        i = 0
        times = int(np.ceil(addynumb/4))
        print(times)
        while times > i:
            coords = [format(long + dif, '.7f'),format(lat + dif, '.7f')]
            addy = coordtoaddynvalidate(coords,postal)
            if addy == False or addy in addylist:
                times += 1
            else:
                print(addy)
                addylist.append(addy)
            coords = [format(long + dif, '.7f'),format(lat - dif, '.7f')]
            addy = coordtoaddynvalidate(coords,postal)
            if addy == False or addy in addylist:
                times += 1
            else:
                print(addy)
                addylist.append(addy)
            coords = [format(long - dif, '.7f'),format(lat + dif, '.7f')]
            addy = coordtoaddynvalidate(coords,postal)
            if addy == False or addy in addylist:
                times += 1
            else:
                print(addy)
                addylist.append(addy)
            coords = [format(long - dif, '.7f'),format(lat - dif, '.7f')]
            addy = coordtoaddynvalidate(coords,postal)
            if addy == False or addy in addylist:
                times += 1
            else:
                print(addy)
                addylist.append(addy)
            if len(addylist) >= addynumb:
                break
            dif = dif - 0.0002
            i += 1
        finallist = addylist[:addynumb]
        k = "\n"
        i = 0
        while len(finallist) > i: 
            print(finallist[i])
            k = k + finallist[i] + "\n"
            i += 1
            
        #insertar a csv ya en ese formato
        f = open('Accounts\ToolBox\Geocoder\Addresses.csv','a')
        f.write(k)
        f.close()
        print(str(len(finallist)) + " addys geocoded and saved in Addresses.csv!")
        return finallist

    def geocodecity():
        city = input("please input the city you want to geocode")
        country = input("please input the country where the city belongs")
        addynumb = int(input("please input the amount of addys youw would like to generate"))
        def city2cord(city,country):
            response = requests.get(
                f"https://maps.googleapis.com/maps/api/geocode/json?address={city},{country}&key={googleAPI}"
            )
            location = response.json()["results"][0]["geometry"]["location"]
            return [location["lng"], location["lat"]]


        def coordtoaddynvalidate(coords,city):
            lat = coords[0]
            long = coords[1]
            response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?latlng={long},{lat}&key={googleAPI}")
            respcity = response.json()["results"][1]["address_components"][2]["long_name"]
            addy = response.json()['results'][0]['formatted_address']
            if respcity in city:        
                return addy
            else:
                return False
        orgcoords = city2cord(city,country)
        long = orgcoords[0]
        lat = orgcoords[1]
        addylist = []
    #return addys, while len addys is mas bajo, empezar por 5 de proximidad y ir bajando 0.1 cada vez
        dif = 0.0002
        i = 0
        times = int(np.ceil(addynumb/4))
        print(times)
        while times > i:
            coords = [format(long + dif, '.7f'),format(lat + dif, '.7f')]
            addy = coordtoaddynvalidate(coords,city)
            if addy == False or addy in addylist:
                times += 1
            else:
                print(addy)
                addylist.append(addy)
            coords = [format(long + dif, '.7f'),format(lat - dif, '.7f')]
            addy = coordtoaddynvalidate(coords,city)
            if addy == False or addy in addylist:
                times += 1
            else:
                print(addy)
                addylist.append(addy)
            coords = [format(long - dif, '.7f'),format(lat + dif, '.7f')]
            addy = coordtoaddynvalidate(coords,city)
            if addy == False or addy in addylist:
                times += 1
            else:
                print(addy)
                addylist.append(addy)
            coords = [format(long - dif, '.7f'),format(lat - dif, '.7f')]
            addy = coordtoaddynvalidate(coords,city)
            if addy == False or addy in addylist:
                times += 1
            else:
                print(addy)
                addylist.append(addy)
            if len(addylist) >= addynumb:
                break
            dif = dif - 0.0002
            i += 1
        finallist = addylist[:addynumb]
        k = "\n"
        i = 0
        while len(finallist) > i: 
            print(finallist[i])
            k = k + finallist[i] + "\n"
            i += 1
            
        #insertar a csv ya en ese formato
        f = open('Accounts\ToolBox\Geocoder\Addresses.csv','a')
        f.write(k)
        f.close()
        print(str(len(finallist)) + " addys geocoded and saved in Addresses.csv!")
        return finallist






    #print(geocodeexpand(10,"via antonio gramsci 19","Ercolano","Italy",3))
    #print(geocodecity("Berlin","Germany",100))
    #print(geocodeexpand(50,"Tenor Viñas, 4","Barcelona","Spain",3))
    #geocodepostal("08021","Barcelona","Spain",50)


    print("Welcome to the Geocoder!")
    print("1. Addys from Addy")
    print("2. Addys from Postal Code")
    print("3. Addys from City")

    mode = int(input("What geocode mode do you want to use?(1-3):"))

    if mode == 1:
        clear()
        geocodeexpand()
    elif mode == 2:
        clear()
        geocodepostal()
    elif mode == 3:
        clear()
        geocodecity()

    else:
        print("Error: Wrong answer")

