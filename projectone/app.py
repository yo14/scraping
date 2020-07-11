import requests
from lxml import html

resp = requests.get(url="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
                    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})

tree = html.fromstring(html=resp.text)

product_main = tree.xpath("//div[contains(@class,'product_main')]")[0]
title = product_main.xpath(".//h1/text()")[0]
price = product_main.xpath(".//p[1]/text()")[0]
availibility = product_main.xpath(".//p[2]/text()")[1].strip()
description = tree.xpath("//div[@id='product_description']/following-sibling::p/text()")[0]

book_information = {
    'title':title,
    'price':price,
    'in_stock': availibility,
    'description': description
}

print(book_information)



