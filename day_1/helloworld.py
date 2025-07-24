# Jour 1 - Exercices

# Exercice niveau 1

# 1. Vérifiez la version Python que vous utilisez
import sys
print("Version de Python :", sys.version)

# 2. Opérations arithmétiques avec 3 et 4
a = 3
b = 4
print("Addition :", a + b)
print("Soustraction :", a - b)
print("Multiplication :", a * b)
print("Modulo :", a % b)
print("Division :", a / b)
print("Exponentielle :", a ** b)
print("Division entière :", a // b)

# 3. Affichage de chaînes
print("Votre nom : John")
print("Votre nom de famille : Doe")
print("Votre pays : Togo")
print("Je profite de 30 jours de python")

# 4. Vérification des types de données
print("Type de 10 :", type(10))
print("Type de 9.8 :", type(9.8))
print("Type de 3.14 :", type(3.14))
print("Type de 4 - 4j :", type(4 - 4j))
print("Type de ['Asabeneh', 'Python', 'Finlande'] :", type(['Asabeneh', 'Python', 'Finlande']))
print("Type de votre nom :", type("John"))
print("Type de votre nom de famille :", type("Doe"))
print("Type de votre pays :", type("Togo"))

# Exercice niveau 3

# 1. Exemples pour différents types de données Python
entier = 10
flottant = 3.14
complexe = 2 + 3j
chaine = "Python"
booleen = True
liste = [1, 2, 3]
tuple_ex = (4, 5, 6)
ensemble = {7, 8, 9}
dictionnaire = {"nom": "John", "age": 23}

print("Exemple entier :", entier, type(entier))
print("Exemple flottant :", flottant, type(flottant))
print("Exemple complexe :", complexe, type(complexe))
print("Exemple chaîne :", chaine, type(chaine))
print("Exemple booléen :", booleen, type(booleen))
print("Exemple liste :", liste, type(liste))
print("Exemple tuple :", tuple_ex, type(tuple_ex))
print("Exemple ensemble :", ensemble, type(ensemble))
print("Exemple dictionnaire :", dictionnaire, type(dictionnaire))

# 2. Distance euclidienne entre (2, 3) et (10, 8)
import math # importation du module math pour utiliser sqrt
x1, y1 = 2, 3
x2, y2 = 10, 8
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance euclidienne entre (2,3) et (10,8) :", distance)