#encoding: ISO-8859-1

# sets 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24] 


#Exercises: Level 1 
# 1. Find the length of the set it_companies
print("Length of it_companies:", len(it_companies))
# 2. Add an IT company to it_companies
it_companies.add('Twitter')
print("Updated it_companies:", it_companies)
# 3. Insert a new set of IT companies to it_companies
it_companies.update({'Netflix', 'Spotify'})
print("Updated it_companies:", it_companies)
# 4. Remove one of the companies from the set it_companies
it_companies.remove('Oracle')
print("it_companies after removal:", it_companies)
# 5. What is the difference between remove and discard
# remove renvoie une erreur si l'élément n'existe pas, discard ne renvoie pas d'erreur

#Exercises: Level 2
print("les unions de A et B:", A.union(B)) # union de A et B

if A.issubset(B) :
    print("A est un sous ensemble de B.")
else :
    print("A n'est un sous ensemble de B.")


if A.isdisjoint(B) :
    print("A et B sont disjoints.")
else :
    print("A et B ne sont pas disjoints.")

print("les unions de A et B et B with A :", A.union(B), B.union(A))

print(" La différence symétrique entre A et B est :", A.symmetric_difference(B))

del it_companies # suppression de l'ensemble

# Exercises: Level 3 
set_age = set(age)
length_set_age = len(set_age)
length_list_age = len(age)

if length_list_age < length_set_age :
    print("la longueur de la liste des ages et plus petite que celle de l'ensemble des ages.")
elif length_list_age > length_set_age :
    print("la longueur de l'ensemble des ages et plus petite que celle de  la liste des ages.")
else :
    print("la longueur de la liste des ages et de l'ensemble des ages sont égales.")


# la différence entre les types de données suivants :
# - String : une chaîne de caractères, immuable, utilisée pour stocker du texte.
# - List : une liste ordonnée, mutable, utilisée pour stocker une collection d'éléments.
# - Tuple : un tuple ordonné, immuable, utilisé pour stocker une collection d'éléments.
# - Set : un ensemble non ordonné, mutable, utilisé pour stocker une collection d'éléments uniques.

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words. 
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Nombre de mots uniques dans la phrase :", len(unique_words))

