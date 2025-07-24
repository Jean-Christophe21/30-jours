#coding utf-8

#Jour 2: 30 Days of Python Programming

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


len_first_name = len(first_name)
len_last_name = len(last_name)

if len_first_name < len_last_name :
    print("le nom est plus long prenom")

elif len_first_name > len_last_name :
    print("le prenom est plus long nom")

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

print(result1, result2, result3, result4, result5, result6 )
# 