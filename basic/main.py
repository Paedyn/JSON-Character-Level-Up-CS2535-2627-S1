import json

with open("level_1_character.json", "r") as file:
    data = json.load(file)

data["level"] += 1
data["armor_class"] += 1
data["attributes"]["strength"] += 2
data["attributes"]["constitution"] += 1
data["skills"].append("survival")
data["weapons"].append("Silver_Dagger")

with open("level_2_character.json", "w") as file:
    json.dump(data, file, indent=4)


