# If y operaciones

number = int(input("Qué numero quieres checar?\n"))

if number % 2 == 0:
  print("\nThis is an even number.")
else:
  print("\nThis is an odd number.")

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