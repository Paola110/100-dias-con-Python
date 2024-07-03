# Print, input y debugg

# Imprimir 5 lineas con print
  
print ("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.",
       "\n2. Knead the dough for 10 minutes.",
       "\n3. Add 3g of Salt.",
       "\n4. Leave to rise for 2 hours.",
       "\n5. Bake at 200 degrees C for 30 minutes.")

print ("\n -----------------------\n")

# Uso de comillas

print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote")

print ("\n -----------------------\n")

# Concatenar cadenas y saltos de linea 

print ("Hola Mundo \nSalto de linea")
print ("Hola" + " Mundo") # Tener cuidado con los espacios 

print ("\n -----------------------\n")

# Debugear codigo

#   Codigo sin debugear

    # print(Day 1 - String Manipulation")
    # print("String Concatenation is done with the "+" sign.")
    #   print('e.g. print("Hello " + "world")')
    # print(("New lines can be created with a backslash and n.")

#   Codigo arreglado

print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

print ("\n -----------------------\n")

# Input

print ("Numero 1 = " + input("Dame el numero 1 = ") )

print ("\n -----------------------\n")

# Numero de letras en una cadena

nombre = input("Dame un nombre = ")
numOfLetters = len(nombre) # Usamos la funcion "len"
print(numOfLetters)

print ("\n -----------------------\n")

# Variables y cambio de valores 

a = input() #29
b = input() #41

tempA = a
a = b
b = tempA

print("a: " + a) #41
print("b: " + b) #29

print ("\n -----------------------\n")