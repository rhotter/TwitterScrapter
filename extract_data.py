from bs4 import BeautifulSoup, Comment
import requests
import json
from pprint import pprint

time = 1003064346519187456

url = 'https://twitter.com/i/profiles/show/realDonaldTrump/timeline/tweets?include_available_features=1&include_entities=1&max_position={}&reset_error_state=false'.format(time)
r = requests.get(url)
site = r.json()
site = BeautifulSoup(site['items_html'], "lxml")
tweets = site.find_all(class_='tweet')
data = []

print(tweets[1])


for tweet in tweets:
    text = tweet.find(class_='tweet-text').text
    stats = tweet.find_all(class_='ProfileTweet-actionCountForAria')
    stats = [stat.text.split()[0].replace(',', '') for stat in stats]
    data.append({'text': text, 'replies': stats[0], 'retweets': stats[1], 'likes': stats[2]})

#add if there is a photo checking if there exists a div with the classname AdaptiveMedia-photoContainer

pprint (data)
