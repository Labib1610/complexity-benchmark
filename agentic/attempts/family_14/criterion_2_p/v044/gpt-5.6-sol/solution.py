import sys

data = sys.stdin.buffer.read()

def integers():
    num = 0
    in_num = False
    for b in data:
        if 48 <= b <= 57:
            num = num * 10 + (b - 48)
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

count = [0] * n
for _ in range(t):
    count[next(it) - 1] = 1

graph = [[] for _ in range(n)]
for _ in range(m):
    u = next(it) - 1
    v = next(it) - 1
    w = next(it)
    graph[u].append((v, w))
    graph[v].append((u, w))

parent = [-1] * n
parent_weight = [0] * n
order = [0]

for u in order:
    for v, w in graph[u]:
        if v != parent[u]:
            parent[v] = u
            parent_weight[v] = w
            order.append(v)

answer = 0

for i in range(n - 1, 0, -1):
    v = order[i]
    terminals = count[v]
    if 0 < terminals < t:
        answer += parent_weight[v]
    count[parent[v]] += terminals

print(answer)