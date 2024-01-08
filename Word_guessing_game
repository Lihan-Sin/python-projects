import random
# Library that we use in order to choose on random words from a list of words.

name = input("What is your name? ")

# Here there user is asked to enter the name first

print("Good luck", name)

worlds = ["rainbow", "computer", "science", "programing",
          "python", "mathmathetics", "player", "condition",
          "reverse", "water", "board", "geeks"]

# Function will choose one of these list of word

word = random.choice(worlds)

print("Guess the chracters")

guesses = ""

# Any number of turns  can be used here
turns = 12

while turns > 0 :
    # count the number of times a user fails
    failed = 0

    # All chracters from the input 
    # Word taking one at a time.

    for char in word :

        # Comparing that chracter with the chracter in guesses

        if char in guesses:
            print(char, end = " ")
        else:
            print("_")

            # For every failure 1 will be incremented in failure
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0 and 'you win' will be given as output
        print("You win!")

        # this print the correct word
        print("The word is: ", word)
        break

    # if user has input the wrong alphabet then it will ask user to enter another alphabet.
    print()
    guess = input("Guess a chracter:- ")

    # Every input chracter will be stored in guesses 
    guesses += guess

    # if check input with the chracter in word
    if guess not in word:

        turns -= 1

        # if the chracter dosen't match the word then "wrong" will be given as output.
        print("Wrong") 

        # this will print the number of turns left for the user.
        print("You have", + turns, "more  guesses")

        if turns == 0:
            print("You loose")
        

