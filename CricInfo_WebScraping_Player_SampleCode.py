import requests from bs4 
import BeautifulSoup

# Define the URL of the player's profile page
url = 'https://www.espncricinfo.com/player/virat-kohli-253802'

# Send a GET request to the URL and get the HTML response
response = requests.get(url)
html = response.content

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the player's name
name = soup.find('div', {'class': 'player-card__player-name'}).text.strip()

# Find the player's batting statistics
batting_stats = soup.find('div', {'class': 'player-stats-block'}).find_all('div', {'class': 'player-stats-card'})

# Extract the player's batting average
batting_average = batting_stats[0].find('div', {'class': 'player-stats-value'}).text.strip()

# Extract the player's batting strike rate
batting_strike_rate = batting_stats[1].find('div', {'class': 'player-stats-value'}).text.strip()

# Find the player's bowling statistics
bowling_stats = soup.find('div', {'class': 'player-stats-block'}).find_all('div', {'class': 'player-stats-card'})[2]

# Extract the player's bowling average
bowling_average = bowling_stats.find_all('div', {'class': 'player-stats-value'})[0].text.strip()

# Extract the player's economy rate
economy_rate = bowling_stats.find_all('div', {'class': 'player-stats-value'})[2].text.strip()

# Print the player's name and statistics
print('Name:', name)
print('Batting Average:', batting_average)
print('Batting Strike Rate:', batting_strike_rate)
print('Bowling Average:', bowling_average)
print('Economy Rate:', economy_rate)
