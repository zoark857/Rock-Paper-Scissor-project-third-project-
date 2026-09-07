# this is mysecond proect
# it is a number guessing name usig while loop from{1-100}

import random

# this is to get computer to select a random number
secret = random.randint(1, 100)

# I am using while lopp to get game in lopp till the user get it right
while True:
 guess = int(input("write your Guess: "))

# using if/else 
 if guess == secret:
      print("you are correct")

# using break to exit the loop
      break

# using elif statement to work as hinting system

 elif guess > secret:
     print("OOPS! try to get a smaller no")

 elif guess < secret:
    print("OOPS! try toget a bigger no")