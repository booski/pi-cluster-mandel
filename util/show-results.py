import sys
import os
from PIL import Image
import time

base = os.path.dirname(os.path.realpath(__file__))
size = int(sys.argv[1])
itermax = int(sys.argv[2])
width = size
height = size

resultdir = base + "/results"
resultlist = {}
for result in os.listdir(resultdir):
    with open(resultdir + "/" + result) as infile:
        resultlist.update({(int(x),int(y)): int(i) for (x,y,i) in [tuple(line.strip().split(',')) for line in infile]})

img = Image.new('RGB', (width,height), "white")
pixels = img.load()

def getColor(iteration, itermax):
    colormax = 0xffffff
    colorval = int(iteration / (itermax / float(0xffffff)))
    r = (colorval & 0xff0000) / 0x00ffff
    g = (colorval & 0x00ff00) / 0x0000ff
    b = (colorval & 0x0000ff)
    return (r,g,b)

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if resultlist.has_key((x,y)):
            iteration = resultlist[(x,y)]
            pixels[x,y] = getColor(iteration, itermax)


img.save(base + "/images/" + "result-" + time.strftime("%y%m%d-%H%M") + ".png")
