import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/final_data.csv')
pos = df[df['sentiment_class'] == 'Pos']
neg = df[df['sentiment_class'] == 'Neg']

data_list = [(row['reviews.text'], 'pos') for i, row in pos.iterrows()] + \
            [(row['reviews.text'], 'neg') for i, row in neg.iterrows()]
