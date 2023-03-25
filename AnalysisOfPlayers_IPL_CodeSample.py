import pandas as pd

# Load the CSV dataset of IPL 2021 player statistics
df = pd.read_csv('IPL_Player_Statistics.xlsx')

# Calculate the batting average for each player
df['Batting_Average'] = df['Runs'] / df['Innings']

# Calculate the bowling average for each player
df['Bowling_Average'] = df['Runs_Conceded'] / df['Wickets']

# Print the top 10 batsmen by batting average
top_batsmen = df[['Player', 'Batting_Average']].sort_values(by='Batting_Average', ascending=False).head(10)
print('Top 10 Batsmen:\n', top_batsmen)

# Print the top 10 bowlers by bowling average
top_bowlers = df[['Player', 'Bowling_Average']].sort_values(by='Bowling_Average', ascending=True).head(10)
print('Top 10 Bowlers:\n', top_bowlers)
