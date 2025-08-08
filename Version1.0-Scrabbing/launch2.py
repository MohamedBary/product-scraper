import requests
from bs4 import BeautifulSoup
import pandas as pd

#Scrabbing html buit-in
html ='''
<article class="prd _fb col c-prd">
         <a class="btn _i _rnd -mas -fsh0 -me-start _wslt _sec" data-ga4-discount="86.56" data-ga4-is_second_chance="false" data-ga4-item_brand="Asus" data-ga4-item_category="Computing" data-ga4-item_category2="Computers &amp; Accessories" data-ga4-item_category3="Computers &amp; Tablets" data-ga4-item_category4="Laptops" data-ga4-item_id="AS040CL33QT8JNAFAMZ" data-ga4-item_name="ASUS Vivobook Go 15 E1504FA-NJ005W - AMD Ryzen 5 7520U Processor 2.8GHz - 8GB - 512 SSD - 15.6 Inch " data-ga4-item_variant="" data-ga4-price="346.22" data-ga4-tags="JA23_30|TBOOST|XMAS22_88" data-moengage-brand_key="asus" data-moengage-brand_name="Asus" data-moengage-category_key="laptops" data-moengage-category_name="Laptops" data-moengage-discount="86.56" data-moengage-item_variant="" data-moengage-product_image="https://eg.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/87/6883231/1.jpg?7599" data-moengage-product_name="ASUS Vivobook Go 15 E1504FA-NJ005W - AMD Ryzen 5 7520U Processor 2.8GHz - 8GB - 512 SSD - 15.6 Inch " data-moengage-product_price="346.22" data-moengage-product_sku="AS040CL33QT8JNAFAMZ" data-pop-open="addToWishlist" data-pop-trig="atw" data-sku="AS040CL33QT8JNAFAMZ" data-track-onclick="wishlist" data-track-providers="ga4|moengage" href="/customer/account/login/?tkWl=AS040CL33QT8JNAFAMZ-213561834&amp;return=%2Flaptops%2F" rel="nofollow" role="button" data-track-onclick-bound="true">
          <svg aria-label="Add to wishlist" class="ic -f-or5" height="16" viewBox="0 0 24 24" width="16">
           <use xlink:href="https://www.jumia.com.eg/assets_he/images/i-icons.85419111.svg#saved-items">
           </use>
          </svg>
         </a>
         <a class="core" data-ga4-discount="86.56" data-ga4-index="1" data-ga4-is_second_chance="false" data-ga4-item_brand="Asus" data-ga4-item_category="Computing" data-ga4-item_category2="Computers &amp; Accessories" data-ga4-item_category3="Computers &amp; Tablets" data-ga4-item_category4="Laptops" data-ga4-item_id="AS040CL33QT8JNAFAMZ" data-ga4-item_name="ASUS Vivobook Go 15 E1504FA-NJ005W - AMD Ryzen 5 7520U Processor 2.8GHz - 8GB - 512 SSD - 15.6 Inch " data-ga4-list="" data-ga4-price="346.22" data-ga4-tags="JA23_30|TBOOST|XMAS22_88" data-gtm-brand="Asus" data-gtm-category="Computing/Computers &amp; Accessories/Computers &amp; Tablets/Laptops" data-gtm-dimension23="" data-gtm-dimension26="" data-gtm-dimension27="" data-gtm-dimension28="1" data-gtm-dimension37="0" data-gtm-dimension43="JA23_30|TBOOST|XMAS22_88" data-gtm-dimension44="0" data-gtm-id="AS040CL33QT8JNAFAMZ" data-gtm-list="" data-gtm-name="ASUS Vivobook Go 15 E1504FA-NJ005W - AMD Ryzen 5 7520U Processor 2.8GHz - 8GB - 512 SSD - 15.6 Inch " data-gtm-position="1" data-gtm-price="346.22" data-track-onclick="eecProduct" data-track-onview="eecProduct" data-track-providers="gtm|ga4" href="/asus-asus-vivobook-go-15-e1504fa-nj005w-amd-ryzen-5-7520u-processor-2.8ghz-8gb-512-ssd-15.6-inch-windows-11-132388678.html" data-track-onclick-bound="true">
          <div class="img-c">
           <img alt="" class="img" data-src="https://eg.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/87/6883231/1.jpg?7599" height="208" src="https://eg.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/87/6883231/1.jpg?7599" width="208">
          </div>
          <div class="info">
           <h3 class="name">
            Asus ASUS Vivobook Go 15 E1504FA-NJ005W - AMD Ryzen 5 7520U Processor 2.8GHz - 8GB - 512 SSD - 15.6 Inch - Windows 11
           </h3>
           <div class="prc">
            EGP 19,599.00
           </div>
           <div class="s-prc-w">
            <div class="old">
             EGP 24,499.00
            </div>
            <div class="bdg _dsct _sm">
             20%
            </div>
           </div>
           <svg aria-label="Express Shipping" class="ic xprss" height="10" viewBox="0 0 114 12" width="94">
            <use xlink:href="https://www.jumia.com.eg/assets_he/images/i-shop-jumia.9dea3b69.svg#express">
            </use>
           </svg>
          </div>
         </a>
         <footer class="ft">
          <form action="/cart/products/AS040CL33QT8JNAFAMZ-213561834/quantity/" class="-df -i-ctr -pr -j-bet" data-add-cart="" data-ga4-discount="86.56" data-ga4-is_second_chance="false" data-ga4-item_brand="Asus" data-ga4-item_category="Computing" data-ga4-item_category2="Computers &amp; Accessories" data-ga4-item_category3="Computers &amp; Tablets" data-ga4-item_category4="Laptops" data-ga4-item_id="AS040CL33QT8JNAFAMZ" data-ga4-item_name="ASUS Vivobook Go 15 E1504FA-NJ005W - AMD Ryzen 5 7520U Processor 2.8GHz - 8GB - 512 SSD - 15.6 Inch " data-ga4-item_variant="" data-ga4-price="346.22" data-ga4-tags="JA23_30|TBOOST|XMAS22_88" data-gtm-brand="Asus" data-gtm-category="Computing/Computers &amp; Accessories/Computers &amp; Tablets/Laptops" data-gtm-dimension23="" data-gtm-dimension26="" data-gtm-dimension27="" data-gtm-dimension28="1" data-gtm-dimension37="0" data-gtm-dimension43="JA23_30|TBOOST|XMAS22_88" data-gtm-dimension44="0" data-gtm-id="AS040CL33QT8JNAFAMZ" data-gtm-name="ASUS Vivobook Go 15 E1504FA-NJ005W - AMD Ryzen 5 7520U Processor 2.8GHz - 8GB - 512 SSD - 15.6 Inch " data-gtm-price="346.22" data-gtm-simplesku="AS040CL33QT8JNAFAMZ-213561834" data-gtm-variant="" data-moengage-brand_key="asus" data-moengage-brand_name="Asus" data-moengage-category_key="laptops" data-moengage-category_name="Laptops" data-moengage-discount="86.56" data-moengage-item_variant="" data-moengage-product_image="https://eg.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/87/6883231/1.jpg?7599" data-moengage-product_name="ASUS Vivobook Go 15 E1504FA-NJ005W - AMD Ryzen 5 7520U Processor 2.8GHz - 8GB - 512 SSD - 15.6 Inch " data-moengage-product_price="346.22" data-moengage-product_sku="AS040CL33QT8JNAFAMZ" data-sku="AS040CL33QT8JNAFAMZ" data-svar="AS040CL33QT8JNAFAMZ-213561834" data-track-onsubmit="addToCart" data-track-onsuccess="addToCart" data-track-providers="gtm|ga4|moengage" data-xhr="true" method="post" data-track-onsubmit-bound="true" data-track-onsuccess-bound="true">
           <button class="add btn _prim -pea _md" data-submit="" name="action" type="button" value="in">
            Add to cart
           </button>
           <input name="capiId" type="hidden" value="_1754634353_{eventType}">
           <input name="csrfToken" type="hidden" value="ee685ab059d8dcb6c91ea00076a393d9">
          </form>
         </footer>
        </article>
'''
#parsing the html
soup = BeautifulSoup(html, 'html.parser')

# Product Name
name = soup.find('h3', class_='name').text.strip()

# Price
price = soup.find('div', class_='prc').text.strip()

# Old Price (optional)
old_price_tag = soup.find('div', class_='old')
old_price = old_price_tag.text.strip() if old_price_tag else None

# Discount (optional)
discount_tag = soup.find('div', class_='bdg _dsct _sm')
discount = discount_tag.text.strip() if discount_tag else None

# Product URL
product_link_tag = soup.find('a', class_='core')
product_url = 'https://www.jumia.com.eg' + product_link_tag['href']

# Image URL
img_tag = soup.find('img', class_='img')
image_url = img_tag.get('data-src') or img_tag.get('src')

# Brand
brand = product_link_tag.get('data-ga4-item_brand')

# Show result
#test#print("Name:", name);print("Price:", price);print("Old Price:", old_price);print("Discount:", discount);print("URL:", product_url);print("Image URL:", image_url);print("Brand:", brand)
