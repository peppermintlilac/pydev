#!/usr/bin/python3
import twitter

#add keys and token
c_key = ''
c_secret = ''
a_key =''
a_secret = ''

api = twitter.Api(consumer_key=c_key, consumer_secret=c_secret, access_token_key=a_key, access_token_secret=a_secret)
#add user
userwho=""

def VerifyCred():
    print(api.VerifyCredentials())

def ShowUserTimeLine():
    statuses = api.GetUserTimeline(screen_name=userwho)
    print([s.text for s in statuses])

def PostTweet():
    asktweet=input("What would you like to tweet today?\n")
    status=api.PostUpdate(asktweet)
    return(status.text)

def PostLongTweet():
    asklongtweet=input("Fire away...tweet as many words as you can!\n")
    longpost=api.PostUpdates(asklongtweet)
    return(longpost)

def main():
    while True:
        ask=input("\n\n\
    \tWhat to you want to do today?\n\
    \t=============================\n\
    0: Nothing. Get me out of here!\n\
    1: Show me my credentials.\n\
    2: Show me my previous tweets.\n\
    3: Gonna tweet something.\n\
    4: I want to post a long tweet. Seriously?\n\n\n")

        answer=int(ask)

        if answer is 1:
            VerifyCred()

        elif answer is 2:
            ShowUserTimeLine()

        elif answer is 3:
            PostTweet()

        elif answer is 4:
            PostLongTweet()

        elif answer is 0:
            break
            return()

        else:
            print("Invalid option. Choose between 1 thru 4.\n")

if __name__ == "__main__": main()
