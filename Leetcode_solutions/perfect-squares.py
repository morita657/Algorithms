class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        # make square array
        i = 1
        candidates = []
        # initialization
        while i < n:
            candidates.append(i * i)
            i += 1
        candidates.reverse()
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for checkCandidate in toCheck:
                print checkCandidate
                for cadidate in candidates:
                    if checkCandidate == cadidate:
                        return cnt
                    if checkCandidate < cadidate:
                        break
                    print 'checkCandidate - cadidate: ', checkCandidate - cadidate
                    temp.add(checkCandidate - cadidate)
            print 'toCheck = temp: ', toCheck, temp
            toCheck = temp
        return cnt


# s = Solution()
# s.numSquares(12)


class Solution(object):
    def numSquares(self, n):
        front, back, pm = [0], [n], 1  # pm is "plus minus"
        # depth[0] == 0, depth[n] == -1, depth[everythingElse] == None
        depth = [0] + [None] * (n - 1) + [-1]
        print 'front: ', front, back, pm, depth
        while front:
            newFront = []
            for v in front:
                i = 1
                while True:
                    w = v + pm * i * i  # generate a neighbor
                    if w < 0 or w > n:  # all neighbors have been generated
                        break
                    if depth[w] is None:  # w has not been discovered
                        # mark it as discovered by assigning a depth to it
                        depth[w] = depth[v] + pm
                        newFront.append(w)
                    # w has been discovered in the `back` tree, so we're done
                    elif (depth[w] < 0) != (depth[v] < 0):
                        return abs(depth[w] - depth[v])
                    i += 1
            front = newFront
            if len(front) > len(back):
                front, back, pm = back, front, -pm  # always expand the tree with fewer leaves


s = Solution()
print s.numSquares(12)
# print s.numSquares(13)
