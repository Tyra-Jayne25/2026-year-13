#Adding buttons to the program using pygame
#adding buttons for add, search, edit, delete, print, and quit functions


#adding in the functions
def add_contact(NAME):
    NAME[ID] = {}

    NAME[ID]["First Name"] = input("first Name: ")
    NAME[ID]["Last Name"] = input("Last Name: ")
    NAME[ID]["Mobile"] = input("Mobile: ")
    NAME[ID]["Email"] = input("Email: ")
    print("\nContact added!")
#able to add more than one contact and when printing the dictionary, it shows all the contacts added

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

#adding the buttons using pygame
import pygame
pygame.init()

#colour variables
light_grey=(200,200,200)
lightish_grey=(180,180,180)
dark_grey=(100,100,100)
darker_grey=(70,70,70)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)

#window
screen = pygame.display.set_mode([500, 550])
pygame.display.set_caption("Contact Manager")

#font
font = pygame.font.SysFont(None, 30)

#button
button_add = pygame.Rect(50, 50, 100, 50)
button_search = pygame.Rect(200, 50, 100, 50)
button_edit = pygame.Rect(350, 50, 100, 50)
button_delete = pygame.Rect(50, 150, 100, 50)
button_print = pygame.Rect(200, 150, 100, 50)
button_quit = pygame.Rect(350, 150, 100, 50)






