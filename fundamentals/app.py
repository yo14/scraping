from lxml import etree

tree = etree.parse("src/web_page.html")

title_element = tree.xpath("//title/text()")[0]
print(title_element)

paragraph_element = tree.xpath("//p/text()")[0]
print(paragraph_element)

list_items = tree.xpath("//li")
for li in list_items:
    text = ''.join(map(str.strip, li.xpath(".//text()")))
    print(text)


