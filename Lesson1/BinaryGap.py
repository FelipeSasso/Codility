"""
Copyright [2015] <Felipe Coral Sasso>
BinaryGap.py
"""

def solution(N):
    a = bin(N)
    maxCount = 0
    count = 0
    for i in xrange(2, len(a)):        
        if (str(a[i]) == str(0)):            
            count = count + 1            
        else:
            if (count > maxCount):
                maxCount = count                
            count = 0
    return maxCount
