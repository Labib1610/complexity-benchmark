import sys
from collections import deque

data = list(map(int, sys.stdin.buffer.read().split()))
n, m = data[0], data[1]

graph = [[] for _ in range(n)]
p = 2
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    graph[u].append(v)
    graph[v].append(u)

color = bytearray(n)

for start in range(n):
    if color[start]:
        continue

    color[start] = 1
    queue = deque([start])

    while queue:
        u = queue.popleft()
        expected = 3 - color[u]

        for v in graph[u]:
            if color[v] == 0:
                color[v] = expected
                queue.append(v)
            elif color[v] != expected:
                sys.stdout.write("NO\n")
                sys.exit()

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, color)))
sys.stdout.write("\n")