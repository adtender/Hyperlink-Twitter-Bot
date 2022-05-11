# Hyperlink-Twitter-Bot
Post a video and copy the hyperlink from it and use that hyperlink to post scheduled media tweets.
Can be used with a free AWS Lambda account or by any other means.

Requires Python3 and tweepy
tweepy can be installed with
pip3 install tweepy

Configure config.py to match the keys given when you created a twitter developer program.
Can be found on creation of a program here:
developer.twitter.com/

python3 tweet.py
Will post the hyperlink which embeds the video

python3 tweet.py "text here"
Will post the embedded video along with additional text of your choosing

python3 tweet.py "" "alternate hyperlink"
Will post another embedded video, additional text is optional
