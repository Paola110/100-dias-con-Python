 # Funciones con inpu y parametros

# Funcion con un input
def mi_funcion (algo):
    print("Imprimir " + algo)

mi_funcion ("Algo")

print ("\n -----------------------\n")

# Funcion con multiples inputs
def mi_funcion_multiple (algo, algo_mas, otra_cosa):
    print("Imprime" + algo)
    print("Imprime" + algo_mas)
    print("Imprime" + otra_cosa)

mi_funcion_multiple ("Algo", "Algo más", "Otra cosa")

print ("\n -----------------------\n")

# Funcion con multiples inputs y redondear numero hacia arriba

import math

def paint_calc (height, width, cover): # Calcula cuantas latas de pintura se ocupan para pintar una pared
  latas = math.ceil(height * width / cover) # math.ceil redondea un numero decimal hacia arriba
  print(f"You'll need {latas} cans of paint.")

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

print ("\n -----------------------\n")

# Checar si un numero es primo 

def prime_checker (number):
  div = False
  for i in range (2,number):
    if number % i == 0:
      div = True
      break
  if div == False and number % number == 0 or number == 2:
    print ("It's a prime number.")
  else :
    print("It's not a prime number.")
    
n = int(input()) # Check this number
prime_checker(number=n)
