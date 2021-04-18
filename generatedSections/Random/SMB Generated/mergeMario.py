from os import listdir
from os.path import isfile, join
import numpy as np
import os
from os import walk
import natsort

levelNos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
levelLengths = [202, 158, 150, 197, 197, 149, 222, 187, 198, 150, 184, 215, 165, 176, 373]

for level, levelLength in zip(levelNos, levelLengths):
    level = level
    levelLength = levelLength
    completeLevels = levelLength // 16
    extraLevelColumns = levelLength - completeLevels*16
    basePath = "./" + str(level) + "/"
    path = basePath + "mergedLevel" + str(level) + ".txt"
    levelColumn = 0
    # mergedMatrix = np.zeros(shape=(14, levelLength))
    mergedMatrix = np.chararray(shape=(14, levelLength))
    mergedMatrix[:] = 'G'


    fileList = os.listdir(basePath)
    sortedFileList = natsort.natsorted(fileList,reverse=False)
    # completeList = sortedFileList[:-1]
    # incompleteList = ''
    if extraLevelColumns>0:
        completeList = sortedFileList[:-1]
    else:
        completeList = sortedFileList[:]

    with open(path, "a") as mergeFile:
        for file in completeList:
            with open(basePath + file,"rt") as infile:
                inputLevel = np.matrix([list(line.strip("\n")) for line in infile.readlines()])
                for j in range(0,14):
                    for l in range(inputLevel.shape[1]-16,inputLevel.shape[1]):
                        mergedMatrix[j, l+16*levelColumn] = (inputLevel[j, l])
                    # mergeFile.write("\n")
                levelColumn+=1
                infile.close()
        if extraLevelColumns > 0:
            with open(basePath + sortedFileList[-1], "rt") as infile:
                inputLevel = np.matrix([list(line.strip("\n")) for line in infile.readlines()])
                extraColumnCount = 0
                for j in range(0,14):
                    for l in range(inputLevel.shape[1]-extraLevelColumns,inputLevel.shape[1]):
                        mergedMatrix[j, 16*levelColumn+extraColumnCount] = (inputLevel[j, l])
                        extraColumnCount += 1
                    # mergeFile.write("\n")
                    extraColumnCount=0
                infile.close()
        for row in range(0,14):
            for col in range(0, levelLength):
                mergeFile.write(mergedMatrix[row, col].decode("utf-8"))
            mergeFile.write("\n")
        mergeFile.close()