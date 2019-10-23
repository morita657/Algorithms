class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=0
        ret=""
        carry=0
        while i<max(len(a),len(b)) or carry>0:
            aC=0
            bC=0
            if i<len(a):
                aC=int(a[len(a)-i-1])
            if i<len(b):
                bC=int(b[len(b)-i-1])
            ret = str(aC ^ bC ^ carry)+ret
            carry = ((aC ^ bC) & carry) | (aC & bC)
            i += 1
        return ret