# -*- coding: utf-8 -*-  

import re

fileName =  'wordtest.txt'
linesCount = 0
wordsCount = 0
charsCount = 0

with open(fileName,"r") as f:
    for line in f:
        #print(line)
        linesCount +=1
        linesList = line.split()
        wordsCount += len(linesList)
        match = re.findall(r'[\s]+',line)
        for i in match:
            line = line.replace(i, '')
        charsCount += len(line)

print(linesCount)
print(charsCount)
print(wordsCount)
