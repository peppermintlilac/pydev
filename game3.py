#!/usr/local/bin/python3
from random import randint
secret = randint(1,10)

#always setting the variable to something
guess = 0

while guess != secret:
   g = input("Guess the number:")
   guess = int(g)
   if guess > secret:
      print("Too high!")
   elif guess < secret:
      print("Too low!")
   else:
       print("You win!")
       break
print("Game over!")
