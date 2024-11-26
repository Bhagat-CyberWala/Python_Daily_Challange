"""Using the random module the computer “thinks” about a whole number between 1 and 20.
The user has to guess the number. After the user types in the guess the computer tells if this was bigger or smaller than the number it generated, or if was the same.
The game ends after just one guess"""

import random

sys_no=random.randrange(1,21)
game_over=0
game_chance=0
while game_over==0:
    usr_no=int(input("Guess Number in between 1 to 20 : "))
    if usr_no >= sys_no:
        print("***You Have three chance ***")
        print("Your number is bigger then system")
        game_chance +=1
        if game_chance==3:
            print("Game Over")
            print(sys_no)
            game_over=1
        elif usr_no == sys_no :
            print("You won!")
            game_over=1
    else:
        print("you Lose !")
        print(sys_no)
        game_over = 1
