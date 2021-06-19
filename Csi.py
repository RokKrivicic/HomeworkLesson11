import json

with open("dna.txt", "r") as dna:
    dna_string = dna.read()  # got data from file dna.txt

with open("dna.json", "r") as dna_info:
    dna_data = json.loads(dna_info.read())  # got data from file dna.json

rez = []  # create an empty list for storing the result

for x in dna_data:  # going trough all the elements of the list
    t = list(x.values())[0]  # saved the value for every element, [0] is for the first element of the list
    w = list(x.keys())[0]  # saved the key for every element
    for y in t:  # going trough all the elements of the list(5 list generated with the previous for)
        z = str(list(y.values())[0])  # saved the value for every element
        r = str(list(y.keys())[0])  # saved the key for every element
        if dna_string.find(z) > -1:  # if -find gives -1 as a result the string is not part of the bigger string
            rez.append("(\'" + w + "\', \'" + r + "\')")  # add element to the list

rez.sort()  # sort the list you got in alphabetical order

rez_string = str(rez)  # convert it to string

rez_string = rez_string.replace('"', '')  # remove " from the string

eva = {"Gender": "Female",
       "Race": "White",
       "Hair color": "Blonde",
       "Eye color": "Blue",
       "Facial shape": "Oval"}

larisa = {"Gender": "Female",
          "Race": "White",
          "Hair color": "Brown",
          "Eye color": "Brown",
          "Facial shape": "Oval"}

matej = {"Gender": "Male",
         "Race": "White",
         "Hair color": "Black",
         "Eye color": "Blue",
         "Facial shape": "Oval"}

miha = {"Gender": "Male",
        "Race": "White",
        "Hair color": "Brown",
        "Eye color": "Green",
        "Facial shape": "Square"}

# compare the strings and write who did it

if rez_string == str(sorted(eva.items())):
    print("Eva ate the ice cream")
elif rez_string == str(sorted(larisa.items())):
    print("Larisa ate the ice cream")
elif rez_string == str(sorted(matej.items())):
    print("Matej ate the ice cream")
elif rez_string == str(sorted(miha.items())):
    print("Miha ate the ice cream")
else:
    print("Nobody of the suspects ate the ice cream")
