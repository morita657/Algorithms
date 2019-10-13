class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
            print(n)
        return n == 1

class Solution:
    def isHappy(self, n: int) -> bool:
        flag = True
        seen=[]
        current = []
        ans=False
        while True:
            for i in range(len(str(n))):
                current.append(int(str(n)[i])**2)
            total = sum(current)
            if total==1:
                ans=True
                break
            else:
                if total in seen:
                    ans=False
                    break
                else:
                    seen.append(total)
                    n=total
                    current=[]
        return ans