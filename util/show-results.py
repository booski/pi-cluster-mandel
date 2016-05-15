#!/usr/bin/env python

import sys
import os
from PIL import Image
import time

base = os.path.dirname(os.path.realpath(__file__))
rundata = base + "/../rundata"
size = None
with open(rundata + "/size") as infile:
    size = int(infile.read().strip())
    
itermax = None
with open(rundata + "/iterations") as infile:
    itermax = int(infile.read().strip())

width = size
height = size

resultdir = rundata + "/results"
resultlist = {}
for result in os.listdir(resultdir):
    if not result.startswith('.'):
        with open(resultdir + "/" + result) as infile:
            resultlist.update({(int(x),int(y)): int(i) for (x,y,i) in [tuple(line.strip().split(',')) for line in infile]})
            
img = Image.new('HSV', (width,height), "black")
pixels = img.load()

def getColor(iteration, itermax):
    colorval = iteration % 360
    saturation = 100
    value = 100 - iteration / (itermax / 100)
    return (colorval, saturation, value)
    
    # colorval = int(iteration / (itermax / float(0xffffff)))
    # r = 0xff - (colorval & 0xff0000) / 0x00ffff
    # g = 0xff - (colorval & 0x00ff00) / 0x0000ff
    # b = 0xff - (colorval & 0x0000ff)
    # return (r,g,b)

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if resultlist.has_key((x,y)):
            iteration = resultlist[(x,y)]
            pixels[x,y] = getColor(iteration, itermax)


img.convert('RGB').save(base + "/../images/" + "result-" + time.strftime("%y%m%d-%H%M") + ".png")
