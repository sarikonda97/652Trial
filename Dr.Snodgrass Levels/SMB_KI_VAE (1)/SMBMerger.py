from os import listdir
from os.path import isfile, join
import numpy as np
import os
from os import walk
import natsort

basePath = "./SMB-VAE/"
fileList = os.listdir(basePath)
sortedFileList = natsort.natsorted(fileList,reverse=False)

starter = 0
ender = 1
for levelNo in range(0,10):
    levelColumn = 0
    mergedMatrix = np.chararray(shape=(14, 140))
    mergedMatrix[:] = 'G'
    for file in sortedFileList[starter*10:ender*10]:
        with open(basePath + file,"rt") as infile:
            inputLevel = np.matrix([list(line.strip("\n")) for line in infile.readlines()])
            for j in range(0,14):
                for l in range(0, 14):
                    mergedMatrix[j, l+14*levelColumn] = (inputLevel[j, l])
                # mergeFile.write("\n")
            levelColumn+=1    
        infile.close()
        
    with open((basePath + "SMBLevel" + str(ender) + ".txt"), "a") as mergeFile:
        for row in range(0,14):
            for col in range(0, 140):
                mergeFile.write(mergedMatrix[row, col].decode("utf-8"))
            mergeFile.write("\n")
    mergeFile.close()
    starter += 1
    ender += 1
