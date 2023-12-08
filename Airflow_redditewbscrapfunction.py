import requests
import pandas as pd
import json
import s3fs
from datetime import datetime
from pprint import pprint

# Establishing url and subreddit variables
sub = 'science'
url = f'https://www.reddit.com/r/{sub}/hot.json?t=all'
# Header needed for requests.get function
headers = { 'User-Agent' : 'Virboxbot'}

res = requests.get( url, headers = headers)

# Parsing title of each top (of all time) post in the r/science subreddit
title_list = []
if res.ok:
    data = res.json()['data']
    for d in data['children']:
        data2 = d['data']
        title_dict = { 'Title' : data2['title'],
                        'Upvotes' : data2['ups'],
                        'Upvote_percentage' : data2['upvote_ratio']*100,
                        'Author' : 'u/' + data2['author']}
        title_list.append(title_dict)
else:
    print(f'Error code received:{res.status_code}')

df = pd.DataFrame(title_list)
df.to_csv("science_top.csv")