#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from instabot_py import InstaBot

def run_the_bot(arguments):
    username = arguments['username'][0]
    passkey = arguments['passkey'][0]
    hashtags = str(arguments['hashtags'][0]).split(',')
    target_nickname = arguments['target_nickname'][0]

    bot = InstaBot(
        login=username,  # Enter username (lowercase). Do not enter email!
        password=passkey,
        like_per_day=1000,
        comments_per_day=0,
        tag_list=hashtags,
        tag_blacklist=["rain", "thunderstorm"],
        user_blacklist={},
        max_like_for_one_tag=50,
        follow_per_day=300,
        follow_time=1 * 60 * 60,
        unfollow_per_day=300,
        unlike_per_day=0,
        unfollow_recent_feed=True,
        # If True, the bot will also unfollow people who dont follow you using the recent feed. Default: True
        time_till_unlike=3 * 24 * 60 * 60,  # 3 days
        unfollow_break_min=15,
        unfollow_break_max=30,
        user_max_follow=0,
        # session_file=False, # Set to False to disable persistent session, or specify custom session_file (ie ='myusername.session')
        user_min_follow=0,
        log_mod=0,
        proxy="",
        # List of list of words, each of which will be used to generate comment
        # For example: "This shot feels wow!"
        comment_list=[
            ["Semoga sehat selalu ya {} 😍".format(target_nickname), "Halo {}... Lucu banget dehh! 😍".format(target_nickname), "Halo {}. Semoga sehat terus ya sekeluarga! 😍".format(target_nickname)],
            ["Sudah coba minyak kutus kutus?","Kami punya minyak kutus kutus lhoo!"],
            ["Bagus banget buat si kecil kalo lagi flu atau demam", "Khasiatnya banyak banget lhoo, bisa buat berbagai macam penyakit juga!", "Bisa buat pegel-pegel, gangguan syaraf, bahkan buat vitalitas!"],
            ["Btw, kita lagi ada promo gratis ongkir lho, mampir yuk cek ig kita ya"],
            [".", "🙌", "... 👏", "!", "! 😍", "😎"],
        ],
        # Use unwanted_username_list to block usernames containing a string
        # Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
        # 'free_followers' will be blocked because it contains 'free'
        unwanted_username_list=[
            "second",
            "stuff",
            "art",
            "project",
            "love",
            "life",
            "food",
            "blog",
            "free",
            "keren",
            "photo",
            "graphy",
            "indo",
            "travel",
            "art",
            "shop",
            "store",
            "sex",
            "toko",
            "jual",
            "online",
            "murah",
            "jam",
            "kaos",
            "case",
            "baju",
            "fashion",
            "corp",
            "tas",
            "butik",
            "grosir",
            "karpet",
            "sosis",
            "salon",
            "skin",
            "care",
            "cloth",
            "tech",
            "rental",
            "kamera",
            "beauty",
            "express",
            "kredit",
            "collection",
            "impor",
            "preloved",
            "follow",
            "follower",
            "gain",
            ".id",
            "_id",
            "bags",
        ],
        unfollow_whitelist=["arizhopratama", "portalmiliarder"],
        # Enable the following to schedule the bot. Uses 24H
        # end_at_h = 23, # Hour you want the bot to stop
        # end_at_m = 30, # Minute you want the bot stop, in this example 23:30
        # start_at_h = 9, # Hour you want the bot to start
        # start_at_m = 10, # Minute you want the bot to start, in this example 9:10 (am).
    )

    bot.mainloop()
