from lxml import etree

tree = etree.parse("src/web_page.html")

title_element = tree.find("head/title")
print(title_element.text)

paragraph_element = tree.find("body/p")
print(paragraph_element.text)

list_items = tree.findall("body/ul/li")
print(list_items)

for li in list_items:
    a = li.find("a")
    if a is not None:
        print(f"{li.text.strip()} {a.text}")
    else:
        print(li.text)

