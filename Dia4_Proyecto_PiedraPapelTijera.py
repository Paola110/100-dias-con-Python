rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

=== ROCK ===
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

=== PAPER ===
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

=== SCISSORS ===
'''

import random

RPS = input("\nWhat do you choose? (rock / paper / scissors)\n").lower()

options = ["r","p","s"]
print_options = [rock,paper,scissors]

user = options.index(RPS[0])

print ("\nYour choose\n", print_options[user], "\n")

computer = random.randint(0,2)

print ("\nComputer choose\n", print_options[computer], "\n")

if (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print ("You win!!\n")
elif user == computer:
    print ("Tied!!\n")
else:
    print ("You loose :(\n")
