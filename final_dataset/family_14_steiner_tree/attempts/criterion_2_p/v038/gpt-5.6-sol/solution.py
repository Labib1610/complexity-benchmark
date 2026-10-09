import sys

it = iter(map(int, sys.stdin.buffer.read().split()))

n = next(it)
m = next(it)
t = next(it)

priority = [False] * (n + 1)
for _ in range(t):
    priority[next(it)] = True

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u = next(it)
    v = next(it)
    w = next(it)
    graph[u].append((v, w))
    graph[v].append((u, w))

del it

parent = [0] * (n + 1)
parent_weight = [0] * (n + 1)
parent[1] = -1

order = []
stack = [1]

while stack:
    u = stack.pop()
    order.append(u)
    for v, w in graph[u]:
        if v != parent[u]:
            parent[v] = u
            parent_weight[v] = w
            stack.append(v)

count = [int(x) for x in priority]
answer = 0

for u in reversed(order):
    p = parent[u]
    if p > 0:
        if 0 < count[u] < t:
            answer += parent_weight[u]
        count[p] += count[u]

print(answer)