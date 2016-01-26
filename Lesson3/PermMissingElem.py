"""
Copyright [2015] <Felipe Coral Sasso>
PermMissingElem.py
"""

def solution(A):
    # write your code in Python 2.7
    A.sort()
    arraySize = len(A)
    
    if arraySize == 0:
        return 1
    elif arraySize == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    
    if arraySize == A[arraySize - 1]:
        return arraySize + 1
    
    for i in range(arraySize):    
        if i + 1 != A[i]:
            return i + 1
