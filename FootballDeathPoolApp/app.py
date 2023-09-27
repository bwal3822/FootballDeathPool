from flask import Flask, render_template, request, jsonify
import pandas as pd
from DeathPool import check_elimination  # Importing the function from DeathPool.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/players')
def players():
    return render_template('players.html')

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
    current_week = 3  # This could be dynamic based on the actual current week
    updated_player_list_df = check_elimination(player_list_df, weekly_game_outcome_df, current_week)
    
    # update the FootballDeathPool.csv and PlayerList.xlsx files here
    
    return 'Checked for eliminations.'

if __name__ == '__main__':
    app.run(debug=True)
