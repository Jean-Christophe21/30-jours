#encoding: ISO-8859-1

from csv import list_dialects


dog = {} # création d'un dictionnaire vide nommé dog

dog = {
    "name": "medor",
    "color": "brun",
    "breed": "bulldog",
    "legs": 4,
    "age": 5
}

student_isaac = {
    "first_name": "Isac",
    "last_name": "Doe",
    "gender": 'M',
    "age": 14, 
    "marital_status": True,
    "skills": ["programmation python"],
    "country": "Togo",
    "city": "Lomé",
    "address": "rue de la paix"
}


print("la longueur du dictionnaire student_isaac est :", len(student_isaac)) # longueur du dictionnaire"

# . Get the value of skills and check the data type, it should be a list 
skills = student_isaac.get("skills")
print("La valeur de skills est :", skills)

#modify the skills values by adding one or two skills 
student_isaac["skills"].extend(["JavaScript", "HTML"])
skills = student_isaac.get("skills")
print("La valeur de skills est :", skills)

# Get the dictionary keys as a list 
keys = list(student_isaac.keys())
print("Les clés du dictionnaire student_isaac sont :", keys)

# Get the dictionary values as a list
values = list(student_isaac.values())

# Convertir le dictionnaire en liste de tuples avec items()
student_isaac_items = list(student_isaac.items())
print("Liste de tuples (clé, valeur) du dictionnaire student_isaac :", student_isaac_items)

#  Delete one of the items in the dictionary 
del student_isaac["marital_status"]

#  Delete one of the dictionaries
del student_isaac["address"]
