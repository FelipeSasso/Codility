"""
Copyright [2015] <Felipe Coral Sasso>
TapeEquilibrium.py
"""
def solution(A):    

        P = len(A)
        sumLeft = A[0]
        sumRight = sum(A[1:P])
        aux = 9999999
        
        minimalDifference = abs(sumLeft - sumRight)

        for i in range(1, P - 1):                
            sumLeft  += A[i]
            sumRight -= A[i]            
            
            aux = abs(sumLeft - sumRight)
            
            if aux < minimalDifference:
                minimalDifference = aux
        
        return minimalDifference
