import pygame
pygame.init()

def add_contact(NAME):
    ID = input("Person ID: ")
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

def get_text_input(prompt):
    window = pygame.display.set_mode((500, 200))
    font = pygame.font.SysFont(None, 60)
    text = ""
    input_active = True
    clock = pygame.time.Clock()

    while input_active:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                input_active = False
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                    return text
                elif event.key == pygame.K_BACKSPACE:
                    text =  text[:-1]
                else:
                    text += event.unicode

        window.fill((0, 0, 0))
        prompt_surf = font.render(prompt, True, (255, 255, 255))
        window.blit(prompt_surf, (20, 20))
                                  
        text_surf = font.render(text, True, (255, 0, 0))
        window.blit(prompt_surf, (20, 20))
        window.blit(text_surf, (20, 100))
        
        pygame.display.flip()

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


#colour 
light_grey=(200,200,200)
lightish_grey=(180,180,180)
darker_grey=(70,70,70)
black=(0,0,0)

#window
screen = pygame.display.set_mode([500, 550])
pygame.display.set_caption("Contact Manager")

#font
font = pygame.font.SysFont(None, 30)

#button functions
button_add = pygame.Rect(50, 150, 100, 50)
button_search = pygame.Rect(200, 150, 100, 50)
button_edit = pygame.Rect(350, 150, 100, 50)
button_delete = pygame.Rect(50, 250, 100, 50)
button_print = pygame.Rect(200, 250, 100, 50)
button_quit = pygame.Rect(350, 250, 100, 50)

running = True

while running:
    screen.fill(darker_grey)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #draw buttons + hover effect
    for rect, label in [
        (button_add, "Add"),
        (button_search, "Search"),
        (button_edit, "Edit"),
        (button_delete, "Delete"),
        (button_print, "Print"),
        (button_quit, "Quit")
    ]:
        color = lightish_grey if rect.collidepoint(mouse_x, mouse_y) else light_grey
        pygame.draw.rect(screen, color, rect)
        text_surf = font.render(label, True, black)
        screen.blit(text_surf, (rect.x +10, rect.y +15))    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_add.collidepoint(event.pos):
                add_contact(NAME)
            elif button_search.collidepoint(event.pos):
                search_contact(NAME)
            elif button_edit.collidepoint(event.pos):
                edit_contact(NAME)
            elif button_delete.collidepoint(event.pos):
                delete_contact(NAME)
            elif button_print.collidepoint(event.pos):
                print_contacts(NAME)
            elif button_quit.collidepoint(event.pos):
                print("Goodbye!")
                running = False

    pygame.display.update()

pygame.quit()
exit()