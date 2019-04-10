import extraction
import transformation
import loader


def main():
    df1 = extraction.extract_csv("Data/2018NFLPlayerStatistics.csv")
    df2 = extraction.extract_csv("Data/PlayerSalaries.csv")
    df3 = extraction.extract_csv("Data/sportsref_download_AFC_2018.csv")
    df4 = extraction.extract_csv("Data/sportsref_download_NFC_2018.csv")
    transformation.clean_playerstats(df1)
    transformation.playersalaries(df2)
    tranformation.teamdata(df3,df4)
    # loader.loadzone()
    # print("Done!")

if __name__ == '__main__':
    main()
