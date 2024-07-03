# Crear una calculadora que calcule cuanto debe pagar cada persona de una cuenta

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

#Ejemplo de input

# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

#Ejemplo de output

#Each person should pay: $19.93

print("\nBienvenidos a la calculadora de cuentas y propinas!")

cuenta = float (input("Cual es el total de la cuenta?\n$ "))

porcentaje = float(input("Que porcentaje de propina deja? 10, 12, o 15?\n")) / 100

personas = int (input("Entre cuantas personas se divide la cuenta?\n"))

print ("Cada persona debe pagar: $ ", round((cuenta*(1+porcentaje)/personas),2), "\n") #redondeamos usando round
