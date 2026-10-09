import sys

data = sys.stdin.buffer.read()
idx = 0
length = len(data)

def next_int():
    global idx
    while idx < length and data[idx] <= 32:
        idx += 1
    value = 0
    while idx < length and data[idx] > 32:
        value = value * 10 + data[idx] - 48
        idx += 1
    return value

n = next_int()
m = next_int()
t = next_int()

is_core = bytearray(n + 1)
for _ in range(t):
    is_core[next_int()] = 1

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u = next_int()
    v = next_int()
    w = next_int()
    graph[u].append((v, w))
    graph[v].append((u, w))

if t <= 1:
    print(0)
    sys.exit()

parent = [0] * (n + 1)
parent_weight = [0] * (n + 1)
order = [1]
parent[1] = -1

for u in order:
    for v, w in graph[u]:
        if v != parent[u]:
            parent[v] = u
            parent_weight[v] = w
            order.append(v)

core_count = [0] * (n + 1)
answer = 0

for u in reversed(order):
    count = core_count[u] + is_core[u]
    core_count[u] = count
    if parent[u] > 0:
        if 0 < count < t:
            answer += parent_weight[u]
        core_count[parent[u]] += count

print(answer)