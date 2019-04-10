
import pandas as pd
from sqlalchemy import create_engine
import extraction


def clean_playerstats():
#PLAYER INFORMATION
#Dropping Nan from NFLPayer2018_df
    try:
        NFLPlayer2018_df=NFLPlayer2018_df.fillna(value=0)
        NFLPlayer2018_df

        #Player Information
        player_info_df=NFLPlayer2018_df[['Player', 'Player.1', 'Player.2','Player.3','Player.5']]
        player_info_df

        #Change header

        header=player_info_df.iloc[0]
        player_info_df=player_info_df[1:]
        player_info_df.columns=header

        #Rename Columns
        player_data=player_info_df.rename(columns = {'Rk':'Rank','Tm':'Team'})
        player_data=player_data.set_index('Rank')
        #Player and Game database

        player_game_df=NFLPlayer2018_df[['Player', 'Player.1','Player.2', 'Player.3','Games', 'Games.1']]

        #Change header
        header2=player_game_df.iloc[0]
        player_game_df=player_game_df[1:]
        player_game_df.columns=header2

        #Rename Columns
        player_game_data=player_game_df.rename(columns = {'Rk':'Rank','Tm':'Team'})
        player_game_data=player_game_data.set_index('Rank')

        #clean passing dataframe

        player_passing_df=NFLPlayer2018_df[['Player', 'Player.1','Player.2', 'Player.3','Passing', 'Passing.1','Passing.2', 'Passing.3', 'Passing.4' ]]

        #Change header
        header3=player_passing_df.iloc[0]
        player_passing_df=player_passing_df[1:]
        player_passing_df.columns=header3

        #Rename Columns
        player_passing_data=player_passing_df.rename(columns = {'Rk':'Rank','Tm':'Team'})
        player_passing_data=player_passing_data.set_index('Rank')

        #Player and receiving
        player_rushing_df=NFLPlayer2018_df[['Player', 'Player.1','Player.2', 'Player.3','Rushing', 'Rushing.1','Rushing.2', 'Rushing.3' ]]

        #Change header
        header4=player_rushing_df.iloc[0]
        player_rushing_df=player_rushing_df[1:]
        player_rushing_df.columns=header4

        #Rename Columns
        player_rushing_data=player_rushing_df.rename(columns = {'Rk':'Rank','Tm':'Team'})

        player_rushing_data=player_rushing_data.set_index('Rank')

        #Player and receiving
        player_receiving_df=NFLPlayer2018_df[['Player', 'Player.1','Player.2', 'Player.3','Receiving', 'Receiving.1','Receiving.2', 'Receiving.3' ]]

        #Change header
        header5=player_receiving_df.iloc[0]
        player_receiving_df=player_receiving_df[1:]
        player_receiving_df.columns=header5

        #Rename Columns
        player_receiving_data=player_receiving_df.rename(columns = {'Rk':'Rank','Tm':'Team'})
        player_receiving_data=player_receiving_data.set_index('Rank')

        #Player and fumbles
        player_fumbles_df=NFLPlayer2018_df[['Player', 'Player.1','Player.2', 'Player.3','Fumbles', 'Fumbles.1']]

        #Change header
        header6=player_fumbles_df.iloc[0]
        player_fumbles_df=player_fumbles_df[1:]
        player_fumbles_df.columns=header6

        #Rename Columns
        player_fumbles_data=player_fumbles_df.rename(columns = {'Rk':'Rank','Tm':'Team'})
        player_fumbles_data=player_fumbles_data.set_index('Rank')

        #Player and scoring
        player_scoring_df=NFLPlayer2018_df[['Player', 'Player.1','Player.2', 'Player.3','Scoring', 'Scoring.1']]

        #Change header
        header7=player_scoring_df.iloc[0]
        player_scoring_df=player_scoring_df[1:]
        player_scoring_df.columns=header7

        #Rename Columns
        player_scoring_data=player_scoring_df.rename(columns = {'Rk':'Rank','Tm':'Team'})
        player_scoring_data=player_scoring_data.set_index('Rank')

        #NFL SALARIES
        NFLPlayer2018_df['Full Name']=NFLPlayer2018_df['Player.1'].str.cat(NFLPlayer2018_df['Player.2'],sep=' ')

        PlayerSalariesdf['Full Name']=PlayerSalariesdf['First Name'].str.cat(PlayerSalariesdf['Last Name'],sep=' ')

        salaries2018_df = pd.merge(NFLPlayer2018_df, PlayerSalariesdf, on='Full Name')

        #Player Salary (SQL Table player_salary)
        player_salary_data=salaries2018_df[['First Name', 'Last Name', 'Team', 'Salary']]

        #TEAM DATA
        team_df = AFC_df.append(NFC_df)
        team_df = team_df.reset_index(drop=True)
        team_df = team_df.rename(columns = {"Tm":"Team"})
        team_df["Tm"] = ["NE","MIA","BUF","NYJ","BAL","PIT","CLE","CIN","HOU","IND","TEN","JAX","KC","LAC","DEN","OAK","DAL",
                         "PHI","WAS","NYG","CHI","MIN","GB","DET","NO","CAR","ALT","TB","LAR","SEA","SF","ARI"]
        team_df.columns
        team_df = team_df[['Team', 'Tm', 'W', 'L', 'T', 'W-L%', 'PF', 'PA', 'PD', 'MoV', 'SoS', 'SRS',
               'OSRS', 'DSRS']]

    except:
        print("failed")

if __name__ == '__main__':
    clean_playerstats()
