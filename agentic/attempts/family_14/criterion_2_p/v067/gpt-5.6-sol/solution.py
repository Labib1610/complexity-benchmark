import sys
from collections import deque

def integers():
    data = sys.stdin.buffer.read()
    num = 0
    in_number = False
    for byte in data:
        if 48 <= byte <= 57:
            num = num * 10 + byte - 48
            in_number = True
        elif in_number:
            yield num
            num = 0
            in_number = False
    if in_number:
        yield num

it = iter(integers())
n = next(it)
m = next(it)
t = next(it)

primary = bytearray(n)
for _ in range(t):
    primary[next(it) - 1] = 1

graph = [[] for _ in range(n)]
degree = [0] * n
answer = 0

for _ in range(m):
    u = next(it) - 1
    v = next(it) - 1
    w = next(it)
    graph[u].append((v, w))
    graph[v].append((u, w))
    degree[u] += 1
    degree[v] += 1
    answer += w

queue = deque(
    node for node in range(n)
    if degree[node] <= 1 and not primary[node]
)
removed = bytearray(n)

while queue:
    node = queue.popleft()
    if removed[node]:
        continue
    removed[node] = 1

    for neighbor, weight in graph[node]:
        if not removed[neighbor]:
            answer -= weight
            degree[neighbor] -= 1
            if degree[neighbor] == 1 and not primary[neighbor]:
                queue.append(neighbor)

print(answer)