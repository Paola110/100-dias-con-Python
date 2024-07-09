# Encriptado y desencriptado de mensajes usando Cesar Cipher 

import os
import time

# letras_simbolos_numeros = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','!', '#', '$', '%', '&', '(', ')', '*', '+',' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# let_sim_num = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','!', '#', '$', '%', '&', '(', ')', '*', '+',' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

let_sim_num = ['k', 'B', '1', 'a', 'Q', '$', ')', 'y', '*', 'p', 'g', 'C', 'M', 'K', 'b', 'w', 'W', '9', '#', 'q', 'G', 'U', 'd', 'A', '7', 'x', '!', 'X', 't', '(', 'N', 'Z', 'F', 'D', 'c', 'Y', 'S', 'o', 's', '+', 'H', 'i', '3', 'f', '4', 'T', 'l', 'm', 'R', '5', 'O', '8', 'h', 'V', 'J', '0', 'e', 'r', 'P', ' ', 'I', 'E', 'j', 'z', 'L', '%', 'v', '2', '&', 'u', '6', 'n']

option = 0
msg = ""
temporal = ""

def encripta (msg, num_enc, let_sim_num):
    nuevo_msg = ""
    temp = num_enc
    for letra in msg:
        num_enc = temp
        indice = let_sim_num.index(letra) # 69
        if indice + num_enc > len(let_sim_num)-1: # 72 > 71
            num_enc = num_enc - (len(let_sim_num) - 1 - indice) # 3 - (72 - 1 - 69) = 1
            indice = -1
        nuevo_msg += let_sim_num[indice + num_enc]
    print("\nEl nuevo mensaje es: ", nuevo_msg)
    return nuevo_msg

def desencripta (msg, num_enc, let_sim_num):
    nuevo_msg = ""
    temp = num_enc
    for letra in msg:
        num_enc = temp
        indice = let_sim_num.index(letra)
        nuevo_msg += let_sim_num[indice - num_enc]
    print("\nEl nuevo mensaje es: ", nuevo_msg)
    return nuevo_msg


while option != 5:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla, cls para windows y clear para linux/macOS
    print('''
Bienvenido a el encriptado de little cesars!!
    1. Encriptar un nuevo mensaje
    2. Desencriptar un nuevo mensaje
    3. Encriptar el mensaje anterior
    4. Desencriptar el mensaje anterior
    5. Salir
          
Ingresa el numero de la opcion que deseas: ''')
    option = int(input())

    if option == 1:
        msg = list(input("\nDame un mensaje: ")) # list(mensaje) descompone el mensaje en una lista de caracteres individuales
        num_enc = int (input("\nDame el numero de encriptado: "))
        temporal = encripta(msg, num_enc, let_sim_num)
    elif option == 2:
        msg = list(input("\nDame un mensaje: "))
        num_enc = int (input("\nDame el numero de encriptado: "))
        temporal = desencripta(msg, num_enc, let_sim_num)
    elif option == 3:
        if msg == "":
            print("\nNo hay un mensaje para encriptar")
        else:
            print("\nEl mensaje anterior es: ", msg)
            print("\nEl numero de encriptado anterior es: ", num_enc)
            temporal = encripta(msg, num_enc, let_sim_num)
    elif option == 4:
        if msg == "":
            print("\nNo hay un mensaje para desencriptar")
        else:
            print("\nEl mensaje anterior es: ", msg)
            print("\nEl numero de encriptado anterior es: ", num_enc)
            temporal = desencripta(msg, num_enc, let_sim_num)
    elif option == 5:
        print ("\nGracias por usar el ¡¡Encriptado de little cesars!!")
    else:
        print("\nIngresaste una opcion invalida!")
    msg = temporal
    time.sleep(5)