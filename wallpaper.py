#!/usr/bin/env python3
import json
import os
import random
import sys
# note: the wallpaper folder has to be in the chrome folder

updatedusercontent = []
scriptpath = os.path.dirname(os.path.realpath(__file__))
arguments = sys.argv

with open(scriptpath + '/wallpaper-cfg.json', 'rt') as cfg:
    cfgdata = json.load(cfg)
    folname = cfgdata['wallpaperfoldername']
    cfg.close()

if cfgdata['change']:
    for profile in cfgdata['chromefilepath']:
        with open(profile + '/userContent.css', 'rt') as con:
            usercontent = con.read().split('\n')
            con.close()
        
        wallpapers = os.listdir(profile + '/' + folname)
        randomwallpaper = ''
        if len(arguments) == 1:
            randomwallpaper = wallpapers[random.randint(0, len(wallpapers)-1)]
        else: 
            match arguments[1]:
                case '-wi':
                    randomwallpaper = wallpapers[int(arguments[1+1])%len(wallpapers)]
                case '-wn':
                    randomwallpaper = arguments[1+1]
        
        #print(randomwallpaper)
        for line in usercontent:
            if 'background-image' in line:
                front = line[0:line.index('(')+1]
                back = line[line.index(')'):len(line)]
                combined = '{}"{}/{}"{}'
                combined = combined.format(front, folname, randomwallpaper, back)
                updatedusercontent.append(combined)
            else:
                updatedusercontent.append(line)
        
        temp = updatedusercontent.copy()
        updatedusercontent = ''
        for line in temp:
            updatedusercontent = updatedusercontent + line + "\n"
        #print(updatedusercontent)
        with open(profile + '/userContent.css', "w") as cont:
            cont.write(updatedusercontent.rstrip())
