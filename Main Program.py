import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = "Contacts.csv"

def readfile():

    import pandas as pd

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
        file.close()

        # Collecting data for the file update using pandas
        update_data = pd.read_csv('Contacts.csv')

    return Number,Forename,Surname, update_data
    

def addcontact(Number,Forename,Surname,update_data):

    import pandas as pd

    NewNum = ""
    NewForename = ""
    NewSurname = ""
    NewRow = []

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

    return Number,Forename,Surname, update_data

def updateFile(update_data):

    import pandas

    header = ["Number","Forename","Surname"]

    row_data = update_data

    data = pandas.DataFrame(row_data, columns= header)
    data.to_csv('my_file.csv', index = False)

def displaylist(Number,Forename,Surname):

    pos = 0

    for value in Number:

        print(Forename[pos])
        print(Surname[pos])
        print(Number[pos])
        print("--------------")

        pos += 1


#---- Main System ----#

Number, Forename, Surname, update_data = readfile() 

Con = True

while Con == True:

    Dec = input(print("Input an option from the list: 'Add Contact', 'Display' "))

    if Dec == "Add Contact":

        Number, Forename, Surname = addcontact(Number, Forename, Surname, update_data) 
        updateFile(update_data) 

    elif Dec == "Display":

        displaylist(Number,Forename,Surname)

    Awn = input(print("Do you wish to continue?"))

    if Awn == "Yes":

        Con = True

    else:
        
        Con = False
        print("Goodbye!")