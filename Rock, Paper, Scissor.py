import random 
user_win = 0
computer_win = 0
opction = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type rock paper scissor or Q to quit:- ").lower()
    if user_input == "q":
        print("Okey")
        break
    if user_input not in opction:
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = opction[random_number]
    print("Computer pick", computer_pick)
    
    if user_input == "rock" and computer_pick == "scissor":
        print("You win!")
        user_win += 1 
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_win += 1 
        
    elif user_input == "scissor" and computer_pick == "paper":
        print("You win!")
        user_win += 1 
    
    elif user_input == "rock" and computer_pick == "rock":
        print("Draw!")
        
    elif user_input == "paper" and computer_pick == "paper":
        print("Draw!")
        
    elif user_input == "scissor" and computer_pick == "scissor":
        print("Draw!")
    
    else:
        print("Computer win!")
        computer_win += 1 
    
    
print("You win", str(user_win), "times.")
print("And computer win", str(computer_win), "times.")
