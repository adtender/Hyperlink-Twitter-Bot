import tweepy
import config
import tweet
import sys

class TWEET:

    def __init__(self, arg):
            self.api_key = config.API_Key
            self.api_key_secret = config.API_Key_Secret
            self.access_token = config.Access_Token
            self.access_token_secret = config.Access_Token_Secret
            self.auth = tweepy.OAuthHandler(self.api_key, self.api_key_secret)
            self.auth.set_access_token(self.access_token, self.access_token_secret)
            self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
            self.arg = arg
            self.videoSource = config.videoSource

    def tweet_media(self):
        arg = ""
        
        if len(self.arg) == 2:
            arg = " " + str(self.arg[1])
        elif len(self.arg) == 3:
            self.videoSource = str(self.arg[2])
        
        self.api.update_status(self.videoSource + arg)

if __name__ == "__main__":
    tweet = tweet.TWEET(sys.argv)
    tweet.tweet_media()