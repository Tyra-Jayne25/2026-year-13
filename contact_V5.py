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
    if choice == "a":
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

#Changing the search function to search by first name or last name instead of ID"
    elif choice == "s":
        search_term = input("\n\nFirst Name or Last Name: ")
        found = False 
        for ID in NAME:
            if search_term in NAME[ID]["First Name"] or search_term in NAME[ID]["Last Name"]:
                print("\n\nPerson ID:", ID)
                print("First Name:", NAME[ID]["First Name"])
                print("Last Name:", NAME[ID]["Last Name"])
                print("Mobile:", NAME[ID]["Mobile"])
                print("Email:", NAME[ID]["Email"])
                found = True
        if not found:
            print("No contacts found.")

    elif choice == "e":
        ID = input("\n\nPerson ID: ")
        First = input("\n\nFirst Name: ")
        NAME[ID]["First Name"] = First

        Last = input("\n\nLast Name: ")
        NAME[ID]["Last Name"] = Last

        Mobile = input("\n\nMobile: ")
        NAME[ID]["Mobile"] = Mobile

        Email = input("\n\nEmail: ")
        NAME[ID]["Email"] = Email

    elif choice == "d":
        ID = input("\n\nPerson ID: ")
        del NAME[ID]

    elif choice == "p":
        for ID in NAME:
            print("\n\nPerson ID:", ID)
            print("First Name:", NAME[ID]["First Name"])
            print("Last Name:", NAME[ID]["Last Name"])
            print("Mobile:", NAME[ID]["Mobile"])
            print("Email:", NAME[ID]["Email"])

    elif choice == "q":
        print("Goodbye!")
        break

print("==================================")