import random
opcje = ["Kamień", "Papier", "Nożyce"]
print(opcje)

scores = {"Player": 0, "Computer": 0}

def countPoints(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "The same choice!", 0
    elif (player_choice == "Kamień" and computer_choice == "Nożyce") or \
         (player_choice == "Papier" and computer_choice == "Kamień") or \
         (player_choice == "Nożyce" and computer_choice == "Papier"):
        scores["Player"] += 1
        return "You win!", 1
    else:
        scores["Computer"] += 1
        return "Computer wins!", -1

while True:
    print("\nWelcome to the Kamień, Papier, Nożyce! Choose your move:")
    print("K = Kamień")
    print("P = Papier")
    print("N = Nożyce")
    print("To exit, type 'end'")

    player_input = input("Enter your move: ")
    if player_input == "end":
        print("\nGoodbye!")
        break

    player_choice_dict = {"K": "Kamień", "P": "Papier", "N": "Nożyce"}
    player_choice = player_choice_dict.get(player_input)
    computer_choice = random.choice(opcje)

    if player_choice:
        print(f"Player choice: {player_choice}")
        print(f"Computer choice: {computer_choice}")

        message, result = countPoints(player_choice, computer_choice)
        print(message)
        print(f"Score - Player: {scores['Player']}, Computer: {scores['Computer']}")
    else:
        print("Invalid option! Please choose again.")
