# Steam Game Information

import requests
from pprintpp import pprint as pp
from sys import argv

argv.pop(0)

query = " ".join(i for i in argv)

api_key = "BA9B426CFBE18C92A921E6B9487B83D6"

url = f"https://api.steampowered.com/IStoreService/GetAppList/v1/?key={api_key}&max_results=50000"

req = requests.get(url).json()

games = []
appids = []

for game in req["response"]["apps"]:
        games.append(game["name"])
        appids.append(game["appid"])

is_match = False

for game in games:
    if query == game:
	    is_match = True
	    appid_game = appids[games.index(query)]
	    game_info_url = f"http://store.steampowered.com/api/appdetails?appids={appid_game}"
	    price_req = requests.get(game_info_url).json()
	    try:
	    	controller = price_req[f'str(appid_game)']['data']['controller_support']
	    except:
	    	controller = 'None'
	    print(f"""Name: {price_req[str(appid_game)]['data']['name']}
AppID: {appids[games.index(query)]}
Developers: {price_req[str(appid_game)]['data']['developers']}
Publishers: {price_req[str(appid_game)]['data']['publishers']}
Release Date: {price_req[str(appid_game)]['data']['release_date']['date']}
Recommendations: {price_req[str(appid_game)]['data']['recommendations']['total']}
Required Age: {price_req[str(appid_game)]['data']['required_age']}
Controller Support: {controller}
Website: {price_req[str(appid_game)]['data']['website']}
Steam Store Url: https://store.steampowered.com/app/{appid_game}""")

if not is_match:
    print("I can't find this game, please make sure spelling is correct and the name of the game is exactly as it appears in the steam store")

