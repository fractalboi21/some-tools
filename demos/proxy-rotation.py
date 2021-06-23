import requests

proxy = "165.225.77.46:80"
url = "https://httpbin.org/ip"

r = requests.get(url, proxies = {'http':proxy,'https':proxy})

print(r.json())