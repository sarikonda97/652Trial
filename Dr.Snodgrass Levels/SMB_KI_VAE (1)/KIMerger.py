from os import listdir
from os.path import isfile, join
import numpy as np
import os
from os import walk
import natsort

basePath = "./KI-VAE/"
fileList = os.listdir(basePath)
sortedFileList = natsort.natsorted(fileList,reverse=False)

starter = 0
ender = 1
for levelNo in range(0,10):
    for file in sortedFileList[starter*10:ender*10]:
        with open((basePath + "KILevel" + str(ender) + ".txt"), "a") as mergeFile:
            with open(basePath + file,"rt") as infile:
                inputLevel = np.matrix([list(line.strip("\n")) for line in infile.readlines()])
                for k in range(inputLevel.shape[0]-16, inputLevel.shape[0]):
                    for m in range(0,16):
                        mergeFile.write(inputLevel[k,m])
                    mergeFile.write('\n')
                infile.close()
        mergeFile.close()
    starter += 1
    ender += 1