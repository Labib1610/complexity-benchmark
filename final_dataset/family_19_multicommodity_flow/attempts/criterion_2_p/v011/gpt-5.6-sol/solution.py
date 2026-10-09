import sys
from collections import deque

def integers():
    data = sys.stdin.buffer.read()
    num = 0
    in_num = False
    for c in data:
        if 48 <= c <= 57:
            num = num * 10 + c - 48
            in_num = True
        elif in_num:
            yield num
            num = 0
            in_num = False
    if in_num:
        yield num

it = iter(integers())
try:
    n = next(it)
    m = next(it)
    _ = next(it)
    s = next(it)
    t = next(it)
    required = next(it)
except StopIteration:
    sys.exit()

sys.setrecursionlimit(max(1_000_000, 2 * n + 100))

adj = [[] for _ in range(n + 1)]
to = []
capacity = []
original = [0] * m
edge_id = [0] * m

def add_edge(u, v, cap):
    idx = len(to)
    to.append(v)
    capacity.append(cap)
    to.append(u)
    capacity.append(0)
    adj[u].append(idx)
    adj[v].append(idx ^ 1)
    return idx

for i in range(m):
    u = next(it)
    v = next(it)
    cap = next(it)
    original[i] = cap
    edge_id[i] = add_edge(u, v, cap)

if required == 0:
    sys.stdout.write("YES\n" + " ".join("0" for _ in range(m)) + "\n")
    sys.exit()

if s == t:
    sys.stdout.write("NO\n")
    sys.exit()

flow = 0
level = [-1] * (n + 1)

while flow < required:
    for i in range(n + 1):
        level[i] = -1
    level[s] = 0
    q = deque([s])

    while q:
        u = q.popleft()
        next_level = level[u] + 1
        for e in adj[u]:
            v = to[e]
            if capacity[e] > 0 and level[v] == -1:
                level[v] = next_level
                q.append(v)

    if level[t] == -1:
        break

    ptr = [0] * (n + 1)

    def dfs(u, pushed):
        if u == t:
            return pushed
        edges = adj[u]
        while ptr[u] < len(edges):
            e = edges[ptr[u]]
            v = to[e]
            if capacity[e] > 0 and level[v] == level[u] + 1:
                sent = dfs(v, min(pushed, capacity[e]))
                if sent:
                    capacity[e] -= sent
                    capacity[e ^ 1] += sent
                    return sent
            ptr[u] += 1
        return 0

    while flow < required:
        sent = dfs(s, required - flow)
        if sent == 0:
            break
        flow += sent

if flow < required:
    sys.stdout.write("NO\n")
else:
    result = [
        str(original[i] - capacity[edge_id[i]])
        for i in range(m)
    ]
    sys.stdout.write("YES\n" + " ".join(result) + "\n")