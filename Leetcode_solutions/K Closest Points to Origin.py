class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d=[]
        total=[]
        for i in range(len(points)):
            distance = pow(points[i][0],2) + pow(points[i][1],2)
            d.append([distance, points[i]])
        d.sort()
        for j in range(K):
            total.append(d[j][1])
        return total
            