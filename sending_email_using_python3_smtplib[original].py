import smtplib
from random import choice
from time import sleep

lst = ["world","bye","yay","boom","jam","yummy","tummy","yo"]

#import varibles
sender_email = ""
sender_email_password = "#"
receiver_email = ""
#number of time you want to spam
wait_for_sec = 300
no_of_times = 10
# 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
# 
s.login(sender_email,sender_email_password) 
# 
message = choice(lst)
#
def send_email():
    s.sendmail(sender_email,receiver_email, message)
    print("success")
    s.quit()
    
for i in range(no_of_times):
    send_email()
    sleep(wait_for_sec)