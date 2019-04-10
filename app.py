import pandas as pd
from sqlalchemy import create_engine
import extraction
import transformation
import loader


if __name__ == '__main__':
    df1 = extraction.extract_csv("Data/2018NFLPlayerStatistics.csv")
    df2 = extraction.extract_csv("Data/PlayerSalaries.csv")
    df3 = extraction.extract_csv("Data/sportsref_download_AFC_2018.csv")
    df4 = extraction.extract_csv("Data/sportsref_download_NFC_2018.csv")
    transformation.clean_playerstats(df1)
    # loader.loadzone()
    # print("Done!")
