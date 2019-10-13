class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        commons = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j] and i + j in commons.keys():
                    commons[i + j].append(list1[i])
                elif list1[i] == list2[j] and not i + j in commons.keys():
                    commons[i + j] = [list1[i]]
        ans = []
        for k in range(len(commons[list(commons.keys())[0]])):
            ans.append(commons[list(commons.keys())[0]][k])
        return ans
