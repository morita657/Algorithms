class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
    # def replaceWords(self, roots, sentence):
        rootset = set(dict)

        def replace(word):
            # print(word)
            for i in range(1, len(word)):
                # print(word[:i])
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))