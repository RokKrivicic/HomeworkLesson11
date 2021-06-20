import json

with open("users.json", "r") as users:
    users_data = json.loads(users.read())

for i in users_data:
    i["name2"] = i["name"].split()
    i["firstname"] = i["name2"][0]
    i["lastname"] = i["name2"][1]
    i.pop("name2")

lastName = input("Enter your last name: ")

for i in users_data:
    if lastName.lower() == i["lastname"].lower():
        print("Name: " + i["name"] + ", email: " + i["email"] + ", company: " + i["company"]["name"])
        break
