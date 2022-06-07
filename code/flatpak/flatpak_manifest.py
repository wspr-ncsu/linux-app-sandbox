#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:25:28 2020

@author: tdunlap
info: main file to run. Will get list of apps from Flathub, download the
respective manifest file from GitHub.
"""
from flatpak_manifest import flatpak_pull_manifest as fp
import pandas as pd
import os

#set data directory and error directory
data_dir = os.getcwd() + "/data/"
error_dir = data_dir + "error_files/"

#create error directory if it doesn't exist
if not os.path.exists(error_dir):
     os.makedirs(error_dir)
     
#pulls initial apps from flathub.org
app_info = fp.flathubRequest()
print("App Info", len(app_info))

#downloads all of the manifest files from their respective GitHub Repo
app_names = fp.flatpakManifest(app_info, data_dir)

print("done")
