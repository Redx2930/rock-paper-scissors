import random

choices = {"1": "rock", "2": "paper", "3": "scissors", "4": "quit"}

while True:
    print("")
    print("Enter...")
    print("")
    playerchoice = input(
        "1 for rock\n"
        "2 for paper\n"
        "3 for scissors\n"
        "4 to quit\n"
        ""
        "Your choice: "
    )

    if playerchoice not in choices:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        continue
    if playerchoice == "4":
        print("Thanks for playing! Goodbye!")
        break

    computerchoice = str(random.randint(1, 3))

    print("")
    print("You chose:", choices[playerchoice])
    print("Python chose:", choices[computerchoice])
    print("")

    if playerchoice == computerchoice:
        print("***************")
        print("It's a tie!")
        print("***************")

    elif (
        (playerchoice == "1" and computerchoice == "3")
        or (playerchoice == "2" and computerchoice == "1")
        or (playerchoice == "3" and computerchoice == "2")
    ):

        print("***************")
        print("You win!")
        print("***************")

    else:

        print("***************")
        print("Python wins!")
        print("***************")
