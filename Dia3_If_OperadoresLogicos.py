# If y operadores logicos

# If simple

number = int(input("Qué numero quieres checar?\n"))

if number % 2 == 0:
  print("\nThis is an even number.")
else:
  print("\nThis is an odd number.")

print ("\n -----------------------\n")

# Uso de elif

height = float(input("\nIngresa tu altura en metros: "))

weight = int(input("\nIngresa tu peso en kilogramos: "))

BMI = weight / (height ** 2)

if BMI < 18.5 :
  interpretation = "are underweight."
elif BMI >= 18.5 and BMI < 25 :
  interpretation = "have a normal weight."
elif BMI >= 25 and BMI < 30 :
  interpretation = "are slightly overweight."
elif BMI >= 30 and BMI < 35 :
  interpretation = "are obese."
else :
  interpretation = "are clinically obese."

print (f"\n\nYour BMI is {BMI}, you " + interpretation + "\n")

print ("\n -----------------------\n")

year = int(input("\nQue año quieres revisar si es bisiesto?\n"))

if year % 4 == 0:
  if year % 100 != 0:
    print ("\nLeap year")
  elif year % 400 == 0:
    print("\nLeap year")
  else: 
    print ("\nNot leap year")
else:
  print ("\nNot leap year")

print ("\n -----------------------\n")

print("\nThank you for choosing Python Pizza Deliveries!")
size = input("\nWhat size pizza do you want? S, M, or L\n")
add_pepperoni = input("\nDo you want pepperoni? Y or N\n")
extra_cheese = input("\nDo you want extra cheese? Y or N\n")
bill = 0

if size == "S":
  bill += 15
  if add_pepperoni == "Y":
    bill += 2
elif size == "M":
  bill += 20
else:
  bill += 25

if size == "M" or size == "L" and add_pepperoni == "Y":
  bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"\nYour final bill is: ${bill}.")

print ("\n -----------------------\n")

# Operadores logicos 

# && == and
# || == or 
# ~ == not

# No se pone el operador, se usa con palabras 

print("\nThe Love Calculator is calculating your score...\n")

name1 = input("\nWhat is your name?\n")
name2 = input("\nWhat is their name?\n")

name_combination = name1 + name2 # Combinamos los dos nombres

name_low = name_combination.lower() #La funcion .lowe() pasa a minusculas el texto

score1 = 0 # Score para la palabra true ( Cuenta en los nombres las letras T R U E )
score2 = 0 # Score para la palabra love ( Cuenta en los nombres las letras L O V E )

score1 += name_low.count("t")
score1 += name_low.count("r")
score1 += name_low.count("u")
score1 += name_low.count("e")

score2 += name_low.count("l")
score2 += name_low.count("o")
score2 += name_low.count("v")
score2 += name_low.count("e")

total_score = score1 * 10 + score2 # Decenas = score1, unidades = score2

if total_score < 10 or total_score > 90:
  print (f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score < 50 and total_score > 40:
  print (f"Your score is {total_score}, you are alright together.")
else:
  print (f"Your score is {total_score}.")

print ("\n -----------------------\n")