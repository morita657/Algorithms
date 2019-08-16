r, c = map(int, raw_input().split())
sy, sx = map(int, raw_input().split())
gy, gx = map(int, raw_input().split())

maze = []
for i in range(r):
    maze.append([])
    col = raw_input()
    for j in range(c):
        maze[i].append(col[j])

d = []

x = [1, 0, -1,  0]
y = [0, 1, 0, -1]


def bfs():
    for i in range(r):
        d.append([])
        for j in range(c):
            d[i].append(float('inf'))
    q = [[sx - 1, sy - 1]]
    d[sy - 1][sx - 1] = 0
    step = 0
    while len(q) > 0:
        now = q.pop(0)
        nowX, nowY = now[0], now[1]
        if nowX == gx - 1 and nowY == gy - 1:
            break
        for i in range(len(x)):
            dx = nowX + x[i]
            dy = nowY + y[i]
            if 0 <= nowX + x[i] and nowX + x[i] < c \
                    and 0 <= nowY + y[i] and nowY + y[i] < r and maze[dy][dx] != '#' \
                    and d[dy][dx] == float('inf'):
                q.append([dx, dy])
                d[dy][dx] = d[nowY][nowX] + 1
    return d[gy - 1][gx - 1]


print bfs()
