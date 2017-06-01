# basic urllib scrapper

from urllib.request import urlopen

html = urlopen("http://www.bloomberg.com")

print(type(html))

print(html.read())