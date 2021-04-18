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
    kiLinearityFactor = []
    smbLinearityFactor = []
    nonLinearities = []
    for kiFolder, kiFile in zip(kiFolders, kiFiles):
        kiLinearityFactor = []
        with open("../generatedSections/" + coCreativity + "/KI Generated/" + kiFolder + "/" + kiFile + ".txt","rt") as kiInfile:
        # currentKILevel = np.loadtxt("../generatedSections/" + coCreativity + "/KI Generated/" + kiFolder + "/" + kiFile + ".txt", dtype='V')
            currentKILevel = np.matrix([list(line.strip("\n")) for line in kiInfile.readlines()])
        # do something here
            pass
            for k in range(0, currentKILevel.shape[0]):
                for m in range(0, currentKILevel.shape[1]):
                    if currentKILevel[k, m] != '-':
                        kiLinearityFactor.append(m)
            nonLinearity = sum(kiLinearityFactor)/len(kiLinearityFactor)
            print ("The non-linearity of " + "co-creativity type " + coCreativity + " and level " + kiFolder + " is: " + str(sum(kiLinearityFactor)/len(kiLinearityFactor)))
        nonLinearities.append(nonLinearity)
    print("\n")
    for smbFolder, smbFile in zip(marioFolders, marioFiles):
        smbLinearityFactor = []
        with open("../generatedSections/" + coCreativity + "/SMB Generated/" + smbFolder + "/" + smbFile + ".txt","rt") as smbInfile:
            currentSMBLevel = np.matrix([list(line.strip("\n")) for line in smbInfile.readlines()])
            for k in range(0, currentSMBLevel.shape[0]):
                for m in range(0, currentSMBLevel.shape[1]):
                    if currentSMBLevel[k, m] != '-':
                        smbLinearityFactor.append(k )
            nonLinearity = sum(smbLinearityFactor)/len(smbLinearityFactor)
            print ("The non-linearity of " + "co-creativity type " + coCreativity + " and level " + smbFolder + " is: " + str(sum(smbLinearityFactor)/len(smbLinearityFactor)))
    #     # do something here
    #     pass
        nonLinearities.append(nonLinearity)
    print("The mean of the nonLinearities for " + "co-creativity type " + coCreativity + " is: " + str(std.mean(nonLinearities)) )
    print("\nThe SD of the nonLinearities for " + "co-creativity type " + coCreativity + " is: " + str(std.stdev(nonLinearities)))
    print("\n")
    print("-----------------------------------------------------")
        