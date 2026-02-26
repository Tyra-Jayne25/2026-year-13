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

    elif choice == "s":
        ID = input("\n\nPerson ID: ")
        print(NAME[ID])

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
        print(NAME)

    elif choice == "q":
        print("Goodbye!")
        break

print("==================================")