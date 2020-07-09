from lxml import etree

tree = etree.parse("src/web_page.html")

print(etree.tostring(tree))