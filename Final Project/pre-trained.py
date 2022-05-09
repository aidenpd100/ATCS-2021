import decimal
from nltk.sentiment import SentimentIntensityAnalyzer

# get and return review input
def inputReview():
    review_title = input('Write your title here: ')
    review_text = input('Write your review here: ')
    return review_title, review_text

# calculate and return sentiment scores
def getSentimentScores(review_title, review_text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(review_title), sia.polarity_scores(review_text)

# scale sentiment scores to 1-5 and return rating
def scaleScores(sentiment_scores):
    rating = 3 + 2*(sentiment_scores['compound'])
    return rating

review_title, review_text = inputReview()
title_score, text_score = getSentimentScores(review_title, review_text)
title_rating, text_rating = scaleScores(title_score), scaleScores(text_score)
avg_rating = round((title_rating + text_rating) / 2)

# print prediction based on title and text
print('Rating prediction based on title:', str(round(title_rating)))
print('Rating prediction based on text:', str(round(text_rating)))
print('Overall rating:', str(avg_rating))
