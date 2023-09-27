from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Read initial data
player_list_df = pd.read_excel('../data/PlayerList.xlsx')
weekly_game_outcome_df = pd.read_csv('../data/WeeklyGameOutcome.csv')
football_death_pool_df = pd.read_csv('../data/FootballDeathPool.csv')

# Placeholder for your check_elimination logic
def check_elimination_logic(player_list_df, weekly_game_outcome_df, current_week):
    # Your existing logic for checking eliminations goes here.
    # Replace the following line with your actual logic and return the updated DataFrame.
    updated_player_list_df = player_list_df.copy()
    return updated_player_list_df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/players')
def players():
    return render_template('players.html')

@app.route('/status')
def status():
    global football_death_pool_df
    player_status = dict(zip(football_death_pool_df['Player'], football_death_pool_df['Status']))
    return render_template('status.html', player_status=player_status)

@app.route('/check-elimination', methods=['POST'])
def check_elimination():
    global football_death_pool_df
    current_week = 3  # This would ideally be dynamic based on actual game weeks
    football_death_pool_df = check_elimination_logic(player_list_df, weekly_game_outcome_df, current_week)
    football_death_pool_df.to_csv('../data/FootballDeathPool.csv', index=False)
    return 'Checked for eliminations.'

if __name__ == '__main__':
    app.run(debug=True)
