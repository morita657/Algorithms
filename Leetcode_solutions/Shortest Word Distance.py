class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        distance = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                for j in range(len(words)):
                    if words[j] == word2:
                        distance = min(distance, abs(j - i))
        return distance
