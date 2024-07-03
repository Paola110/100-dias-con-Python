# Tipos de variables, uso y manipulacion

two_digit_number = input("Ingresa un numero de dos digitos: ") # Variable tipo string (str)

decimal = int(two_digit_number[0]) # Conversion a entero (int) y 
                                   # seleccion de caracteres en string
unidad = int(two_digit_number[1])

print("La suma de los digitos es: " , decimal + unidad) # Suma de enteros

print ("\n -----------------------\n")

# Operaciones con numeros

#   Reordar PEMDASLR = Parent Expon Mult Div Add Substract Left Right

resultado = 4 / 2 # 2

    # resultado = resultado / 2 # 1

resultado /= 2 # 1

print (resultado)

print ("\n -----------------------\n")

# Uso de la f-string

age = input("Ingresa tu edad: ")

print(f"\nYou have {(90 - int (age)) * 52} weeks left.")

print ("\n -----------------------\n")