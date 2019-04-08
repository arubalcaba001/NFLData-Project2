#Import dependencies
import pandas as pd
from bs4 import BeautifulSoup
import requests

#Extract 2018 players data
NFLPlayer2018_Data = "Data/2018NFLPlayerStatistics.csv"
NFLPlayer2018_df = pd.read_csv(NFLPlayer2018_Data)

#Extract 2018 player salaries
NFLPlayerSalaries = "Data/PlayerSalaries.csv"
PlayerSalariesdf = pd.read_csv(NFLPlayerSalaries)

#Still deciding whether to keep this part
#Extract entire win/loss records (all years)
url = "https://en.wikipedia.org/wiki/List_of_all-time_NFL_win%E2%80%93loss_records#Combined_regular_season_and_playoffs"
#source = requests.get(url).text
dfs = pd.read_html(url)
