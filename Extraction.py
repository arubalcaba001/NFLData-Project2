#Import dependencies
import pandas as pd

#Extract 2018 players data
NFLPlayer2018_Data = "Data/2018NFLPlayerStatistics.csv"
NFLPlayer2018_df = pd.read_csv(NFLPlayer2018_Data)

#Extract 2018 player salaries
NFLPlayerSalaries = "Data/PlayerSalaries.csv"
PlayerSalariesdf = pd.read_csv(NFLPlayerSalaries)

#Extract team data
csv_file = "../team/sportsref_download_AFC_2018.csv"
AFC_df = pd.read_csv(csv_file)

csv_file = "../team/sportsref_download_NFC_2018.csv"
NFC_df = pd.read_csv(csv_file)
