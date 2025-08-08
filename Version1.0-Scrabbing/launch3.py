import requests
from bs4 import BeautifulSoup
import pandas as pd

#Reading page.html
with open("C:/Users/windows/VSCprojects/PythonProject/.vscode/Konecta-Training/Lab2-WebScapping/Version1.0/page.html", "r", encoding="utf-8") as file:
    html = file.read()
soup = BeautifulSoup(html, "html.parser")

#Find number of products in the given html file
product_articles = soup.find_all("article")
#test#print("Found", len(product_articles), "products")

#Find specific product data in the given html
products = soup.find_all("article", class_="prd _fb col c-prd")
first_product = products[0]
#test#print(first_product.prettify())

# Get the first product article
product = soup.find("article", class_="prd _fb col c-prd")

# Get the name
name = product.find("h3", class_="name").text.strip()

# Get the current price
price = product.find("div", class_="prc").text.strip()

# Get the product link
link_tag = product.find("a", class_="core")
url = "https://www.jumia.com.eg" + link_tag["href"] if link_tag else "No link"

# Get the image URL
img_tag = product.find("img")
image_url = img_tag["data-src"] if img_tag and "data-src" in img_tag.attrs else "No image"

#  Print results 
#test#print("Name:", name);print("Price:", price);print("URL:", url);print("Image:", image_url)



