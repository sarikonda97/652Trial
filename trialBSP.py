import numpy as np
import pickle

with open("partition.txt","rt") as infile:
    base =  np.matrix([list(line.strip()) for line in infile.readlines()])

with open("inputBase.txt","rt") as infile:
    inputBase =  np.matrix([list(line.strip()) for line in infile.readlines()])

print(base)
# print(base[0,0])

# print(base.shape[1])

def checkAboveMeBorder(row, col, border):
    for j in range(border, col):
        if base[row-1, j] != '#':
            return False
        else:
            return True

subsections = []
TopLeftBorder = []
BottomLeftBorder = []
TopRightBorder = []
BottomRightBorder = []
start = 0

for i in range(0, base.shape[0]):
    for j in range(0, base.shape[1]):
        # print(i,j)
        if base[i,j] == '-' and base[i, j-1] == '#' and base[i-1, j-1] == '#' and base[i-1, j] == '#':
            TopLeftBorder.append((i-1, j-1))
        if base[i,j] == '-' and base[i, j-1] == '#' and base[i+1, j-1] == '#' and base[i+1, j] == '#':
            if i+1 == base.shape[0]-1:
                BottomLeftBorder.append((i+1, j-1))
            else:
                BottomLeftBorder.append((i, j-1))
            
        if base[i,j] == '-' and base[i, j+1] == '#' and base[i-1, j+1] == '#' and base[i-1, j] == '#':
            if j+1 == base.shape[1]-1:
                TopRightBorder.append((i-1, j+1))
            else:
                TopRightBorder.append((i-1, j))
        if base[i,j] == '-' and base[i, j+1] == '#' and base[i+1, j+1] == '#' and base[i+1, j] == '#':
            if i+1 != base.shape[0]-1 and j+1 == base.shape[1]-1:
                BottomRightBorder.append((i, j+1))
            elif i+1 == base.shape[0]-1 and j+1 != base.shape[1]-1:
                BottomRightBorder.append((i+1, j))
            elif i+1 == base.shape[0]-1 and j+1 == base.shape[1]-1:
                BottomRightBorder.append((i+1, j+1))
            else:
                BottomRightBorder.append((i, j))
            
        # if base[i,j] == '-' and base[i, j+1] == '#':
        #     if checkAboveMeBorder(i, j, start):
        #         rightBorder = (i-1,j)
        #         print(rightBorder)
        #     # else:
        pass
    
# print (TopLeftBorder)
# print (TopRightBorder)
# print (BottomLeftBorder)
# print (BottomRightBorder)

finalTopCord = []
finalBottomCord = []
topPossible = []
bottomPossible = []

for tl in TopLeftBorder:
    for tr in TopRightBorder:
        if tl[0] == tr[0] and tl[1] < tr[1]:
            topPossible.append(tr[1])
    topCords = {"top-left": tl, "top-right": (tl[0], min(topPossible))}
    topPossible = []
    finalTopCord.append(topCords)
for bl in BottomLeftBorder:
    for br in BottomRightBorder:
        if bl[0] == br[0] and bl[1] < br[1]:
            bottomPossible.append(br[1])
    bottomCords = {"bottom-left": bl, "bottom-right": (bl[0], min(bottomPossible))}
    bottomPossible = []
    # finalBottomCord.append({**topCords, **bottomCords})
    finalBottomCord.append(bottomCords)

# print(finalTopCord)
# print(finalBottomCord)

min = {}
btm = []
finalCords = []
for top in finalTopCord:
    for bottom in finalBottomCord:
        # print(top['top-left'][1])
        if top['top-left'][1] == bottom['bottom-left'][1] and top['top-left'][0] < bottom['bottom-left'][0]:
            btm.append(bottom)
    min = btm[0]
    for b in btm:
        if b['bottom-left'][0] < min['bottom-left'][0]:
            min = b
    btm = []
    finalCords.append({**top, **min})
# print(finalCords)

subsectionCount = 0
for fc in finalCords:
    f = open("./subsections/subSection" + str(subsectionCount) + ".txt", "w")
    for i in range(fc["top-left"][0], fc["bottom-left"][0]+1):
        for j in range(fc["top-left"][1], fc["bottom-right"][1]+1):
            print (inputBase[i,j], end="")
            f.write(inputBase[i,j])
        print("\n")
        f.write("\n")
    subsectionCount += 1
    f.close()

cordFile = open('./subsections/cordinates', 'wb')
pickle.dump(finalCords, cordFile)
cordFile.close()