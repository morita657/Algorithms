class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hashtable = {"6": "9", "9": "6", "8": "8"}
        original = num
        copy = ["" for _ in num]
        for n in range(len(num)):
            if num[n] in hashtable.keys():
                print('hi')
                copy[n] = hashtable[num[n]]
            else:
                copy[n] = num[n]
        print(original, copy, "".join(copy))
        return original == "".join(copy[::-1])
