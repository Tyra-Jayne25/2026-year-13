#Adding buttons to the program using pygame
#adding buttons for add, search, edit, delete, print, and quit functions

import pygame
pygame.init()

# Set colour variables
light_grey=(200,200,200)
lightish_grey=(180,180,180)
dark_grey=(100,100,100)
darker_grey=(70,70,70)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)

# Set up the display window
screen = pygame.display.set_mode([500, 550])

# Intialise button 1 variables
x1_pos=100
y1_pos=150
rec1_colour=light_grey
button1=pygame.Rect(x1_pos,y1_pos,80,80)
# Intialise button 2 variables
x2_pos=300
y2_pos=150
rec2_colour=light_grey
button2=pygame.Rect(x2_pos,y2_pos,80,80)

running = True
click=0

while running:
    screen.fill((darker_grey))

    # When the user clicks x in the game window
    for event in pygame.event.get():
        mouse_x,mouse_y=pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running=False

        # When the user clicks on a button, animate the button and change its colour
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                rec1_colour=white
                x1_pos=x1_pos+3
                y1_pos=y1_pos+3
                button1=pygame.Rect(x1_pos,y1_pos,80,80)
            elif button2.collidepoint(event.pos):
                rec2_colour=white
                x2_pos=x2_pos+3
                y2_pos=y2_pos+3
                button2=pygame.Rect(x2_pos,y2_pos,80,80)
            

        # When the user releases the button, reset button to original colour and position
        elif event.type==pygame.MOUSEBUTTONUP:
            if button1.collidepoint(event.pos):
                rec1_colour=light_grey
                x1_pos=100
                y1_pos=150
                button1=pygame.Rect(x1_pos,y1_pos,80,80)
            elif button2.collidepoint(event.pos):
                rec2_colour=light_grey
                x2_pos=300
                y2_pos=150
                button2=pygame.Rect(x2_pos,y2_pos,80,80)
    # Draw the buttons
    pygame.draw.rect(screen, rec1_colour, button1)
    pygame.draw.rect(screen, rec2_colour, button2)
    pygame.display.flip()
pygame.quit()
exit()

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