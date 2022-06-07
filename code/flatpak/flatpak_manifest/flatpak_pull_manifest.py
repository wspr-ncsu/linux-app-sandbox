#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:28:29 2020

@author: tdunlap

info: pulling all of the flatpak apps info from flathub.org
"""
import requests
import pandas
import time
import os

#pull data from flathub.org
def flathubRequest():
    #retrieve all flathub apps
    url = 'https://flathub.org/api/v1/apps'
    
    response = requests.get(url=url) #request response from url
    data = pandas.DataFrame(response.json()) #parse json from response into pandas 
    
    #add github url path to the data frame
    github_url = 'https://github.com/flathub/'
    data['githHubRepo'] = data.apply(lambda row: github_url + row['flatpakAppId'], 
                                    axis = 1)
    #this is the flatpak info from flathub
    return data
    
    
#download each manifest file from their respective github repo.  
#looking for either json or yaml file
#the raw link contains the actual file: https://raw.githubusercontent.com/flathub/...
def flatpakManifest(app_info, data_dir): 
    flatpak_app_id = app_info['flatpakAppId'].tolist() #convert df column to list
    flatpak_app_id.remove("org.mozilla.firefox")
    data_dir = data_dir + "manifest/"
    app_list = []
    for index, app_id in enumerate(flatpak_app_id):
        try:
            time.sleep(0.2) #sleep so we don't get blocked
            raw_file_url = 'https://raw.githubusercontent.com/flathub/' + app_id + '/master/' + app_id + '.json'
            file = requests.get(raw_file_url)
            
            if file.status_code == 200: #check if json manifest file exists
                directory = data_dir + app_id + '.json'
                f = open(directory, 'wb') #open and write bytes
                f.write(file.content) #write file
                f.close()
                print(index, raw_file_url)
                app_list.append([app_id, app_id + '.json'])
                
            elif file.status_code == 404: #pull yaml file
                time.sleep(0.2)
                raw_file_url = 'https://raw.githubusercontent.com/flathub/' + app_id + '/master/' + app_id + '.yaml'
                file = requests.get(raw_file_url)
                if file.status_code == 200:
                    directory = data_dir + app_id + '.yaml'
                    f = open(directory, 'wb') #open and write bytes
                    f.write(file.content) #write file
                    f.close()
                    print(index, raw_file_url)
                    app_list.append([app_id, app_id + '.yaml'])
                else: #files can also be named with yml extension
                    time.sleep(0.2)
                    raw_file_url = 'https://raw.githubusercontent.com/flathub/' + app_id + '/master/' + app_id + '.yml'
                    file = requests.get(raw_file_url)
                    directory = data_dir + app_id + '.yml'
                    f = open(directory, 'wb') #open and write bytes
                    f.write(file.content) #write file
                    f.close()
                    print(index, raw_file_url)
                    app_list.append([app_id, app_id + '.yml'])
    
        except Exception:
            print(Exception)
    app_list.append(known_issues(data_dir))
    return app_list
