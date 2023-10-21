
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

print("enter 0 for rock 1 for paper and 2 for scissors\n")
val = int(input())
if (val == 0):
    print(rock)
elif (val == 1):
    print(paper)
else:
    print(scissors)
key = random.randint(0, 2)
if (key == 0):
    print(rock)
elif (key == 1):
    print(paper)
else:
    print(scissors)
if (val == key):
    print("Draw")
elif (val > key):
    print("You won")
else:
    print("you lost")
