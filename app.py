import pandas as pd
from sqlalchemy import create_engine
import extraction
import transformation
import loader


if __name__ == '__main__':
    df1 = extraction.extract_csv("Data/2018NFLPlayerStatistics.csv")
    tdf = transformation.clean_playerstats()
    loader.loadzone()
    print("Done!")
