from os import listdir
from os.path import isfile, join
import numpy as np
import os
from os import walk
import natsort

level = "2"
levelLength = 159
completeLevels = levelLength // 16
extraLevelColumns = levelLength - completeLevels*16
basePath = "./" + level + "/"
path = basePath + "mergedLevel" + level + ".txt"
levelColumn = 0
# mergedMatrix = np.zeros(shape=(14, levelLength))
mergedMatrix = np.chararray(shape=(14, levelLength))
mergedMatrix[:] = 'G'


fileList = os.listdir(basePath)
sortedFileList = natsort.natsorted(fileList,reverse=False)

with open(path, "a") as mergeFile:
    for file in sortedFileList[:-1]:
        with open(basePath + file,"rt") as infile:
            inputLevel = np.matrix([list(line.strip("\n")) for line in infile.readlines()])
            for j in range(0,14):
                for l in range(inputLevel.shape[1]-16,inputLevel.shape[1]):
                    mergedMatrix[j, l+16*levelColumn] = (inputLevel[j, l])
                # mergeFile.write("\n")
            levelColumn+=1
            infile.close()
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