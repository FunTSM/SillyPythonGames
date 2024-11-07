from time import sleep
from random import randint

print("why hello there user! we should play a game. You got any ideas?")
sleep(2)
print("Ah! i got one, i will look away and you give the program a number, Then i will try and guess it! lets play")
sleep(1)
print("Just give me one sec to re configure some of my code, brb")
sleep(4)
print("")
print("All done, now just input a number 1-100. Dont worry i made it so i cant see this variable :P")
num = input("number:")
correct = False

while correct == False:
  try:
    num = int(num)
    correct = True
    if num > 100 or num <1:
      correct = False
      print("")
      print("I said a number 1-100 silly :)")
      num = input("Do a number 1-100 this time:")
  except:
    print("")
    print("thats not a number you silly goose:)")
    num = input("Pick a number this time:")

print("")
sleep(1)
print("now that you have a number chosen i am going to start guessing random numbers and you will confirm or deny if i guess yours")
sleep(1)

guess = 0

print("")
print("")
print("")

running = True
guessed = []

while running:
  guess = randint(1,99)
  while guess in guessed:
    guess = randint(1,99)
    

    
  ans = input("is your number "+str(guess)+"? [y/n]:")
  if ans == "y":
    print("No way, really! i'm gonna check the variable with your number to make sure you aren't trying to lie to me")
    sleep(3)
    print("")
    if guess == num:
      print("Hey, i really did guess it, thats so cool!")
    else:
      print("awww you liar, you got my hopes up for no reason :(")
    running = False
    
  if guess == num and ans == "n":
    print("")
    print("THE PROGRAM HAS DETECTED A USER ERROR")
    print("woah, what was that about. Give me one sec too look around the code some. BRB")
    sleep(3)
    print("ahh, thats the issue. I guessed your number and you said i got it wrong. Oh well, just restart the program to play again")
    running = False
  guessed.append(guess)
  new = False
