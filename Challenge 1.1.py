import json

with open("users.json", "r") as users:
    users_data = json.loads(users.read())

for i in users_data:
    i["name"] = i["name"].split()
    i["firstname"] = i["name"][0]
    i["lastname"] = i["name"][1]
    i.pop("name")
    print("Last name: " + i["lastname"])
    print("First name: " + i["firstname"])
    print("Latitude of the city the person lives in: " + i["address"]["geo"]["lat"])
    print("The catch phrase of the company that this person works for: " + i["company"]["catchPhrase"])
