#!/usr/local/bin/python3

import urllib.request

page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
text = page.read().decode("utf8")
price = text[233:238]

#print(text)
print(price)
