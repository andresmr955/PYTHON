name = "David"
last_name = "Andres Marquez"

print(name)
print(last_name)

full_name = name + " "+ last_name
print(full_name)

#FORMAT 
template = "Hola mi nombre es " + name + " y mi apellido es " + last_name
print('v1', template)

template = "Hola mi nombre es {} y mi apellido es {}".format(name, last_name)

print("v2", template)

name = input("Cual es tu nombre? ")
edad = input("Cual es tu age? ")

template = "Hola mi nombre es {} y mi edad es {}".format(name, edad)
print("v3" + template)