import sys
import os
import glob
from PIL import Image

#Load sprites
sprites = {}
for filename in glob.glob("./sprites/*.png"):
	im = Image.open(filename)
	splits = filename.split("/")
	name = splits[-1][:-4].split("\\")[-1]
	sprites[name] = im

visualization = {}
visualization["#"] = "ground"
visualization["D"] = "door"
visualization["H"] = "hazard"
visualization["M"] = "moving"
visualization["T"] = "grassGround"
visualization["S"] = "brick"
visualization["?"] = "questionMark"
visualization["Q"] = "emptyBlock"
visualization["E"] = "goomba"
visualization["<"] = "topLeftPipe"
visualization[">"] = "topRightPipe"
visualization["["] = "leftPipe"
visualization["]"] = "rightPipe"
visualization["o"] = "coin"
visualization["B"] = "cannonTop"
visualization["b"] = "cannonBottom"

#Visualize Output Level
level = {}
with open("./generatedSections/finalSection.txt") as fp:
	y = 0
	for line in fp:
		level[y] = line
		y+=1

image = Image.new("RGB", (256, 224), color=(0, 0, 0))
pixels = image.load()

maxY = 14
maxX = 16

for y in range(0, maxY):
	for x in range(0, maxX):
		imageToUse = None
		if level[y][x] in visualization.keys():
			imageToUse = sprites[visualization[level[y][x]]]
		elif level[y][x]=="X":
				if y>maxY-2:
					imageToUse = sprites["marioGround"]
				else:
					imageToUse = sprites["stair"]
		if not imageToUse == None:
			pixelsToUse = imageToUse.load()
			for x2 in range(0, 16):
				for y2 in range(0, 16):
					if pixelsToUse[x2,y2][3]>0:
						pixels[x*16+x2,y*16+y2] = pixelsToUse[x2,y2][0:-1]

image.save("./visualizedSections/output.jpeg", "JPEG")
