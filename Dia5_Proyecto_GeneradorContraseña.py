#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("\nWelcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = []

for l in range(0,nr_letters):
    letra = letters[random.randint(0,len(letters)-1)]
    password.append(letra)

for s in range(0,nr_symbols):
    simbolo = symbols[random.randint(0,len(symbols)-1)]
    password.append(simbolo)
    

for n in range(0,nr_numbers):
    numero = numbers[random.randint(0,len(numbers)-1)]
    password.append(numero)

Password = "Tu contraseña es: "+ "".join(password) # Join unir lista a string
print(Password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

Password = ""

for pas in range(0,len(password)):
    temp = random.randint(0,len(password)-1)
    Password += password[temp]
    password.remove(password[temp])

Password = "Tu contraseña aleatoria es: " + Password
print(Password)