# Crear un juego con condicionales para llegar o no a el tesoro

print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----/
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~____~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------/
 \_/__________________________________________________________________/
      ''')

print ('''Bienvenido a la isla del tesoro
¡Tu misión es encontrar el tesoro! ''')

LR = input('Estás en una encrucijada. ¿A dónde quieres ir? Escribe "izquierda" o "derecha" \n').lower()
if LR == "izquierda":

    SW = input('Has llegado a un pueblo. Hay un vendedor vendiendo manzanas y pescado. Escribe "manzanas" para comprar manzanas. Escribe "pescado" para comprar pescado. \n').lower()
    if SW == "manzanas":

        Door = input("Sigues tu aventura y te encaminas hacia el bosque. Hay una casa con 3 puertas. Un sendero oscuro, un sendero lleno de arboles y uno completamente despejado. ¿Qué sendero eliges? 'oscuro', 'arboles' o 'despejado' \n").lower()
        if Door == "arboles":
            print ("¡Encontraste el tesoro! ¡Ganaste!")
        elif Door == "despejado":
            print("Nada te protege del sol durante el dia y no puedes hacer fuego por la noche. Fin del juego.")
        elif Door == "oscuro":
            print("Esta lleno de bestias. Fin del juego.")
        else : print("Elegiste un sendero que no existe. Fin del juego.")

    else : print("El pescado estaba en mal estado y no puedes seguir. Fin del juego.")

else : print("Te perdiste en el desierto. Fin del juego.")
