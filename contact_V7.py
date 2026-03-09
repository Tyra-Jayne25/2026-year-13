import pygame
pygame.init()

#contact functions
def add_contact(contacts, next_id):
    contact_id = str(next_id)
    contacts[contact_id] = {}
    contacts[contact_id]["First Name"] = input("First Name: ")
    contacts[contact_id]["Last Name"] = input("Last Name: ")
    contacts[contact_id]["Mobile"] = input("Mobile: ")
    contacts[contact_id]["Email"] = input("Email: ")
    print("\nContact added! ID is", contact_id)
    next_id += 1
    return contacts, next_id

def search_contact(contacts):
    search_term = input("First Name or Last Name: ")
    found = False
    for contact_id, info in contacts.items():
        if search_term in info["First Name"] or search_term in info["Last Name"]:
            print("\nPerson ID:", contact_id)
            print("First Name:", info["First Name"])
            print("Last Name:", info["Last Name"])
            print("Mobile:", info["Mobile"])
            print("Email:", info["Email"])
            found = True
    if not found:
        print("No contacts found.")

def edit_contact(contacts):
    contact_id = input("Person ID: ")
    if contact_id in contacts:
        contacts[contact_id]["First Name"] = input("First Name: ")
        contacts[contact_id]["Last Name"] = input("Last Name: ")
        contacts[contact_id]["Mobile"] = input("Mobile: ")
        contacts[contact_id]["Email"] = input("Email: ")
        print("\nContact updated!")
    return contacts


def delete_contact(contacts):
    contact_id = input("Person ID: ")
    if contact_id in contacts:
        del contacts[contact_id]
        print("\nContact deleted!")
    return contacts

def print_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return

    for contact_id, info in contacts.items():
        print("\nPerson ID:", contact_id)
        print("First Name:", info["First Name"])
        print("Last Name:", info["Last Name"])
        print("Mobile:", info["Mobile"])
        print("Email:", info["Email"])

#text input box function GUI

def get_text_input(prompt):
    window = pygame.display.set_mode((500, 200))
    font = pygame.font.SysFont(None, 60)
    text = ""
    active = True
    clock = pygame.time.Clock()

    while active:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                    return text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        window.fill((0, 0, 0))
        prompt_surf = font.render(prompt, True, (255, 255, 255))
        text_surf = font.render(text, True, (255, 0, 0))

        window.blit(prompt_surf, (20, 20))
        window.blit(text_surf, (20, 100))

        pygame.display.flip()

#GUI button set up 

#colour 
light_grey=(200,200,200)
lightish_grey=(180,180,180)
dark_grey=(70,70,70)
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
    screen.fill(dark_grey)
    mouse_x, mouse_y = pygame.mouse.get_pos()

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
        screen.blit(text_surf, (rect.x + 10, rect.y + 15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_add.collidepoint(event.pos):
                contacts, next_id = add_contact(contacts, next_id)

            elif button_search.collidepoint(event.pos):
                search_contact(contacts)

            elif button_edit.collidepoint(event.pos):
                contacts = edit_contact(contacts)

            elif button_delete.collidepoint(event.pos):
                contacts = delete_contact(contacts)

            elif button_print.collidepoint(event.pos):
                print_contacts(contacts)

            elif button_quit.collidepoint(event.pos):
                print("Goodbye!")
                running = False
                
                pygame.display.update()

#Main program
contacts = {}
next_id = 1

while True:
    choice = input("Do you want to: (a)dd a contact, (S)earch a contact, (e)dit a contact, (d)elete a contact, (p)rint all contacts, or (q)uit? ")
    if choice == "a":
        contacts, next_id = add_contact(contacts, next_id)

    elif choice == "s":
        search_contact(contacts)

    elif choice == "e":
        edit_contact(contacts)

    elif choice == "d":
        delete_contact(contacts)

    elif choice == "p":
        print_contacts(contacts)

    elif choice == "q":
        print("Goodbye!")
        break

print("==================================")
print(contacts)

pygame.quit()