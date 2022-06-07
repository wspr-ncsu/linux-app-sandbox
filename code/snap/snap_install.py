#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 08:44:54 2020

@author: tdunlap
@info: module to create executable shell scripts to install snap applications
"""
import os
import pandas

#set data/install directory 
data_dir = os.getcwd() + "/data/"
install_dir = os.getcwd() + "/install_scripts/"

#import snap info
df_snaps = pandas.read_csv(data_dir + "SnapInfo.csv")

#install all the games
# df_games = df_snaps[df_snaps["snapCategory"] == "games"]
install_list = df_snaps[["snapName", "snapInstallCommand"]].drop_duplicates()
install_list = install_list.values.tolist()
install_list = [[s[0].replace('/',''), s[1]] for s in install_list] #remove slash in name



#creating a shell script with commands to install the snaps
f_install=open(install_dir + "install_snap_apps_complete_missing_matching.sh", "w+")
f_install.write("#!/bin/sh \n")
install_total = len(install_list)
for index, snap_name in enumerate(install_list):
    f_install.write("%s\n" % snap_name[1])
    f_install.write("python3 snap_details.py %s\n" % snap_name[0])
    f_install.write("sudo snap remove %s\n" % snap_name[0])
    f_install.write("echo " + str(index) + " of " + str(install_total) + " completed\n")
    f_install.write("# ~~~~~~~~\n")
f_install.close()
#make the shell script executable 
os.system("chmod +x " + install_dir + "install_snap_apps_complete_missing_matching.sh")

#creating a shell script with commands to uninstall the installed snaps
f_uninstall=open(install_dir + "uninstall_snap_apps.sh", "w+")
f_uninstall.write("#!/bin/sh \n")
for command in install_list:
    f_uninstall.write("%s\n" % command.replace("install", "remove"))
f_uninstall.close()
#make the shell script executable 
os.system("chmod +x " + install_dir + "uninstall_snap_apps.sh")

print("done")
