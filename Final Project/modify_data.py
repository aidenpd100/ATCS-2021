import pandas as pd
import numpy as np

df = pd.read_csv('data/Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv')
df = df[['reviews.rating', 'reviews.text', 'reviews.title']]
df = df.dropna()

df['sentiment_class'] = 'Neu'
df.loc[df['reviews.rating'] < 3, 'sentiment_class'] = 'Neg'
df.loc[df['reviews.rating'] > 3, 'sentiment_class'] = 'Pos'

print(df.groupby('sentiment_class').count())
