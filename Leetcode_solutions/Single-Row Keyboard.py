class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        time = 0
        currentPos = 1
        for ch in word:
            nextPos = keyboard.index(ch) + 1
            diff = abs(nextPos - currentPos)
            time += diff
            currentPos = nextPos
        return time
