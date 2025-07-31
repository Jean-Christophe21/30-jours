#encoding: ISO-8859-1

# Exercices: Level 1

# Exercice 1: V�rifier si l'utilisateur est assez �g� pour conduire
print("Exercice 1:")
age = int(input("Entrez votre �ge: "))
if age >= 18:
    print("Vous �tes assez �g� pour apprendre � conduire.")
else:
    years_to_wait = 18 - age
    print(f"Vous avez besoin de {years_to_wait} ans de plus pour apprendre � conduire.")

# Exercice 2: Comparer l'�ge de l'utilisateur avec mon �ge
print("\nExercice 2:")
my_age = 25  # J'ai d�fini mon �ge � 25 ans
user_age = int(input("Entrez votre �ge: "))
age_difference = abs(my_age - user_age)

if my_age > user_age:
    if age_difference == 1:
        print("J'ai 1 an de plus que vous.")
    else:
        print(f"J'ai {age_difference} ans de plus que vous.")
elif user_age > my_age:
    if age_difference == 1:
        print("Vous avez 1 an de plus que moi.")
    else:
        print(f"Vous avez {age_difference} ans de plus que moi.")
else:
    print("Nous avons le m�me �ge.")

# Exercice 3: Comparer deux nombres
print("\nExercice 3:")
num_one = int(input("Entrez le premier nombre: "))
num_two = int(input("Entrez le deuxi�me nombre: "))

if num_one > num_two:
    print(f"{num_one} est sup�rieur � {num_two}")
elif num_one < num_two:
    print(f"{num_one} est inf�rieur � {num_two}")
else:
    print(f"{num_one} est �gal � {num_two}")

# Exercices: Level 2

# Exercice 1: Noter les �tudiants selon leur score
print("\nExercice 1 - Level 2:")
score = int(input("Entrez le score de l'�tudiant (0-100): "))

if 80 <= score <= 100:
    grade = "A"
elif 70 <= score <= 89:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
elif 0 <= score <= 49:
    grade = "F"
else:
    grade = "Score invalide"

print(f"Note: {grade}")

# Exercice 2: D�terminer la saison en fonction du mois
print("\nExercice 2 - Level 2:")
month = input("Entrez le mois: ").lower().strip()

autumn_months = ["septembre", "octobre", "novembre"]
winter_months = ["d�cembre", "janvier", "f�vrier"]
spring_months = ["mars", "avril", "mai"]
summer_months = ["juin", "juillet", "ao�t"]

if month in autumn_months:
    season = "Automne"
elif month in winter_months:
    season = "Hiver"
elif month in spring_months:
    season = "Printemps"
elif month in summer_months:
    season = "�t�"
else:
    season = "Mois invalide"

print(f"La saison est {season}")

# Exercice 3: G�rer une liste de fruits
print("\nExercice 3 - Level 2:")
fruits = ['banane', 'orange', 'mangue', 'citron']
fruit = input("Entrez un fruit: ").lower()

if fruit in fruits:
    print("Ce fruit existe d�j� dans la liste")
else:
    fruits.append(fruit)
    print(f"Liste modifi�e: {fruits}")

# Exercices: Level 3

# Exercice 1: Manipuler un dictionnaire de personne
print("\nExercice 1 - Level 3:")

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# V�rifier si le dictionnaire a une cl� skills et imprimer la comp�tence du milieu
if 'skills' in person:
    skills_length = len(person['skills'])
    middle_skill_index = skills_length // 2
    print(f"Comp�tence du milieu: {person['skills'][middle_skill_index]}")

# V�rifier si la personne a la comp�tence Python
if 'skills' in person:
    if 'Python' in person['skills']:
        print("La personne a la comp�tence Python")

# V�rifier les comp�tences de la personne pour d�terminer son titre
if 'skills' in person:
    skills = person['skills']
    
    if set(['JavaScript', 'React']).issubset(set(skills)):
        if 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
            print("Il est un d�veloppeur fullstack")
        else:
            print("Il est un d�veloppeur front-end")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("Il est un d�veloppeur backend")
    else:
        print("Titre inconnu")

# Afficher des informations sur la personne
if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} vit en {person['country']}. Il est mari�.")