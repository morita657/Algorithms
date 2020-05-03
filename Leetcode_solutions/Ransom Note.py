from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = defaultdict(int)
        for i in range(len(magazine)):
            magazineDict[magazine[i]] +=1
        for j in range(len(ransomNote)):
            if magazineDict[ransomNote[j]] and magazineDict[ransomNote[j]]>0:
                magazineDict[ransomNote[j]] -=1
            else:
                return False
        return True