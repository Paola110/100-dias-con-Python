# Creacion de numeros random y listas en python

import random # Debemos importar el modulo para obtener las funciones

# Numero entero

random_entero = random.randint (1,10) # Regresa un numero entero entre a y b incluyendo los enteros
print ("Random entero: ", random_entero)

print ("\n -----------------------\n")

# Numero flotante

random_flotante = random.random() # Regresa un numero decimal entre 0.000 y 0.9999
print ("Random flotante: ", random_flotante)

print ("\n -----------------------\n")

# Ejercicio Cara o cruz random

moneda = random.randint(0,1)

if moneda == 1:
  print ("Heads")
else:
  print ("Tails")

print ("\n -----------------------\n")

# Ejercicio persona random de una lista

names = ["Angela, Ben, Jenny, Michael, Chloe"]

cantidad = len(names)

persona = random.randint(0,cantidad-1)

print (f"{names[persona]} is going to buy the meal today!")

print ("\n -----------------------\n")

# Listas y listas anidadas

verduras = [ "calabaza", "chayote", "zanahoria"] # Esto es una lista
frutas = ["platano", "pera", "melon"] # esta es otra lista

frutas_y_verduras = [verduras , frutas] # lista anidada

# Otra representacion = frutas_y_verduras = [[ "calabaza", "chayote", "zanahoria"] , ["platano", "pera", "melon"]]

# Elercicio marcar X en mapa 

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3] # Definimos el mapa

print("Hiding your treasure! X marks the spot.")

position = input("Where do you want to put the treasure?") #Cordenadas ABC, 123

letter = position[0].lower() # Pasa a minuscula
abc = ["a", "b", "c"] # Crea una lista para ABC

letter_index = abc.index(letter) # Busca el indice de la letra de la cordanada = columna
number_index = int(position[1]) - 1 # fila

map[number_index][letter_index] = "X" # cambia a X en fila , columna

print(f"{line1}\n{line2}\n{line3}") # Imprime el mapa

print ("\n -----------------------\n")