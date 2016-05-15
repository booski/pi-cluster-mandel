#!/usr/bin/env python

import sys
import os
from PIL import Image
import time

base = os.path.dirname(os.path.realpath(__file__))
size = int(sys.argv[1])
itermax = int(sys.argv[2])
width = size
height = size

resultdir = base + "/../rundata/results"
resultlist = {}
for result in os.listdir(resultdir):
    if not result.startswith('.'):
        with open(resultdir + "/" + result) as infile:
            resultlist.update({(int(x),int(y)): int(i) for (x,y,i) in [tuple(line.strip().split(',')) for line in infile]})
            
img = Image.new('RGB', (width,height), "black")
pixels = img.load()

def getColor(iteration, itermax):
    colorval = int(iteration / (itermax / float(0xffffff)))
    r = 0xff - (colorval & 0xff0000) / 0x00ffff
    g = 0xff - (colorval & 0x00ff00) / 0x0000ff
    b = 0xff - (colorval & 0x0000ff)
    return (r,g,b)

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if resultlist.has_key((x,y)):
            iteration = resultlist[(x,y)]
            pixels[x,y] = (x,y,int(iteration / (itermax / float(0xff))))
            # pixels[x,y] = getColor(iteration, itermax)


img.save(base + "/../images/" + "result-" + time.strftime("%y%m%d-%H%M") + ".png")
