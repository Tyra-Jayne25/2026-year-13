phone = {"1":
          {"First Name": "John",
           "Last Name": "Matua",
           "Mob": "021 212 3456",
           "Email": "matua_j2maximail.com"},

           "2":
           {"First Name": "Smith",
            "Last Name": "Pearson",
            "Mob": "021 912 7124",
            "Email": "smith@maximail.co.lt"}
}

for phone_id, phone_info in phone.items():
    print("\Phone ID:", phone)

    for key in phone_info:
        print(key + ":", phone_info[key])
phone = {}

for i in range(2):
    ID = input("\n\nEnter ID: ")
    phone[ID] = {}

    First_Name = input("Enter First Name: ")
    phone[ID] ["First Name"] = First_Name

    Last_Name = input("Enter Last Name: ")
    phone[ID] ["Last Name"] = Last_Name

    Mob = input("Enter Mob: ")
    phone[ID] ["Mob"] = Mob

    Email = input("Enter Email: ")
    phone[ID] ["Email"] = Email
   
    print("\n\n")
    print(phone)

#user chooses to search or print full list
search = input("Do you want to search for a contact? (yes/no): ")
if search.lower() == "yes":
    search_id = input("Enter the ID of the contact you want to search for: ")
    if search_id in phone:
        print("\nContact found:")
        for key, value in phone[search_id].items():
            print(key + ": " + value)
    else:
        print("\nContact not found.")

#program should check whether that name is on the contact list
name = input("\n\nEnter the name you want to search for: ")
found = False
for contact in phone.values():
    if contact["First Name"].lower() == name.lower() or contact["Last Name"].lower() == name.lower():
        print("\nContact found:")
        for key, value in contact.items():
            print(key + ": " + value)
        found = True
        break