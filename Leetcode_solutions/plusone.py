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

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            print(idx)
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1 
                digits[idx] += 1
                # and the job is done
                return digits
                
        # we're here because all the digits are nines
        return [1] + digits