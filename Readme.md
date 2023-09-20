
# Football Death Pool Program

## Introduction
This program is designed to manage a Football Death Pool game. In this game, participants choose one team per week that they believe will win their game. If the chosen team loses, the participant is eliminated from the pool. The game continues until one participant remains.

## Features
- Initialize a new game with participants and their initial picks
- Update weekly game outcomes
- Check for participant elimination based on weekly game outcomes
- Output updated participant list and their status

## Requirements
- Python 3.x
- Pandas library
- Openpyxl library (for reading Excel files)

## Installation
1. Install Python 3.x from [here](https://www.python.org/downloads/).
2. Install required Python packages:
    ```
    pip install pandas
    pip install openpyxl
    ```

## Usage

### Initialization
1. Prepare an Excel file (`PlayerList.xlsx`) that contains the list of participants and their picks for each week.
2. Place this file in the `./data/` directory.

### Running the Program
1. Run the program: `python DeathPool.py`
2. The program will read the `PlayerList.xlsx` and `WeeklyGameOutcome.csv` files to update the game state.
3. The program will output updated CSV files with the current state of the game.

### Weekly Update
1. Update the `WeeklyGameOutcome.csv` file with the outcomes of the games for the week.
2. Run the program again to update the game state.

## Contributing
Feel free to fork the project and submit a pull request with your changes!

## License
This project is licensed under the GNU General Public License v3.0
