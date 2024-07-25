# Programa de subasta con diccionarios

import os # Para borrar pantalla
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

jolla = '''
                     _______
                   .'_/_|_\_'.
                   \`\  |  /`/
                    \ \ | / /
                     `\ | /`
                        `
'''
vino = '''
              _
              |-|
              |~|
              |:|
             .'.'.
            /   ::\ .
            |_____|     __          _
            |:.:;.|   <:__:>     .-'o\ .
            |_____|   \  ::/  .o' O. o\ .
            |   ::|    '..'  |--o.--o--|
            |   ;:|     ||   |._._o_._.|
            \_____/    .''.
                      '----'
'''
pintura = '''
               ╔════════════════════╗
               ║          *         ║
               ║  *    ,MMM8&&&. *  ║
               ║      MMMM88&&&&&   ║
               ║     MMMM88&&&&&&&  ║
               ║  *  MMM88&&&&&&&&  ║
               ║     MMM88&&&&&&&&  ║
               ║     'MMM88&&&&&&'  ║
               ║       'MMM8&&&' *  ║
               ║   * |\___/|        ║
               ║     )     (   . '  ║
               ║    =\     /=  *    ║
               ║      )===(         ║
               ║     /     \        ║
               ║     |     |     *  ║
               ║    /       \       ║
               ║    \       /       ║
               ║ _/\ _//\__/\ _//\_ ║
               ║ |  |/  || |  |/  | ║
               ╚════════════════════╝
'''
avion = '''
                             |
                       --====|====--
                             |
                         .-"""""-.
                       .'_________'.
                      /_/_|__|__|_\_\ .
                     ;'-._       _.-';
,--------------------|    `-. .-'    |--------------------,
 ``""--..__    ___   ;       '       ;   ___    __..--""``
           `"-//  \.._\             /_..//  \-"`
              \ _//    '._       _.'    \ _//
               `"`        ``---``        `"`
'''
bote = '''
                         ;~
                       ./|\.
                     ./ /| `\.
                    /  | |   `\.
                   |   | |     `\.
                   |    \|       `\.
                 .  `----|__________\.
                  \-----''----.....___
                   \               ""/
              ~^~^~^~^~^`~^~^`^~^~^`^~^~^
               ~^~^~`~~^~^`~^~^~`~~^~^~
'''

manos = '''
 \)\/))                                        ((\/(/
 \)\ < /))                                  ((\ >//(/
  \ \ \_/_____,----.              ,----._____\_/// /
   \ `(_]_______    `.          ,'    _______[_)  /
    `-------------,   \        /  ,--------------'
                   |   \      /   |
'''

subastados = [jolla,vino,pintura,avion,bote]

postores = "s"
ofertas = []
mayor_oferta = -1

objeto = random.choice(subastados)

while (postores == "s" or postores == "S"):
    clear()
    print (objeto)
    print ("¡¡Bienvenido a la subasta!!")
    nombre = input("\nIngresa tu nombre: ")
    oferta = int(input("\nIngresa tu oferta: $"))

    if mayor_oferta < oferta:
        mayor_oferta = oferta

    nuevo_postor = {
        "nombre" : nombre,
        "oferta" : oferta
    }

    ofertas.append(nuevo_postor)

    postores = input("\n\nHay más personas que deseen ofertar? (s/n): ")

for directorio in ofertas:
    if directorio["oferta"] == mayor_oferta:
        clear()
        print(objeto, manos, "\n¡¡Gracias por participar en la subasta!!")
        print ( f"\nEl que se lleva el objeto subastado es {directorio['nombre']}, con una oferta de ${directorio['oferta']}\n")
        break


