# -*- coding: utf-8 -*-

import time

# measure process time
t0 = time.clock()

wordcount={}
for word in open("/media/miguel/LFS/test0-aa","r"):
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
        
count = 0
ciudad = ""
for num in wordcount:
    print(num, wordcount[num])
    
for num in wordcount:
    if wordcount[num] > count:
        count = wordcount[num]
        ciudad = num
        
print(ciudad, count)    

print ("Seconds time: " , time.clock() - t0)



