
# If the current combination is done - add it to output.
# Iterate over the integers from first to n.
# Add integer i into the current combination curr.
# Proceed to add more integers into the combination : backtrack(i + 1, curr).
# Backtrack by removing i from curr.

# Approach
# backtracking style


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(first=1, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        backtrack()
        return output


s = Solution()
s.combine(4, 2)

# Lexicographic (binary sorted) combinations
# Initiate nums as a list of integers from 1 to k. Add n + 1 as a last element, it will serve as a sentinel.
# Set the pointer in the beginning of the list j = 0.

# While j < k :

# Add the first k elements from nums into the output, i.e. all elements but the sentinel.

# Find the first number in nums such that nums[j] + 1 != nums[j + 1] and increase it by one nums[j]++ to move to the next combination.


# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         # init first combination
#         nums = list(range(1, k + 1)) + [n + 1]

#         output, j = [], 0
#         while j < k:
#             # add current combination
#             output.append(nums[:k])
#             # increase first nums[j] by one
#             # if nums[j] + 1 != nums[j + 1]
#             j = 0
#             while j < k and nums[j + 1] == nums[j] + 1:
#                 nums[j] = j + 1
#                 j += 1
#             nums[j] += 1

#         return output
