import requests
import json

start_time = 881839523126272000
end_time = 883064346519187456
diff = end_time - start_time

while True:
    url = 'https://twitter.com/i/profiles/show/realDonaldTrump/timeline/tweets?include_available_features=1&include_entities=1&max_position={}&reset_error_state=false'.format(time)
    url = 'https://twitter.com/i/search/timeline?f=tweets&vertical=default&q=from%3ArealDonaldTrump%20since%3A2017-06-06%20until%3A2017-07-07&include_available_features=1&include_entities=1&max_position=TWEET-{}-{}&reset_error_state=false'.format(start_time, end_time)
    print (url)
    r = requests.get(url)
    data = r.json()
    start_time = end_time
    end_time += diff
    print (data)
