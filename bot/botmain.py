import tweepy

from bot import timetool, loggingservice, grabber
from secret import keys

bot_username = 'Tagesenergie-Twitterbot'
logfile_name = bot_username + ".log"


def create_tweet():
    """Creates the text of the tweet."""

    try:
        text = "Die Tagesenergie-Werte vom " + timetool.get_date()
        text = text + "\nMagie-O-Meter:  " + grabber.get_magicvalue()
        text = text + "\nEnergie Impulswert:  " + grabber.get_energyimpulsvalue()
        text = text + "\nBewusstwerdungsindex:  " + grabber.get_consiousvalue()
    except AttributeError as ae:
        loggingservice.log(repr(ae), logfile_name)
        text = grabber.get_errortext()
    return text


def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        loggingservice.log(repr(e), logfile_name)
    else:
        loggingservice.log("Tweeted:\n" + text + "\n", logfile_name)


if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)
