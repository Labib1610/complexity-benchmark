import sys
from collections import deque

def integers():
    data = sys.stdin.buffer.read()
    num = 0
    in_num = False
    for b in data:
        if 48 <= b <= 57:
            num = num * 10 + b - 48
            in_num = True
        elif in_num:
            yield num
            num = 0
            in_num = False
    if in_num:
        yield num

it = iter(integers())
n = next(it)
m = next(it)
t = next(it)

important = bytearray(n)
for _ in range(t):
    important[next(it) - 1] = 1

graph = [[] for _ in range(n)]
degree = [0] * n
total_cost = 0

for _ in range(m):
    u = next(it) - 1
    v = next(it) - 1
    w = next(it)
    graph[u].append((v, w))
    graph[v].append((u, w))
    degree[u] += 1
    degree[v] += 1
    total_cost += w

queue = deque(
    i for i in range(n)
    if not important[i] and degree[i] <= 1
)
removed = bytearray(n)

while queue:
    u = queue.popleft()
    if removed[u]:
        continue

    removed[u] = 1

    for v, w in graph[u]:
        if not removed[v]:
            total_cost -= w
            degree[v] -= 1
            if not important[v] and degree[v] <= 1:
                queue.append(v)
            break

print(total_cost)