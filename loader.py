###################### Loading #######################
from sqlalchemy import create_engine


# Create a database connection


def loadzone():
    try:
        connection_name = "root:root@127.0.0.1/nfl_db"
        engine = create_engine(f'mysql+pymysql://{connection_name}')

# #Confirm tables
# def confirm():
#     return engine.table_names()

# Load dataframes into DATABASE
        player_data.to_sql(name='player_info', con=engine, if_exists='append', index=True)
        player_game_data.to_sql(name='player_game', con=engine, if_exists='append', index=True)
        player_passing_data.to_sql(name='player_passing', con=engine, if_exists='append', index=True)
        player_rushing_data.to_sql(name='player_rushing', con=engine, if_exists='append', index=True)
        player_receiving_data.to_sql(name='player_receiving', con=engine, if_exists='append', index=True)
        player_fumbles_data.to_sql(name='player_fumbles', con=engine, if_exists='append', index=True)
        player_scoring_data.to_sql(name='player_scoring', con=engine, if_exists='append', index=True)
        print("Completed")
    except:
        print("Failed")
