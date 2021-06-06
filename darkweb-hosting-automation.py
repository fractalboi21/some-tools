import os
import time
import threading
def spawnHttpService():
    os.system("python3 -m http.server 8080")
    
def spawnTorService():
    os.system("tor")
    
def displayHostname():
    os.system("cd")
    while True:
        time.sleep(5)
        print("copy paste this link in your torbrowser.")
        os.system("sudo cat /var/lib/tor/hidden_service/hostname")
    

threading.Thread(target=spawnHttpService).start()
threading.Thread(target=spawnTorService).start()
threading.Thread(target=displayHostname).start()



    