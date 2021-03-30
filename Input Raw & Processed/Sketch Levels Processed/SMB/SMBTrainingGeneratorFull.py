import numpy as np

with open("mario-8-1-Processed.txt","rt") as infile:
    inputLevel =  np.matrix([list(line.strip("\n")) for line in infile.readlines()])
    
print(inputLevel.shape[1]//16)

startRange = 259
endRange = startRange + inputLevel.shape[1]//16
extractLast = False
if inputLevel.shape[1]%16 != 0:
    extractLast = True
levelColumn = 0
for i in range(startRange,endRange):
    # print(i)
    f = open("./trainingExtracted/sketch" + str(i) + ".txt", "w")
    for j in range(0,14):
        for l in range(levelColumn,levelColumn + 16):
            f.write(inputLevel[j, l])
        f.write("\n")
    levelColumn+=16
    f.close()

if extractLast == True:
    f2 = open("./trainingExtracted/sketch" + str(endRange) + ".txt", "w")
    for k in range(0,14):
        for m in range(inputLevel.shape[1]-16,inputLevel.shape[1]):
            f2.write(inputLevel[k, m])
        f2.write("\n")
    f2.close()