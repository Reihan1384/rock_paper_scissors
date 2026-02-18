import random

print("Help note:")
print("Enter rock,paper or scissors to play.")
print("Enter 'quit' to end the game")
print("Be careful on the spelling!")

randomNum = random.randint(0, 2)
computerMove = ""

if randomNum == 0:
    computerMove = "rock"
elif randomNum == 1:
    computerMove = "paper"
elif randomNum == 2:
    computerMove = "scissors"
    
player1Score = 0
player2Score = 0
winningScore = int(input("How many points should winner earn? "))

while player1Score < winningScore and player2Score < winningScore:
    print(f"Player 1 : {player1Score} , Player 2 : {player2Score}")
    player1 = input("Player 1 , Make your move \nrock,paper,scissors: ").lower()
    print(f"Player 2 , Make your move \nrock,paper,scissors: {computerMove}")
    player2 = computerMove
    
    if player1 == "quit":
        print("Player 1 ended the game")
        break
    
    if player1 == player2:
        print("It's a tie!")
        
    elif player1 == "rock":
        if player2 == "scissors":
            print("Player 1 won this round!")
            player1Score += 1
        elif player2 == "paper":
            print("Player 2 won this round!")
            player2Score += 1
            
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 won this round!")
            player1Score += 1
        elif player2 == "rock":
            print("Player 2 won this round!")
            player2Score += 1
            
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 won this round!")
            player1Score += 1
        elif player2 == "scissors":
            print("Player 2 won this round!")
            player2Score += 1
            
    else:
        print("Somthing is wrong...")
        
print(f"Final scores : Player 1: {player1Score} , Player 2: {player2Score}")
if player1Score > player2Score:
    print("Player 1 won the game!")
elif player1Score < player2Score:
    print("Player 2 won the game!")