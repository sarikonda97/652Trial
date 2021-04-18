import numpy as np
import statistics as std

coCreativities = ['Random', "MinUnique", "MaxUnique", "MaxSMB", "MaxReward", "MaxKI", "MaxEnemies", "Last", "First", "FiftyFifty"]
# mergedIdentifier = "mergedLevel"
kiFolders = ["level1", "level2", "level3", "level4", "level5", "level6"]
kiFiles = ["mergedlevel1", "mergedlevel2", "mergedlevel3", "mergedlevel4", "mergedlevel5", "mergedlevel6"]
marioFolders = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
marioFiles = ["mergedlevel1", "mergedlevel2", "mergedlevel3", "mergedlevel4", "mergedlevel5", "mergedlevel6", "mergedlevel7", "mergedlevel8", "mergedlevel9", "mergedlevel10", "mergedlevel11", "mergedlevel12", "mergedlevel13", "mergedlevel14", "mergedlevel15"  ]
# KILengths = [173, 203, 281, 159, 206, 233]

for coCreativity in coCreativities:
    kiDensityFactor = 0
    smbDensityFactor = 0
    densities = []
    for kiFolder, kiFile in zip(kiFolders, kiFiles):
        kiDensityFactor = 0
        with open("../generatedSections/" + coCreativity + "/KI Generated/" + kiFolder + "/" + kiFile + ".txt","rt") as kiInfile:
        # currentKILevel = np.loadtxt("../generatedSections/" + coCreativity + "/KI Generated/" + kiFolder + "/" + kiFile + ".txt", dtype='V')
            currentKILevel = np.matrix([list(line.strip("\n")) for line in kiInfile.readlines()])
        # do something here
            pass
            for k in range(0, currentKILevel.shape[0]):
                for m in range(0, currentKILevel.shape[1]):
                    if currentKILevel[k, m] != '-' and currentKILevel[k, m] != '#':
                        kiDensityFactor += 1
            density = kiDensityFactor/(currentKILevel.shape[0] * currentKILevel.shape[1])
            # print ("The density of " + "co-creativity type " + coCreativity + " and level " + kiFolder + " is: " + str(density))
        densities.append(density)
    print("\n")
    for smbFolder, smbFile in zip(marioFolders, marioFiles):
        smbDensityFactor = 0
        with open("../generatedSections/" + coCreativity + "/SMB Generated/" + smbFolder + "/" + smbFile + ".txt","rt") as smbInfile:
            currentSMBLevel = np.matrix([list(line.strip("\n")) for line in smbInfile.readlines()])
            for k in range(0, currentSMBLevel.shape[0]):
                for m in range(0, currentSMBLevel.shape[1]):
                    if currentSMBLevel[k, m] != '-' and currentSMBLevel[k, m] != 'X':
                        smbDensityFactor += 1
            density = smbDensityFactor/(currentSMBLevel.shape[0] * currentSMBLevel.shape[1])
            # print ("The density of " + "co-creativity type " + coCreativity + " and level " + smbFolder + " is: " + str(smbDensityFactor/(currentSMBLevel.shape[0] * currentSMBLevel.shape[1])))
    #     # do something here
    #     pass
        densities.append(density)
    # print("The mean of the densities for " + "co-creativity type " + coCreativity + " is: " + str(sum(densities)/len(densities)))
    print("The mean of the interestingness for " + "co-creativity type " + coCreativity + " is: " + str(std.mean(densities)) )
    print("\nThe SD of the interestingness for " + "co-creativity type " + coCreativity + " is: " + str(std.stdev(densities)))
    print("\n")
    print("-----------------------------------------------------")
        