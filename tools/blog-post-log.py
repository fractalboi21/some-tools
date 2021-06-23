"""
So, i read a lot of blog post related to cyber-security, evolutionary-biology, Artifical-Intelligence.
This program is keep track of the blog that i read every day.
"""
import time
import json
blogs_list = []

def inputAndupdatedict():
    blog_dict = {
    "title":"",
    "link":"",
    "time":""
    }
    #input
    title = input("title:")
    link = input("link:")
    current_time = time.ctime()
    #update
    blog_dict.update({"title": title})
    blog_dict.update({"link": link})
    blog_dict.update({"time": current_time})
    
    return blog_dict


with open("blog_log.json","r") as f:
    var = f.read()

current_data = inputAndupdatedict()
loaded_json = json.loads(var)
loaded_json.append(current_data)

with open("blog_log.json","w") as f:
    f.write(json.dumps(loaded_json))

print("saved successfully!")
