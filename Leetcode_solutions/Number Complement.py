class Solution:
    def findComplement(self, num: int) -> int:
        res=[]
        binary=""
        def converter(number):
            if number>1:
                converter(number // 2)
                res.append(number%2)
            
        if num > 1:
            converter(num)
            for i in range(len(res)):
                if res[i]==1:
                    binary+="0"
                else:
                    binary+="1"
            return int(binary,2)
        else:
            return 0 if num==1 else 1
        