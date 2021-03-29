import numpy as np
import re

file1 = open('mario-8-1.txt', 'r')
Lines = file1.readlines()

with open('mario-8-1-Processed.txt', 'a') as the_file:
    count = 0
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
        modifiedline = re.sub("[^/-]", "#", line.strip("\n"))
        print("Modified Line{}: {}".format(count, modifiedline.strip()))
        the_file.write(modifiedline.strip())
        the_file.write('\n')
the_file.close()
file1.close()
    