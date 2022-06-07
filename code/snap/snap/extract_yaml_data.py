#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:02:21 2020

@author: tdunlap
info: extract data from the yaml files
    combine the category data
    snap data mapping from the dataMapping.csv
"""

import pandas as pd
import numpy as np

def extractYamlData(params, file_name):
    name = params["name"]
    version = params["version"]
    summary = params["summary"]
    plug_distinct = []
    slot_distinct = []
    command = np.nan
    command_chain = np.nan
    environment = {}
    confinement = np.nan
    base = np.nan
    architectures = np.nan
    
    
    plugs=[]
    slots=[]
    apps = []
    apps_plugs = []
    interface = []
    try:
        for element in params["apps"]:
            apps.append(list(params["apps"].keys())[0])
            for each in params["apps"][element]:
                if each == "plugs":
                    plugs.append(params["apps"][element][each])
                if each == "slots":
                    slots.append(params["apps"][element][each])
                if each == "command":
                    command = params["apps"][element][each]
                if each == "command-chain":
                    command_chain = params["apps"][element][each]
                if each == "environment":
                    environment = params["apps"][element][each]
    except Exception as e:
        print(e, file_name)
        
    try:
        for element in params["plugs"]:
            apps_plugs.append(list(params["plugs"].keys())[0])
            for each in params["plugs"][element]:
                if each == "interface":
                    interface.append(params["plugs"][element][each])
    except Exception as e:
        print(e, file_name)
        
    try:
        confinement = params["confinement"]
    except Exception as e:
        print(e, file_name)
    try:
        base = params["base"]
    except Exception as e:
        print(e, file_name)
    try:
        architectures = params["architectures"]
    except Exception as e:
        print(e, file_name)
    
    #distinct list of plugs
    for each in plugs:
        plug_distinct = plug_distinct + each + interface
    plug_distinct = list(set(plug_distinct))
    
    #distinct list of slots
    for each in slots:
        slot_distinct = slot_distinct + each
    slot_distinct = list(set(slot_distinct))
        
    

        
    columns = ["name", "version", "summary", "plugs", "slots", 
               "environment", "command", "command-chain",
               "confinement", "base", "architectures", "apps", "interface"]
        
    results = [[name, version, summary, plug_distinct, slot_distinct, 
                environment, command, command_chain,
                confinement, base, architectures, apps, interface]]
    
    df = pd.DataFrame(results, columns=columns)
    
    return df
                    

def snapCategoryClean(snap_dir, df_snap):
    #combine category data
    df_snap_cat = pd.read_csv(snap_dir + "SnapCategory.csv")
    df_snap_cat['snapName'] = df_snap_cat['snapName'].map(lambda x: x.lstrip('/'))
    df_snap = df_snap.merge(df_snap_cat, left_on="name", right_on="snapName", how="left")
    df_snap = df_snap.drop_duplicates(subset="name", keep="first") #drop dups
        
    #return the clean data sets
    return df_snap

def snapCategoryMapping(df, comparison_dir):
    #get data mapping
    df_data_map = pd.read_csv(comparison_dir + "/categoryMapping.csv")
    data_map = df_data_map[["snapCat", "finalCat"]]
    
    #merge category data
    df = df.merge(data_map[["snapCat", "finalCat"]], 
                              left_on="snapCategory", right_on="snapCat", how="left")
    
    #drop flatpak column
    df = df.drop(columns=["snapCat"])
    

    return df

def snapDataMapping(df, comparison_dir):
    #get data mapping
    df_data_map = pd.read_csv(comparison_dir + "/dataMapping.csv")
    data_map = df_data_map[["fieldName", "snapName"]].values.tolist()
    
    #had some float values in there
    df.plugs = df.plugs.astype(str)
    df.confinement = df.confinement.astype(str)
    
    #data mapping
    for value in data_map:
        field_name = value[0].lower()
        field_map = value[1].lower()
        print(field_map)
        #snap filesystem access
        df[field_name] = df.apply(lambda row: 1 if field_map in row['plugs'].lower() else 0, 
                                            axis = 1)
    df["filesystem_host_access"] = df.apply(lambda row: 1 if "classic" == row['confinement'] else 0, 
                                            axis = 1)
    df["filesystem_host_ro_access"] = df.apply(lambda row: None, 
                                            axis = 1)
    df["filesystem_home_ro_access"] = df.apply(lambda row: None, 
                                            axis = 1)
    
    snap_remove_columns = ['environment',
                       'command', 'command-chain', 
                       'summary']
    
    df = df.drop(columns=snap_remove_columns)
    return df

def snapDataMappingNew(df, comparison_dir):
    #get data mapping
    df_data_map = pd.read_csv(comparison_dir + "/dataMappingNew2.csv")

    filesystem = []
    device = []
    socket = []
    interprocess = []
    network = []
    gui = []
    x11 = []
    filesystem_home_access = []
    filesystem_host_access = []
    network_access = []
    camera = []
    bus_full_access = []
    wayland_access = []
    secrets_password = []
    filesystem_xdg_path = []
    
    df_data_map = df_data_map[["fieldName", "snapName"]].values.tolist()
    
    for each in df_data_map:
        if each[0] == "filesystem" and str(each[1]) != 'nan':
            filesystem.append(each[1])
        if each[0] == "device" and str(each[1]) != 'nan':
            device.append(each[1])
        if each[0] == "socket" and str(each[1]) != 'nan':
            socket.append(each[1])
        if each[0] == "interprocess" and str(each[1]) != 'nan':
            interprocess.append(each[1])
        if each[0] == "network" and str(each[1]) != 'nan':
            network.append(each[1])
        if each[0] == "gui" and str(each[1]) != 'nan':
            gui.append(each[1])
        if each[0] == "x11" and str(each[1]) != 'nan':
            x11.append(each[1])
        if each[0] == "filesystem_home_access" and str(each[1]) != 'nan':
            filesystem_home_access.append(each[1])
        if each[0] == "filesystem_host_access" and str(each[1]) != 'nan':
            filesystem_host_access.append(each[1])
        if each[0] == "network_access" and str(each[1]) != 'nan':
            network_access.append(each[1])
        if each[0] == "camera" and str(each[1]) != 'nan':
            camera.append(each[1])
        if each[0] == "bus_full_access" and str(each[1]) != 'nan':
            bus_full_access.append(each[1])
        if each[0] == "wayland_access" and str(each[1]) != 'nan':
            wayland_access.append(each[1])
        if each[0] == "secrets_password" and str(each[1]) != 'nan':
            secrets_password.append(each[1])
        if each[0] == "filesystem_xdg_path" and str(each[1]) != 'nan':
            filesystem_xdg_path.append(each[1])
    
    #create a new column for each lookup
    df["filesystem"] = df.apply(lambda row: 1 if len(set(filesystem) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    #give filesystem access to classic confinement applications
    df["filesystem"] = df.apply(lambda row: 1 if row['confinement'] == "classic" else row["filesystem"], 
                                                axis = 1)
    
    df["device"] = df.apply(lambda row: 1 if len(set(device) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
     #give network access to classic confinement applications
    df["device"] = df.apply(lambda row: 1 if row['confinement'] == "classic" else row["device"], 
                                                axis = 1)
    
    df["socket"] = df.apply(lambda row: 1 if len(set(socket) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    #give network access to classic confinement applications
    df["socket"] = df.apply(lambda row: 1 if row['confinement'] == "classic" else row["socket"], 
                                                axis = 1)
    
    df["interprocess"] = df.apply(lambda row: 1 if len(set(interprocess) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    #give network access to classic confinement applications
    df["interprocess"] = df.apply(lambda row: 1 if row['confinement'] == "classic" else row["interprocess"], 
                                                axis = 1)
    
    df["network"] = df.apply(lambda row: 1 if len(set(network) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    #give network access to classic confinement applications
    df["network"] = df.apply(lambda row: 1 if row['confinement'] == "classic" else row["network"], 
                                                axis = 1)
    
    df["gui"] = df.apply(lambda row: 1 if len(set(gui) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    #give network access to classic confinement applications
    df["gui"] = df.apply(lambda row: 1 if row['confinement'] == "classic" else row["gui"], 
                                                axis = 1)
    
    df["x11"] = df.apply(lambda row: 1 if len(set(x11) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    #give network access to classic confinement applications
    df["x11"] = df.apply(lambda row: 1 if row['confinement'] == "classic" else row["x11"], 
                                                axis = 1)
    
    df["filesystem_home_access"] = df.apply(lambda row: 1 if len(set(filesystem_home_access) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    #give network access to classic confinement applications
    df["filesystem_home_access"] = df.apply(lambda row: 1 if row['confinement'] == "classic" else row["filesystem_home_access"], 
                                                axis = 1)
    
    
    df["filesystem_host_access"] = df.apply(lambda row: 1 if len(set(filesystem_host_access) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    #give network access to classic confinement applications
    df["filesystem_host_access"] = df.apply(lambda row: 1 if row['confinement'] == "classic" else row["filesystem_host_access"], 
                                                axis = 1)
    
    
    df["network_access"] = df.apply(lambda row: 1 if len(set(network_access) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    #give network access to classic confinement applications
    df["network_access"] = df.apply(lambda row: 1 if row['confinement'] == "classic" else row["network_access"], 
                                                axis = 1)
    
    df["camera"] = df.apply(lambda row: 1 if len(set(camera) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    
    df["bus_full_access"] = df.apply(lambda row: 1 if len(set(bus_full_access) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    
    df["wayland_access"] = df.apply(lambda row: 1 if len(set(wayland_access) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    #give network access to classic confinement applications
    df["wayland_access"] = df.apply(lambda row: 1 if row['confinement'] == "classic" else row["wayland_access"], 
                                                axis = 1)
    
    df["secrets_password"] = df.apply(lambda row: 1 if len(set(secrets_password) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    
    df["filesystem_xdg_path"] = df.apply(lambda row: 1 if len(set(filesystem_xdg_path) & set(row['plugs'])) > 0 else 0, 
                                                axis = 1)
    
    
    snap_remove_columns = ['environment',
                       'command', 'command-chain', 
                       'summary']
    
    df = df.drop(columns=snap_remove_columns)
    return df