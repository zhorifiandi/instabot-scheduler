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
import os

def start_smart_run(arguments):
    username = arguments['username'][0]
    passkey = arguments['passkey'][0]
    hashtags = arguments['hashtags'][0]
    influencers = arguments['influencers'][0]

    # get a session!
    session = InstaPy(username=username, password=passkey, bypass_suspicious_attempt=True, headless_browser=True)
    business_target = str(influencers).split(',')

    # let's go! :>
    with smart_run(session):
        # general settings
        session.set_relationship_bounds(enabled=True,
                                        potency_ratio=None,
                                        delimit_by_numbers=True,
                                        max_followers=6000,
                                        max_following=3000,
                                        min_followers=30,
                                        min_following=30)
        session.set_user_interact(amount=2, randomize=True, percentage=30,
                                  media='Photo')
        session.set_do_like(enabled=True, percentage=60)
        session.set_do_comment(enabled=True, percentage=40)
        session.set_comments(
            [u'Semoga sehat selalu ya Bunda. Kami punya minyak '
            u'kutus kutus lho, bagus banget buat si kecil kalo lagi '
            u'flu, cek ya bun :wink:',
            u'Halo Bunda. Sudah coba minyak kutus kutus? Bagus banget buat si kecil lagi flu, cek ya bun :wink:',
            u'Halo Bunda. Semoga sehat terus ya dedeknya :smile:'
            u' Sudah coba minyak kutus kutus? Bagus banget buat'
            u' si kecil lagi flu, cek ya bun :wink:'],
            media='Photo')

        # # follow activity
        ammount_number = 500
        session.follow_user_followers(business_target,
                                      amount=ammount_number, randomize=False,
                                      interact=True, sleep_delay=240)

        hashtags = str(hashtags).split(',')
        random.shuffle(hashtags)
        my_hashtags = hashtags[:10]

        session.set_delimit_liking(enabled=True, max=100, min=0)
        session.set_delimit_commenting(enabled=True, max=400, min=0)
        session.set_relationship_bounds(enabled=True,
                                        potency_ratio=None,
                                        delimit_by_numbers=True,
                                        max_followers=3000,
                                        max_following=2000,
                                        min_followers=10,
                                        min_following=10)
        # activity
        session.like_by_tags(my_hashtags, amount=60, media=None)
        session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                               style="FIFO",
                               unfollow_after=12 * 60 * 60, sleep_delay=501)
        session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                               style="FIFO", unfollow_after=24 * 60 * 60,
                               sleep_delay=501)
