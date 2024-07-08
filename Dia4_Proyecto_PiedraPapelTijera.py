# Proyecto piedra, papel o tijera contra computadora
piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

=== PIEDRA ===
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

=== PAPEL ===
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

=== TIJERA ===
'''

import random
import os # para cls, nos permite entrar a "operating system-specific functions"

os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla, cls para windows y clear para linux/macOS

eleccion = input("\n¿Qué eliges? (piedra / papel / tijera)\n").lower()

opciones = ["piedra","papel","tijera"]
imprimir_opciones = [piedra,papel,tijera]

usuario = opciones.index(eleccion)

os.system('cls' if os.name == 'nt' else 'clear')

print ("\nTu elección\n", imprimir_opciones[usuario], "\n")

computadora = random.randint(0,2)

print ("\nLa computadora eligió\n", imprimir_opciones[computadora], "\n")

if (usuario == 0 and computadora == 2) or (usuario == 1 and computadora == 0) or (usuario == 2 and computadora == 1):
    print ("¡Ganaste!\n")
elif usuario == computadora:
    print ("¡Empate!\n")
else:
    print ("Perdiste :(\n")
