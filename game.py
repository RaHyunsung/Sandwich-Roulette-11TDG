import random
import math

# ---------- GLOBAL VARIABLES ----------

ITEMS = [
    'MTI',           # Heal 1 health bar
    'Detector',      # Detects poison in the current sandwich
    'Synergist',     # If the current sandwich is poisoned the damage will be doubled, if the sandwich is normal nothing happens
    'Sleep pills',   # Skips the enemy players next turn
    'Milk',          # Skip the current sandwich
    'Reversor'       # Reverses the current sandwich, normal becomes poisoned and poisoned becomes normal.
]

# ---------- GAME FUNCTIONS MODULE ----------

class Core:
    def getSandwiches(round):
        round += 1
        sandwiches = []
        total_poisoned_sandwiches = round
        total_normal_sandwiches = round
        total_random_sandwiches = round
        for poisoned_sandwiches in range(total_poisoned_sandwiches):
            sandwiches.append(1)
        for normal_sandwiches in range(total_normal_sandwiches):
            sandwiches.append(0)
        for random_sandwiches in range(total_random_sandwiches):
            sandwiches.append(random.randint(0, 1))
        random.shuffle(sandwiches)
        return sandwiches
    
    def getItems(round, item_list:list):
        items = []
        for i in range(round+2):
            choosen_item = random.choice(item_list)
            items.append(choosen_item)
        return items
    
    def getItems(round, item_list:list):
        items = []                                      # Define a item list using equal symbol with straight brackets []
        for i in range(round+2):                        # Repeat round+2 times which can be 1+2=3, 2+2=4, 3+2=5, ...
            choosen_item = random.choice(item_list)     # Define a random item that is choosen from item_list and put it in to choosen_item variable using random.choice
            items.append(choosen_item)                  # Add choosen_item variable in to the defined item list using .append
        return items                                    # Give the list back
        

for i in range(3):
    print(f"[+] Round {i+1}: {Core.getSandwiches(i)}")
    print(f"Items: {Core.getItems(i, ITEMS)}")

for i in range(3):
    