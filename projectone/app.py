import requests

resp = requests.get(url="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html", headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})

print(resp.headers)
print('-' * 20)
print(resp.request.headers)