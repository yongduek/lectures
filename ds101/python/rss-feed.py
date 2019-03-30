# filename: rss-feed.py
# src: https://alvinalexander.com/python/python-script-read-rss-feeds-database

import feedparser
import time
from subprocess import check_output
import os, sys

feed_name = 'sisain'
url = 'http://www.sisainlive.com/rss.xml'
#feed_name = sys.argv[1]
#url = sys.argv[2]

db = 'myrssfeeds.db'
limit = 12 * 3600 * 1000 # mili seconds
limit = 60 * 1000 # 60 seconds

#
# function to get the current time
#
current_time_millis = lambda: int(round(time.time() * 1000))
current_timestamp = current_time_millis()

def post_is_in_db(title):
    with open(db, 'r') as database:
        for line in database:
            if title in line:
                return True
    return False

# return true if the title is in the database with a timestamp > limit
def post_is_in_db_with_old_timestamp(title):
    if not os.path.exists (db):
        return False # since the file does not exist.
    #
    with open(db, 'r') as database:
        for line in database:
            if title in line:
                ts_as_string = line.split('|', 1)[1]
                ts = int(ts_as_string)
                if current_timestamp - ts > limit:
                    return True
    return False

#
# get the feed data from the url
#
feed = feedparser.parse(url)

#
# figure out which posts to print
#
posts_to_print = []
posts_to_skip = []

for post in feed.entries:
    # if post is already in the database, skip it
    # TODO check the time
    title = post.title
    if post_is_in_db_with_old_timestamp(title):
        posts_to_skip.append(title)
    else:
        posts_to_print.append(title)
#
print ('posts_to_print: ', len(posts_to_print))
print ('posts_to_skip : ', len(posts_to_skip))

#
# add all the posts we're going to print to the database with the current timestamp
# (but only if they're not already in there)
#
f = open(db, 'a')
for title in posts_to_print:
    if not post_is_in_db(title):
        f.write(title + "|" + str(current_timestamp) + "\n")
f.close()
print ('data file: ', db)
#
# output all of the new posts
#
count = 1
blockcount = 1
for title in posts_to_print:
    if count % 5 == 1:
        print("\n" + time.strftime("%a, %b %d %I:%M %p") + '  ((( ' + feed_name + ' - ' + str(blockcount) + ' )))')
        print("-----------------------------------------\n")
        blockcount += 1
    print(title + "\n")
    count += 1
    if count > 11: # let's just see 11 titles
        break 
#
# EOF 
