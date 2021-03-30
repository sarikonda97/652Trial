import numpy as np

with open("kidicarus_6.txt","rt") as infile:
    inputLevel =  np.matrix([list(line.strip("\n")) for line in infile.readlines()])
    
print(inputLevel.shape[0]//14)

startRange = 76
endRange = startRange + inputLevel.shape[0]//14
extractLast = False
if inputLevel.shape[0]%14 != 0:
    extractLast = True
levelLine = 0
for i in range(startRange,endRange):
    # print(i)
    f = open("./trainingExtracted/full" + str(i) + ".txt", "w")
    for j in range(0,14):
        for l in range(0,16):
            f.write(inputLevel[levelLine, l])
        f.write("\n")
        levelLine+=1
    f.close()

if extractLast == True:
    f2 = open("./trainingExtracted/full" + str(endRange) + ".txt", "w")
    for k in range(inputLevel.shape[0]-14, inputLevel.shape[0]):
        for m in range(0,16):
            f2.write(inputLevel[k, m])
        f2.write("\n")
    f2.close()
        