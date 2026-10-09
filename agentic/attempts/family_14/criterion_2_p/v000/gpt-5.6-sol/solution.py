import sys
from array import array

data = map(int, sys.stdin.buffer.read().split())
it = iter(data)

n = next(it)
m = next(it)
t = next(it)

required = bytearray(n + 1)
root = next(it)
required[root] = 1
for _ in range(t - 1):
    required[next(it)] = 1

head = array('i', [-1]) * (n + 1)
to = array('i')
weight = array('i')
nxt = array('i')

for _ in range(m):
    u = next(it)
    v = next(it)
    w = next(it)

    idx = len(to)
    to.append(v)
    weight.append(w)
    nxt.append(head[u])
    head[u] = idx

    idx = len(to)
    to.append(u)
    weight.append(w)
    nxt.append(head[v])
    head[v] = idx

parent = array('i', [0]) * (n + 1)
parent_weight = array('i', [0]) * (n + 1)
parent[root] = -1

order = array('i')
stack = [root]

while stack:
    u = stack.pop()
    order.append(u)
    e = head[u]
    while e != -1:
        v = to[e]
        if v != parent[u]:
            parent[v] = u
            parent_weight[v] = weight[e]
            stack.append(v)
        e = nxt[e]

answer = 0
for i in range(len(order) - 1, 0, -1):
    u = order[i]
    if required[u]:
        answer += parent_weight[u]
        required[parent[u]] = 1

print(answer)