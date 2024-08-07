# this is stone paper scissor game
def play_comp():  # when user input 1
    l = ["Stone", "Paper", "Scissor"]  # "stone paper scissor
    import random
    c = random.choice(l)
    print("....play with computer....")
    print("ENTER S FOR STONE, P FOR PAPER, SC FOR SCISSOR")
    p = input("YOUR TURN..\n")
    print(p)
    if p in ["s", "S", "p", 'P', 'sc', 'SC']:
        if p == "s" or "S" and c == "Scissor" or p == "p" or "P" and c == "Stone" or p == "sc" or "SC" and c == "Paper":

            print("Computer:", c, "/", "You:", p)
            print("YOU WON..!")

        elif p == "s" or "S" and c == "Paper" or p == "p" or "P" and c == "Scissor" or p == "sc" or "SC" and c == "Stone":

            print("Computer:", c, "/", "You:", p)
            print("YOU LOSS..!")

        elif p == "s" or "S" and c == "Stone" or p == "p" or "P" and c == "Paper" or p == "sc" or "SC" and c == "Scissor":

            print("Computer:", c, "/", "You:", p)
            print("TIE..!")
    else:
        print("enter valid input\n")
        play_comp()


def play_friend():  # when user input any key
    print("....play with friend....")
    print("'ENTER S FOR STONE, P FOR PAPER, SC FOR SCISSOR'")
    p1 = input("PLAYER ONE TURN..\n")
    p2 = input("PLAYER TWO TURN..\n")
    if p1 and p1 in ["s", "S", "p", "P", "sc", "SC"]:
        if p1 in "s" or "S" and p2 == "sc" or "SC" or p1 == "p" or "P" and p2 == "s" or "S" or p1 == "sc" or "SC" and p2 == "p" or "p":
            print("PLAYER ONE WON..!\n")
        elif p1 == "s" or "S" and p1 == "p" or "P" or p1 == "p" or "P" and p1 == "sc" or "SC" or p1 == "sc" or "SC" and p2 == "s" or "S":
            print("PLAYER TWO WON..!\n")
        elif p1 == "s" or "S" and p2 == "s" or "S" or p1 == "p" or "P" and p2 == "p" or "P" or p1 == "sc" or "SC" and p2 == "sc" or "SC":
            print("TIE..!")
    else:
        print("enter valid input\n")
        play_friend()


def game(n):  # when game is started
    while n != "e" or "E":
        print("1 TO PLAY WITH COMPUTER")
        print("ANY TO PLAY WITH FRIEND")
        play = input("--\n")
        if play == "1":
            play_comp()

        else:
            play_friend()

        n = input("ENTER E TO EXIT OR ANY KEY TO PLAY AGAIN \n")
        if n == ("e" or "E"):
            break
        else:
            start()


def start():  # to start game
    print("...STONE PAPER SCISSOR....\n")
    n = input("PRESS 'S' TO START THE GAME :\n")
    if n != ("s" or "S"):
        print("enter the valid input")
        start()
    else:
        game(n)


# beginning of the code
start()
