from flask import Flask, render_template, request, jsonify
import pandas as pd
from DeathPool import check_elimination  # Importing the function from DeathPool.py

app = Flask(__name__)

@app.route('/')
def index():
    # Read the player data from the Excel file
    player_list_df = pd.read_excel('../data/PlayerList.xlsx')
    
    # Filter the DataFrame to get only the active players
    active_players_df = player_list_df[player_list_df['Status'] == 'Active']
    
    # Convert the DataFrame to a dictionary
    active_players_dict = active_players_df[['Player', 'Status']].to_dict('records')
    
    return render_template('index.html', active_players=active_players_dict)



@app.route('/players')
def players():
    # Read the player data from the Excel file
    player_list_df = pd.read_excel('../data/PlayerList.xlsx')
    
    # Convert the DataFrame to a dictionary
    players_dict = player_list_df[['Player', 'Status']].to_dict('records')
    
    return render_template('players.html', players=players_dict)



@app.route('/status')
def status():
    # FootballDeathPool.csv source of truth
    df = pd.read_csv('../data/FootballDeathPool.csv')  
    player_status = dict(zip(df['Player'], df['Status']))
    return render_template('status.html', player_status=player_status)

@app.route('/check-elimination', methods=['POST'])
def check_elimination_route():
    player_list_df = pd.read_excel('../data/PlayerList.xlsx')
    weekly_game_outcome_df = pd.read_csv('../data/WeeklyGameOutcome.csv')
    current_week = 3  # In future, make dynamic
    updated_player_list_df = check_elimination(player_list_df, weekly_game_outcome_df, current_week)
    updated_player_list_df.to_csv('../data/FootballDeathPool.csv', index=False)
    # update the FootballDeathPool.csv and PlayerList.xlsx files here
    
    return 'Checked for eliminations.'
@app.route('/pool_status')
def pool_status():
    player_list_df = pd.read_excel('../data/PlayerList.xlsx')

    #Convert Dataframe to dictionary
    player_dict = player_list_df.to_dict('records')

    return render_template('pool_status.html', players=player_dict)

@app.route('/view_picks')
def view_picks():
    player_list_df = pd.read_excel('../data/PlayerList.xlsx')
    player_picks_dict = {}
    for index, row in player_list_df.iterrows():
        player_name = row['Player']
        status = row['Status']
        player_picks = row.drop(['Player', 'Status']).apply(lambda x: x if pd.notna(x) else 'N/A').to_dict()
    
    # Note the week of elimination if the player is eliminated
    if status == 'Eliminated':
        for week in range(1, 19):
            if player_picks[f"Week{week}"] == 'N/A':
                player_picks[f"Week{week}"] = f"DiedWeek{week - 1}"
                break
    
    player_picks_dict[player_name] = {'Status': status, 'Picks': player_picks}

    print(player_picks_dict) #Debug
    return render_template('view_picks.html', players_picks=player_picks_dict)



if __name__ == '__main__':
    app.run(debug=True)
