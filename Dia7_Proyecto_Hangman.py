# Proyecto Hangman usando todos los conocimientos previos

import random
import time
import os # para cls, nos permite entrar a "operating system-specific functions"

palabra_adivinada = []
cadena_palabra_adivinada = ""
pierde_vida = 6
letras_usadas = ""

gana ='''

       .-''.        ___              ___
 ( '  / o o \ ' )   \  \    ___     /  /
  \ \ |  _, |/ /     \  \  /   \   /  /
   \ \ \___// /       \   v      v   /
     \ \ - / /         \_____/\_____/
      \ . . /           ____________
       |   |           |___      ___|
       | . |               |    |
       |___|            ___|    |___
       || ||           |____________|
       || ||            ______   ___   
       || ||           |      \ |   |
       || ||           |       \|   |
      / | | |          |   |\       |
"""""""""""""""""      |___| \______|
'''

pierde = '''
              _.--""--._
             /  _    _  \ 
          _  ( (_\  /_) )  _
         { \._\   /\   /_./ }
         /_"=-.}______{.-="_\ 
          _  _.=("""")=._  _
         (_'"_.-"`~~`"-._"'_)
          {_"            "_} 
                                            
  __        _______   _______   _______        
 |  |      |       | |   ____| |   ____|            
 |  |      |   _   | |  |____  |  |__                       
 |  |      |  |_|  | |____   | |   __|                
 |  |____  |       |  ____|  | |  |____                   
 |_______| |_______| |_______| |_______|                             

'''

pierde1 = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y|
| |       // |   | ||
| |      //  | . |  ||
| |     ('   |___|   ')
| |          || ||
| |          || ||
| |          || ||
| |          || ||
| |         / | | |
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .

'''

pierde2 = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y|
| |       // |   | ||
| |      //  | . |  ||
| |     ('   |___|   ')
| |          || 
| |          || 
| |          ||
| |          ||
| |        _/ |_ _ _
""""""""""| _______ |"""|
|"|"""""""          '"|"|
| |                   | |
: :                   : :  
. .                   . .

'''

pierde3 = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y|
| |       // |   | ||
| |      //  | . |  ||
| |     ('   |___|   ')
| |           
| |           
| |          
| |          
| |        _ _ _ _ _
""""""""""| _______ |"""|
|"|"""""""          '"|"|
| |                   | |
: :                   : :  
. .                   . .

'''

pierde4 = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . | 
| |       // |   | 
| |      //  | . |  
| |     ('   |___|   
| |           
| |           
| |          
| |          
| |        _ _ _ _ _
""""""""""| _______ |"""|
|"|"""""""          '"|"|
| |                   | |
: :                   : :  
. .                   . .

'''

pierde5 = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |         | . . | 
| |          |   | 
| |          | . |  
| |          |___|   
| |           
| |           
| |          
| |          
| |        _ _ _ _ _
""""""""""| _______ |"""|
|"|"""""""          '"|"|
| |                   | |
: :                   : :  
. .                   . .

'''

pierde6 = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |           `--'
| |        
| |        
| |         
| |             
| |           
| |           
| |          
| |          
| |        _ _ _ _ _
""""""""""| _______ |"""|
|"|"""""""          '"|"|
| |                   | |
: :                   : :  
. .                   . .

'''

print_pierde_vidas = [pierde1, pierde2, pierde3, pierde4, pierde5, pierde6]

lista_palabras = ["manzana", "libro", "sol", "agua", "perro", "gato", "mesa", "silla", "flor", "arbol", "cielo", "nube", "estrella", "canguro", "caballo", "casa", "coche", "bicicleta", "telefono", "ordenador", "raton", "teclado", "pantalla", "camara", "musica", "pelicula", "juego", "juguete", "revista"]

#Elegir palabra random
palabra_elegida = random.choice(lista_palabras)

for letra in palabra_elegida:
    palabra_adivinada.append(" _ ")

cadena_palabra_adivinada = "".join(palabra_adivinada)

# Checar si todos los espacios estan llenos 
# Checar si ya no le quedan vidas

while cadena_palabra_adivinada.find(" _ ") != -1 and pierde_vida > 0:
    
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla, cls para windows y clear para linux/macOS
    print(cadena_palabra_adivinada)

    # Mostrar el hangman 
    if pierde_vida != 6:
        print (print_pierde_vidas[pierde_vida])
    
    #Pedir letra
    letra_usuario = input("\nIngresa una letra: ").lower()

    # Lista con las letras usadas 
    while letras_usadas.find(letra_usuario) != -1: # cadena.find(sub-cadena) regresa el indice de la subcadena o un -1 si no la encuentra
        print("\nYa has usado esta letra")
        letra_usuario = input("\nIngresa una letra: ").lower()

    letras_usadas += letra_usuario

    # Ver donde esta la letra y llenar espacios
    # Si no esta quitar una vida e ir contando las vidas perdidas
    indice = 0
    cambio = False 

    for letra in palabra_elegida:
        if letra == letra_usuario: 
            palabra_adivinada[indice] = letra 
            cambio = True
            cadena_palabra_adivinada = " ".join(palabra_adivinada)

        if cambio == False and indice == len(palabra_elegida)-1 :
            pierde_vida -= 1

        indice += 1


if pierde_vida < 1:
    print (print_pierde_vidas[pierde_vida])
    time.sleep(5) #sleep, se queda pausado 5 segundos
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla, cls para windows y clear para linux/macOS
    print(pierde)
else :
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla, cls para windows y clear para linux/macOS
    print(gana)


