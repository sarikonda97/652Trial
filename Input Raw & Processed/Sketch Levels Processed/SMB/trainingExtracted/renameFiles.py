import os
counter = 0
path = "./"
for file in os.listdir(path):
    if file.endswith(".txt"):
        if file.find("full") > -1:
            counter = counter + 1
            os.rename(os.path.join(path, file), os.path.join(path, file.replace("full", "sketch")))
if counter == 0:
    print("No file has been found")