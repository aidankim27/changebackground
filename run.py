import urllib.request as urllib2
import sys
import json
import time
import wget

url="https://www.reddit.com/r/EarthPorn/top/.json"

def getpicture(url):
    seen=open("/usr/local/bin/changebackground/seen.txt","r+")
    s=seen.read()
    seenlist=s.split("\n")
    print(seenlist,"\n")
    obj=urllib2.urlopen(url)
    data=json.load(obj)
    for i in data["data"]["children"]:
        jpgurl=i["data"]["url"]
        if(jpgurl in seenlist):
            continue
        if(jpgurl[8:17]=='instagram'):
            continue
        break
    filename=wget.download(jpgurl,"/Users/aidankim/Documents/backgrounds/background.jpg")
    seen.write(jpgurl+"\n")
    seen.close()

def getlastpicture(url):
    seen=open("/usr/local/bin/changebackground/seen.txt","r")
    s=seen.read()
    seenlist=s.split("\n")
    print(seenlist)
    jpgurl = seenlist.pop()
    seen.close()
    if(jpgurl==''):
        jpgurl  = seenlist[-2]
    else:
        jpgurl = seenlist[-1]
    print(jpgurl)
    filename=wget.download(jpgurl,"/Users/aidankim/Documents/backgrounds/background.jpg")

if(sys.argv[1]=='last'): 
    getlastpicture(url) 
else:
    getpicture(url)
