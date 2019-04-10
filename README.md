NFLData-Project2

Extraction

You can also web scrape from the three websites if you do not want to store the data locally.  However in the interest of time we download
CSV

NFL Player Statistics 
Download CSV files for Player Statistics from n\
https://www.pro-football-reference.com/years/2018/fantasy.htm n\
Go to share&more and get table as CSV and download
In CSV had to separate player column to first name and last name with text-column function
save as 2018NFLPlayerStatistics.csv

NFL Player Salary
Download CSV files for Player Salary from 
https://www.pro-football-reference.com/players/salary.htm 
Go to share&more and get table as CSV and download
In CSV had to separate player column to first name and last name with text-column function
save as PlayerSalaries.csv

NFL Team Information 
https://www.pro-football-reference.com/years/2018/
Download CSV files for both AFC and NFC 
Go to share&more and get table as CSV and download
Team Accronyms from wikipidia
save as sportsref_download_AFC_2018.csv and sportsref_download_NFC_2018.csv 

Tranformation 

NFL Player Statistics
Fill in NaN with 0
Keep the headings of Player, Games,Passing,Rushing, Receiving,Fumbles, 
Scoring as this will help guide you to create tables

Create the following databases to convert them into Tables
Table: player_info
Grab all of the columns that have player in the heading 
Remove that header and you are left with a new Header
Rename columns RK to Rank and Tm to Team

Table: player_info
Grab columns: 'Player', 'Player.1', 'Player.2','Player.3','Player.5'
Remove that header and you are left with a new Header
Rename columns RK to Rank and Tm to Team

Table: player_game_data
Grab columns: 'Player', 'Player.1','Player.2', 'Player.3','Games', 'Games.1''Player', 'Player.1', 'Player.2','Player.3','Player.5'
Remove that header and you are left with a new Header
Rename columns RK to Rank and Tm to Team

Table: player_passing_data
Grab columns:'Player', 'Player.1','Player.2', 'Player.3','Passing', 'Passing.1','Passing.2', 'Passing.3', 'Passing.4'
Remove that header and you are left with a new Header
Rename columns RK:Rank, Tm:Team, Int: IT

Table: player_rushing_data
Grab columns: 'Player', 'Player.1','Player.2', 'Player.3','Rushing', 'Rushing.1','Rushing.2', 'Rushing.3'
Remove that header and you are left with a new Header
Rename columns RK:Rank, Tm:Team,Y/A:YA_rate

Table: player_receiving_data
Grab columns: 'Player', 'Player.1','Player.2', 'Player.3','Receiving', 'Receiving.1','Receiving.2', 'Receiving.3' 
Remove that header and you are left with a new Header
Rename columns RK:Rank, Tm:Team,Y/A:YA_rate

Table: player_fumbles_data
Grab columns: 'Player', 'Player.1','Player.2', 'Player.3','Fumbles', 'Fumbles.1'
Remove that header and you are left with a new Header
Rename columns RK:Rank, Tm:Team

Table: player_scoring_data
Grab columns: 'Player', 'Player.1','Player.2', 'Player.3','Scoring', 'Scoring.1'
Remove that header and you are left with a new Header
Rename columns RK:Rank, Tm:Team


NFL Player Salary
Create Column for Full Name and combine
Merge NFLPlayer data base with Player Salary

NFL Team Information
Rename columns Tm:Team
Enter Team Acronyms to match up with Team Name
Grab the following to make a database: 'Team', 'Tm', 'W', 'L', 'T', 'W-L%', 'PF', 'PA', 'PD'

Load 

Create Schema with Schema file
Create the following tables using your above database
player_info
player_game_data
player_passing_data
player_rushing_data
player_receiving_data
player_fumbles_data
player_scoring_data
player_salary
team

