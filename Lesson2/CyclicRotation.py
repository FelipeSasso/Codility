# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, K):
    
    if not A:
        return A
    
    lastElement = len(A) - 1
    
    for i in range(K):
        last = A[lastElement]
        for j in range(lastElement, 0, -1):
            A[j] = A[j - 1]
        A[0] = last
    return A
