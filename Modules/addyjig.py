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


def addressjigger():

    def soft():
        #convertir el csv a una lista con listas dentro de cada row
        with open(r'Accounts\ToolBox\Addresses\Pureaddys.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Pass reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)
  
        #empezar por el row 1 porque el 0 es el titulo y se ignora
        jigtimes = int(input("How many jigs do you want per addy"))
        z = 1
        while len(list_of_rows) > z: 
            letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            randletters = letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)]

            #todos los jigs de las distintas palabras de la street en estas listas
            wordstreet1 = []
            wordstreet2 = []
            wordstreet3 = []
            wordstreet4 = []
            wordstreet5 = []

            #user input
            streetname = str(list_of_rows[z][0])
            streetnum = str(list_of_rows[z][1])
            apartment = str(list_of_rows[z][2])

            streetlist = streetname.split()


            i = 0
            #loop para jiggear primera, segunda, tercera.. palabra de la street
            while len(streetlist) > i:
                #extraer palabra para el doble jig
                wordtojig = list(streetlist[i])
                k = 0
                vecesjig = len(wordtojig)
                while vecesjig > k:
                    wordtojig = list(streetlist[i])
                    wordtojig.insert(k, wordtojig[k])
                    #unir a la lista de jigs de la primera, segunda o tercera palabra para hacer listas separadas con las palabras 
                    if i == 0:
                        wordstreet1.append("".join(wordtojig))
                    elif i == 1:
                        wordstreet2.append("".join(wordtojig))
                    elif i == 2:
                        wordstreet3.append("".join(wordtojig))
                    elif i == 3:
                        wordstreet4.append("".join(wordtojig))
                    else:
                        wordstreet5.append("".join(wordtojig))

                    k +=1
                i += 1

            streetnamejigs = []
            #combinacion de las palabras jigged random
            if len(wordstreet2) == 0:
            #trabajar con una lista
                streetnamejigs = wordstreet1

            elif len(wordstreet3) == 0:
                firstandlastlist = [wordstreet1, wordstreet2]
                combination = [p for p in itertools.product(*firstandlastlist)]
                while len(combination) > i :
                    removenonalpha = str(combination[i])
                    removenonalpha = re.sub(r'[^a-zA-Z\s]', '', removenonalpha)
                    streetnamejigs.append(removenonalpha)
                    i += 1
            elif len(wordstreet4) == 0:
                firstandlastlist = [wordstreet1, wordstreet2, wordstreet3]
                combination = [p for p in itertools.product(*firstandlastlist)] 
                while len(combination) > i :
                    removenonalpha = str(combination[i])
                    removenonalpha = re.sub(r'[^a-zA-Z\s]', '', removenonalpha)
                    streetnamejigs.append(removenonalpha)
                    i += 1

            else:
                firstandlastlist = [wordstreet1, wordstreet2, wordstreet3, wordstreet4, wordstreet5]
                combination = [p for p in itertools.product(*firstandlastlist)]
                while len(combination) > i :
                    removenonalpha = str(combination[i])
                    removenonalpha = re.sub(r'[^a-zA-Z\s]', '', removenonalpha)
                    streetnamejigs.append(removenonalpha)
                    i += 1

            i = 0


            #lista de street name jigged
            userjigs = []
            i = 0
            while jigtimes > i:
                userjigs.append(streetnamejigs[random.randint(0, len(streetnamejigs) - 1)])
                i += 1



            #añadir tres letras random
            i = 0
            while jigtimes > i:
                name3rand =(letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + " " + userjigs[i] )
                userjigs.pop(i)
                userjigs.insert(i, name3rand)
                i += 1

            #jiggear un poco numero
            i = 0
            while jigtimes > i:
                name3rand = (userjigs[i] + ", " + str(streetnum))
                userjigs.pop(i)
                userjigs.insert(i, name3rand)
                i += 1

            #añadir piso si tiene
            i = 0
            while jigtimes > i:
                if len(list(apartment)) != 0:
                    namewapart =(userjigs[i] + ", " + apartment)
                    userjigs.pop(i)
                    userjigs.insert(i, namewapart)
                i += 1

            i = 0
            while len(userjigs) > i:
                finaladdy = str(userjigs[i])
                with open('Accounts\ToolBox\Addresses\Addyjigs.csv', 'a') as f:
                    f.write("\n")
                    f.write(finaladdy)
                with open('Accounts\ToolBox\Addresses\Addyjigs.txt', 'a') as f:
                    f.write("\n")
                    f.write(finaladdy)
                print(finaladdy)
                i +=1
            z += 1
        print("Jigs succefully saved in Addyjigs.csv and Addyjigs.txt")

    def medium():
        #convertir el csv a una lista con listas dentro de cada row
        with open(r'Accounts\ToolBox\Addresses\Pureaddys.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Pass reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)
  
        #empezar por el row 1 porque el 0 es el titulo y se ignora
        jigtimes = int(input("How many jigs do you want per addy"))
        z = 1
        while len(list_of_rows) > z: 
            letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            randletters = letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)]

            #todos los jigs de las distintas palabras de la street en estas listas
            wordstreet1 = []
            wordstreet2 = []
            wordstreet3 = []
            wordstreet4 = []
            wordstreet5 = []

            #user input
            streetname = str(list_of_rows[z][0])
            streetnum = str(list_of_rows[z][1])
            apartment = str(list_of_rows[z][2])

            streetlist = streetname.split()


            i = 0
            #loop para jiggear primera, segunda, tercera.. palabra de la street
            while len(streetlist) > i:
                #extraer palabra para el doble jig
                wordtojig = list(streetlist[i])
                k = 0
                vecesjig = len(wordtojig)
                while vecesjig > k:
                    wordtojig = list(streetlist[i])
                    wordtojig.insert(k, wordtojig[k])
                    #unir a la lista de jigs de la primera, segunda o tercera palabra para hacer listas separadas con las palabras 
                    if i == 0:
                        wordstreet1.append("".join(wordtojig))
                    elif i == 1:
                        wordstreet2.append("".join(wordtojig))
                    elif i == 2:
                        wordstreet3.append("".join(wordtojig))
                    elif i == 3:
                        wordstreet4.append("".join(wordtojig))
                    else:
                        wordstreet5.append("".join(wordtojig))

                    k +=1
                i += 1

            streetnamejigs = []
            #combinacion de las palabras jigged random
            if len(wordstreet2) == 0:
            #trabajar con una lista
                streetnamejigs = wordstreet1

            elif len(wordstreet3) == 0:
                firstandlastlist = [wordstreet1, wordstreet2]
                combination = [p for p in itertools.product(*firstandlastlist)]
                while len(combination) > i :
                    removenonalpha = str(combination[i])
                    removenonalpha = re.sub(r'[^a-zA-Z\s]', '', removenonalpha)
                    streetnamejigs.append(removenonalpha)
                    i += 1
            elif len(wordstreet4) == 0:
                firstandlastlist = [wordstreet1, wordstreet2, wordstreet3]
                combination = [p for p in itertools.product(*firstandlastlist)] 
                while len(combination) > i :
                    removenonalpha = str(combination[i])
                    removenonalpha = re.sub(r'[^a-zA-Z\s]', '', removenonalpha)
                    streetnamejigs.append(removenonalpha)
                    i += 1

            else:
                firstandlastlist = [wordstreet1, wordstreet2, wordstreet3, wordstreet4, wordstreet5]
                combination = [p for p in itertools.product(*firstandlastlist)]
                while len(combination) > i :
                    removenonalpha = str(combination[i])
                    removenonalpha = re.sub(r'[^a-zA-Z\s]', '', removenonalpha)
                    streetnamejigs.append(removenonalpha)
                    i += 1

            i = 0


            #lista de street name jigged
            userjigs = []
            i = 0
            while jigtimes > i:
                streetname = streetnamejigs[random.randint(0, len(streetnamejigs) - 1)]
                namelisted = list(streetname)
                namelisted.insert(random.randint(1, len(namelisted)-1), ".")
                namelistedstr = "".join(namelisted)
                userjigs.append(namelistedstr)
                i += 1


            #añadir tres letras random
            i = 0
            while jigtimes > i:
                name3rand =(letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + " " + userjigs[i] )
                userjigs.pop(i)
                userjigs.insert(i, name3rand)
                i += 1

            #jiggear un poco numero
            i = 0
            while jigtimes > i:
                name3rand = (userjigs[i] + ", " + str(streetnum))
                userjigs.pop(i)
                userjigs.insert(i, name3rand)
                i += 1

            #añadir piso si tiene
            i = 0
            while jigtimes > i:
                if len(list(apartment)) != 0:
                    namewapart =(userjigs[i] + ", " + apartment)
                    userjigs.pop(i)
                    userjigs.insert(i, namewapart)
                i += 1

            i = 0
            while len(userjigs) > i:
                finaladdy = str(userjigs[i])
                with open('Accounts\ToolBox\Addresses\Addyjigs.csv', 'a') as f:
                    f.write("\n")
                    f.write(finaladdy)
                with open('Accounts\ToolBox\Addresses\Addyjigs.txt', 'a') as f:
                    f.write("\n")
                    f.write(finaladdy)
                print(finaladdy)
                i +=1
            z += 1
        print("Jigs succefully saved in Addyjigs.csv and Addyjigs.txt")

    def hard():
        #convertir el csv a una lista con listas dentro de cada row
        with open(r'Accounts\ToolBox\Addresses\Pureaddys.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Pass reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)
  
        #empezar por el row 1 porque el 0 es el titulo y se ignora
        jigtimes = int(input("How many jigs do you want per addy"))
        z = 1
        while len(list_of_rows) > z: 
            letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            randletters = letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)]

            #todos los jigs de las distintas palabras de la street en estas listas
            wordstreet1 = []
            wordstreet2 = []
            wordstreet3 = []
            wordstreet4 = []
            wordstreet5 = []

            #user input
            streetname = str(list_of_rows[z][0])
            streetnum = str(list_of_rows[z][1])
            apartment = str(list_of_rows[z][2])

            streetlist = streetname.split()


            i = 0
            #loop para jiggear primera, segunda, tercera.. palabra de la street
            while len(streetlist) > i:
                #extraer palabra para el doble jig
                wordtojig = list(streetlist[i])
                k = 0
                vecesjig = len(wordtojig)
                while vecesjig > k:
                    wordtojig = list(streetlist[i])
                    wordtojig.insert(k, wordtojig[k])
                    #unir a la lista de jigs de la primera, segunda o tercera palabra para hacer listas separadas con las palabras 
                    if i == 0:
                        wordstreet1.append("".join(wordtojig))
                    elif i == 1:
                        wordstreet2.append("".join(wordtojig))
                    elif i == 2:
                        wordstreet3.append("".join(wordtojig))
                    elif i == 3:
                        wordstreet4.append("".join(wordtojig))
                    else:
                        wordstreet5.append("".join(wordtojig))

                    k +=1
                i += 1

            streetnamejigs = []
            #combinacion de las palabras jigged random
            if len(wordstreet2) == 0:
            #trabajar con una lista
                streetnamejigs = wordstreet1

            elif len(wordstreet3) == 0:
                firstandlastlist = [wordstreet1, wordstreet2]
                combination = [p for p in itertools.product(*firstandlastlist)]
                while len(combination) > i :
                    removenonalpha = str(combination[i])
                    removenonalpha = re.sub(r'[^a-zA-Z\s]', '', removenonalpha)
                    streetnamejigs.append(removenonalpha)
                    i += 1
            elif len(wordstreet4) == 0:
                firstandlastlist = [wordstreet1, wordstreet2, wordstreet3]
                combination = [p for p in itertools.product(*firstandlastlist)] 
                while len(combination) > i :
                    removenonalpha = str(combination[i])
                    removenonalpha = re.sub(r'[^a-zA-Z\s]', '', removenonalpha)
                    streetnamejigs.append(removenonalpha)
                    i += 1

            else:
                firstandlastlist = [wordstreet1, wordstreet2, wordstreet3, wordstreet4, wordstreet5]
                combination = [p for p in itertools.product(*firstandlastlist)]
                while len(combination) > i :
                    removenonalpha = str(combination[i])
                    removenonalpha = re.sub(r'[^a-zA-Z\s]', '', removenonalpha)
                    streetnamejigs.append(removenonalpha)
                    i += 1

            i = 0


            #lista de street name jigged
            userjigs = []
            i = 0
            while jigtimes > i:
                streetname = streetnamejigs[random.randint(0, len(streetnamejigs) - 1)]
                namelisted = list(streetname)
                namelisted.insert(random.randint(1, len(namelisted)-1), ".")
                namelisted.insert(random.randint(1, len(namelisted)-1), ".")
                namelistedstr = "".join(namelisted)
                userjigs.append(namelistedstr)
                i += 1


            #añadir tres letras random
            i = 0
            while jigtimes > i:
                name3rand =(letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + " " + userjigs[i] )
                userjigs.pop(i)
                userjigs.insert(i, name3rand)
                i += 1

            #jiggear un poco numero
            i = 0
            while jigtimes > i:
                infront = random.randint(0, 1)
                if infront == 0:
                    name3rand = (userjigs[i] + ", " + letterlist[random.randint(0, 25)] + str(streetnum))
                    userjigs.pop(i)
                    userjigs.insert(i, name3rand)
                else:
                    name3rand = (userjigs[i] + ", " + str(streetnum) + letterlist[random.randint(0, 25)])
                    userjigs.pop(i)
                    userjigs.insert(i, name3rand)  

                i += 1

            #añadir piso si tiene
            i = 0
            while jigtimes > i:
                if len(list(apartment)) != 0:
                    namewapart =(userjigs[i] + ", " + apartment)
                    userjigs.pop(i)
                    userjigs.insert(i, namewapart)
                i += 1

            i = 0
            while len(userjigs) > i:
                finaladdy = str(userjigs[i])
                with open('Accounts\ToolBox\Addresses\Addyjigs.csv', 'a') as f:
                    f.write("\n")
                    f.write(finaladdy)
                with open('Accounts\ToolBox\Addresses\Addyjigs.txt', 'a') as f:
                    f.write("\n")
                    f.write(finaladdy)
                print(finaladdy)
                i +=1
            z += 1
        print("Jigs succefully saved in Addyjigs.csv and Addyjigs.txt")

    def abcjig():
        #convertir el csv a una lista con listas dentro de cada row
        with open(r'Accounts\ToolBox\Addresses\Pureaddys.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Pass reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)
  
        #empezar por el row 1 porque el 0 es el titulo y se ignora
        jigtimes = int(input("How many jigs do you want per addy"))
        z = 1
        while len(list_of_rows) > z:

    #module para jigg con tres letras
            letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

            randletters = letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)]

            streetname = str(list_of_rows[z][0])
            streetnum = str(list_of_rows[z][1])
            apartment = str(list_of_rows[z][2])
            

            jiglist = []

    #preguntar si quieren space between the abc jig and the steet name

            i = 0
            while jigtimes > i:
                jiglist.append(letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + " " + streetname + ", " + streetnum + ", " + apartment)
                i += 1

    #convertir lista a CSV mode con dos columnas
            i = 0
            while jigtimes > i:
                finaladdy = str(jiglist[i])
                with open('Accounts\ToolBox\Addresses\Addyjigs.csv', 'a') as f:
                    f.write("\n")
                    f.write(finaladdy)
                with open('Accounts\ToolBox\Addresses\Addyjigs.txt', 'a') as f:
                    f.write("\n")
                    f.write(finaladdy)
                print(finaladdy)
                i +=1
            z += 1
    #insertar a csv ya en ese formato
        print("Jigs succefully saved in Addyjigs.csv and Addyjigs.txt")

    def numericjig():
        jigtimes = int(input("How many jigs do you want per addy"))
        m = ""
        letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        randletters = letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)]



        with open(r'Accounts\ToolBox\Addresses\Pureaddys.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Pass reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)


        i = 1
        while len(list_of_rows) > i:
            streetlist = []
            f = 0
            while jigtimes > f:
                #trabajar con el primer row
                row = list_of_rows[i] 
                wordlist = row[0].split()
                wordjigs = []
                k = 0
                finalword = ""
                while len(wordlist) > k:
                    #trabjar con la palabra exacta
                    word = wordlist[k]
                    #convertir palabra a lista
                    word = list(word)

                    word.insert(random.randint(0, len(word)-1), str(random.randint(0, 9)))
                    finalword = finalword + "".join(word) + " "
                    k += 1
                finalword = finalword[:-1]
                print(letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + " " + finalword + ", " + list_of_rows[i][1] + ", " + list_of_rows[i][2])
                m = m + "\n" + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + " " + finalword + ", " + list_of_rows[i][1] + ", " + list_of_rows[i][2]
                f += 1
            i += 1



        with open('Accounts\ToolBox\Addresses\Addyjigs.csv', 'a') as f:
            f.write(m)
        with open('Accounts\ToolBox\Addresses\Addyjigs.txt', 'a') as f:
            f.write(m)

        print("Jigs succefully saved in Addyjigs.csv and Addyjigs.txt")

    def nikejig():
        jigtimes = int(input("How many jigs do you want per addy"))
        m = ""
        letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        randletters = letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)]
        comaordot = [",", "."]



        with open(r'Accounts\ToolBox\Addresses\Pureaddys.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Pass reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)


        i = 1
        while len(list_of_rows) > i:
            streetlist = []
            f = 0
            while jigtimes > f:
                #trabajar con el primer row
                row = list_of_rows[i] 
                wordlist = row[0].split()
                wordjigs = []
                k = 0
                finalword = ""
                while len(wordlist) > k:
                    #trabjar con la palabra exacta
                    word = wordlist[k]
                    #convertir palabra a lista
                    word = list(word)

                    #extraer el simbolo que se pondra en la addy
                    jigsymbol = ""
                    l = 0
                    while random.randint(2, 4) > l:
                        jigsymbol = random.choice(comaordot)
                        word.insert(random.randint(1, len(word)-1), jigsymbol)
                        l += 1


                    finalword = finalword + "".join(word) + " "

            
                    k += 1
                finalword = finalword[:-1]
                if len(list(list_of_rows[i][1])) == 0:
                    print(letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + " " + finalword)
                    m = m + "\n" + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + " " + finalword
                elif len(list(list_of_rows[i][2])) == 0:
                    print(letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + " " + finalword + ", " + list_of_rows[i][1])
                    m = m + "\n" + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + " " + finalword + ", " + list_of_rows[i][1]
                else:
                    print(letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + " " + finalword + ", " + list_of_rows[i][1] + ", " + list_of_rows[i][2])
                    m = m + "\n" + letterlist[random.randint(0, 25)] + letterlist[random.randint(0, 25)] + " " + finalword + ", " + list_of_rows[i][1] + ", " + list_of_rows[i][2]

                f += 1
            i += 1




        with open('Accounts\ToolBox\Addresses\Addyjigs.txt', 'a') as f:
            f.write(m)

        print("Jigs succefully saved in Addyjigs.txt")


    print("Welcome to the address jigger")
    print("1. Soft")
    print("2. Medium")
    print("3. Hard")
    print("4. ABC jigger")
    print("5. Numeric jigger")
    print("6. Nike\SNKRS jigger")

    Jigmode = int(input("What jig mode do you want to use?(1-2):"))

    if Jigmode == 1:
        soft()
    elif Jigmode == 2:
        medium()
    elif Jigmode == 3:
        hard()
    elif Jigmode == 4:
        abcjig()
    elif Jigmode == 5:
        numericjig()
    elif Jigmode == 6:
        nikejig()
    else:
        print("Error: Wrong answer")

