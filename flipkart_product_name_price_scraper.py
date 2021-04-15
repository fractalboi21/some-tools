import requests
from bs4 import BeautifulSoup

def flipkart_product_name_price(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "lxml")
    product_name = soup.find("h1").text
    product_price = soup.find("div",class_="_30jeq3 _16Jk6d").text
    return f"product name: {product_name}"
    return f"product price: {product_price}"


while True:
    url = input("enter url: ")
    
    if str(url) == "exit":
        break
    else:
        print(flipkart_product_name_price(str(url)))

    
 
    
    
    
