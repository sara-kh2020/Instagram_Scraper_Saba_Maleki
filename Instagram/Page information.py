#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:52:38 2020

@author: saba
"""

import pandas as pd
import numpy as np
import sqlalchemy
import psycopg2
import time
import datetime
import instaloader


L = instaloader.Instaloader()
profile = instaloader.Profile.from_username(L.context, 'autopegasus.az')
pages_information = pd.DataFrame(columns=[ 'biography',
 'blocked_by_viewer',
 'business_category_name',
 'external_url',
 'followed_by_viewer',
 'followees',
 'followers',
 'full_name',
 'has_highlight_reels',
 'has_public_story',
 'igtvcount',
 'is_business_account',
 'is_private',
 'is_verified',
 'profile_pic_url',
 'userid',
 'username',
 'last_update'])

pages_information=pages_information.append({
'biography': profile.biography,
'blocked_by_viewer' :profile.blocked_by_viewer,
'business_category_name' : profile.business_category_name,
'external_url' :profile.external_url ,
'followed_by_viewer' : profile.followed_by_viewer,
'followees': profile.followees,
'followers': profile.followers,
'full_name':profile.full_name,
'has_highlight_reels':profile.has_highlight_reels,
'has_public_story':profile.has_public_story,
'igtvcount':profile.igtvcount,
'is_business_account':profile.is_business_account,
'is_private':profile.is_private,
'is_verified':profile.is_verified,
'profile_pic_url':profile.profile_pic_url,
'userid': profile.userid,
'username':profile.username,
'last_update':datetime.datetime.now()
} , ignore_index=True)

engine =sqlalchemy.create_engine('postgresql://test:6037@localhost:5432/autopegasus.az') 
con = engine.connect()
table_name = 'Page_information'
pages_information.to_sql(table_name, con, if_exists = 'append', index = False)
#print(engine.table_names())
con.close()
#print(engine.table_names())
#print(pages_information)