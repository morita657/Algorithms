# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dim = binaryMatrix.dimensions()
        print(dim)
        rows = dim[0]
        cols = dim[1]
        
        if rows==0 or cols ==0:
            return -1
        result =-1;
        r=0
        c=cols-1
        while r<rows and c>=0:
            if binaryMatrix.get(r,c) ==1:
                result =c
                c -= 1
            else:
                r += 1
        return result