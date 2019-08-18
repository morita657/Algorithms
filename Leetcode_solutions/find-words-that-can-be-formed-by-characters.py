class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        output = ""
        characters = []
        for i in range(len(chars)):
            characters.append(chars[i])
        for i in range(len(words)):
            copy = characters[:]
            if self.checker(words[i], copy):
                output += words[i]

        return len(output)

    def checker(self, target, source):
        for i in range(len(target)):
            if target[i] in source:
                source.pop(source.index(target[i]))
            else:
                return False
        return True
