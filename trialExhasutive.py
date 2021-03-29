import numpy as np
import pickle
import os, os.path

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

def select_from_result(result, cordinates, final):
    #for now printing first element of the result
    print("This is the output")
    selected = result[0]
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
full = []
for trainingCount in range(0, 11):
  with open("./training/original/full" + str(trainingCount) + ".txt","rt") as infile:
    full.append(np.matrix([list(line.strip('\n')) for line in infile.readlines()]))
    
# loading all training sketch resolutions
sketch = []
for trainingCount in range(0, 11):
  with open("./training/sketch/sketch" + str(trainingCount) + ".txt","rt") as infile:
    sketch.append(np.matrix([list(line.strip('\n')) for line in infile.readlines()]))

# initializing final output file
final = np.empty([14,16], dtype="str")

# main driver code
for subsection in range(0, number_files):
  with open("./subsections/subSection" + str(subsection) + ".txt","rt") as infile:
    sub_matrix =  np.matrix([list(line.strip('\n')) for line in infile.readlines()])
    select_from_result(find_slice(sketch, sub_matrix, full, base, 11), cordinates[subsection], final)

print(final)
f = open("./finalSection.txt", "w")
for i in range(final.shape[0]):
    for j in range(final.shape[1]):
        f.write(final[i,j])
    f.write("\n")
f.close()

