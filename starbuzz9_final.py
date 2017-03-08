#!/usr/bin/python3

#install twitter module through pip
import urllib.request
import time
import twitter as t

# copy keys from twitter app
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''

def tweet(status_msg):
    if len(status_msg) > 140:
        raise Exception ('Status message too long. Tweet is limited to 140 characters.')
    else:
        authkey=t.Twitter(auth=t.OAuth(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
        result = authkey.statuses.update(status=status_msg)
        return result

def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find("$")
    start_of_price = where + 1
    end_of_price = start_of_price + 4
    return(float(text[start_of_price:end_of_price]))

ask = input("Is price required immediately? Y/N ")
if ask == "Y":
    #print(get_price())
    status_msg = "@starbuzzceo\nCurrent price of coffee = $" + str(get_price())
    res = tweet(status_msg)

else:
    price = 99.99
    while price > 4.74:
       time.sleep(900)
       price = get_price()
    #print("Buy!")
    status_msg = "@starbuzzceo\nCurrent price of coffee is $" + str(get_price()) + "; BUY!"
    res = tweet(status_msg)
