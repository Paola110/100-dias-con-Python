# Uso de loops, rango y bloques de codigo

# For loop y rango

student_heights = input("\nIngresa las alturas de los estudiantes, separados por espacios, al finalizar pulsa enter\n").split()
for n in range(0, len(student_heights)): # Por cada n en el rango de 0 a cantidad de ittems en student_heights
  student_heights[n] = int(student_heights[n])

altura = 0
cont = 0
promedio = 0

for student in student_heights:
  altura += student # Sumatoria de estaturas
  cont +=1 # Cantidad de estudiantes
  promedio = round(altura / cont) # Promedio de estatura

print (f'''\ntotal height = {altura}
number of students = {cont}
average height = {promedio}''')

print ("\n -----------------------\n")

# Input a list of student scores
student_scores = input("\Ingresa los puntajes de los estudiantes, separados por espacios, al finalizar pulsa enter\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

max = student_scores[0]

for std in student_scores:
  if std > max :
    max = std

print(f"\nThe highest score in the class is: {max}")

print ("\n -----------------------\n")

# Uso de rango

print ("\nNumeros del 1 al 9")
for number in range (1,10): #Imprime 1 - 9
    print (number)  # como si pusieramos i = 1 , i < 10

print ("\n -----------------------\n")

print ("\nNumeros entre 1 y 10 dando saltos de 3")
for number in range (1,11,3): # Imprime los numeros de 1 - 10 
    print (number) # dando saltos de 3, es decir, [1, 4, 7, 10]

print ("\n -----------------------\n")

target = int(input("\nEnter a number between 0 and 1000\n"))
suma = 0

for num in range(0, target+1, 2):
  suma += num

print (f"La sumatoria de los numeros entre 0 y {target} es: {suma}")

print ("\n -----------------------\n")

print ("FizzBuzz Game\n")

for n in range (1, 101):
  if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
  elif n % 3 == 0:
    print ("Fizz")
  elif n % 5 == 0:
    print ("Buzz")
  else: print(n)
    
print ("\n -----------------------\n")


