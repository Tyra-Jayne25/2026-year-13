contact = {"1":
    {"First Name": "John",
    "Last Name": "Smith",
    "Mobile": "123 456 7890",
    "Email": "johnsmith@example.com"},

    "2":
    {"First Name": "Jane",
    "Last Name": "Rose",
    "Mobile": "987 654 3210",
    "Email": "janerose@example.com"}

}
print(contact["1"]["First Name"])
print(contact["1"]["Last Name"])
print(contact["1"]["Mobile"])
print(contact["1"]["Email"])

print(contact["2"]["First Name"])
print(contact["2"]["Last Name"])
print(contact["2"]["Mobile"])
print(contact["2"]["Email"])


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

    
    
