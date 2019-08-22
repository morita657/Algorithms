import math
#  public class Solution {
#     public int largestRectangleArea(int[] heights) {
#         int maxarea = 0;
#         for (int i = 0; i < heights.length; i++) {
#             for (int j = i; j < heights.length; j++) {
#                 int minheight = Integer.MAX_VALUE;
#                 for (int k = i; k <= j; k++)
#                     minheight = Math.min(minheight, heights[k]);
#                 maxarea = Math.max(maxarea, minheight * (j - i + 1));
#             }
#         }
#         return maxarea;
#     }
# }

# [2,1,5,6,2,3]


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # find the largest
        # linear search and keep the current with the index
        # compare with the left and right side centering the largest element
        maxarea = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                minheight = math.inf
                for k in range(i, j + 1):
                    minheight = min(minheight, heights[k])
                maxarea = max(maxarea, minheight * (j - i + 1))
        return maxarea


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        for i in range(len(heights)):
            minheight = math.inf
            for j in range(i, len(heights)):
                minheight = min(minheight, heights[j])
                maxarea = max(maxarea, minheight * (j - i + 1))
        return maxarea
# public class Solution {
#     public int calculateArea(int[] heights, int start, int end) {
#         if (start > end)
#             return 0;
#         int minindex = start;
#         for (int i = start; i <= end; i++)
#             if (heights[minindex] > heights[i])
#                 minindex = i;
#         return Math.max(heights[minindex] * (end - start + 1), Math.max(calculateArea(heights, start, minindex - 1), calculateArea(heights, minindex + 1, end)));
#     }
#     public int largestRectangleArea(int[] heights) {
#         return calculateArea(heights, 0, heights.length - 1);
#     }
# }


class Solution:
    def calculateArea(self, heights: List[int], start: int, end: int) -> int:
        if start > end:
            return 0
        minindex = start
        for i in range(start, end + 1):
            if heights[minindex] > heights[i]:
                minindex = i
        return max(heights[minindex] * (end - start + 1), max(self.calculateArea(heights, start, minindex - 1), self.calculateArea(heights, minindex + 1, end)))

    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.calculateArea(heights, 0, len(heights) - 1)


# Python3 program to find maximum
# rectangular area in linear time
class Solution:
    def largestRectangleArea(self, histogram: List[int]) -> int:

        # Create an empty stack. The stack
        # holds indexes of histogram[] list.
        # The bars stored in the stack are
        # always in increasing order of
        # their heights.
        stack = list()

        max_area = 0  # Initalize max area

        # Run through all bars of
        # given histogram
        index = 0
        while index < len(histogram):

            # If this bar is higher
            # than the bar on top
            # stack, push it to stack

            if (not stack) or (histogram[stack[-1]] <= histogram[index]):
                stack.append(index)
                index += 1

            # If this bar is lower than top of stack,
            # then calculate area of rectangle with
            # stack top as the smallest (or minimum
            # height) bar.'i' is 'right index' for
            # the top and element before top in stack
            # is 'left index'
            else:
                # pop the top
                top_of_stack = stack.pop()

                # Calculate the area with
                # histogram[top_of_stack] stack
                # as smallest bar
                area = (histogram[top_of_stack] *
                        ((index - stack[-1] - 1)
                         if stack else index))

                # update max area, if needed
                max_area = max(max_area, area)

        # Now pop the remaining bars from
        # stack and calculate area with
        # every popped bar as the smallest bar
        while stack:

            # pop the top
            top_of_stack = stack.pop()

            # Calculate the area with
            # histogram[top_of_stack]
            # stack as smallest bar
            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))

            # update max area, if needed
            max_area = max(max_area, area)

        # Return maximum area under
        # the given histogram
        return max_area

# This code is contributed
# by Jinay Shah


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append(-1)
        maxarea = 0
        for i in range(len(heights)):
            while stack[len(stack) - 1] != -1 and heights[stack[len(stack) - 1]] >= heights[i]:
                maxarea = max(
                    maxarea, heights[stack.pop()] * (i - stack[len(stack) - 1] - 1))
            stack.append(i)
        while stack[len(stack) - 1] != -1:
            maxarea = max(maxarea, heights[stack.pop()]
                          * (len(heights) - stack[len(stack) - 1] - 1))
        return maxarea
