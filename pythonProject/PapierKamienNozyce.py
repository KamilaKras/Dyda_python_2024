import random

opcje = ["Kamien", "Papier", "Nozyce"]
print(opcje)

def countPoints(player, computer):
    if player == "K":
        xx


while True:
    print("\n")
    print("Welcome to the Kamień, Papier, Nożyce! Choose your move:")
    print("K = Kamień")
    print("P = Papier")
    print("N = Nożyce")
    print("To exit, type 'end'")

    playerChoice = input("Enter your move: ")
    computerChoice = random.choice(opcje)
    print(f"Player choice: {playerChoice}")
    print(f"Computer choice: {computerChoice}")

    if playerChoice == "end":
        print("\nGoodbye!")
        break

    if playerChoice in [opcje]:
        print("\nGreat")
        choice = input("Enter first number: ")
        if playerChoice == "K":

        elif playerChoice == "P":

        elif playerChoice == "N":


    else:
        print("Invalid option! Please choose again.")
