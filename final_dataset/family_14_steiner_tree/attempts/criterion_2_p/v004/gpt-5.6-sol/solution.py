import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, m, t = data[0], data[1], data[2]

required = [False] * (n + 1)
pos = 3
for i in range(t):
    required[data[pos + i]] = True
pos += t

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = data[pos], data[pos + 1], data[pos + 2]
    pos += 3
    graph[u].append((v, w))
    graph[v].append((u, w))

del data

parent = [0] * (n + 1)
parent_weight = [0] * (n + 1)
order = [1]

for u in order:
    for v, w in graph[u]:
        if v != parent[u]:
            parent[v] = u
            parent_weight[v] = w
            order.append(v)

required_count = [0] * (n + 1)
answer = 0

for u in reversed(order):
    count = required_count[u] + required[u]
    required_count[u] = count
    if u != 1:
        if 0 < count < t:
            answer += parent_weight[u]
        required_count[parent[u]] += count

print(answer)