import requests
from bs4 import BeautifulSoup
import re

HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'})

def getLink():
    link = input('Link to amazon product: ')
    return link

def getText(link):
    r = requests.get(link, headers=HEADERS)
    return r.text

def getHTML(link):
    soup = BeautifulSoup(getText(link), 'html.parser')
    return soup

def filterReviews(soup):
    data_str = ""

    for item in soup.find_all("span", class_="a-size-base review-text review-text-content"):
            data_str = data_str + item.get_text()

    return data_str.split("\n")

def getProductID(link):
    ID = re.search('dp/(.*)/ref', link)
    return ID.group(1)

l = getLink()
productID = getProductID(l)
all_reviews_link = 'http://amazon.com/product-reviews/' + productID

reviews = []
all_reviews = []
i = 0
while reviews != None:
    reviews = []
    link = all_reviews_link + '?pageNumber=' + str(i)
    soup = getHTML(all_reviews_link)
    for review in filterReviews(soup):
        if review != '':
            reviews += review
    all_reviews += reviews
    i+=1
    print(i)

