import random

real_inputs = "rps"

def get_inputs(player_count):
    user_1 = " "
    user_2 = " "

    while user_1 not in real_inputs:
        user_1 = input("Player 1, make your choice (r, p, s):\n").lower()

        # ensures the input is not just something like 'rps'
        if len(user_1) != 1:
            user_1 = " "

    if player_count == "2":
        while user_2 not in real_inputs:
            user_2 = input("Player 2, make your choice (r, p, s):\n").lower()
            if len(user_2) != 1:
                user_2 = " "

    else:
        user_2 = real_inputs[random.randrange(0, 3)]
        print("Player 2 chose: ", user_2, "\n")

    round_result(user_1, user_2)

def round_result(input1, input2):
    print("This round's result is: ")
    if input1 == input2:
        print("Draw!\n")
        return "0"

    else:

        # win conditions

        if (input1 == "r" and input2 == "s"):
            print("Player 1 wins!\n")
            return "1"
        if (input1 == "s" and input2 == "p"):
            print("Player 1 wins!\n")
            return "1"
        if (input1 == "p" and input2 == "r"):
            print("Player 1 wins!\n")
            return "1"
        else:
            print("Player 2 wins!\n")
            return "2"


def play_rps():
    p_count = ""
    play = "y"

    print("Welcome to Rock Paper Scissors!\n")
    while p_count != "1" and p_count != "2":
        p_count = input("Will there be 1 or 2 players?\n")

    while play == "y" or play == "yes":
        get_inputs(p_count)

        play = input("Continue? (y/n)\n").lower()
        if play == "n" or play == "no":
            print("Thank you for playing!")

        elif play!= "y" or play != "yes":
            # incase user makes a typo, will not close game
            play = input("Please enter a valid response. (y/n)\n").lower()




if __name__ == "__main__":
    play_rps()