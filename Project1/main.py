import random

# 1 for Snake, -1 for Water, 0 for Gun
options = {"s": 1, "w": -1, "g": 0}
names = {1: "Snake", -1: "Water", 0: "Gun"}

# Get user's input
youstr = input("Choose (s for Snake, w for Water, g for Gun): ").lower()

# Validate input
if youstr not in options:
    print("Invalid choice, Jani!")
else:
    you = options[youstr]
    computer = random.choice([1, -1, 0])

    print(f"You chose {names[you]} and Computer chose {names[computer]}")

    if computer == you:
        print("Draw 🤝")
    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        print("🎉 You Win!")
    else:
        print("💔 You Lose!")
