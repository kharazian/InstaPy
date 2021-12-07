from instapy import InstaPy
import random

"""
This template is written by @the-unknown
What does this quickstart script aim to do?
- This is my template which includes the new QS system.
  It includes a randomizer for my hashtags... with every run, it selects 10
  random hashtags from the list.
NOTES:
- I am using the bot headless on my vServer and proxy into a Raspberry PI I
have at home, to always use my home IP to connect to Instagram.
  In my comments, I always ask for feedback, use more than 4 words and
  always have emojis.
  My comments work very well, as I get a lot of feedback to my posts and
  profile visits since I use this tactic.
  As I target mainly active accounts, I use two unfollow methods. 
  The first will unfollow everyone who did not follow back within 12h.
  The second one will unfollow the followers within 24h.
"""

# !/usr/bin/python2.7
import random
from instapy import InstaPy
from instapy import smart_run
import time

# get a session!
# session = InstaPy(username="developerghost",password="Amir@0913",
session = InstaPy(username="develop4infinity",password="Amir@09134",
			headless_browser=False,
          disable_image_load=True,
                  multi_logs=True)
time.sleep(10)

# let's go! :>
with smart_run(session):
    hashtags = [		
				'#codinghumor'
				,'#webdevelopers'
				,'#nodejs'
				,'#docker'
				,'#developer'
				,'#machinelearning'
				,'#neuralnetworks'
				,'#coder '
				,'#coderlife'
				,'#coderpower'
				,'#coders'
				,'#coding'
				,'#codingbootcamp'
				,'#codingisfun'
				,'#javascript'
				,'#programing'
				,'#programmer'
				,'#programmerrepublic'
				,'#programmerslife'
				,'#programming'
				,'#computerscience'
				,'#js'
				,'#developer'
				,'#softwareengineer'
] 
    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]

    # general settings
    session.set_dont_like(['sad', 'rain', 'depression'])
    session.set_do_follow(enabled=True, percentage=80, times=1)
    session.set_do_comment(enabled=True, percentage=80)
    session.set_comments([	'All Right!'
							,'Exactly right'
							,'Excellent!'
							,'Exceptional'
							,'Fabulous!'
							,'Fantastic!'
							,'Sensational!'
							,'Wonderful!'
							,'Outstanding!'
							,'That’s it!'
							,'Just right!'
							,'Unbelievable'
							,'Way to go!'
							,'Simply superb'
							,'Stupendous!'
							,'Magnificent'
							,'Marvelous!'
							,'First class job'
							,'First class work'
							,'Good for you!'
							,'That’s great'
							,'Good going!'
							,'Good thinking'
							,'Right on!'
							,'Better than ever!'
							,'I’m impressed!'
							,'You’re one of a kind'
							,'You’ve got it now.'
							,'You’ve mastered it!'
							,'What an improvement!'
							,'You always amaze me'
							,'You are fantastic'
							,'You are learning a lot'
							,'You are learning fast'
							,'You are so good'
							,'You did it that time!'
							,'You did that very well'
							,'You don’t miss a thing'
							,'You got it right!'
							,'You hit the target'
							,'I’m very proud of you'
							,'Keep up the great work!'
							,'Nothing can stop you now'
							,'Now you’ve figured it out'
							,'You make it look easy'
							,'You haven’t missed a thing'
							,'You did that all by yourself'
							,'That’s really nice work!'
							,'You’re doing beautifully!'
							,'You are very good at that'
							,'That’s the way to do it'
							,'It’s perfect!'
							,'Nice going!'
							,'That’s right!'
							,'Well done'
							,'I’m speechless!'
							,'Great work'
							,'How creative'
							,'Keep it up!'
							,'Keep on trying!'
							,'You got it!'
							,'Not bad at all!'
							,'That’s the way!'
							,'Now you have it'
							,'I knew you could do it!'
							,'Great improvement!'
							,'That’s much better'
							,'That’s it exactly'
							,'That’s the best ever'
							,'That’s the way to do it'
							,'Couldn’t have done it better myself '
							,'Tremendous job'
							,'What a creative idea!'
							,'What a good try!'
							,'What a neat work!'
							,'You’re doing well'
							,'You’re learning fast'
							,'That looks like it is going to be a great paper '
							,'That’s quite an improvement'
							,'That’s the right way to do it'
							,'That’s a real work of art'
							,'That’s coming along nicely'
							,'You’re doing a great job'
							,'You’ve just about mastered it'
							,'Your studying really paid off'
							,'You must have been practicing'
							,'You’re on the right track now'
							,'You’re getting better every day'
							,'You’ve just about mastered that'
							,'I’ve never seen anyone do it better'
							,'One more time and you’ll have it'
							,'It looks like you’ve put a lot of work into this'
							,'Now that’s what I call a great job'
							,'We couldn’t have done it without you'
							,'Keep working on it, you’re improving'
							,'I’m happy to see you working like that'
							,'That’s an interesting way of looking at it'
							,'That’s the right way to do it'
							,'You certainly did well today.'
	],
                        media='Photo')
    session.set_do_like(True, percentage=70)
    session.set_delimit_liking(enabled=True, max_likes=100, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=2000,
                                    min_followers=50,
                                    min_following=50)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=200,
                                 peak_likes_daily=585,
                                 peak_comments_hourly=80,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700)

    session.set_user_interact(amount=10, randomize=True, percentage=80)

    # activity
    session.like_by_tags(my_hashtags, amount=15, media=None)
    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=501)
    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="all",
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=501)

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='Art', engagement_mode='no_comments')