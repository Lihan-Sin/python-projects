    import random
import math
# Taking input from user.
lower  = int(input("Enter lower boudn:- "))

# Taking iput.
upper = int(input("Enter upper bound:- "))

# Generating rnaodm number between the lower and upper.

x = random.randint(lower, upper)
print("\n\tYou've only", round(math.log(upper - lower + 1, 2)),"chances to guess the integer!\n" )

# Initializing the number of guesses.
count = 0

# For calculation of minimum number of guesses depends upon range.
while count < math.log(upper - lower + 1, 2):
    count += 1

    # Taking guessing number as input
    guess  = int(input("Guess the number:- "))

    # Condition testig
    if x  ==  guess :
        print("Congratulations you did it in", count, "try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guess too high!")

# If guessing is more than required guesses, show this output.

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")
