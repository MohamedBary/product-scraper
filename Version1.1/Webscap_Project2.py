import csv
from bs4 import BeautifulSoup

#1. Load HTML

with open("C:/Users/windows/VSCprojects/PythonProject/.vscode/Konecta-Training/Lab2-WebScapping/Version1.1/page.html", "r", encoding="utf-8") as file:
    html = file.read()
#
soup = BeautifulSoup(html, "html.parser")

#Find number of products in the given html file
product_articles = soup.find_all("article",class_="prd _fb col c-prd")
#test#print("Found", len(product_articles), "products")

#filtering 
#2.Find all product cards 
products = soup.find_all("article", class_="prd _fb col c-prd")

#3. Prepare data
product_data = []
for product in products:
    # Get product name
    name_tag = product.find("h3", class_="name")
    name = name_tag.text.strip() if name_tag else "No name"

    # Get price
    price_tag = product.find("div", class_="prc")
    price = price_tag.text.strip() if price_tag else "No price"

    # Get product URL
    link_tag = product.find("a", class_="core")
    url = "https://www.jumia.com.eg" + link_tag["href"] if link_tag and "href" in link_tag.attrs else "No link"

    # Get image URL
    img_tag = product.find("img")
    image_url = img_tag["data-src"] if img_tag and "data-src" in img_tag.attrs else "No image"

    # Add to list
    product_data.append([name, price, url, image_url])

#Save Data to a CSV File
# Save to CSV
'''
with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price", "URL", "Image URL"])
    writer.writerows(product_data)
#test#print("Saved", len(product_data), "products to products.csv")
'''