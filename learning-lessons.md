#issue1
Path worked here
with open("page.html", "w", encoding="utf-8") as f:
      f.write(soup.prettify())
 Path didn't work here Why??????????????????????????????????????????????????????
with open("page.html", "w", encoding="utf-8") as f:
    html = file.read()

#Solution1
Mistake:
Solution: C:/Users/windows/VSCprojects/PythonProject/.vscode/Konecta-Training/Lab2-WebScapping/page.html
========================================================================================================================================
#path recommedned not to be put in variable, it could be if just for maintainability of the code ,not haveing full advantage of variable as containter and intergity of data
#Source_path="C:/Users/windows/VSCprojects/PythonProject/.vscode/Konecta-Training/Lab2-WebScapping/page.html"
========================================================================================================================================
crawlVS scrabe??????????????????????????????
========================================================================================================================================
#Steps of Scrabbing
1.go to url to scrab (crawl/scrabe????????)
GO fo network-->search for document type--->Request Headers-->you will find user-agend of the browser to scrab
2.Prepare the User-Agent in the network tab and put it in the header {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}


3.parsing using BeautifulSoup
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

4.
Inspect where section of the product in the html
========================================================================================================================================
this code{
    soup = []
soup.append(BeautifulSoup(response_url1.content, "html.parser"))
soup.append(BeautifulSoup(response_url2.content, "html.parser"))  # ✅ FIXED

all_products = []

for page in soup:
    # Example: print number of <article> elements
    products = page.find_all("article", class_="prd _fb col c-prd")
    soup.extend(products)  # Append products to the final list

print("Total number of products:", len(soup))
} output 82

HOWEVER!!!!! 
This code{
    soup = []
soup.append(BeautifulSoup(response_url1.content, "html.parser"))
soup.append(BeautifulSoup(response_url2.content, "html.parser"))  # ✅ FIXED

all_products = []

for page in soup:
    # Example: print number of <article> elements
    products = page.find_all("article", class_="prd _fb col c-prd")
    soup.extend(products)  # Append products to the final list

print("Total number of products:", len(soup))
} output is 80 (WHY?),and 80 is the correct answer
========================================================================================================================================