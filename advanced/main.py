import json

#json files
n = str(1)
json_file = "level_" + n + "_character.json"

#messages for inputs
level_up = "Do you want to level up? Type yes or no.\n"
attribute_choice = """You have three points to increase you attributes. What would you like to increase?
Strength | Dexterity | Constitution | Intelligence | Wisdom | Charisma\n"""


#list of attributes
attributes = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
]

#values for points
attribute_points = 3
selected_points = 0

#reads the level 1 character jason file
with open(json_file, "r") as file:
    data = json.load(file)

#loop to ask and assign new values to file
while True:
    try:
        level_up_input = input(level_up).strip().lower()
        if level_up_input == "no":
            print("You will remain at", data["level"])
        else:
            data["level"] += 1
            data["armor_class"] += 1
            print("You are now", data["level"], "with an armor class of", data["armor_class"])
#checkpoint to return to the start of the attribute select in order to assign values to multiple attributes
            while True:
                attribute_select = input(attribute_choice).strip().lower()
                for attribute in attributes:
                    if attribute_select == attributes:
                        selected_points += int(input(f"How many points do you want to assign to {attributes}. You have {attribute_points} left."))
                        if selected_points >= 0 and selected_points <= 3:
                            attribute_points -= selected_points
                            data[attributes] += selected_points
                            if attribute_points == 0:
                                print("you have no more points to spend")
                                break
    except ValueError:
        pass


with open("level_2_character.json", "w") as file:
    json.dump(data, file, indent=4)
