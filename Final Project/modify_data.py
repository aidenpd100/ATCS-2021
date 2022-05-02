import pandas as pd
import numpy as np

# read data and select desired variables
df = pd.read_csv('data/Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv')
df = df[['reviews.rating', 'reviews.text']]
df = df.dropna()

# make new column with sentiment class
df['sentiment_class'] = 'Neu'
df.loc[df['reviews.rating'] < 3, 'sentiment_class'] = 'Neg'
df.loc[df['reviews.rating'] > 3, 'sentiment_class'] = 'Pos'
# drop neutrals
df.drop(df[df['sentiment_class'] == 'Neu'].index, inplace=True)

# cut down number of positive reviews to be equal to the negative sample size
df_final = df.groupby('sentiment_class').head(1581)

# export modified data file
df_final.to_csv('data/final_data.csv', index=False)


