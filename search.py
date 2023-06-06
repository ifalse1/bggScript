import requests
import xmltodict
import sys


def printGame(boardgames):
    for key, value in boardgames.items():
        if isinstance(value, dict):
            print(key + " = " + value["#text"])
        else:
            print(key + " = " + value)


try:
    original_user_input = sys.argv[1:]
    user_input = "+".join(original_user_input)

    response = requests.get(f"https://boardgamegeek.com/xmlapi/search?search={user_input}", verify=False)
    d = xmltodict.parse(response.content)
    boardgame_list = d["boardgames"]["boardgame"]
    print()  # Prints new line to separate from error message
    if isinstance(boardgame_list, list):
        for boardgame in boardgame_list:
            printGame(boardgame)
            print()
    else:
        printGame(boardgame_list)
except requests.ConnectionError as e:
    print(e)
except IndexError:
    print("Missing argument, try search.py <arg>")
