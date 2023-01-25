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


def jignames():
    print("Welcome to the name jigger")
    allfirstnames = []
    alllastnames = []
    allfullnames = []

    firstname = str(input("what is your first name"))
    firstname = firstname.lower()
    lastname = str(input("what is your last name"))
    lastname = lastname.lower()


    #firstnames jig
    firstnamelist = list(firstname)
    lastnamelist = list(lastname)

    numbofcharf = len(firstnamelist)
    numbofcharl = len(lastnamelist)



    #lista de los jigs puros, incluyendo el nombre no jiggeado
    purefirst = [firstname.capitalize()]

    #joggs empiezan aqui

    #funcion para jiggear nombre
    def fnamejig(ogchar, subchar):
        Jignum = 0
        while numbofcharf > Jignum:
            firstnamelist1 = list(firstname)
            if firstnamelist[Jignum] == ogchar:
                #sustituir la og por la sub y meterla en la lista
                firstnamelist1.pop(Jignum)
                firstnamelist1.insert(Jignum, subchar)
                purefirst.append("".join(firstnamelist1).capitalize())
            Jignum += 1

    #extraer lista de los jigs de las siguientes letras(letra og, letra substituta)
    fnamejig("c", "k")
    fnamejig("c", "q")
    fnamejig("k", "c")
    fnamejig("k", "q")
    fnamejig("q", "c")
    fnamejig("q", "k")
    fnamejig("o", "0")
    fnamejig("i", "y")
    fnamejig("y", "i")
    fnamejig("b", "v")
    fnamejig("v", "b")
    fnamejig("u", "w")
    fnamejig("w", "u")
    #zz por z

    #usar lista de todos los firstanmes jigged puramente y jigg duplicados y meterlos en allfirstnames
    numbofnames = len(purefirst)
    Jignamesnum = 0
    while numbofnames > Jignamesnum:
        Jignum = 0
        while numbofcharf > Jignum:
            #coje el nombre
            firstnamelist1 = list(purefirst[Jignamesnum])
            #lo jiggea duplicando
            firstnamelist1.insert(Jignum, firstnamelist[Jignum])
            allfirstnames.append("".join(firstnamelist1).capitalize())

            Jignum += 1
        Jignamesnum += 1
        
    #lastname apmpieza
    #lista de los jigs puros, incluyendo el nombre no jiggeado
    purelast = [lastname.capitalize()]

    #funcion para jiggear nombre
    def lnamejig(ogchar, subchar):
        Jignum = 0
        while numbofcharl > Jignum:
            lastnamelist1 = list(lastname)
            if lastnamelist[Jignum] == ogchar:
                #sustituir la o por 0 y meterla en la lista
                lastnamelist1.pop(Jignum)
                lastnamelist1.insert(Jignum, subchar)
                purelast.append("".join(lastnamelist1).capitalize())
            Jignum += 1

    #extraer lista de los jigs de los nombres de las siguientes letras(letra og, letra substituta)
    lnamejig("c", "k")
    lnamejig("c", "q")
    lnamejig("k", "c")
    lnamejig("k", "q")
    lnamejig("q", "c")
    lnamejig("q", "k")
    lnamejig("o", "0")
    lnamejig("i", "y")
    lnamejig("y", "i")
    lnamejig("b", "v")
    lnamejig("v", "b")
    lnamejig("u", "w")
    lnamejig("w", "u")



    #Hacer Jig duplicado para el apellido

    numbofnames = len(purelast)
    Jignamesnum = 0
    while numbofnames > Jignamesnum:
        Jignum = 0
        while numbofcharl > Jignum:
            #coje el nombre
            lastnamelist1 = list(purelast[Jignamesnum])
            #lo jiggea duplicando
            lastnamelist1.insert(Jignum, lastnamelist[Jignum])
            alllastnames.append("".join(lastnamelist1).capitalize())



            Jignum += 1
        Jignamesnum += 1



    #combinar nombres
    firstandlastlist = [allfirstnames, alllastnames]
    combination = [p for p in itertools.product(*firstandlastlist)]

    i = 0
    while len(combination) > i :
        removenonalpha = str(combination[i])
        removenonalpha = re.sub(r'[^a-zA-Z\s]', '', removenonalpha)
        allfullnames.append(removenonalpha)
        i += 1

    #how many times do you want to jig your name, it can be igged this many times
    timesjig = input("How many times do you want to jig your name?(your name can be jigged " + str(len(allfullnames)) + " times)")

    #Poner list de nombres que quiere el user en orden y no random

    userlist = []
    i = 0
    while int(timesjig) > i :
        userlist.append(allfullnames[i])
        i += 1



    k = "\n"
    i = 0
#poner los names a formato csv
    while len(userlist) > i:
        print(userlist[i])
        namedivided = str(userlist[i]).split(" ")
        k = k + userlist[i] + ", " +  namedivided[0] + ", " +  namedivided[1] + "\n"
        i += 1


    #insertar a csv ya en ese formato
    f = open(r'Accounts\ToolBox\Names\Namejigs.csv','a')
    f.write(k)
    f.close()
    print("Names succefully saved in Namejigs.csv")




