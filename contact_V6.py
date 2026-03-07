from random import choice
import pygame
pygame.init()

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


#colour variables
light_grey=(200,200,200)
lightish_grey=(180,180,180)
dark_grey=(100,100,100)
darker_grey=(70,70,70)
black=(0,0,0)
white=(255,255,255)

#window
screen = pygame.display.set_mode([500, 550])
pygame.display.set_caption("Contact Manager")

#font
font = pygame.font.SysFont(None, 30)

#button functions
def make_buttons(x, y, w, h, text):
    return{"rect": pygame.Rect(x, y, w, h),
           "colour": light_grey, 
           "text": text}

def draw_button(button):
    pygame.draw.rect(screen, button["colour"], button["rect"])
    text_surf = font.render(button["text"], True, black)
    label = font.render(button["text"], True, black)
    screen.blit(label, (button["rect"].x + 10, button["rect"].y + 25))

def hover(button, mouse_pos):
    if button["rect"].collidepoint(mouse_pos):
        button["colour"] = light_grey
    else:
        button["colour"] = lightish_grey

def is_clicked(button, event):
    return event.type == pygame.MOUSEBUTTONDOWN and button["rect"].collidepoint(event.pos)

#creating the buttons
buttons = [
    make_buttons(50, 150, 100, 50, "Add"),
    make_buttons(200, 150, 100, 50, "Search"),
    make_buttons(350, 150, 100, 50, "Edit"),
    make_buttons(50, 250, 100, 50, "Delete"),
    make_buttons(200, 250, 100, 50, "Print"),
    make_buttons(350, 250, 100, 50, "Quit")
]

running = True

while running:
    screen.fill(darker_grey)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for button in buttons:
            if is_clicked(button, event):
                if button["text"] == "Add":
                    add_contact(NAME)
                elif button["text"] == "Search":
                    search_contact(NAME)
                elif button["text"] == "Edit":
                    edit_contact(NAME)
                elif button["text"] == "Delete":
                    delete_contact(NAME)
                elif button["text"] == "Print":
                    print_contacts(NAME)
                elif button["text"] == "Quit":
                    print("Goodbye!")
                    running = False

    for button in buttons:
        hover(button, pygame.mouse.get_pos())
        draw_button(button)

    pygame.display.flip()
pygame.quit()
exit()

#Menu loop to add, search, edit, delete, print, or quit
while True:
    choice = input("Do you want to: (a)dd a contact, (S)earch a contact, (e)dit a contact, (d)elete a contact, (p)rint all contacts, or (q)uit? ")

#Using the functions instead of repeating code
    if choice == "a":
        add_contact(NAME)
    elif choice == "s":
        search_contact(NAME)
    elif choice == "e":
        edit_contact(NAME)
    elif choice == "d":
        delete_contact(NAME)
    elif choice == "p":
        print_contacts(NAME)
    elif choice == "q":
        print("Goodbye!")
        break

print("==================================")