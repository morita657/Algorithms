class Solution(object):
    def __init__(self):
        self.visited = False

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        v = [[False] * len(image[0]) for _ in range(len(image))]
        origin = image[sr][sc]
        self.compute(image, sr, sc, newColor, v, origin)
        return image

    def compute(self, image, sr, sc, newColor, vm, origin):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != origin or vm[sr][sc] == True:
            return
        image[sr][sc] = newColor
        vm[sr][sc] = True
        self.compute(image, sr + 1, sc, newColor, vm, origin)
        self.compute(image, sr - 1, sc, newColor, vm, origin)
        self.compute(image, sr, sc + 1, newColor, vm, origin)
        self.compute(image, sr, sc - 1, newColor, vm, origin)
