#https://ahmia.fi/search/?q=paypal+cashout
# import os
# import subprocess
# #https://www.kite.com/python/answers/how-to-get-output-from-a-shell-command-in-python
# onion_link = "http://3fcp54di2maqglpg4puyna4stv6yr4kr24au7de2gszmsoajrbn3flyd.onion/"
# 
# subprocess = subprocess.Popen("torify curl -i {}".format(onion_link),shell=True, stdout=subprocess.PIPE)
# 
# sr = subprocess.stdout.read()
# #https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
# sr = sr.decode("utf-8")
# parsed_status_code = sr.split(" ")[1]
# 
# if parsed_status_code[0] == "2":
#     print("alive")
# else:
#     print("dead")


def onionLinkChecker(onion_url):
    import subprocess
    """ sudo apt-get install tor
        sudo servie tor start
        
        torify curl [onion_link]
        
        example:
        torify curl zox6glkwvpuwcw6kdaiu2p3d4em2jffash3yq2fika266iu4sj4zcoqd.onion  
    """
    onion_url = onion_url.lower()
    subprocess = subprocess.Popen("torify curl -i {}".format(onion_url),shell=True, stdout=subprocess.PIPE)
    sr = subprocess.stdout.read()
    parsed_status_code = sr.decode("utf-8").split(" ")[1]
    
    if parsed_status_code[0] == "2":
        return "alive"
    else:
        return "dead"



import requests
from bs4 import BeautifulSoup
 
html = open("/home/pi/Desktop/index.html","r").read()
soup = BeautifulSoup(html,"lxml")

a = soup.find_all("a")

cite = soup.find_all("cite")
lst = []
for link in cite:
    #onionLinkChecker(link)
    lst.append(link.text)
    
for i in lst:
    print(i)
print(len(lst))