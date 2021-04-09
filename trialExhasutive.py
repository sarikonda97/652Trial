import numpy as np
import pickle
import os, os.path
import random
import sys

def check(a, b, upper_left):
    ul_row = upper_left[0]
    ul_col = upper_left[1]
    b_rows, b_cols = b.shape
    a_slice = a[ul_row : ul_row + b_rows, :][:, ul_col : ul_col + b_cols]
    # parent_Slice = parent[ul_row : ul_row + b_rows, :][:, ul_col : ul_col + b_cols]
    if a_slice.shape != b.shape:
        return False
    return (a_slice == b).all() # here also need to return the parent matric slice

def find_slice(big_array, small_array, complex, base, noOfSamples):
  results = []
  for sample in range(0, noOfSamples):
    upper_left = np.argwhere(big_array[sample] == small_array[0,0])
    for ul in upper_left:
      if check(big_array[sample], small_array, ul): # need to keep checking for all values and store them instead of just returning
          start_x = ul[0]
          start_y = ul[1]
          end_x = ul[0] + small_array.shape[0]
          end_y = ul[1] + small_array.shape[1]
          results.append(complex[sample][start_x:end_x,start_y:end_y])
          # print(ul)
  if(len(results)==0):
    #if not found in basic matrix return from base matrix
    return base[:len(small_array),:len(small_array[0])+1]
  else:
    return results

def introduceCoCreativity(results, mode):
  if mode == "first":
    return results[0]
  elif mode == "last":
    return results[-1]
  elif mode == "random":
    return random.choice(results)
  # write something for max enemies
  elif mode == "maxEnemies":
    index = 0
    enemyCount = 0
    maxIndex = 0
    maxEnemyCount = 0
    for result in results:   
      unique, counts = np.unique(result, return_counts=True)
      uniqueList = np.array(unique).reshape(-1,).tolist()
      # countList = counts.tolist()
      for i in range(0, len(uniqueList)):
        if uniqueList[i] == 'H' or uniqueList[i] == 'E':
          # enemyCount += countList[i]
          enemyCount += 1
      if enemyCount > maxEnemyCount:
        maxEnemyCount = enemyCount
        maxIndex=index
      index+=1
    return results[maxIndex]
  elif mode == "fifty-fifty":
    index = 0
    mostEqualIndex = 0
    mostEqualDifference = sys.maxsize
    KICount = 0
    SMBCount = 0
    KITiles = ['#', 'D', 'H', 'M', 'T']
    SMBTiles = ['S', '?', 'Q', 'E', '<', '>', '[', ']', 'o', 'B', 'b']
    for result in results:
      resultArray = result.reshape(-1,).tolist()[0]
      for i in range(0, len(resultArray)):
        if resultArray[i] in KITiles:
          KICount += 1
        if resultArray[i] in SMBTiles:
          SMBCount += 1
      # targetProportionality = len(resultArray)/2
      # if abs(targetProportionality - KICount) < abs(targetProportionality - SMBCount):
      #   if abs(targetProportionality - KICount) < abs(targetProportionality - mostEqualCount):
      #     mostEqualCount = KICount
      #     mostEqualIndex = index
      # else:
      #   if abs(targetProportionality - SMBCount) < abs(targetProportionality - mostEqualCount):
      #     mostEqualCount = SMBCount
      #     mostEqualIndex = index
      if abs(SMBCount - KICount) < mostEqualDifference:
        mostEqualDifference = abs(SMBCount - KICount)
        mostEqualIndex = index
      index+=1
      KICount = 0
      SMBCount = 0
    return results[mostEqualIndex]
  elif mode == "maxUnique":
    index=0
    maxUniqueSize = 0
    maxUniqueIndex = 0
    uniqueSet = set()
    for result in results:
      resultArray = result.reshape(-1,).tolist()[0]
      for resultElement in resultArray:
        uniqueSet.add(resultElement)
      if len(uniqueSet) > maxUniqueSize:
        maxUniqueSize = len(uniqueSet)
        maxUniqueIndex = index
      uniqueSet.clear()
      index+=1
    return results[maxUniqueIndex]
  elif mode == "minUnique":
    index=0
    minUniqueSize = sys.maxsize
    minUniqueIndex = 0
    uniqueSet = set()
    for result in results:
      resultArray = result.reshape(-1,).tolist()[0]
      for resultElement in resultArray:
        uniqueSet.add(resultElement)
      if len(uniqueSet) < minUniqueSize:
        minUniqueSize = len(uniqueSet)
        minUniqueIndex = index
      uniqueSet.clear()
      index+=1
    return results[minUniqueIndex]
  elif mode == "maxKI":
    index=0
    KICount = 0
    maxKICount = 0
    maxKIIndex = 0
    for result in results:
      resultArray = result.reshape(-1,).tolist()[0]
      KITiles = ['#', 'D', 'H', 'M', 'T']
      for resultElement in resultArray:
        if resultElement in KITiles:
          KICount+=1
      if KICount > maxKICount:
        maxKICount = KICount
        maxKIIndex = index
      index += 1
      KICount = 0
    return results[maxKIIndex]
  elif mode == "maxSMB":
    index=0
    SMBCount = 0
    maxSMBCount = 0
    maxSMBIndex = 0
    for result in results:
      resultArray = result.reshape(-1,).tolist()[0]
      SMBTiles = ['S', '?', 'Q', 'E', '<', '>', '[', ']', 'o', 'B', 'b']
      for resultElement in resultArray:
        if resultElement in SMBTiles:
          SMBCount+=1
      if SMBCount > maxSMBCount:
        maxSMBCount = SMBCount
        maxSMBIndex = index
      index += 1
      SMBCount = 0
    return results[maxSMBIndex]
  elif mode == "maxReward":
    index=0
    RewardCount = 0
    maxRewardCount = 0
    maxRewardIndex = 0
    for result in results:
      resultArray = result.reshape(-1,).tolist()[0]
      RewardTiles = ['o']
      for resultElement in resultArray:
        if resultElement in RewardTiles:
          RewardCount+=1
      if RewardCount > maxRewardCount:
        maxRewardCount = RewardCount
        maxRewardIndex = index
      index += 1
      RewardCount = 0
    return results[maxRewardIndex]
          
        
      
  

def select_from_result(result, cordinates, final, mode):
    #for now printing first element of the result
    print("the number of outputs identified")
    print(len(result))
    print("This is the output")
    # selected = result[0]
    selected = introduceCoCreativity(result, mode)
    print(selected)
    k = 0;
    for i in range(cordinates["top-left"][0], cordinates["bottom-left"][0]+1):
      l = 0;
      for j in range(cordinates["top-left"][1], cordinates["bottom-right"][1]+1):
        final[i, j] = selected[k, l]
        l+=1;
      k+=1;
    # for i in range(0,len(result)):
    # 	print(result[i])
    # print("\n")

cordinatesFile = open("./subsections/cordinates", "rb")
cordinates = pickle.load(cordinatesFile)
print(cordinates)


print("No of files")
listFiles = os.listdir('./subsections') # dir is your directory path
number_files = len(listFiles)
number_files -= 1 #removing the cordinates file
print (number_files)

# loading base
with open("inputBase.txt","rt") as infile:
    base =  np.matrix([list(line.strip('\n')) for line in infile.readlines()])
  
print(base)
    
# loading all training full resolutions
sampleSize = 282
full = []
for trainingCount in range(0, sampleSize):
  with open("./training/original/full" + str(trainingCount) + ".txt","rt") as infile:
    full.append(np.matrix([list(line.strip('\n')) for line in infile.readlines()]))
    
# loading all training sketch resolutions
sketch = []
for trainingCount in range(0, sampleSize):
  with open("./training/sketch/sketch" + str(trainingCount) + ".txt","rt") as infile:
    sketch.append(np.matrix([list(line.strip('\n')) for line in infile.readlines()]))

# initializing final output file
final = np.empty([14,16], dtype="str")

coCreativityMode = 'maxReward'
# main driver code
for subsection in range(0, number_files):
  with open("./subsections/subSection" + str(subsection) + ".txt","rt") as infile:
    sub_matrix =  np.matrix([list(line.strip('\n')) for line in infile.readlines()])
    select_from_result(find_slice(sketch, sub_matrix, full, base, sampleSize), cordinates[subsection], final, coCreativityMode)

print(final)
f = open("./generatedSections/finalSection.txt", "w")
for i in range(final.shape[0]):
    for j in range(final.shape[1]):
        f.write(final[i,j])
    f.write("\n")
f.close()

