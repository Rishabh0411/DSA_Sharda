import random

def door1_condition(number):
    return number % 3 == 2 and number % 5 == 3 and number % 7 == 2 and number < 200

def door2_condition(n):
    return n % 6 == 0 and (n + 4) % 8 == 0 and (n - 3) % 5 == 0 and n % 4 == 2 

def play_game():
    energy_points = 100
    print("Welcome to the Door Challenge!")
    print("Rules: Solve the condition for the door to progress. Wrong guesses deduct 5 points. Clearing the door grants 20 points. You can request one hint.")

    # Door 1
    print("\nDoor 1: Guess the number.")
    hint_used = False

    while True:
        if energy_points <= 0:
            print("You have no energy left. Game over!")
            return

        guess = input("Enter your guess (or type 'hint' for a hint): ")
        if guess.lower() == "hint":
            if not hint_used:
                print("Hint: The number satisfies Chinese Remainder Theorem")
                hint_used = True
            else:
                print("You have already used your hint for this door.")
            continue

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if door1_condition(guess):
            print("Correct! You cleared the door.")
            energy_points += 20
            break
        else:
            print("Wrong guess.")
            energy_points -= 5

        print(f"Energy points remaining: {energy_points}")

    # Door 2
    print("\nDoor 2: Guess the number.")
    hint_used = False

    while True:
        if energy_points <= 0:
            print("You have no energy left. Game over!")
            return

        guess = input("Enter your guess (or type 'hint' for a hint): ")
        if guess.lower() == "hint":
            if not hint_used:
                print("Hint: The number satisfies Chinese Remainder Theorem")
                hint_used = True
            else:
                print("You have already used your hint for this door.")
            continue

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if door2_condition(guess):
            print("Correct! You cleared the door.")
            energy_points += 20
            break
        else:
            print("Wrong guess.")
            energy_points -= 5

        print(f"Energy points remaining: {energy_points}")

    print(f"Congratulations! You cleared both the doors with {energy_points} energy points remaining.")
    print("JACKPOT!!!!")

if __name__ == "__main__":
    play_game()