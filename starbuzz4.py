#!/usr/local/bin/python3

import urllib.request

page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
text = page.read().decode("utf8")
price = text[233:238]
pattern = text.find("$")
firstchar = pattern + 1
upto = firstchar + 4
newprice = text[firstchar:upto]

#print(text)
#print(price)
#find index of pattern
print(pattern)
print(newprice)
