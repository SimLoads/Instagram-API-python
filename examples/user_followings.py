#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import time
from datetime import datetime

def getTotalFollowing(api, user_id):
    """
    Returns the list of people the user is following.
    It should be equivalent of calling api.getTotalFollowings from InstagramAPI
    """

    api.getUsernameInfo(user_id)
    api.LastJson
    following = []
    next_max_id = True
    while next_max_id:
        print(next_max_id)
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        following.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return following

if __name__ == "__main__":
    api = InstagramAPI("login", "password")
    api.login()
    user_id = api.username_id
    following = getTotalFollowing(api, user_id)
    for elem in following:
        print(elem['username'])
