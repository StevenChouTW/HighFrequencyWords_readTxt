# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:37:08 2021

@author: Steven

"""

import os
def topKFrequentWords( words, k):
    # write your code here
    wordlist = []

    worddic={}
    
    for word in words:
        if word in worddic:
            worddic[word] =   worddic[word]+1
        else:
            worddic[word]=1
        
    for key, v in worddic.items():
        wordlist.append((key, v))
        
    wordlistSort = sorted(wordlist)
    wordlistSort.sort(key=lambda x:x[1],reverse=True)

    resultWordlist=[]
    for i in range(0,k,1):
        resultWordlist.append(wordlistSort[i][0])
        
    return resultWordlist
            

# read data
f = open(r"E:\01_imageSet\txt\result.txt")
text = []
for line in f:
    text.append(line)

# list 200 top Frequenct words
Final_wordlist=topKFrequentWords(text,200)
print(Final_wordlist)

# write result data
path = r'E:\01_imageSet\txt\topFrequency.txt'

if(os.path.isfile(path)):
    os.remove(path)
    
write_f = open(path, 'a')
write_f.writelines(Final_wordlist)
write_f.close()