import requests
from bs4 import BeautifulSoup
import csv

# Read headers to chrome browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

# Target Jumia-Page1URL & # Jumia-Page2URL & # Jumia-Page3URL
Page1_url = "https://www.jumia.com.eg/laptops/?page=1#catalog-listing"
Page2_url = "https://www.jumia.com.eg/laptops/?page=2#catalog-listing"
Page3_url = "https://www.jumia.com.eg/laptops/?page=3#catalog-listing"

#Fetch &Parse 
# Scraper 1: Scraping from the first page
response_url1 = requests.get(Page1_url, headers=headers)
# Scraper 2: Scraping from the second page
response_url2 = requests.get(Page2_url, headers=headers)
# Scraper 3: Scraping from the second page
response_url3 = requests.get(Page3_url, headers=headers)

soup = []
soup.append(BeautifulSoup(response_url1.content, "html.parser"))
soup.append(BeautifulSoup(response_url2.content, "html.parser"))  
soup.append(BeautifulSoup(response_url3.content, "html.parser"))  

all_products = []
for page in soup:
    # Example: print number of <article> elements
    products = page.find_all("article", class_="prd _fb col c-prd")
    all_products.extend(products)  # Append products to the final list
#test#print("Total number of products:", len(all_products))


#3. Prepare data
product_data = []
for product in all_products:
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
#test#print("Data of products:");print(product_data)

#Save Data to a CSV File
# Save to CSV
with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price", "URL", "Image URL"])
    writer.writerows(product_data)
#test
print("Saved", len(product_data), "products to products.csv")

