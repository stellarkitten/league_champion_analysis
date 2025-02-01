import requests
import csv

url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-summary.json"
response = requests.get(url)
data = response.json()

ids = [i["id"] for i in data]
ids.remove(-1)

rows = [["ID", "Name", "Alias", "Title", "Style", "Difficulty", "Damage Type", "Damage", "Durability", "Crowd Control", "Mobility", "Utility", "Primary Role", "Secondary Role", "Skins", "Passive"]]
for i in ids:
    print(i)

    url = f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/{i}.json"
    response = requests.get(url)
    data = response.json()

    name = data["name"]
    alias = data["alias"]
    title = data["title"]

    tactical_info = data["tacticalInfo"]
    style = tactical_info["style"]
    difficulty = tactical_info["difficulty"]
    damage_type = tactical_info["damageType"].removeprefix("k")

    playstyle_info = data["playstyleInfo"]
    damage = playstyle_info["damage"]
    durability = playstyle_info["durability"]
    crowd_control = playstyle_info["crowdControl"]
    mobility = playstyle_info["mobility"]
    utility = playstyle_info["utility"]

    roles = data["roles"]
    primary_role = roles[0]
    if len(roles) == 2:
        secondary_role = roles[1]
    else:
        secondary_role = ""

    skins = len(data["skins"])
    passive = data["passive"]["name"]

    row = [i, name, alias, title, style, difficulty, damage_type, damage, durability, crowd_control, mobility, utility, primary_role, secondary_role, skins, passive]
    rows.append(row)

with open("data/data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
