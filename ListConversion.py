'''
This is used if you want to convert a list of a bunch of things to a json file
Useful if you need a list to compare against
'''

import json
fulllist = []
f= open("keywords.txt","r")
for line in f:
    line = line.replace("\n","")
    temp = line.split(" ")
    for word in temp:
        if word:
            fulllist.append(word)
with open("keywords.json","w") as outfile:
    json.dump(fulllist,outfile)
    
