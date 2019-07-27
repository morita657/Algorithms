class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        prosessed = []
        splitted_s = s.split("[")
        for elem in splitted_s:
            if "]"in elem:
                splitted_elem = elem.split("]")
                # concat in prosessed
                prosessed = prosessed + splitted_elem
            else:
                prosessed.append(elem)
        num = 0
        string = ""
        result = ""
        for e in prosessed:
            if e.isdigit():
                num = e
            else:
                string = e
            result += string * num
        return result
