# Hyperlink-Twitter-Bot
Post a video and copy the hyperlink from it and use that hyperlink to post scheduled media tweets. <br/>
Can be used with a [free AWS Lambda account](https://aws.amazon.com/lambda/) or by any other means. <br/>

Requires Python3 and tweepy <br/>
tweepy can be installed with <br/>
```pip3 install tweepy```

Configure config.py to match the keys given when you created a twitter developer program. <br/>
Can be found on creation of a program here: <br/>
[developer.twitter.com/](developer.twitter.com/)

```python3 tweet.py``` <br/>
Will post the hyperlink which embeds the video

```python3 tweet.py "text here"``` <br/>
Will post the embedded video along with additional text of your choosing

```python3 tweet.py "" "alternate hyperlink"``` <br/>
Will post another embedded video, additional text is optional
