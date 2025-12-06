from bs4 import BeautifulSoup as BS
import requests
import pandas

url = "https://steamunlocked.org/"

reply = requests.get(url)

gameWebsite = BS(reply.text, features="html.parser")

recentGames = gameWebsite.find_all("a", class_="cover-item")

gamesLink = []
if recentGames:
    for link in recentGames:
        gamesLink.append(link.get("href"))
else:
    print("No recent games found")

gameDataFrame = pandas.DataFrame(gamesLink)

gameDataFrame.to_csv("Recently_Added_Games.csv")
