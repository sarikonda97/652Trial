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




coCreativities = ['Random', "MinUnique", "MaxUnique", "MaxSMB", "MaxReward", "MaxKI", "MaxEnemies", "Last", "First", "FiftyFifty"]
# mergedIdentifier = "mergedLevel"
kiFolders = ["level1", "level2", "level3", "level4", "level5", "level6"]
kiFiles = ["mergedlevel1", "mergedlevel2", "mergedlevel3", "mergedlevel4", "mergedlevel5", "mergedlevel6"]
marioFolders = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
marioFiles = ["mergedlevel1", "mergedlevel2", "mergedlevel3", "mergedlevel4", "mergedlevel5", "mergedlevel6", "mergedlevel7", "mergedlevel8", "mergedlevel9", "mergedlevel10", "mergedlevel11", "mergedlevel12", "mergedlevel13", "mergedlevel14", "mergedlevel15"  ]
KILengths = [173, 203, 281, 159, 206, 233]
SMBLengths = [202, 158, 150, 197, 197, 149, 222, 187, 198, 150, 184, 215, 165, 176, 373]


for coCreativity in coCreativities:
    # for kiFolder, kiFile, kiLength in zip(kiFolders, kiFiles, KILengths):
    #     with open("./generatedSections/" + coCreativity + "/KI Generated/" + kiFolder + "/" + kiFile + ".txt","rt") as fp:
    #         level = {}
    #         y = 0
    #         for line in fp:
    #             level[y] = line
    #             y+=1

    #     image = Image.new("RGB", (256, 16*kiLength), color=(0, 0, 0))
    #     pixels = image.load()

    #     maxY = kiLength
    #     maxX = 16

    #     for y in range(0, maxY):
    #         for x in range(0, maxX):
    #             imageToUse = None
    #             if level[y][x] in visualization.keys():
    #                 imageToUse = sprites[visualization[level[y][x]]]
    #             elif level[y][x]=="X":
    #                     if y>maxY-2:
    #                         imageToUse = sprites["marioGround"]
    #                     else:
    #                         imageToUse = sprites["stair"]
    #             if not imageToUse == None:
    #                 pixelsToUse = imageToUse.load()
    #                 for x2 in range(0, 16):
    #                     for y2 in range(0, 16):
    #                         if pixelsToUse[x2,y2][3]>0:
    #                             pixels[x*16+x2,y*16+y2] = pixelsToUse[x2,y2][0:-1]

    #     image.save("./visualizedSections/kiLevels/" + coCreativity + kiFile + ".jpeg", "JPEG")

            
            
    for smbFolder, smbFile, smbLength in zip(marioFolders, marioFiles, SMBLengths):
        with open("./generatedSections/" + coCreativity + "/SMB Generated/" + smbFolder + "/" + smbFile + ".txt","rt") as fp:
            level = {}
            y = 0
            for line in fp:
                level[y] = line
                y+=1

        image = Image.new("RGB", (16*smbLength, 224), color=(91, 153, 254))
        pixels = image.load()

        maxY = 14
        maxX = smbLength

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

        image.save("./visualizedSections/smbLevels/" + coCreativity + smbFile + ".jpeg", "JPEG")

            
            
            



# #Visualize Output Level
# level = {}
# with open("./generatedSections/finalSection.txt") as fp:
# 	y = 0
# 	for line in fp:
# 		level[y] = line
# 		y+=1

# image = Image.new("RGB", (256, 224), color=(0, 0, 0))
# pixels = image.load()

# maxY = 14
# maxX = 16

# for y in range(0, maxY):
# 	for x in range(0, maxX):
# 		imageToUse = None
# 		if level[y][x] in visualization.keys():
# 			imageToUse = sprites[visualization[level[y][x]]]
# 		elif level[y][x]=="X":
# 				if y>maxY-2:
# 					imageToUse = sprites["marioGround"]
# 				else:
# 					imageToUse = sprites["stair"]
# 		if not imageToUse == None:
# 			pixelsToUse = imageToUse.load()
# 			for x2 in range(0, 16):
# 				for y2 in range(0, 16):
# 					if pixelsToUse[x2,y2][3]>0:
# 						pixels[x*16+x2,y*16+y2] = pixelsToUse[x2,y2][0:-1]

# image.save("./visualizedSections/output.jpeg", "JPEG")
