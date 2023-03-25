import pandas as pd

# Load the Excel dataset
df = pd.read_excel('Cricket.xlsx')

# Calculate batting averages and strike rates
df['Batting Average'] = df['Runs Scored'] / df['Innings Played']
df['Strike Rate'] = df['Runs Scored'] / df['Balls Faced'] * 100

# Print the results
print(df[['Player Name', 'Batting Average', 'Strike Rate']])