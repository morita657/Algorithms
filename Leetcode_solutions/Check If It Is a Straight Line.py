class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        answer=False
        x1=coordinates[0][0]
        y1=coordinates[0][1]
        x2=coordinates[1][0]
        y2=coordinates[1][1]
        xdiff = x2-x1
        ydiff = y2-y1
        if coordinates[0][0] == coordinates[1][0]:
            diff = 100000
        else:
            diff = ydiff/xdiff
        if len(coordinates)==2:
            return True
        for i in range(2,len(coordinates)):
            current_diff = (coordinates[i][1]-coordinates[0][1]) / (coordinates[i][0]-coordinates[0][0])
            if current_diff != diff:
                return False
        return True