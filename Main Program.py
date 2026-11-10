import csv # Used so the CSV File functions work
from pathlib import Path # Used for file path

# Directory for the main file
BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = "src/Contacts.csv"

def inputvalidation():

    "All the lists used for input validation"

    #Lists used for 'Continue'
    AcceptedYes = ["yes","y","yeah","yea"]
    AcceptedNo = ["no","n","nope","nah"]

    #Lists used for 'UserInputContinue'
    AddContactList = ["add contact","add","a"]
    DeleteContactList = ["delete contact", "delete", "remove","bin","del","r"]
    DisplayList = ["display", "view","d","v"]

    return AcceptedYes, AcceptedNo, AddContactList, DisplayList, DeleteContactList

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
        read_data = pd.read_csv('src/Contacts.csv')

    return Number,Forename,Surname, read_data

def deletecontact(Number,read_data):

    import pandas as pd

    "Deletes a value from the list"

    "Local Variables"

    length = len(read_data) # Gets length of list (didnt work in loop for some reason)
    position = 0
    found = False

    Deleted_value = input("Enter the phone number of the contact you want deleted: ") # Getting the number of the contact being removed, basically a Primary Key

    while found == False:

        for i in range(length): # For Loop

            if Number[i] == Deleted_value: # If the phone number = deleted valud
                position = i # Saving the position of the removed number
                update_data = read_data.drop(position) # New Data Table is the old data table with the indexed row removed
                found = True
                break
                
            else:
                found = False

        if found == False:
            Deleted_value = input("Enter the phone number of the contact you want deleted: ") # Input Validating the number entered

    return update_data

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
    data.to_csv(('src/Contacts.csv'), index = False)

def displaylist(read_data):

    "Prints the data frame created in the readfile function"
    print(read_data)


"---- Main System ----"

AcceptedYes, AcceptedNo, AddContactList, DisplayList, DeleteContactList = inputvalidation() # Activates the input validation procedure so the lists are available

Continue = True # Sets Continue to true so the program actually runs

while Continue == True: # Program runs while the user chooses too

    UserDescison = input("Input an option from the list: 'Add Contact', 'Delete Contact', 'Display': ").strip().lower() # strip and lower validate the text

    while UserDescison not in AddContactList or UserDescison not in DeleteContactList or UserDescison not in DisplayList: # Loops while the decision is not valid

        if UserDescison in AddContactList: # If Add Contact == to a string in the accepted Add Contact items list

            Number, Forename, Surname, read_data = readfile() # Activates the readfile function to read the 'Contacts.csv' file
            Number, Forename, Surname, update_data = addcontact(Number, Forename, Surname, read_data) # Activates the 'addcontact' function so the user can add a new contact
            updateFile(update_data) # Activates the update File function
            break

        elif UserDescison in DeleteContactList: # If Decision == to a string in the accepted Delete Contact list

            Number, Forename, Surname, read_data = readfile() # Activates the readfile function to read the 'Contacts.csv' file
            update_data = deletecontact(Number,read_data) # Activates the 'DeleteFile' function to delete a chosen contact
            updateFile(update_data)
            break 

        elif UserDescison in DisplayList: # If Decision == to a string in the accepted Display data list

            Number, Forename, Surname, read_data = readfile() # Activates the readfile function to read the 'Contacts.csv' file
            displaylist(read_data) # Activates the 'displaylist' procedure to display the read-in data
            break 

        else: # Repeats the input till an appropiate value is received

            UserDescison = input("Input an option from the list: 'Add Contact', 'Delete Contact', 'Display': ").strip().lower()

    UserInputContinue = input("Do you wish to continue?: ").strip().lower() # Finding out if the user wants to quit the program or not

    while UserInputContinue not in AcceptedYes or UserInputContinue not in AcceptedNo: # Loops while the Continue is not valid

        if UserInputContinue in AcceptedYes: # Repeats the program so the user can either add another contact, delete one, etc
            Continue = True
            break

        elif UserInputContinue in AcceptedNo: # Quits the program
            Continue = False
            break

        else: # Repeats the input till an appropiate value is received
            UserInputContinue = input("Please enter a valid operator(Eg, 'Y' or 'N'): ").strip().lower()