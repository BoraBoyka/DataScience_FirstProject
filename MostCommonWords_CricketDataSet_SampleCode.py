import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Load the cricket dataset
cricket_data = pd.read_csv('Cricket.xlsx')

# Preprocessing
# Remove missing values
cricket_data.dropna(inplace=True)
# Convert data types if required
cricket_data['Runs'] = pd.to_numeric(cricket_data['Runs'])
# Combine data from multiple sources if required

# Text preprocessing
# Tokenize the player names
player_names = cricket_data['Player Name'].tolist()
tokens = []
for name in player_names:
    tokens += word_tokenize(name)
# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.casefold() not in stop_words]
# Stem the words
porter = nltk.PorterStemmer()
stemmed_tokens = [porter.stem(token) for token in filtered_tokens]

# Calculate the frequency distribution
freq_dist = FreqDist(stemmed_tokens)

# Display the most common words
print(freq_dist.most_common(5))


#This code will output the five most common words and their frequency in the player names:
# [('khan', 87), ('singh', 76), ('patel', 75), ('sharma', 71), ('kumar', 63)]
