#  Exercices - Jour 3 

age = 15
taille = 1.75
nombre_complexe = 3 + 4j

# demande a l'utilisateur de la base et la hauteur d'un triangle et calcul de la zone
base = float(input("Entrez la base du triangle : "))
hauteur = float(input("Entrez la hauteur du triangle : "))
zone = (base * hauteur) / 26

print(f"\nLa zone du triangle est : {zone}")

# demande a l'utilisateur de saisir les cotes d'un triangle et calcul du perimetre
cote1 = float(input("Entrez le premier cote du triangle : "))
cote2 = float(input("Entrez le deuxieme cote du triangle : "))
cote3 = float(input("Entrez le troisieme cote du triangle : "))

perimetre = cote1 + cote2 + cote3
print(f"\nLe perimetre du triangle est : {perimetre}")

#6. Obtention de la longueur et la largeur d'un rectangle a l'aide de l'invite
longeur = float(input("Entrez la longueur du rectangle : "))
largeur = float(input("Entrez la largeur du rectangle : "))
perimetre_rectangle = 2 * (longeur + largeur)
zone = longeur * largeur
print(f"\nLe perimetre du rectangle est : {perimetre_rectangle}")
print(f"\nLa zone du rectangle est : {zone}")

#6. Obtention du rayon d'un cercle a l'aide de l'invite
rayon = float(input("Entrez le rayon du cercle : "))
pi = 3.14
circonference = 2 * pi * rayon
zone_cercle = pi * rayon ** 2
print(f"\nLa circonference du cercle est : {circonference}")
print(f"\nLa zone du cercle est : {zone_cercle}")

# Calculez la pente, l'ordonnee X et l'ordonnee y de y = 2x -2 
x1 = 0
y1 = 2 * x1 - 2
x2 = 1
y2 = 2 * x2 - 2
pente1 = (y2 - y1) / (x2 - x1)
print(f"\nLa pente de la droite est : {pente1}")

# pente entre deux points  (2, 2) et le point (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
pente2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"\nLa pente entre les points ({x1}, {y1}) et ({x2}, {y2}) est : {pente2}")
print(f"\nLa distance euclidienne entre les points ({x1}, {y1}) et ({x2}, {y2}) est : {distance}")

# comparaison des pentes 
if pente1 < pente2 :
    print("\nla pente1 est plus petite que la pente2")

elif pente1 > pente2 :
    print("\nla pente1 est plus grande que la pente2")

else :
    print("\nles pentes sont de taille egale")

import numpy
X = numpy.arange(-10, 10, 1)
y = lambda x: x**2 + 6 * x + 9

verif_val = 0
for x in X:
    if y(x) == 0:
        print(f"\nLa valeur de x pour laquelle y = 0 est : {x}")
        verif_val = 1
        break
if verif_val == 0 :
    print("\naucune solution trouvee pour y = 0 dans l'intervalle donne.")


# la longeur de 'python' et 'dragon'
# Trouvez la longueur de "Python" et "Dragon" et faites une instruction de comparaison Falsy.
print(f"\nLa longueur de 'python' est : {len('python')}")
print(f"\nLa longueur de 'dragon' est : {len('dragon')}")

if len('python') == len('dragon'):
    print("\nLes longueurs de 'python' et 'dragon' sont egales.")
else :
    print("\nLes longueurs de 'python' et 'dragon' ne sont pas egales.")

if 'on' in 'python' and 'on' in 'dragon':
    print("\n'on' est present dans les deux mots.")
else :
    print("\n'on' n'est pas present dans les deux mots.")

if 'jargon' in ' I hope this course is not fu l of jargon.':
    print("\n'jargon' est present dans la phrase.")
    
else :
    print("\n6'jargon' n'est pas present dans la phrase.")

# calcul et conversion de la longeur de 'python' flottant 
len_python = len('python')
len_python_float = float(len_python)
print(f"\nLa longueur de 'python' en entier est : {len_python}")
print(f"\nLa longueur de 'python' en flottant est : {len_python_float}")