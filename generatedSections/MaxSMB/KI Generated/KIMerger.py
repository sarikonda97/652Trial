from os import listdir
from os.path import isfile, join
import numpy as np
import os
from os import walk
import natsort

levelNos = ["level1","level2", "level3", "level4", "level5", "level6"]
levelLengths = [173, 203, 281, 159, 206, 233]

for levelVal, levelLengthVal in zip(levelNos, levelLengths):
    level = levelVal
    levelLength = levelLengthVal
    completeLevels = levelLength // 14
    extraLevelLines = levelLength - completeLevels*14
    basePath = "./" + level + "/"
    path = basePath + "merged" + level + ".txt"

    # print(basePath)
    # print(path)
    fileList = os.listdir(basePath)
    sortedFileList = natsort.natsorted(fileList,reverse=False)

    with open(path, "a") as mergeFile:
        for file in sortedFileList[:-1]:
            with open(basePath + file,"rt") as infile:
                inputLevel = np.matrix([list(line.strip("\n")) for line in infile.readlines()])
                for k in range(inputLevel.shape[0]-14, inputLevel.shape[0]):
                    for m in range(0,16):
                        mergeFile.write(inputLevel[k,m])
                    mergeFile.write('\n')
                infile.close()
        with open(basePath + sortedFileList[-1], "rt") as infile:
            inputLevel = np.matrix([list(line.strip("\n")) for line in infile.readlines()])
            for k in range(inputLevel.shape[0]-extraLevelLines, inputLevel.shape[0]):
                for m in range(0,16):
                    mergeFile.write(inputLevel[k,m])
                mergeFile.write('\n')
        mergeFile.close()