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