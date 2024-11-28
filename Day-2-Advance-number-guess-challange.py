"""Exercise: Number guessing game
Level 0
• Using the random module the computer “thinks” about a whole number between 1 and 20.
• The user has to guess the number. After the user types in the guess the computer tells if this
was bigger or smaller than the number it generated, or if was the same.
• The game ends after just one guess.
Level 1
• The user can guess several times. The game ends when the user guessed the right number.
Level 2
• If the user hits ‘x’, we leave the game without guessing the number.
Level 3
• If the user presses ‘s’, show the hidden value (cheat)
Level 4
• Soon we’ll have a level in which the hidden value changes after each guess. In oredr to make
that mode easier to track and debug, first we would like to have a “debug mode”.
• If the user presses ‘d’ the game gets into “debug mode”: the system starts to show the current
number to guess every time, just before asking the user for new input.
• Pressing ‘d’ again turns off debug mode. (It is a toggle each press on “d” changes the value to
to the other possible value.)
Level 5
• The ‘m’ button is another toggle. It is called ‘move mode’. When it is ‘on’, the hidden number
changes a little bit after every step (+/-2). Pressing ‘m’ again will turn this feature off.
Level 6
• Let the user play several games.
• Pressing ‘n’ will skip this game and start a new one. Generates a new number to guess

"""







# txt='hello world'
# for i in txt:
#     print(i)


# list=["Apple","Banana", "Orange", "Papaya", "Grapes"]
# for fruits in list:
#     print(fruits)


"""for loop  on range"""
# for i in range(3,7):
#     print(i)

"""for in loop with early end using break"""
# txt="hello World"
# for i in txt:
#     if i==" ":
#         break
#     print(i)


"""for in loop skipping parts using continue"""
# txt='hello world'
# for i in txt:
#     # if i==" " or i=="w": #botho 26 and 27 lline are same working
#     if i in [" ","w","o"]:
#         continue
#     print(i)

"""While loop"""
# import random
# total=0
# while total <=100:
#     total += random.randrange(20)
#     print(total)

# print("Done : " + str(total))

"""Infinite while loop"""
# i=1
# while True:
#    i +=1
#    print(i) 

"""Break with while loop"""

# import random
# total=0
# while True:
#     print(total)
#     total +=random.randrange(20)
#     if total >=10000000:
#         print("1st")
#         break
#     if total %17==1:
#         print("2nd")
#         break
#     if total**2%23==7:
#         print("3rd")
#         break
# print("done : " +str(total))

"""check str type"""

# a = "hi"
# print(type(a))

# if type(a)==str:
#     print(True)
# else:
#     print(False)


import random
sys_no=random.randrange(1,21)

def game_menu():
    print("""
        Press x to exit
        press s to show the hidden value
        press d to 'debug mode '
        press m to 'move mode'
        press n to restart """)

    print("""
          Game Start""")


def move_mode():
    print("""               You entered in move mode
            Press m agian to Exit in 'Move Mode'""")
    symb=[-2,2]
    sys_value1=sys_no + int(random.choice(symb))
    while True:
        usr=input("Enter your Guess Number in between 1 to 20 : ")
        if usr=='m':
            print("Move Mode Exited")
            game_start()
        if int(usr) !=sys_value1:
            print("try Again")
            continue
        else:
            print("Conguralations you got the The number")
            exit()
            

def game_start():
    usr=input("Enter your Guess Number in between 1 to 20 : ")
    debug=False
    while True:
        if usr=='x':
            print("""
                  Bye! Bye! """)
            exit()
        elif usr =='s' :
            print("this is cheat value : " +str(sys_no))
            game_start()
        elif usr == 'd':
            debug = not debug
            if debug:
                print("Debug : " + str(sys_no))
                game_start()
        elif usr == 'm':
            move_mode()
        elif usr=='n':
            print('Game Restarted')
            restart()
        elif int(usr)!=sys_no:
            print("Wrong Guess")
            game_start()
        else:
            print("Conguralations you got the The number")
            exit()

def restart():
    global sys_no 
    sys_no = random.randrange(1,21)
    main()
def main():
    game_menu()
    game_start()
    
try:
    main()
except:
    print("you enter wrong Value please enter correct value ")
    restart()
