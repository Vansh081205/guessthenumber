import random
Target = random.randint(1,200)

while True:
    userchoice = (input("enter your number or quit(Q); "))
    if(userchoice=="Q"):
        print("PLAYER QUIET THE GAME")
      
    userchoice = int(userchoice)

    if(userchoice==Target):
        print("VICTORY!!!!!!:YOU HAVE GUESSED THE COREECT NUMBER")
        break
    elif(userchoice<Target):
        print("OOPS!!YOUR GUESS IS TO SMALL","\nTRY AGAIN")
    else:
        print("OOPS!!YOUR GUESS IS TO Large","\nTRY AGAIN")

print("----GAME OVER----")











