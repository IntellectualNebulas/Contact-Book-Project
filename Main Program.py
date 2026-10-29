import csv # Used so the CSV File functions work
from pathlib import Path # Used for file path

# Directory for the main file
BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = "File/Contacts.csv"

def inputvalidation():

    "All the lists used for input validation"

    "Lists used for 'Con'"
    acc_val_foryes = ["yes","y","yeah","yea"]
    acc_val_forno = ["no","n","nope","nah"]

    "Lists used for 'Awn'"
    acc_val_addcon = ["add contact","add","a"]
    acc_val_dis = ["display","d"]

    return acc_val_foryes, acc_val_forno, acc_val_addcon, acc_val_dis

def readfile():

    "Reads in the 'Contacts.csv' file"

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
        read_data = pd.read_csv('File/Contacts.csv')

    return Number,Forename,Surname, read_data

def addcontact(Number,Forename,Surname,read_data):

    "Adds a new value to the end of the data frame that then later gets printed to the 'Contacts.csv' file"

    "LISTS CODE"

    import pandas

    # Local Variable so the Len command works immediately
    NewNum = ""

    # Validates the length of the phone number
    while len(NewNum) != 11:

        NewNum = input("Enter the phone number: ")

        if len(NewNum) != 11:
                    
            NewNum = input("Re-Enter a valid phone number: ")

        else: # Only if the phone number is not 13 characters long (INCLUDING SPACES)

            break

    # Getting the new forename to be added
    NewForename = input("Enter the new Forename: ")

    # Getting the new surname to be added 
    NewSurname = input("Enter the new Surname: ")

    "PANDAS CODE"
        
    import pandas as pd

    # The new row to be appended, is made into a small dataframe so it can be appended to another dataframe
    new_row = pd.DataFrame([{
        "Number": NewNum,
        "Forename": NewForename,
        "Surname": NewSurname
    }])

    # Combining the new row and the existing data already read in to be a updated data frame that can be written to the file
    update_data = pd.concat([read_data, new_row], ignore_index=True) # Appends the new_row data to the end of the read_data dataframe. Essentially like appending a list and a new value being added to the end

    return Number,Forename,Surname, update_data

def updateFile(update_data):

    "Writes the 'update_data' data frame to 'Contacts.csv'"

    import pandas

    # File column headings
    header = ["Number","Forename","Surname"]

    # Writing the file with appropiate layout and path
    data = pandas.DataFrame(update_data, columns= header)
    data.to_csv(('File/Contacts.csv'), index = False)

def displaylist(read_data):
    "Prints the data frame created in the readfile function"
    print(read_data)


"---- Main System ----"

acc_val_foryes, acc_val_forno, acc_val_addcon, acc_val_dis = inputvalidation() # Activates the input validation procedure so the lists are available

Con = True # Sets Continue to true so the program actually runs

while Con == True: # Program runs while the user chooses too

    Dec = input("Input an option from the list: 'Add Contact', 'Display': ").strip().lower() # strip and lower validate the text

    while Dec not in acc_val_addcon or Dec not in acc_val_dis: # Loops while the decision is not valid

        if Dec in acc_val_addcon: # If Add Contact == to a string in the accepted Add Contact items list

            Number, Forename, Surname, read_data = readfile() # Activates the readfile function to read the 'Contacts.csv' file
            Number, Forename, Surname, update_data = addcontact(Number, Forename, Surname, read_data) # Activates the 'addcontact' function so the user can add a new contact
            updateFile(update_data) # Activates the update File function
            break

        elif Dec in acc_val_dis: # If Decision == to a string in the accepted Display items list

            Number, Forename, Surname, read_data = readfile() # Activates the readfile function to read the 'Contacts.csv' file
            displaylist(read_data) # Activates the displaylist procedure to display the read-in data
            break 

        else: # Repeats the input till an appropiate value is received

            Dec = input("Re-Input an option from the list: 'Add Contact', 'Display': ").strip().lower()

    Awn = input("Do you wish to continue?: ").strip().lower() # Finding out if the user wants to quit the program or not

    while Awn not in acc_val_foryes or Awn not in acc_val_forno: # Loops while the Continue is not valid

        if Awn in acc_val_foryes: # Repeats the program so the user can either add another contact, delete one, etc
            Con = True
            break

        elif Awn in acc_val_forno: # Quits the program
            Con = False
            break

        else: # Repeats the input till an appropiate value is received
            Awn = input("Please enter a valid operator(Eg, 'Y' or 'N'): ").strip().lower()