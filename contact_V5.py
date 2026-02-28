#adding in the functions
def add_contact(NAME):
    NAME[ID] = {}

    NAME[ID]["First Name"] = input("first Name: ")
    NAME[ID]["Last Name"] = input("Last Name: ")
    NAME[ID]["Mobile"] = input("Mobile: ")
    NAME[ID]["Email"] = input("Email: ")
    print("\nContact added!")

def search_contact(NAME):
    search_term = input("First Name or Last Name: ")
    found = False 
    for ID in NAME:
        if search_term in NAME[ID]["First Name"] or search_term in NAME[ID]["Last Name"]:
            print("\nPerson ID:", ID)
            print("First Name:", NAME[ID]["First Name"])
            print("Last Name:", NAME[ID]["Last Name"])
            print("Mobile:", NAME[ID]["Mobile"])
            print("Email:", NAME[ID]["Email"])
            found = True
    if not found:
        print("No contacts found.")

def edit_contact(NAME):
    ID = input("Person ID: ")
    if ID in NAME:
        NAME[ID]["First Name"] = input("First Name: ")
        NAME[ID]["Last Name"] = input("Last Name: ")
        NAME[ID]["Mobile"] = input("Mobile: ")
        NAME[ID]["Email"] = input("Email: ")
        print("\nContact updated!")

#Adding a delete function to remove a contact from the dictionary
def delete_contact(NAME):
    ID = input("Person ID: ")
    if ID in NAME:
        del NAME[ID]
        print("\nContact deleted!")

#Adding a print function to display all contacts
def print_contacts(NAME):
    if not NAME:
        print("No contacts to display.")
        return
    for ID, info in NAME.items():
        print("\nPerson ID:", ID)
        print("First Name:", info["First Name"])
        print("Last Name:", info["Last Name"])
        print("Mobile:", info["Mobile"])
        print("Email:", info["Email"])

#Main program
NAME = {}

for i in range (2):
    ID = input("\n\nPerson ID: ")
    NAME[ID] = {}

    First = input("\n\nFirst Name: ")
    NAME[ID]["First Name"] = First

    Last = input("\n\nLast Name: ")
    NAME[ID]["Last Name"] = Last

    Mobile = input("\n\nMobile: ")
    NAME[ID]["Mobile"] = Mobile

    Email = input("\n\nEmail: ")
    NAME[ID]["Email"] = Email

print(NAME)

#Menu loop to add, search, edit, delete, print, or quit
while True:
    choice = input("Do you want to: (a)dd a contact, (S)earch a contact, (e)dit a contact, (d)elete a contact, (p)rint all contacts, or (q)uit? ")

#Using the functions instead of repeating code
    if choice == "a":
        add_contact(NAME)

#Changing the search function to search by first name or last name instead of ID"
    elif choice == "s":
        search_contact(NAME)

    elif choice == "e":
        edit_contact(NAME)

    elif choice == "d":
        delete_contact(NAME)

    elif choice == "p":
        print_contacts(NAME)

#Adding a quit option to exit the program
    elif choice == "q":
        print("Goodbye!")
        break

print("==================================")