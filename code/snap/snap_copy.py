#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:34:17 2020

@author: tdunlap
"""
import time
import os
import yaml
from shutil import copyfile
import sys

snap_name = sys.argv[1]

start = time.time()
#set data directory 
data_dir = os.getcwd() + "/data/yaml/"

#snap directory
snap_yaml = "/snap/" + snap_name + "/current/meta/snap.yaml"

#copy file from installation path
copyfile(snap_yaml, data_dir + snap_name + "_snap.yaml")


# file = data_dir + "snap.yaml"

# with open(file) as f:
# #loads a subset of the YAML language safely
#     yaml_data = yaml.load(f, Loader=yaml.SafeLoader) 
#     f.close()
    
