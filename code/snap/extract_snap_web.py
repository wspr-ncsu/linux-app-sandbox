#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 09:26:34 2020

@author: tdunlap
@info: this is the intial file to pull a list of available apps from the
       snapcraft store. The time for script to complete ~7-8 minutes.    
"""
import pandas
import time
import os
import random
from snap import snap_apps as sa

start = time.time()
# set data directory
data_dir = os.getcwd() + "/data/"
print("Data dir:", data_dir)
# get the list of snap categories on snapcraft store
url = "https://snapcraft.io/store"

#gets the beautiful soup response
soup = sa.getSoup(url)
categories = sa.getCategory(soup)

 # get the last page number of each category
category_complete = []
for cat_name in categories:
    print(cat_name)
    category_url = "https://snapcraft.io/search?category=" + cat_name

    soup = sa.getSoup(category_url)
    pages = sa.getLastPage(soup)
    # splitting out the pages so we can properly loop later
    if len(pages) > 0:
        last_page_num = int(pages[-1].split("=")[-1])
    else:
        last_page_num = 1
    category_complete.append([cat_name, 20])

# create a complete list of the snaps
snaps_complete = []
for category in category_complete:
    # category[1] is the last page number for each category
    for category_page in range(1,category[1]+1):
        time.sleep(5) # let's not get blocked
        category_url = "https://snapcraft.io/search?category="+str(category[0])+"&page="+str(category_page)
        print(category_url)
        soup = sa.getSoup(category_url)
        snap_names = sa.getSnaps(soup, category[0])
        snaps_complete = snaps_complete + snap_names

# create final dataframe for easy manipulation
columns = ["snapName","snapCategory"]
df_snaps = pandas.DataFrame(snaps_complete, columns=columns)
df_snaps.to_csv(data_dir + "SnapCategory.csv", encoding='utf-8', index=False)

print("done")
