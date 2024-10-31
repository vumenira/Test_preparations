# Mountains Elevation Quiz - www.101computing.net/mountains-elevation-quiz/

import random

mountains = [["Mount Everest","Nepal / Tibet",8849],
             ["Mount K2","Pakistan / China",8611],
             ["Mount Aconcagua","Argentina",6959],
             ["Mount McKinley","Alaska, USA",6190],
             ["Mount Kilimanjaro","Tanzania",5895],
             ["Mount Kenya","Kenya",5199],
             ["Mount Blanc","France",4809],
             ["Mount Fuji","Japan",3776],
             ["Mount Etna","Italy",3369],
             ["Ben Nevis","Scotland, UK",1345]]

print("""

    /\\    /\\  /\\      /\\            /\\/\/\\  /\\
   /  \\/\\/  \/  \  /\\/  \\/\\  /\\  /\\/ / /  \\/  \\
  /    \\ \\  /    \/ /   /  \\/  \\/  \\  /    \\   \\
 /      \\  /     /     /    \\       \\       \\   \\
__________________________________________________

""")

print("You are going to play a game, try to guess the height of mountains. "
      "\nYour starting health is 10000, n you have 0 points."
      "\nLet's start!")

health = 10000
pts = 0

while True:
    peak = mountains[random.randint(0, len(mountains) - 1)]
    name = peak[0]
    location = peak[1]
    elevation = peak[2]
    guess = int(input(f"Guess the height of the {name} peak, which is located in {location}: "))
    health -= abs(guess - elevation)
    pts += 1
    print(f"It's {elevation}.")
    if health > 0:
        print(f"Remaining health is {health}. \nYou have {pts} points.")
    else:
        print("You've lost :-(")
        break



