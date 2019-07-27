class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = [1]
        for room in range(len(rooms)):
            keys = keys + rooms[room]
            # print rooms
            if (room + 1) < len(rooms):
                if (room + 1) not in keys:
                    # print 'room: ', room+1
                    return False
        return True


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        dfs = [0]
        seen = set(dfs)
        while dfs:
            i = dfs.pop()
            for j in rooms[i]:
                if j not in seen:
                    dfs.append(j)
                    seen.add(j)
                    if len(seen) == len(rooms):
                        return True
        return len(seen) == len(rooms)
