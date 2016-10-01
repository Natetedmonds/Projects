import praw
import pdb
import re
import os

user_agent = ("WallpaperPuller Buddy v.1.0.0")    #unique user_agent to keep reddit from banning or screaming
r = praw.Reddit(user_agent = user_agent)          #call praw to connect to Reddit

subreddit = r.get_subreddit("wallpapers")         #grabs the subreddit to scan

strings = []                                      #initializes our list of images

for submission in subreddit.get_hot(limit=10):    #loop for scraping
  if "imgur.com/" not in submission.url:
    continue
  strings.append(submission.url)

print ' \n'.join(strings)                          #outputs the list in a readable manner
  
