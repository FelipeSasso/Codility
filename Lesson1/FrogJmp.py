# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

import math

def solution(X, Y, D):    
    
    if X == Y:
        return 0
    
    return int(math.ceil(float(Y - X) / float(D)))
