import random
import math

choices = {"1": "Simple Interest", "2": "Compound Interest", "3": "Quit"}
while True:
    print("")
    print("Enter...")
    print("")
    playerchoice = input(
        "1 for Simple Interest\n"
        "2 for Compound Interest\n"
        "3 to quit\n"
        ""
        "Your choice: "
    )

    if playerchoice not in choices:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue
    if playerchoice == "3":
        print("Thanks for using the interest calculator! Goodbye!")
        break

    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time (in years): "))

    if playerchoice == "1":
        interest = (principal * rate * time) / 100
        total_amount = principal + interest
        print(f"Simple Interest: {interest:.2f}")
        print(f"Total Amount: {total_amount:.2f}")

    elif playerchoice == "2":
        n = int(input("Enter the number of times interest is compounded per year: "))
        total_amount = principal * (1 + (rate / (n * 100))) ** (n * time)
        interest = total_amount - principal
        print(f"Compound Interest: {interest:.2f}")
        print(f"Total Amount: {total_amount:.2f}")
