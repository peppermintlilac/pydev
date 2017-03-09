#!/usr/bin/python3
# work in progress, this doesn't do as it's told
import twitter

c_key = ''
c_secret = ''
a_key = ''
a_secret = ''
userwho=''

api = twitter.Api(consumer_key=c_key, consumer_secret=c_secret, access_token_key=a_key, access_token_secret=a_secret)

def VerifyCred():
    return(api.VerifyCredentials())

def ShowUserTimeLine():
    statuses = api.GetUserTimeline(screen_name=userwho)
    return([s.text for s in statuses])

def PostTweet():
    status=api.PostUpdate('I love python-twitter')
    return(status.text)

def PostLongTweet():
    longstatus="This tweet is more than one hundred forty characters. The big fox jumps over the lazy dog with the white rabbit. Roses are red. Violets are blue. Posting continuation to next tweet."
    longpost=api.PostUpdates(longstatus)
    return(longpost)

def main():
    ask=input("What to you want to do? 1: Verify Credentials,\
            2: Show User Timeline\
            3: Post a Tweet\
            4: Post a Long Tweet")
    answer=int(ask)

    if answer is 1:
        VerifyCred
    elif answer is 2:
        ShowUserTimeLine
    elif answer is 3:
        PostTweet
    elif answer is 4:
        PostLongTweet
    else:
        print("Invalid option")

if __name__ == "__main__": main()
