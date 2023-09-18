# Football Death Pool
from calendar import week
import csv
import os
import pandas as pd
# Initialize file path
csv_file_path = '/mnt/data/FootballDeathPool.csv'

def initialize_pool(weeks):
    # Create CSV file and write headers
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            headers = ['Player', 'Status'] + [f"Week {i+1}" for i in range(weeks)]
            csvwriter.writerow(headers)

# Assuming an 18-week NFL season
initialize_pool(18)

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

#Enter Game Results
def check_elimination(week, game_outcomes):
    # Load the current CSV into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Iterate through each player to check for elimination
    for index, row in df.iterrows():
        player_name = row['Player']
        player_status = row['Status']
        player_pick = row[f"Week {week}"]
        
        # Skip if the player is already eliminated
        if player_status == 'eliminated':
            continue
        
        # Update status if the player's pick lost
        if game_outcomes.get(player_pick) == 'Lose':
            df.loc[index, 'Status'] = 'eliminated'
            df.loc[index, f"Week {week+1}:"] = 'Eliminated'
    
    # Save the updated DataFrame back to the CSV
    df.to_csv(csv_file_path, index=False)

# Test the function with some sample game outcomes for Week 3
# Assuming Rams won and Bills lost in Week 3
sample_game_outcomes_week3 = {'Rams': 'Win', 'Bills': 'Lose'}
check_elimination(3, sample_game_outcomes_week3)

# Show the first few lines of the updated CSV to confirm the eliminations
pd.read_csv(csv_file_path).head(10)

#Player Eliminated

#Initialize WeeklyGameOutcome.csv with headers
weekly_game_outcome_csv_file_path = '/mnt/data/WeeklyGameOutcome.csv'

def initialize_weekly_game_outcome(weeks):
    # Create CSV file and write headers
    if not os.path.exists(weekly_game_outcome_csv_file_path):
        with open(weekly_game_outcome_csv_file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            headers = ['Week'] + [f"Game {i+1}" for i in range(weeks)]
            csvwriter.writerow(headers)

#initialize the WeeklyGameOutcome.csv file
initialize_weekly_game_outcome()

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
