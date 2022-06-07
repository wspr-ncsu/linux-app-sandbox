#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:35:43 2020

@author: tdunlap
info: module to scrape snapcraft
"""
import requests
from bs4 import BeautifulSoup
import datetime

#get html soup page for requested url
def getSoup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url=url, headers=headers) #request response from url
    soup = BeautifulSoup(response.content, 'html.parser')
    
    return soup

#snapcraft store only shows apps in category types
def getCategory(soup):
    category = soup.findAll("div", {"class": "js-store-category"})
    
    categories = []
    
    for each in category:
        categories.append(each["data-category"])
    
    return categories

#get last page number for each category
def getLastPage(soup):
    page = soup.findAll("nav", {"class": "u-fixed-width u-clearfix"})
    
    pages = []
    
    for last_page in page:
        for a in last_page.findAll("a"):
            pages.append(a["href"])
    return pages

#get the apps listed on each category page
def getSnaps(soup, category):
    
    snaps = soup.findAll("a", {"class": "p-media-object p-media-object--snap"})
    
    snap_names = []
    
    featured = soup.find("a", {"class": "p-featured-snap--banner"})
    if featured != None:
        snap_names.append([featured["href"], category])
    
    for snap_name in snaps:
        snap_names.append([snap_name["href"], category])

    return snap_names


def getInstallCommand(soup):
    command = soup.findAll("input", {"class": "p-code-copyable__input"})
    final_command = None
    for each in command:
        final_command = each['value']

    if final_command == None:
        final_command = soup.find("code", {"id": "snap-install"}).text

    return final_command

def getRefreshLicense(soup):
    license_value = soup.findAll("dd", {"data-live": "license"})
    for each in license_value:
        license_result = each.text.strip()
    
    refresh_value = soup.findAll("dd")
    
    values = []
    for each in refresh_value:
        values = values + [each.text.strip()]
    
    #convert to datetime
    try:
        values[1] = datetime.datetime.strptime(str(values[1]), '%d %b %Y')
    except:
        try:
            values[1] = datetime.datetime.strptime(str(values[1]), '%d %B %Y')
        except:
            try:
                values[1] = str(values[1])
            except:
                print(values)
                values.append("missing")
                print("missing time")
            
        
    return values
    # all_dd = refresh_value.find("dd")
    # print(all_dd)