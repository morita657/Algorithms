# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
# We give the general idea below on how one can apply the above pseudocode template to implement a backtracking algorithm.

# - [1]. One can model each step of the robot as a recursive function (i.e. backtrack()).

# - [2]. At each step, technically the robot would have four candidates of direction to explore,
# e.g. the robot located at the coordinate of (0, 0). Since not each direction is available though,
# one should check if the cell in the given direction is an obstacle or it has been cleaned before,
# i.e. is_valid(candidate). Another benefit of the check is that it would greatly reduce the number of possible paths that one needs to explore.

# - [3]. Once the robot decides to explore the cell in certain direction, the robot should mark its decision (i.e. place(candidate)).
# More importantly, later the robot should be able to revert the previous decision (i.e. remove(candidate)),
# by going back to the cell and restore its original direction.

# - [4]. The robot conducts the cleaning step by step, in the form of recursion of the backtrack() function.
# The backtracking would be triggered whenever the robot reaches a point that it is surrounded either by the obstacles
# (e.g. cell at the row 1 and the column -3) or the cleaned cells. At the end of the backtracking,
# the robot would get back to the its starting point, and each cell in the grid would be traversed at least once.
# As a result, the room is cleaned at the end.


class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0],
                            cell[1] + directions[new_d][1])

                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()

        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()
