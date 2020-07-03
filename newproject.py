
import random

throws = ["rock" , "paper" , "scissors"]
player_scores = 0
ai_scores = 0
max_score = 3
while player_scores or ai_scores < max_score:
    print("Please throws your choice: rock , paper , scissors")
    player_throw= str(input())
    if player_throw == "rock":
        ai_throw = random.choice(throws)
        if ai_throw == "scissors":
            print("You win!")
            print("The CPU picked: " ,ai_throw)
            player_scores +=1
            print("Your current score is: " , player_scores)
        if ai_throw == "paper":
            print("You lose!")
            print("The CPU picked: ", ai_throw)
            ai_scores +=1
            print("The CPU current score is: " , ai_scores)
        if ai_throw == "rock":
            print("Draw!")
            print("The CPU picked: ", ai_throw)


    if player_throw == "paper":
        ai_throw = random.choice(throws)
        if ai_throw == "rock":
            print("You win!")
            print("The CPU picked: ", ai_throw)
            player_scores +=1
            print("Your current score is: ", player_scores)
        if ai_throw == "scissors":
            print("You lose!")
            print("The CPU picked: ", ai_throw)
            ai_scores +=1
            print("The CPU current score is: ", ai_scores)
        if ai_throw == "paper":
            print("Draw!")
            print("The CPU picked: ", ai_throw)

    if player_throw == "scissors":
        ai_throw = random.choice(throws)
        if ai_throw == "paper":
            print("You win!")
            print("The CPU picked: ", ai_throw)
            player_scores +=1
            print("Your current score is: ", player_scores)
        if ai_throw == "rock":
            print("You lose!")
            print("The CPU picked: ", ai_throw)
            ai_scores +=1
            print("The CPU current score is: ", ai_scores)
        if ai_throw == "scissors":
            print("Draw!")
            print("The CPU picked: ", ai_throw)
    if player_scores >= max_score:
        print("You won the game!")
        break
    elif ai_scores >= max_score:
        print("The CPU won the game!")
        break