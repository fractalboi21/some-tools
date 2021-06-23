import sys
from googlesearch import search
import requests

print(sys.argv)
query = sys.argv[1]
count = 0
for i in search(query,num_results=int(sys.argv[2])):
    
    count+=1
    temp = requests.get(str(i))
    sc = temp.status_code
    if sc == 200:
        print(f"[{str(count).zfill(3)}] link: {i} [{sc}]")
    else:
        pass
