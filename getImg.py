#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import re
import os
import sys
import urllib
import random


def getImg(color):
    print("Retrieving wallpaper...")
    if color == "0x008080":
        wcolor = "7"
    elif color == "0x007A11":
        wcolor = "4"
    elif color == "0x003355":
        wcolor = "8"
    elif color == "0x660066":
        wcolor = "5"
    elif color == "0x800000":
        wcolor = "9"
    elif color == "0x997300":
        wcolor = "2"
    elif color == "0xe65c00":
        wcolor = "1"
    elif color == "0x829900":
        wcolor = "3"
    else:
        wcolor = "7"

    url = "http://desk.zol.com.cn/fengjing/1920x1080_c" + wcolor + "/"
    req = urllib2.Request(url)
    content = urllib2.urlopen(req).read()

    match = re.compile(r'(?<=href=["]/bizhi).*?(?=["])')
    links = re.findall(match, content)

    ran = random.randint(0, 15)

    url = "http://desk.zol.com.cn/bizhi" + links[ran]
    req = urllib2.Request(url)
    content = urllib2.urlopen(req).read()

    match = re.compile(r'(?<=href=["]/showpic/1920x1080).*?(?=["])')
    links = re.findall(match, content)

    temp = links[0]
    filename = temp[1:len(temp) - 5]
    filename = 'wallpaper/' + filename + '.jpg'

    url = "http://desk.zol.com.cn/showpic/1920x1080" + links[0]
    req = urllib2.Request(url)
    content = urllib2.urlopen(req).read()

    match = re.compile(r'src="(http.+?\.jpg)"')
    img = re.findall(match, content)

    urllib.urlretrieve(img[0], filename)
    return filename
