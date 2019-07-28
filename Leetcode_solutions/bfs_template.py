# Return the length of the shortest path between root and target node.
class Solution(object):
    # def __init__(self):
    #     self.root = root
    #     self.
        # return super(Solution, self).__init__()
    def bfs(self, root, target):
        queue = []
        # store all nodes which are waiting to be processed
        step = 0
        # number of steps neeeded from root to current node
        # initialize
        queue.append(root)
        # BFS
        while(len(queue) > 0):
            step += 1
            # iterate the nodes which are already in the queue
            size = len(queue)
            for i in size:
                cur = queue[0]
                if cur == target:
                    return step
                # for (Node next: the neighbors of cur)
                for neighbors in cur:
                    # add next to queue
                    queue.append(cur.neighbors)
                # remove the first node from queue
                queue.pop(0)
        # there is no path from root to target
        return -1


# add a hash set to the code not to get stuck in an infinite loop,
# e.g. in graph with cycle

class Solution(object):
    # def __init__(self):
    #     self.root = root
    #     self.
    # return super(Solution, self).__init__()
    def bfs(self, root, target):
        # store all nodes which are waiting to be processed
        queue = []
        # store all the nodes that we've visited
        visited = set()
        # number of steps neeeded from root to current node
        step = 0
        # initialize
        queue = [root]
        visited = set(root)
        # BFS
        while(len(queue) > 0):
            step += 1
            # iterate the nodes which are already in the queue
            size = len(queue)
            for i in size:
                # Node cur = the first node in queue
                cur = queue[0]
                if cur == target:
                    return step
                for next in cur:
                    if next not in visited:
                        #  add next to queue;
                        queue.append(next)
                        # add next to visited;
                        visited.append(next)
                    # remove the first node from queue;
                    queue.pop(0)
        #  there is no path from root to target
        return -1
