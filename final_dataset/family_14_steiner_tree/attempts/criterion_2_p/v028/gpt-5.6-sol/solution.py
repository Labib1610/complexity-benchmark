import sys

def ints():
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

it = iter(ints())
n = next(it)
m = next(it)
t = next(it)

marked = bytearray(n)
for _ in range(t):
    marked[next(it) - 1] = 1

graph = [[] for _ in range(n)]
for _ in range(m):
    u = next(it) - 1
    v = next(it) - 1
    w = next(it)
    graph[u].append((v, w))
    graph[v].append((u, w))

parent = [-1] * n
parent_weight = [0] * n
order = []
stack = [0]

while stack:
    u = stack.pop()
    order.append(u)
    for v, w in graph[u]:
        if v != parent[u]:
            parent[v] = u
            parent_weight[v] = w
            stack.append(v)

count = list(marked)
answer = 0

for i in range(n - 1, 0, -1):
    u = order[i]
    c = count[u]
    if 0 < c < t:
        answer += parent_weight[u]
    count[parent[u]] += c

print(answer)