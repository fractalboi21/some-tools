#"https://ipapi.co/json/"
#reddit comment scraper
import json

with open('/home/pi/Desktop/reddit_comments.json') as json_file:
    data = json.load(json_file)
#    print("="*50 + "[" + str(i) + "]" + "="*50)
#children_data = data["data"]["children"][i]["data"]
dist = data["data"]["dist"]

for i in range(dist):
    children_data = data["data"]["children"][i]["data"]

    subreddit = children_data["subreddit"]
    ups = children_data["ups"]
    selftext = children_data["selftext"]
    url = children_data["url"]
    
    print("="*50 + "[" + str(i) + "]" + "="*50)
    print(f"subreddit: {subreddit}")
    print(f"ups: {ups}")
    print(f"selftext: \n{selftext}")
    print(f"url: {url}")



