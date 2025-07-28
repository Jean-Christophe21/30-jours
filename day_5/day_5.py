#encoding: ISO-8859-1

my_list = list() # d�claration d'une liste vide

lst = [1, 2, 3, 4, 5] # d�claration d'une liste avec plus de 5 �l�ments

length_list = len(lst) # longueur de la liste
print("La longueur de la liste est :", length_list)

print("Le premier �l�ment de la liste est :", lst[0]) # premier �l�ment de la liste
print("Le dernier �l�ment de la liste est :", lst[-1]) # dernier �l�ment de la liste
print("l'�lement du mileu de la liste est :", lst[length_list // 2]) # �l�ment du milieu de la liste


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
print("La liste des entreprises IT apr�s modification est :", it_companies)
it_companies.append("Tesla") # ajout de l'entreprise Tesla � la liste
it_companies.insert(len(it_companies) // 2, "Nvidia") # insertion de Nvidia au milieu de la liste
it_companies[0] = it_companies[0].upper() # conversion de la liste en majuscules 
it_companies = [var1, var2, var3, var4, var5, var6, var7]
print("La liste des entreprises IT est :", it_companies)
print("Le nombre d'entreprises IT est :", len(it_companies))

it_companies[1] = "Alphabet" # modification de l'entreprise Google en Alphabet
print("La liste des entreprises IT apr�s modification est :", it_companies)
it_companies.append("Tesla") # ajout de l'entreprise Tesla � la liste
it_companies.insert(len(it_companies) // 2, "Nvidia") # insertion de Nvidia au milieu de la liste
it_companies = [company.upper() for company in it_companies] # conversion de chaque �l�ment en majuscules
it_companies_str = '#;  '.join(it_companies)

if "MICROSOFT" in it_companies: # recherche de l'entreprise Microsoft dans la liste 
    print("MICROSOFT est dans la liste des entreprises IT")
else:
    print("MICROSOFT n'est pas dans la liste des entreprises IT")

it_companies.sort() # tri de la liste des entreprises IT
print("La liste des entreprises IT tri�e est :", it_companies)

it_companies.sort(reverse=True) # tri de la liste des entreprises IT en ordre d�croissant
print("La liste des entreprises IT tri�e en ordre d�croissant est :", it_companies)

first_three_companies = it_companies[:3]
print("Les trois premi�res entreprises IT sont :", first_three_companies)

# Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print("Les trois derni�res entreprises IT sont :", last_three_companies)

# Remove the first IT company from the list
it_companies.pop(0)
print("La liste des entreprises IT apr�s suppression de la premi�re entreprise est :", it_companies)

# Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2

#remove the last IT company from the list
it_companies.pop(-1)
print("La liste des entreprises IT apr�s suppression de la derni�re entreprise est :", it_companies)

it_companies.clear() # vide la liste des entreprises IT
print("La liste des entreprises IT apr�s suppression de toutes les entreprises est :", it_companies)

del it_companies # supprime la liste des entreprises IT

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] 
back_end = ['Node','Express', 'MongoDB'] 

full_stack = front_end + back_end
full_stack.insert(len(front_end),"Python") # ajout de Python � la liste full_stack
full_stack.insert(len(front_end) +1 , "SQL") # ajout de SQL � la liste full_stack
print("La liste full_stack est :", full_stack)

# Exercises: Level 2 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() # tri de la liste des �ges
ages.append(max(ages)) # ajout de l'�ge maximum � la liste
ages.append(min(ages)) # ajout de l'�ge minimum � la liste
print("La liste des �ges apr�s tri et ajout des �ges maximum et minimum est :", ages)

# Find the median age (one middle item or two middle items divided by two) 
def find_median(ages):
    n = len(ages)
    if n % 2 == 0:
        return (ages[n // 2 - 1] + ages[n // 2]) / 2
    else:
        return ages[n // 2]
    
median_age = find_median(ages)
somme = sum(ages)
print("La somme des �ges est :", somme)
print("le minimum des �ges est :", min(ages))
print("le maximum des �ges est :", max(ages))
moyenne = somme / len(ages)
print("La moyenne des �ges est :", moyenne)

# comparaison de l'�ge minimum et de l'�ge maximum par rapport � la moyenne
if abs(min(ages) - moyenne) < abs(max(ages) - moyenne): 
    print("L'�ge minimum est plus proche de la moyenne que l'�ge maximum")
elif abs(min(ages) - moyenne) > abs(max(ages) - moyenne):
    print("L'�ge maximum est plus proche de la moyenne que l'�ge minimum")
elif abs(min(ages) - moyenne) == abs(max(ages) - moyenne):
    print("L'�ge minimum et l'�ge maximum sont �galement �loign�s de la moyenne")

#the middle country(ies) in the countries list

countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbie et Mont�n�gro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzanie', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisie', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
print("l'�l�ment du milieu de la liste des pays est :", countries[len(countries) // 2])

if len(countries) % 2 == 0: # si la liste des pays a un nombre pair d'�l�ments
    list1 = countries[len(countries) // 2 - 1] # l'�l�ment du milieu est le premier �l�ment de la seconde moiti� de la liste
else :
    liste1 = countries[len(countries) // 2 ] # l'�l�ment du milieu est le seul �l�ment de la seconde moiti� de la liste.on n'ajoute pas +1 car la liste commence � z&ro

list_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

list1 = list_countries[0:3]
list2 = list_countries[3:6]
print("Les trois premiers pays sont :", list1)
print("Les trois derniers pays sont :", list2)