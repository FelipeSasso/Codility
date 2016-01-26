"""
Copyright [2015] <Felipe Coral Sasso>
FrogJmp.py
"""

import math

def solution(X, Y, D):    
    
    if X == Y:
        return 0
    
    return int(math.ceil(float(Y - X) / float(D)))
