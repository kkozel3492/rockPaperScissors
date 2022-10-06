import random
import Graphics


#Tell the user to choose rock, paper, or scissors

print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors")
userChoice = int(input("> "))
computerChoice = random.randint(0,3)

#Check user input
if userChoice >= 3 or userChoice <0:
    print("You typed an invalid number")
else:
    #Rock loop statements
    while userChoice == 0:
        print(f"You chose: \n {Graphics.rock}")
        if computerChoice == 0:
            print(f"Computer chose: \n {Graphics.rock}")
            print("Tie!")
            break
        elif computerChoice == 1:
            print(f"Computer chose: \n {Graphics.paper}")
            print("You Lose!")
            break
        else:
            print(f"Computer chose: \n {Graphics.scissors}")
            print("You Win!")
            break

    #Paper loop statements
    while userChoice == 1:
        print(f"You chose: \n {Graphics.paper}")
        if computerChoice == 0:
            print(f"Computer chose: \n {Graphics.rock}")
            print("You Win!")
            break
        elif computerChoice == 1:
            print(f"Computer chose: \n {Graphics.paper}")
            print("Tie!")
            break
        else:
            print(f"Computer chose: \n {Graphics.scissors}")
            print("You Lose!")
            break

    #Scissors loop statements
    while userChoice == 2:
        print(f"You chose: \n {Graphics.scissors}")
        if computerChoice == 0:
            print(f"Computer chose: \n {Graphics.rock}")
            print("You Lose!")
            break
        elif computerChoice == 1:
            print(f"Computer chose: \n {Graphics.paper}")
            print("You Win!")
            break
        else:
            print(f"Computer chose: \n {Graphics.scissors}")
            print("You Tie!")
            break

closeProgram = input("Press enter to close")