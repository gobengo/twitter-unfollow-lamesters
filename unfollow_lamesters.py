#!/usr/bin/env python

import sys
import argparse
import tweepy

def search_print_unfollow(SCREEN_NAME, PASSWORD, DESTRUCTIVE, *TERMS):
    if DESTRUCTIVE and not PASSWORD:
        raise Exception("Authentication required for destructive operations. Please add a password argument.")

    print("Connecting to twitter API.")
    if SCREEN_NAME and PASSWORD:
        print("Authenticating.")
        auth = tweepy.BasicAuthHandler(SCREEN_NAME, PASSWORD)
        api = tweepy.API(auth)
    else:
        api = tweepy.API()

    print("Retrieving friend list.")
    friends = set()
    for friend in tweepy.Cursor(api.friends, screen_name=SCREEN_NAME).items():
        friends.add(friend)
        
    print("Searching.")
    lamester_dict = dict.fromkeys(TERMS)
    for term in TERMS:
        lamester_dict[term] = set()
        for friend in friends:
            if friend.description:
                if term.lower() in friend.description.lower():
                    lamester_dict[term].add(friend)

    print('')
    unfollow = set()
    for term, lamesters in lamester_dict.items():
        print("'{0}' Lamesters:".format(term))
        if lamesters:
            for lamester in lamesters:
                print "\t* {0} ({1})".format(lamester.name, lamester.screen_name),
                if DESTRUCTIVE:
                    unfollow.add(lamester)
                    print('unfollowed')
                else:
                    print('')
        else:
            print('\tNone')
    for l in unfollow:
        api.destroy_friendship(screen_name=l.screen_name)
    print('')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Search the description/bio field of your twitter friends to root out potential lamesters")

    parser.add_argument('screen_name', type=str, help="Screen name of twitter user whose friends list you'd like to search against")
    parser.add_argument('-p', '--password', action='store', dest='password', help="Password of twitter account. Only necessary for destructive operation.")
    parser.add_argument('-D', '--destructive', action='store_true', help="Act destructively. That is, unfollow those who match your search.")
    parser.add_argument('terms', action='store', nargs='+', help="The case-insensitive terms you'd like to search descriptions for (e.g. 'SEO', 'social media').")

    args = parser.parse_args()

    SCREEN_NAME = args.screen_name
    PASSWORD = args.password
    DESTRUCTIVE = args.destructive
    TERMS = args.terms

    search_print_unfollow(SCREEN_NAME, PASSWORD, DESTRUCTIVE, *TERMS)
