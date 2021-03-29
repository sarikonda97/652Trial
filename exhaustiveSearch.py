import numpy as np

a = np.array([[0,1,5,6,7],
              [0,4,5,6,8],
              [2,3,5,7,9]])

# with open('filename.txt') as file:
#     # array2d = [[chr(digit) for digit in line.split()] for line in file]
#     array2d = np.genfromtxt('filename.txt',dtype=None)

# with open('filename.txt', 'r') as f:
#     array2d = np.genfromtxt(f,comments="!",dtype=None)

with open("filename.txt","rt") as infile:
    partition =  np.matrix([list(line.strip()) for line in infile.readlines()])
    
with open("mario-1-1.txt","rt") as infile:
    inputF =  np.matrix([list(line.strip()) for line in infile.readlines()])
    


print(partition)
print(inputF)

b = np.array([[5,6],
              [5,7]])

b2 = np.array([[6,7],
               [6,8],
               [7,9]])

print(a)
print(b)
print(b2)

def check(a, b, upper_left):
    ul_row = upper_left[0]
    ul_col = upper_left[1]
    b_rows, b_cols = b.shape
    a_slice = a[ul_row : ul_row + b_rows, :][:, ul_col : ul_col + b_cols]
    # parent_Slice = parent[ul_row : ul_row + b_rows, :][:, ul_col : ul_col + b_cols]
    if a_slice.shape != b.shape:
        return False
    return (a_slice == b).all() # here also need to return the parent matric slice

def find_slice(big_array, small_array):
    upper_left = np.argwhere(big_array == small_array[0,0])
    for ul in upper_left:
        if check(big_array, small_array, ul): # need to keep checking for all values and store them instead of just returning
            return True
    else:
        return False
    
print(find_slice(a, b))