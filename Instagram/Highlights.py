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
 #dir(item)
USER = 'sabainstaloader1'
PASSWORD = '123456Saba'
L = instaloader.Instaloader()
L.login(USER, PASSWORD)
highlights = pd.DataFrame(columns=[ 'date',
 'date_local',
 'date_utc',
 'expiring_local',
 'expiring_utc',
 'is_video',
 'mediaid',
 'owner_id',
 'profile',
 'url',
 'video_url',
 'last_update'])
for highlight in L.get_highlights(user=33931770850):
    # story is a Story object
    for item in highlight.get_items():
        # item is a StoryItem object
        #L.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))

        highlights=highlights.append({
        'date': item.date,
        'date_local' :item.date_local,
        'date_utc' :item.date_utc,
        'expiring_local' :item.expiring_local ,
        'expiring_utc' : item.expiring_utc,
        'is_video': item.is_video,
        'mediaid': item.mediaid,
        'owner_id':item.owner_id,
        'profile':item.profile,
        'url':item.url,
        'video_url':item.video_url,
        'last_update':datetime.datetime.now()
        } , ignore_index=True)
      

engine =sqlalchemy.create_engine('postgresql://test:6037@localhost:5432/autopegasus.az') 
con = engine.connect()
table_name = 'Highlights'
highlights.to_sql(table_name, con, if_exists = 'append', index = False)
#print(engine.table_names())
con.close()
#print(engine.table_names())
#print(pages_information)