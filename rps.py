def check_player(player):
    if player == "rock" or player == "paper" or player == "scissors":
        return True


def talker (i):
    if i == 0:
        return "choose your fighter!!!: "
    elif i == 1:
        return "please choose rock, paper or scissors case sensitive, thanks: "
    elif i == 2:
        return "ok mate lets not make harder for the both of us, choose now or else!"
    elif i == 3:
        return str("you fucking piece of shit, why dont you just choose? \n now choose: ")
    elif i == 4:
        return "you have 5 more attempts"
    elif i == 5:
        return "4"
    elif i == 6:
        return "3"
    elif i == 7:
        return "2"
    elif i == 8:
        return "1"
    elif i == 9:
        return "you are stupidf"



def choose2(player):
    for i in range(10):
        if i == 9:
            print("game over for you")
            return "stupid"
        player = "blank"
        if player == "blank":
            print(talker(i))
            player = str(input(" "))

        if check_player(player):
            return player





def choose(player):
    while True:
        player = "blank"
        if player == "blank":
            print("you need to choose: ")
            player = str(input(" "))

        if check_player(player):
            return player

        else:
            print("choose again")
            continue


def match(a, b):
    if a == b:
        return "no one"
    if a == "stupid":
        return b
    if b == "stupid":
        return a
    if a == "rock":
        if b == "scissors":
            return a
        else:
            return b
    elif a == "paper":
        if b == "rock":
            return a
        else:
            return b
    elif a == "scissors":
        if b == "rock":
            return b
        else:
            return a


def game():
    player1 = "blank"
    player2 = "blank"
    print("player 1")
    player1 = choose2(player1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("player 2 ")
    player2 = choose2(player2)

    print(player1, "vs", player2)
    print(str(match(player1, player2)), "wins")


game()

while True:
    again = "yes"
    again = input("again?")
    # print(again)
    if again == "yes":
        game()
    else:
        print("goodbye")
        break
