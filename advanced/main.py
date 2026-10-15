import json
while True:
    try:

        level = int(input("Which level would you like to level up from? "))
        filename = f"level_{level}_character.json"

        with open(filename, "r") as file:
            data = json.load(file)
            break
    except ValueError:
        print("Please enter a number.")
    except FileNotFoundError:
        print("Please enter a valid file.")



attributes = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma"
]

data["level"] += 1
data["armor_class"] += 1

while True:
    new_att = input("Which attribute would you like to increase? ")

    if new_att in attributes:
        data["attributes"][new_att] += 1
        break

    else:
        print("Invalid attribute name.")

new_skill = input("What skill would you like to add? ")
data["skills"].append(new_skill)

while True:
    weapon = input("Would you like a new weapon?")

    if weapon == "yes":
        ask_weapon = input("What weapon would you like to add? ")
        data["weapons"].append(ask_weapon)
        break

    elif weapon == "no":
        break

    else:
        print("Please enter yes or no.")

new_level = data["level"]

new_filename = f"level_{new_level}_character.json"

with open(new_filename, "w") as file:
    json.dump(data, file, indent=4)