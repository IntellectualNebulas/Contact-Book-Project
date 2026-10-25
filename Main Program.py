import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = "/home/ciaran/Downloads/Contact Book/Contacts.csv"

def readfile():

    # Open the CSV file
    with open(FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)

        # Empty lists to store column values
        Number = []
        Forename = []
        Surname = []

        # Iterating over each row
        for row in reader:
            Number.append(row['Number'])
            Forename.append(row['Forename'])
            Surname.append(row['Surname'])

    return Number,Forename,Surname

def addcontact(Number,Forename,Surname):

    NewNum = ""
    NewForename = ""
    NewSurname = ""

    while len(NewNum) < 13:

        NewNum = input(print("Enter the phone number: "))

        if len(NewNum) < 13:
                    
            NewNum = input(print("Re-Enter a valid phone number: "))

        else:

            Number.append(NewNum)


        NewForename = input(print("Enter the new Forename: "))
        Forename.append(NewForename)

        NewSurname = input(print("Enter the new Surname: "))
        Surname.append(NewSurname)


    return Number,Forename,Surname

def updateFile(Number,Forename,Surname):

    with open(FILE_PATH, 'w', newline='') as file:
        
        fieldnames = ['Number', 'Forename', 'Surname']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(Number,Forename,Surname)

def displaylist(Number,Forename,Surname):

    pos = 0

    for value in Number:

        print(Forename[pos])
        print(Surname[pos])
        print(Number[pos])
        print("--------------")

        pos += 1

#---- Main System

Number, Forename, Surname = readfile() 

Con = True

while Con == True:

    Dec = input(print("Input an option from the list: 'Add Contact', 'Display' "))

    if Dec == "Add Contact":

        Number, Forename, Surname = addcontact(Number, Forename, Surname) 
        updateFile(Number, Forename, Surname) 

    elif Dec == "Display":

        displaylist(Number,Forename,Surname)

    Awn = input(print("Do you wish to continue?"))

    if Awn == "Yes":

        Con = True

    else:
        
        Con = False
        print("Goodbye!")