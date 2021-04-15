import json

with open('/home/pi/Documents/aakashbilly_files/pratice/unpopular.json') as json_file:
    data = json.load(json_file)

#data = data["data"]["children"][0]

#for i in range(25):
#    print(data["data"]["children"][i])
dist = int(data["data"]["dist"])
for i in range(int(dist)):
    children_data = data["data"]["children"][i]["data"]
    subreddit = children_data["subreddit"]
    title = children_data["title"]
    ups = children_data["ups"]
    url = children_data["url"]
    
    print("="*50 + "[" + str(i) + "]" + "="*50)
    print(f"subreddit: {subreddit}")
    print(f"title: {title}")
    print(f"url: {url}")
    print(f"ups: {ups}")

