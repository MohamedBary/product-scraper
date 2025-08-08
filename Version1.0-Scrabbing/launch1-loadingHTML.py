import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
url = "https://www.jumia.com.eg/laptops/"

# Real headers to chrome browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
                   
}

# Send request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
## Preview HTML structure
##print(soup.prettify()[:1000])  # Show first 1000 characters for inspection

# Save the scrabbed html 
with open("page.html", "w", encoding="utf-8") as f:
     f.write(soup.prettify())

#print("Saved the full HTML to page.html")

