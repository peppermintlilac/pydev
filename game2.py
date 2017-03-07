#!/usr/local/bin/python3

#always setting the variable to something
guess=0

while guess != 5:
   g=input("Guess the number:")
   guess=int(g)
   if guess > 5:
      print("Too high!")
   elif guess < 5:
      print("Too low!")
   else:
      break
print("You win!")
