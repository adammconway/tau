import twitter as tw
import json
import random

def tweet_content():
    """Generate tweet string (140 characters or less)
    """
    with open("market.txt", 'r') as f:
        date = f.read()
    index = random.randint(0, (len(date)-140))
    while (date[index] != " "):
	  index += 1
    tweet = date[index:index+120]
    return tweet

def send_tweet(event, context):
    """Post tweet
    """
    with open("twitter_credentials.json", "r") as f:
        credentials = json.load(f)
    t = tw.Api(**credentials)
    try:
        status = tweet_content()
        t.PostUpdate(status=status)
        return "Tweeted {}".format(status)
    except Exception as e:
        return e.message

if __name__ == '__main__':
    print send_tweet(None, None)
