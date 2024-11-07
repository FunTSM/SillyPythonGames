#If you are reading this code, i just want to say i'm sorry. This is one of my first programs i ever built, and i don't care enough to make it better.
#Its error handling is quite literaly to just shut down.
#I also talked about the quality of this in my readme.
#good luck with my code, if it just doesnt work its because i havnt ran it in two years and am just moving it from my last code hosting site to this one.


import random

#This is the rock paper scissors code

  #makes variables
aiChoice = 0
playerChoice = 0
playerScoreMain = 0
aiScoreMain = 0


def game1(playerScore,aiScore):

  #gets ai choice
  aiChoices = ["rock","paper","scissors"]
  aiChoice = random.choice(aiChoices)
  
  #gets player choice
  playerChoice = input("rock, paper or scissors:")

  if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors" and playerChoice != "scissor":
    print("entry data not found shutting down")
    exit()
    
  #checks for all combinations
  if playerChoice == aiChoice:
    print("you tie, next round")
    
  elif playerChoice == "rock" and aiChoice == "paper":
   print("you lose")
   aiScore = aiScore+1
  
  elif playerChoice == "rock" and aiChoice == ("scissors" or "scissor"):
    print("you win")
    playerScore = playerScore+1
    #play again

  elif playerChoice == "paper" and aiChoice == ("scissor" or "scissors"):
   print("you lose")
   aiScore = aiScore+1

  elif playerChoice == "paper" and aiChoice == "rock":
    print("you win")
    playerScore = playerScore+1

  elif playerChoice == "scissors" or "scissor" and aiChoice == "rock":
   print("you lose")
   aiScore = aiScore+1
  
  elif playerChoice == "scissors" or "scissor" and aiChoice == "paper":
    print("you win")
    playerScore = playerScore+1
    
  print("score = ai-", aiScore,"player-",playerScore)
  aiScoremain = aiScore
  playerScoremain = playerScore

  if playerScore == 5:
    print("")
    print("you win!\n restart program please")
  elif aiScore == 5:
    print("")
    print("you lose!\n please restart program")
  else:
    print("")
    game1(playerScoreMain,aiScoreMain)



#Tic tac toe game
#


#makes variables
spot = [" "," "," "," "," "," "," "," "," "]
xChoice = 0
oChoice = 0
win_combinations = [
   [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
   [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
   [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

#makes our functions
def board():
  print(spot[0],"⏐",spot[1],"⏐",spot[2])
  print("--+--+----")
  print(spot[3],"⏐",spot[4],"⏐",spot[5])
  print("--+--+----")
  print(spot[6],"⏐",spot[7],"⏐",spot[8])

def checkWin(player):

  for combo in win_combinations:
   if all(spot[i] == player for i in combo):
    print( player , "wins!")
    exit()



def game2():

#prints board
  board()

  xChoice = input("player x where do you want to play(1-9):")
  xChoice = int(xChoice) - 1
  if spot[xChoice] == "o":
    print("you hecking cheater, program shutting down")
    exit()
  spot[xChoice] = "x"
  
  board()

  checkWin("x")

  oChoice = input("player o where do you want to play(1-9):")
  oChoice = int(oChoice) - 1
  if spot[oChoice] == "x":
    print("you hecking cheater, program shutting down")
    exit()
  spot[oChoice] = "o"

  checkWin("o")
  
  game2()


#pig dice game
def game3(playerScore,aiScore,two):
#variables
  start = 0
  options = [1,2,3,4,5,6,7,8,9,10]
  aiDrawn = random.choice(options)
  playerDrawn = random.choice(options)
  playerScore = playerScore + playerDrawn
  aiScore = aiScore + aiDrawn

#game loop
  start = input("Roll Next(hit enter):")
  if start == "":
    print("")
    print("player 1 drew-",playerDrawn,"  ",two,"drew-",aiDrawn)
    print("")
    print("player 1 score-",playerScore,"  ",two,"score-",aiScore)
    print("")
    aiScoreMain = aiScore
    playerScoreMain = playerScore
    if (playerScoreMain >= 30) and (aiScoreMain >= 30):
      print("players tied! Neat, shutting down now")
      exit()
    elif playerScoreMain >= 30:
      print("Player 1 wins! shutting down")
      exit()
    elif aiScoreMain >= 30:
      print(two, "wins! shutting down")
    else:
      game3(playerScoreMain,aiScoreMain,two)
      
  else:
    print("OH COME ON, YOU CAN'T JUST PRESS ENTER ITS NOT THAT HARD")
    exit()







#plays the games

#makes any needed variables
games = ["1","2","3","3.5"]

print("what game would you like to play(or enter random for a random one)\n")
print("1-rock paper scissors (1player)")
print("2-tic tac toe (2 player)")
print("3-pig dice game (1 player)")
print("3.5-pig dice game (2 player)")
print("")
choiceMain = input("enter number here:")


def check(choice):
  if choice == "random":
    print("choosing random")
    choice = random.choice(games)
    check(choice)
  elif choice == "1":
   print("booting up rock, paper, scissors")
   game1(playerScoreMain,aiScoreMain)
  elif choice == "2":
    print("booting up tic tac toe")
    game2()
  elif choice == "random":
    print("choosing random")
    choice = random.choice(games)
    check(choice)
  elif choice == "3":
    print("booting up pig dice game")
    print("Welcome to pig dice game get to thirty first to win")
    game3(playerScoreMain,aiScoreMain,"ai")
  elif choice == "3.5":
    print("booting up pig dice game 2 player")
    print("Welcome to pig dice game first person to thirty wins")
    game3(playerScoreMain,aiScoreMain,"player 2")
  else:
    print("that wasnt one of the options shutting down")
    exit()

check(choiceMain)
