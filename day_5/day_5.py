#encoding: ISO-8859-1

my_list = list() # déclaration d'une liste vide

lst = [1, 2, 3, 4, 5] # déclaration d'une liste avec plus de 5 éléments

length_list = len(lst) # longueur de la liste
print("La longueur de la liste est :", length_list)

print("Le premier élément de la liste est :", lst[0]) # premier élément de la liste
print("Le dernier élément de la liste est :", lst[-1]) # dernier élément de la liste
print("l'élement du mileu de la liste est :", lst[length_list // 2]) # élément du milieu de la liste


name = "chris"
age = 18
height = 1.66
marital_status = False
address = "rue de la foi"

mixed_data_types = [name, age, height, marital_status, address]

var1 = "Facebook"
var2 = "Google"
var3 = "Microsoft"
var4 = "Apple"
var5 = "IBM"
var6 = "Oracle"
var7 = "Amazon"
it_companies = [var1, var2, var3, var4, var5, var6, var7]
print("La liste des entreprises IT est :", it_companies)
print("Le nombre d'entreprises IT est :", len(it_companies))

it_companies[1] = "Alphabet" # modification de l'entreprise Google en Alphabet
print("La liste des entreprises IT après modification est :", it_companies)
it_companies.append("Tesla") # ajout de l'entreprise Tesla à la liste
it_companies.insert(len(it_companies) // 2, "Nvidia") # insertion de Nvidia au milieu de la liste
it_companies[0] = it_companies[0].upper() # conversion de la liste en majuscules 
it_companies = [var1, var2, var3, var4, var5, var6, var7]
print("La liste des entreprises IT est :", it_companies)
print("Le nombre d'entreprises IT est :", len(it_companies))

it_companies[1] = "Alphabet" # modification de l'entreprise Google en Alphabet
print("La liste des entreprises IT après modification est :", it_companies)
it_companies.append("Tesla") # ajout de l'entreprise Tesla à la liste
it_companies.insert(len(it_companies) // 2, "Nvidia") # insertion de Nvidia au milieu de la liste
it_companies = [company.upper() for company in it_companies] # conversion de chaque élément en majuscules
it_companies_str = '#;  '.join(it_companies)

if "MICROSOFT" in it_companies: # recherche de l'entreprise Microsoft dans la liste 
    print("MICROSOFT est dans la liste des entreprises IT")
else:
    print("MICROSOFT n'est pas dans la liste des entreprises IT")

it_companies.sort() # tri de la liste des entreprises IT
print("La liste des entreprises IT triée est :", it_companies)

it_companies.sort(reverse=True) # tri de la liste des entreprises IT en ordre décroissant
print("La liste des entreprises IT triée en ordre décroissant est :", it_companies)

first_three_companies = it_companies[:3]
print("Les trois premières entreprises IT sont :", first_three_companies)

# Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print("Les trois dernières entreprises IT sont :", last_three_companies)

# Remove the first IT company from the list
it_companies.pop(0)
print("La liste des entreprises IT après suppression de la première entreprise est :", it_companies)

# Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2

#remove the last IT company from the list
it_companies.pop(-1)
print("La liste des entreprises IT après suppression de la dernière entreprise est :", it_companies)

it_companies.clear() # vide la liste des entreprises IT
print("La liste des entreprises IT après suppression de toutes les entreprises est :", it_companies)

del it_companies # supprime la liste des entreprises IT

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] 
back_end = ['Node','Express', 'MongoDB'] 

full_stack = front_end + back_end
full_stack.insert(len(front_end),"Python") # ajout de Python à la liste full_stack
full_stack.insert(len(front_end) +1 , "SQL") # ajout de SQL à la liste full_stack
print("La liste full_stack est :", full_stack)

# Exercises: Level 2 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() # tri de la liste des âges
ages.append(max(ages)) # ajout de l'âge maximum à la liste
ages.append(min(ages)) # ajout de l'âge minimum à la liste
print("La liste des âges après tri et ajout des âges maximum et minimum est :", ages)

# Find the median age (one middle item or two middle items divided by two) 
def find_median(ages):
    n = len(ages)
    if n % 2 == 0:
        return (ages[n // 2 - 1] + ages[n // 2]) / 2
    else:
        return ages[n // 2]
    
median_age = find_median(ages)
somme = sum(ages)
print("La somme des âges est :", somme)
print("le minimum des âges est :", min(ages))
print("le maximum des âges est :", max(ages))
moyenne = somme / len(ages)
print("La moyenne des âges est :", moyenne)

# comparaison de l'âge minimum et de l'âge maximum par rapport à la moyenne
if abs(min(ages) - moyenne) < abs(max(ages) - moyenne): 
    print("L'âge minimum est plus proche de la moyenne que l'âge maximum")
elif abs(min(ages) - moyenne) > abs(max(ages) - moyenne):
    print("L'âge maximum est plus proche de la moyenne que l'âge minimum")
elif abs(min(ages) - moyenne) == abs(max(ages) - moyenne):
    print("L'âge minimum et l'âge maximum sont également éloignés de la moyenne")

#the middle country(ies) in the countries list

countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbie et Monténégro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzanie', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisie', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
print("l'élément du milieu de la liste des pays est :", countries[len(countries) // 2])

if len(countries) % 2 == 0: # si la liste des pays a un nombre pair d'éléments
    list1 = countries[len(countries) // 2 - 1] # l'élément du milieu est le premier élément de la seconde moitié de la liste
else :
    liste1 = countries[len(countries) // 2 ] # l'élément du milieu est le seul élément de la seconde moitié de la liste.on n'ajoute pas +1 car la liste commence à z&ro

list_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

list1 = list_countries[0:3]
list2 = list_countries[3:6]
print("Les trois premiers pays sont :", list1)
print("Les trois derniers pays sont :", list2)