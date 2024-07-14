# Diccionarios y anidacion

# Creacion y uso de diccionarios
diccionario = { "Llave" : "Descripcion / Valor",
               449 : "Lada de Aguascalientes",
               "Manzana": "Fruta roja dulce circular",
               "Numero de telefono": 4491112233 }
print("\n",diccionario)

print ("\n -----------------------\n")

# Obtener valores del diccionario
print ("\n",diccionario["Manzana"])

print ("\n -----------------------\n")

# Agregar cosas al diccionario
diccionario["Llave nueva"] = "Descripcion de la nueva llave"
print (diccionario)

print ("\n -----------------------\n")

# Crear un diccionario vacio
diccionario_vacio = {}

# Editar un item en un diccionario
diccionario["Manzana"] = "Fruta amarilla que cuelga de un arbol"
print(diccionario)

print ("\n -----------------------\n")

# Loop para ver dentro del diccionario

for llave in diccionario:
    print("Llave: ",llave)
    print("Descripcion: ",diccionario[llave],"\n")

print ("\n -----------------------\n")

# Limpiar un diccionario
diccionario = {}
print(diccionario)

print ("\n -----------------------\n")

# Ejercicio crear un nuevo diccionario con calificaciones
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for estudiante in student_scores:
  if student_scores[estudiante] <=100 and student_scores[estudiante] >= 91:
    student_grades[estudiante] = "Outstanding"
  elif student_scores[estudiante] >= 81:
    student_grades [estudiante] = "Exceeds Expectations"
  elif student_scores[estudiante] >= 71:
    student_grades [estudiante] = "Acceptable"
  else:
    student_grades[estudiante] = "Fail"

print(student_grades)

print ("\n -----------------------\n")

# Anidaciones

Mexico = {
  "Ags":
  {
    "municipios": ["JM", "RR", "C"],
    "cantidad_mun": 17
  },

  "Gto": [ ["M1","M2", "M3"],21 ],

  "SLP": [
    { "municipios":["M1","M2", "M3"],"cantidad_mun":23} ,
    2.3,
    "Capital"
    ],
}

# Ejercicio

country = input("Ingresa el nombre del pais: ") # Add country name
visits = int(input("Ingresa el numero de visitas: ")) # Number of visits
list_of_cities = eval(input("Ingresa la lista de ciudades: ")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.

def add_new_country(country, visits, list_of_cities):
  append(travel_log)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

#Brazil
#2
#["Sao Paulo", "Rio de Janeiro"]
