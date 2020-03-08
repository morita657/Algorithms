class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            digits.append(1)
            return digits
        carry = 0
        digits[-1] += 1
        if digits[-1] == 10:
            carry = 1
            digits[-1] = 0
        for i in range(len(digits)-2, -1, -1):
            digits[i] += carry
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
        if carry == 1:
            digits.insert(0, carry)
        return digits