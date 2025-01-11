# Creacion de una calculadora funcional, con operaciones de:
#     Suma
#     Resta
#     Multiplicacion
#     Division

# Con opcion de guadado de memoria

import os

logo = """
 _____________________
|  _________________  |
| | Calculadora Pao | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|


"""

def add(n1, n2):
    """Suma dos numeros"""
    return n1 + n2

def substract(n1, n2):
    """Resta dos numeros"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplica dos numeros"""
    return n1 * n2

def divide(n1, n2):
    """Divide dos numeros"""
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

# print(operations[input("Simbolo de la operación a realizar: ")](int(input("Primer numero: ")), int(input("Segundo numero: "))))

opcion = "y"
memoria = "y"

while opcion == "y":

    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla, cls para windows y clear para linux/macOS

    print(logo)

    primero = int(input("Dame el primer numero: "))
    operacion = input("Dime la operacion que deseas realizar ( +, -, *, / ): ")
    segundo = int(input("Dame el segundo numero: "))

    resultado = operations[operacion](primero, segundo)

    print(primero, " " + operacion + " ", segundo, " = ", resultado)

    memoria = input(f"Quieres continuar calculando con {resultado}? (y/n)")

    while memoria == "y":
        primero = resultado
        operacion = input("Dime la operacion que deseas realizar ( +, -, *, / ): ")
        segundo = int(input("Dame el segundo numero: "))

        resultado = operations[operacion](primero, segundo)

        print(primero , " " + operacion + " " , segundo , " = " , resultado)

        memoria = input(f"Quieres continuar calculando con {resultado}? (y/n)")

    opcion = input("Quieres seguir usando la calculadora? (y/n): ")