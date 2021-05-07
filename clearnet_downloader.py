import webbrowser
import requests


def downloadFromclearnet(search_term):
    search_term = search_term.replace(" ","+")
    url = "https://ahmia.fi/search/?q="+search_term
    response = requests.get(url)
    content = response.text
    with open(f"{search_term}.html","w") as f:
        f.write(content)
    print("content written")  
    webbrowser.open(f"{search_term}.html")
    
    return
    
st = input("enter search terms: ")



downloadFromclearnet(st)

