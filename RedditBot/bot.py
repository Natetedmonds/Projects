import praw
import pdb
import re
import os
from config_bot import *

if not os.path.isfile("config_bot.py"):
  print "You must create a config file for your bot's credentials\n"
  exit(1)

user_agent = ("WallpaperPuller Buddy v.1.0.0")
r = praw.Reddit(user_agent = user_agent)

r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning=True)

subreddit = r.get_subreddit("wallpapers")

strings = []

for submission in subreddit.get_hot(limit=10):
  if "imgur.com/" not in submission.url:
    continue
  # print "Title: ", submission.title
  # print "Text: ", submission.selftext
  # print "Score: ", submission.score
  # print "__________________________\n"
  strings.append(submission.url)

print ', '.join(strings)
  
