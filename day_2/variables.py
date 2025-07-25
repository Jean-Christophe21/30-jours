# Exercices: niveau 1

first_name = 'John'
last_name = 'Doe'
name = 'Guido Van Rossum'
country = 'Togo'
city = 'Lome'
an = 23
est_Married = False
is_true = True
IS_light_on = True
variable1, variable2, variable3 = "string", 1, True

# Exercices: niveau 2

# Affichage des types des variables
print("verification du type des variables :")
print("type first_name = ", type(first_name))
print("type last_name = ", type(last_name))
print("type name = ", type(name))
print("type country = ", type(country))
print("type city = ", type(city))
print("type an = ", type(an))
print("type est_Married = ", type(est_Married))
print("type is_true = ", type(is_true))
print("type IS_light_on  = ", type(IS_light_on))
print("type variable1, variable2, variable3  = ", type(variable1), type(variable2), type(variable3))

#comparaison des longeurs des variables first_name et last_name
len_first_name = len(first_name)
len_last_name = len(last_name)

if len_first_name < len_last_name :
    print("le nom est plus long que le prenom")

elif len_first_name > len_last_name :
    print("le prenom est plus long que le nom")

else :
    print("le nom et le prenom sont de taille egale")


# operations sur num_one et num_two
num_one = 4 
num_two = 5

result1 = num_one + num_two
result2 = num_one - num_two
result3 = num_one * num_two
result4 = num_one / num_two
result5 = num_one % num_two
result6 = num_one // num_two

# Affichage d�taill� des r�sultats des op�rations sur num_one et num_two
print(f"{num_one} + {num_two} = {result1}")
print(f"{num_one} - {num_two} = {result2}")
print(f"{num_one} * {num_two} = {result3}")
print(f"{num_one} / {num_two} = {result4}")
print(f"{num_one} % {num_two} = {result5}")
print(f"{num_one} // {num_two} = {result6}")

# surface et circonference d'un cercle pour un rayon = 30
rayon = 30
area_of_circle = 3.14 * (rayon ** 2)
circum_of_circle = 2 * 3.14 * rayon
print("surface du cercle = ", area_of_circle)
print("circonference du cercle = ", circum_of_circle)

# surface et circonference d'un cercle pour un rayon saisi par l'utilisateur
# Demande � l'utilisateur de saisir le rayon du cercle
verify = True 
while(verify) : # on verifie si l'utilisateur entre un nombre valide
    try :
        rayon = float(input("veuillez entre le rayon du cercle : "))
    except :
        print("veuillez entrer un nombre valide")
    else :
        verify = False


# Calcul de la surface et de la circonf�rence du cercle avec le rayon saisi
area_of_circle = 3.14 * (rayon ** 2)
circum_of_circle = 2 * 3.14 * rayon
# Affichage des r�sultats pour le rayon saisi par l'utilisateur
print("surface du cercle = ", area_of_circle)
print("circonference du cercle = ", circum_of_circle)
    

first_name = input("veuillez entrer le prenom :")
last_name = input("veuillez entrer le nom :")
country = input("veuillez entrer le pays :")
city = input("veuillez entrer la ville :")
age = input("veuillez entrer l'age :")

# Affichage des donn�es saisies
print("\nDonn�es saisies :")
print("Pr�nom :", first_name)
print("Nom :", last_name)
print("Pays :", country)
print("Ville :", city)
print("�ge :", age)




