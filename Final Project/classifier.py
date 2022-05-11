import pandas as pd
import random
import nltk
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split

# load/read data
df = pd.read_csv('data/final_data.csv')
pos = df[df['sentiment_class'] == 'Pos']
neg = df[df['sentiment_class'] == 'Neg']

# input training size and split data accordingly
train_size = int(input('Training size: '))
pos, neg = pos[:train_size], neg[:train_size]

data_list = [(row['reviews.text'], 'pos') for i, row in pos.iterrows()] + \
            [(row['reviews.text'], 'neg') for i, row in neg.iterrows()]

# from DataTechNotes "Sentiment Classification with NLTK Naive Bayes Classifier"
tokens = set(word.lower() for words in data_list for word in word_tokenize(words[0]))
train = [({word: (word in word_tokenize(x[0])) for word in tokens}, x[1]) for x in data_list]

# train model
random.shuffle(train)
train_x, test_x = train_test_split(train, test_size=0.2)
model = nltk.NaiveBayesClassifier.train(train_x)

# accuracy
acc = nltk.classify.accuracy(model, test_x)
print('Accuracy:', acc)
model.show_most_informative_features()

# use model to predict review sentiment
def classifyReview():
    test = input('Review: ')
    t_features = {word: (word in word_tokenize(test.lower())) for word in tokens}
    print(test," : ", model.classify(t_features))

while True:
    classifyReview()

