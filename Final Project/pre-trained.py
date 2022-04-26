from nltk.sentiment import SentimentIntensityAnalyzer

def inputReview():
    review_title = input('Write your title here: ')
    review_text = input('Write your review here: ')
    return review_title, review_text

def getSentimentScores(review_title, review_text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(review_title), sia.polarity_scores(review_text)

def scaleScores(sentiment_scores):
    rating = 3 + 2*(sentiment_scores['compound'])
    return round(rating)

review_title, review_text = inputReview()
title_score, text_score = getSentimentScores(review_title, review_text)
title_rating, text_rating = scaleScores(title_score), scaleScores(text_score)

print('Rating prediction based on title:', str(title_rating))
print('Rating prediction based on text:', str(text_rating))

