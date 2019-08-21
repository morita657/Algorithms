# If the current combination is done - add it to output.

# Iterate over the integers from first to n.

# Add integer i into the current combination curr.

# Proceed to add more integers into the combination : backtrack(i + 1, curr).

# Backtrack by removing i from curr.

# Approach
# backtracking style


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
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
