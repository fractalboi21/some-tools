#this program will download and store onion websites and open browser for you.
import subprocess
import os
import webbrowser

def downloadOnionlink(onion_url):
    import subprocess
    onion_url = onion_url.lower()
    subprocess = subprocess.Popen("torify curl {}".format(onion_url),shell=True, stdout=subprocess.PIPE)
    sr = subprocess.stdout.read()
    
    with open(f"{onion_url}.html","wb") as f:
        f.write(sr)
    return onion_url + ".html"

link = input("enter the link: ")
current_page = downloadOnionlink(link)

webbrowser.open(current_page)
    