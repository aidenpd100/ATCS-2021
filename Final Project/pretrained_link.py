import requests
from bs4 import BeautifulSoup
import re
from nltk.sentiment import SentimentIntensityAnalyzer
from pretrained import scaleScores

HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'})

# input link
def getLink():
    link = input('Link to amazon product: ')
    return link

# returns full page text
def getText(link):
    r = requests.get(link, headers=HEADERS)
    return r.text

def getHTML(link):
    soup = BeautifulSoup(getText(link), 'html.parser')
    return soup

# returns list of all reviews on a given page
def filterReviews(soup):
    data_str = ""

    for item in soup.find_all('span',{'data-hook':'review-body'}):
            data_str = data_str + item.get_text()

    return data_str.split("\n")

# returns section of URL unique to the product
def getProductID(link):
    ID = re.search('dp/(.*)/ref', link)
    return ID.group(1)

# iterates through every page of reviews (or up to i = maxPages) and adds each review to a list that is returned
def allReviewList(all_reviews_link, maxPages):
    reviews = ['']
    all_reviews = []
    i = 1

    while reviews and (i <= maxPages):
        reviews = []
        link = all_reviews_link + '?pageNumber=' + str(i)
        soup = getHTML(link)
        for review in filterReviews(soup):
            if review != '':
                reviews.append(review)
        all_reviews += reviews
        print("Page", i, "complete")
        i += 1
    return all_reviews

# finds sentiment score of each rewiew and returns average
def avgSentimentScore(reviews):
    sia = SentimentIntensityAnalyzer()
    sum = 0
    for review in reviews:
        sum += scaleScores(sia.polarity_scores(review))
    return sum / len(reviews)


l = getLink()
productID = getProductID(l)
all_reviews_link = 'http://amazon.com/product-reviews/' + productID
maxPages = int(input("Number of review pages limit: "))
review_list = allReviewList(all_reviews_link, maxPages)

avgSentimentScaled = round(avgSentimentScore(review_list), 2)
avgSentimentPercent = round(avgSentimentScaled / 5 * 100, 2)

# print results
print('\nThis product might be rated', avgSentimentScaled, 'out of 5 stars.')
print('Reviewers have', avgSentimentPercent, 'percent positive sentiment.')

