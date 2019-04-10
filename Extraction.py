#Import dependencies
import pandas as pd

def extractit():
    try:
        #Extract 2018 players data
        NFLPlayer2018_Data = "Data/2018NFLPlayerStatistics.csv"
        NFLPlayer2018_df = pd.read_csv(NFLPlayer2018_Data)
        NFLPlayer2018_df
        #Extract 2018 player salaries
        NFLPlayerSalaries = "Data/PlayerSalaries.csv"
        PlayerSalariesdf = pd.read_csv(NFLPlayerSalaries)
        NFLPlayer2018_df
        #Extract team data
        csv_file = "Data/sportsref_download_AFC_2018.csv"
        AFC_df = pd.read_csv(csv_file)
        NFLPlayer2018_df
        csv_file = "Data/sportsref_download_NFC_2018.csv"
        NFC_df = pd.read_csv(csv_file)
        NFLPlayer2018_df
        print("Completed")
    except:
        print("Failed")

extractit()
