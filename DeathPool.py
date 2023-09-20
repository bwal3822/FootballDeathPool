# Football Death Pool

import csv
import os
import pandas as pd
import numpy as np
# Initialize file path
csv_file_path = './data/FootballDeathPool.csv'
player_list_path = './data/PlayerList.xlsx'
player_list_df = pd.read_excel(player_list_path)
# Initialize the pool
def initialize_pool():
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            headers = ['Player', 'Status'] + [f"Week{i+1}" for i in range(18)]
            csvwriter.writerow(headers)


# Assuming an 18-week NFL season
initialize_pool(18)

# Weekly Game Outcome Path
weely_outcome_file_path = './data/WeeklyGameOutcome.csv'

# Initialize or load weekly_game_outcome_df
weekly_game_outcome_df = pd.read_csv('./data/WeeklyGameOutcome.csv')

# Show the first few lines of the initialized CSV to confirm its structure
pd.read_csv(csv_file_path).head()


#Enter Player Names player_pool locked for 2023season uncomment next year to add players
#def add_player(player_name):

#    with open(csv_file_path, 'a', newline='') as csvfile:

#        csvwriter = csv.writer(csvfile)

        # Set status as "active" when adding a new player

  #      csvwriter.writerow([player_name, 'active'] + ['' for _ in range(18)])



# Add a couple of sample players to demonstrate

#add_player('Player1')

#add_player('Player2')



# Show the first few lines of the CSV to confirm players have been added

#pd.read_csv(csv_file_path).head()

#Add existiong players to the pool

# Rename columns for easier access

player_list_df.columns = ['Player', 'Week1', 'Week2', 'Week3']



# Drop the first row since it's just another set of headers

player_list_df = player_list_df.iloc[1:].reset_index(drop=True)



# Initialize the pool again to reset the CSV

initialize_pool(18)



# Add players and their picks for Week 1 and Week 2 to the CSV

for index, row in player_list_df.iterrows():

    player_name = row['Player']

    week1_pick = row['Week1']

    week2_pick = row['Week2']

    # Determine the status based on Week 2 results

    status = 'eliminated' if player_name in ['Big Rich', 'Redneck'] else 'active'

    

    with open(csv_file_path, 'a', newline='') as csvfile:

        csvwriter = csv.writer(csvfile)

        # Add player information to CSV

        csvwriter.writerow([player_name, status] + [week1_pick, week2_pick] + [''\
            for _ in range(16)])



# Show the first few lines of the CSV to confirm players and their picks have been added

pd.read_csv(csv_file_path).head()

# List of players eliminated in Week 1 and Week 2
eliminated_week1 = ['Chief', 'Cochise', 'Bossman']
eliminated_week2 = ['Big Rich', 'Redneck']

# Load the current CSV into a DataFrame for updating
df = pd.read_csv(csv_file_path)

# Update the status and picks for players eliminated in Week 1 and Week 2
for player in eliminated_week1:
    df.loc[df['Player'] == player, 'Status'] = 'eliminated'
    df.loc[df['Player'] == player, 'Week 2':] = 'Eliminated'

for player in eliminated_week2:
    df.loc[df['Player'] == player, 'Week 3':] = 'Eliminated'

# Save the updated DataFrame back to the CSV
df.to_csv(csv_file_path, index=False)

# Show the first few lines of the updated CSV to confirm the changes
pd.read_csv(csv_file_path).head(10)

# Read Excel into DataFrame 
player_list_df = pd.read_excel(player_list_path)

# Initialize the 'Status' column with 'Active' for all players
player_list_df['Status'] = 'Active'
#testing New check_elimination function
def check_elimination(player_list_df, weekly_game_outcome_df, current_week):
    for index, row in player_list_df.iterrows():
        if row['Status'] == 'Active':
            player_pick = row[f"Week{current_week}"]
            outcome_row = weekly_game_outcome_df[
                (weekly_game_outcome_df['Week'] == current_week) & 
                (weekly_game_outcome_df['Team'] == player_pick)
            ]
            
            # Skip if the game has not been played yet
            if pd.isna(outcome_row['Team_Score'].values[0]) or pd.isna(outcome_row\
                        ['Opponent_Score'].values[0]):
                print(f"Game for {player_pick} in week {current_week} \
                      has not been played yet. Skipping.")
                continue
            
            # Determine the winner based on the Team_Score and Opponent_Score
            team_score = outcome_row['Team_Score'].values[0]
            opponent_score = outcome_row['Opponent_Score'].values[0]
            
            if team_score > opponent_score:
                continue  # Player moves to the next week
            else:
                player_list_df.at[index, 'Status'] = 'Eliminated'
                print(f"Player {row['Player']} is eliminated.")
        else:
            print(f"Player {row['Player']} is already eliminated. Skipping.")
            
    player_list_df.to_csv(csv_file_path, index=False)
    return player_list_df

#Enter Game Results
'''def check_elimination(player_list_df, weekly_game_outcome_df, current_week):
    # Inside check_elimination function
   
   for index, row in player_list_df.iterrows():
    if row['Status'] == 'Active':
        player_pick = row[str(current_week)]
        outcome_row = weekly_game_outcome_df[(weekly_game_outcome_df['Week']\
         == current_week) & (weekly_game_outcome_df['Team'] == player_pick)]
        
        # Skip if the game has not been played yet
        if np.isnan(outcome_row['Team_Score'].values[0]) or np.isnan(outcome_row\
                                                                     ['Opponent_Score'].values[0]):
            print(f"Game for {player_pick} in week {current_week}\
                   has not been played yet. Skipping.")
            continue
        
        # If the team picked by the player is found in the weekly outcome data
        if not outcome_row.empty:
            team_score = outcome_row['Team_Score'].values[0]
            opponent_score = outcome_row['Opponent_Score'].values[0]
            
            # Determine the winner based on the Team_Score and Opponent_Score
            if team_score > opponent_score and player_pick == outcome_row['Team']\
                .values[0]:
                continue  # Player moves to the next week
            elif team_score < opponent_score and player_pick != outcome_row['Team']\
                .values[0]:
                player_list_df.at[index, 'Status'] = 'Eliminated'
            else:
                print(f"Discrepancy found for {player_pick} in week {current_week}.\
                       Please double-check the data.")


    
    player_list_df.to_csv(csv_file_path, index=False)
    return player_list_df
   print(player_list_df.columns)'''
current_week = 2 # Change to current week

# Call check_elimination
updated_player_list_df = check_elimination\
    (player_list_df, weekly_game_outcome_df, current_week)
# Test the function with some sample game outcomes for Week 3
# Assuming Rams won and Bills lost in Week 3
sample_game_outcomes_week3 = {'Rams': 'Win', 'Bills': 'Lose'}
check_elimination(3, sample_game_outcomes_week3)

# Show the first few lines of the updated CSV to confirm the eliminations
pd.read_csv(csv_file_path).head(10)

#Player Eliminated

#Initialize WeeklyGameOutcome.csv with headers
weekly_game_outcome_csv_file_path = './data/WeeklyGameOutcome.csv'

def initialize_weekly_outcome():
    print("Initializing weekly outcome...")  # Debugging print statement
    try:
        if not os.path.exists(weekly_game_outcome_csv_file_path):
            with open(weekly_game_outcome_csv_file_path, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                headers = ['Week', 'Team', 'Team_Score', 'Opponent', 'Opponent_Score']
                csvwriter.writerow(headers)
        print("Weekly outcome initialized successfully.")  # Debugging print statement
    except Exception as e:
        print(f"An error occurred: {e}")  # Debugging print statement


initialize_weekly_outcome()



# Show the first few lines of the initialized CSV to confirm its structure
pd.read_csv(weekly_game_outcome_csv_file_path).head()

#Current status of all players
def display_current_status():
    # Load the current CSV into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Display the DataFrame for review
    return df

# Test the function to display the current status of all players in the pool
display_current_status().head(10)


#Show Picks of all players for all weeks

#Celebrate the winner
