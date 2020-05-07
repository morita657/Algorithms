class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
#         split and convert elements into integer
        def splitter(version):
            splitted = version.split(".")
            for i in range(len(splitted)):
                splitted[i] = int(splitted[i])
            return splitted
        
        first = splitter(version1)
        second = splitter(version2)
#         add 0s if there are differences between the length of two versions
        if len(first) > len(second):
            count = len(first) - len(second)
            for _ in range(count):
                second.append(0)
        else:
            count = len(second) - len(first)
            for _ in range(count):
                first.append(0)
#                 compare
        for i in range(len(first)):
            if first[i] > second[i]:
                return 1
            if first[i] < second[i]:
                return -1
        return 0
