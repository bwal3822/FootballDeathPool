# Football Death Pool
import csv
import os

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


#Enter Player Names

#Enter Player Picks

#Enter Game Results

#Player Eliminated

#Player Wins

#Show Picks of all players for current week

#Show Picks of all players for all weeks

#Celebrate the winner
