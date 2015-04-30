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
    
