import requests
import xmltodict
import sys

try:
    user_input = sys.argv[1]

    response = requests.get(f"https://boardgamegeek.com/xmlapi/boardgame/{user_input}?stats=1", verify=False)
    d = xmltodict.parse(response.content)
    curr_game = d["boardgames"]["boardgame"]
    print()

    print("id = " + curr_game["@objectid"])
    print()

    for name in curr_game["name"]:
        if "@primary" in name:
            print(name['#text'])
    if curr_game["minplayers"] == curr_game["maxplayers"]:
        player_count = curr_game["maxplayers"]
    else:
        player_count = curr_game["minplayers"] + " - " + curr_game["maxplayers"]
    print("Player Count: " + player_count)
    print("Description: " + curr_game["description"])
    print("Average Rating: " + curr_game["statistics"]["ratings"]["average"] + "/10")
    print("Weight: " + curr_game["statistics"]["ratings"]["averageweight"] + "/5")
    print()

    print("Categories = ", end="")
    for category in curr_game["boardgamecategory"]:
        print(category["#text"], end=", ")
    print()
    print("Game Mechanics = ", end="")
    for mechanic in curr_game["boardgamemechanic"]:

        print(mechanic["#text"], end=", ")
    print()
except requests.ConnectionError as e:
    print(e)
except IndexError:
    print("Missing an id, use search <name> to find an id for the game and then use that as your argument here")
