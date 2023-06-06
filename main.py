import requests
import xmltodict
import sys

input = sys.argv[1]
print(input)

try:
    response = requests.get(f"https://boardgamegeek.com/xmlapi/search?search={input}", verify=False)
    print(response.status_code)
    dict = xmltodict.parse(response.content)
    print(dict)
    for i in dict["boardgames"[1]]:
        print(i)
except requests.ConnectionError as e:
    print(e)

