class Solution:
    def shipWithinDays(self, weights, D):
        total = sum(weights)
        # idealCap = total // D
        idealCap = 15
        flag = True
        while flag:
            output = []
            current = []
            for i in range(len(weights)):
                currentTotal = sum(current)

                if (currentTotal - idealCap == 0) or (currentTotal < idealCap and weights[i] > (idealCap - currentTotal)):
                    output.append(current)
                    current = [weights[i]]
                elif currentTotal < idealCap and weights[i] <= (idealCap - currentTotal):
                    current.append(weights[i])
                if len(output) == D and i < len(weights) - 1:
                    break
                else:
                    # elif len(output) == D and i == len(weights) - 1:
                    flag = False
                    break
            if not flag:
                break
            else:
                idealCap += 1
        return idealCap


s = Solution()
s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)


class Solution:
    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = (left + right) / 2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D:
                left = mid + 1
            else:
                right = mid
        return int(left)
