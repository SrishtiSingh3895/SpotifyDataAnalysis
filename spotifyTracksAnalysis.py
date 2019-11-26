import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

# Reading data file
music = pd.read_csv('top2018.csv')
music.head()
music.info()

# Check for any missing data
music.isnull().sum()

# Add rank order to the data
music.insert(0, 'rank', range(1, len(music)+1))
music.set_index('rank', inplace = True)
music.head()

# Histogram of music duration
plt.hist(music.duration_ms)
music['duration_ms'] = music['duration_ms']/60000
music.rename(columns={'duration_ms':'duration_min'}, inplace = True)
music.head()
plt.hist(music.duration_min, )

# Top music duration
top_duration = music.loc[music['duration_min'] > 6]
print(top_duration)

# Top 10 artists
music['artists'].value_counts().head(10)

# Heatmap of all the attributes
sns.heatmap(music.corr())

# Pair plot of all the attributes having high correlation
sns.pairplot(music, vars = ['danceability', 'energy', 'loudness', 'valence'], hue = 'mode')
sns.clustermap(music.corr())

# Valence Analysis
sns.distplot(music['valence'])
sns.boxplot(music['valence'])

positive = music['valence']>=0.5
negative = (music['valence']<0.5)

happiness = [positive.sum(), negative.sum()]

# Top 10 happiest songs
music[['name','artists','danceability','valence']].sort_values(by='valence',ascending=False).head(10)

# Energy Analysis
sns.distplot(music['energy'], color = 'red')
sns.boxplot(music['energy'])

# Danceability Analysis
sns.distplot(music['danceability'], color = 'blue')
Very = music['danceability']>=0.75
Regular = (music['danceability']>=0.5) & (music['danceability']<0.75)
Non = music['danceability']<0.5

dance = [Very.sum(), Regular.sum(), Non.sum()]

# Top 10 danceable songs
music[['name','artists','danceability','valence','tempo']].sort_values(by='danceability',ascending=False).head(10)

sns.boxplot(music['danceability'])

# Loudness Analysis
sns.distplot(music['loudness'], color = 'purple')
sns.boxplot(music['loudness'])
