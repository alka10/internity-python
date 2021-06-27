import random
import math
lower = int(input("Enter lower range:- "))
 
upper = int(input("Enter upper range:- "))
 
x = random.randint(lower, upper)
print("\n\tYou only got ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the number!\n")
 
count = 0
while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("Guess the number:- "))
    if x == guess:
        print("Yeah! You identified the number ")
        break
    elif x > guess:
        print("Please try again! The number you guessed is too small")
    elif x < guess:
        print("Please try again! The number you guessed is too high")
if count >= math.log(upper - lower + 1, 2):
    
    print("\tOops! All you chances are finished. Better luck next time!")