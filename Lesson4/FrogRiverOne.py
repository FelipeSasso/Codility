"""
Copyright [2015] <Felipe Coral Sasso>
FrogRiverOne.py
"""
def solution(X, A):
    
    count = X
    arraySize = len(A)    
    newArray = [0 for i in xrange(arraySize)]
    
    if arraySize == 1:
        if A[0] < X:
            return -1
    
    for i in xrange(arraySize):
        
        if newArray[A[i] - 1] == 0:
            newArray[A[i] - 1] = newArray[A[i] - 1] + 1
            count = count - 1
        
        if count == 0:
            return i
    
    return -1
