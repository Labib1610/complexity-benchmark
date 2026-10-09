import sys
from collections import deque

sys.setrecursionlimit(300000)

data = list(map(int, sys.stdin.buffer.read().split()))
n, m, k = data[0], data[1], data[2]

adj = [[] for _ in range(n)]
p = 3
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    adj[u].append(v)
    adj[v].append(u)
del data

color = [-1] * n
left = []
right = []
q = deque()

for start in range(n):
    if color[start] != -1:
        continue
    color[start] = 0
    q.append(start)
    while q:
        u = q.popleft()
        if color[u] == 0:
            left.append(u)
        else:
            right.append(u)
        next_color = color[u] ^ 1
        for v in adj[u]:
            if color[v] == -1:
                color[v] = next_color
                q.append(v)

if len(left) >= k:
    answer = left[:k]
    sys.stdout.write("YES\n" + " ".join(str(x + 1) for x in answer))
    sys.exit()

if len(right) >= k:
    answer = right[:k]
    sys.stdout.write("YES\n" + " ".join(str(x + 1) for x in answer))
    sys.exit()

pair = [-1] * n
dist = [-1] * n
INF = n + 1
shortest = INF

def bfs():
    global shortest
    dq = deque()
    for u in left:
        if pair[u] == -1:
            dist[u] = 0
            dq.append(u)
        else:
            dist[u] = -1

    shortest = INF
    while dq:
        u = dq.popleft()
        if dist[u] >= shortest:
            continue
        nd = dist[u] + 1
        for v in adj[u]:
            w = pair[v]
            if w == -1:
                if nd < shortest:
                    shortest = nd
            elif dist[w] == -1:
                dist[w] = nd
                dq.append(w)
    return shortest != INF

def dfs(u):
    nd = dist[u] + 1
    for v in adj[u]:
        w = pair[v]
        if w == -1:
            if nd != shortest:
                continue
        elif dist[w] != nd or not dfs(w):
            continue
        pair[u] = v
        pair[v] = u
        return True
    dist[u] = -1
    return False

matching = 0
while bfs():
    for u in left:
        if pair[u] == -1 and dfs(u):
            matching += 1

if n - matching < k:
    sys.stdout.write("NO")
    sys.exit()

reachable = bytearray(n)
dq = deque()

for u in left:
    if pair[u] == -1:
        reachable[u] = 1
        dq.append(u)

while dq:
    u = dq.popleft()
    matched_v = pair[u]
    for v in adj[u]:
        if v == matched_v or reachable[v]:
            continue
        reachable[v] = 1
        w = pair[v]
        if w != -1 and not reachable[w]:
            reachable[w] = 1
            dq.append(w)

answer = []
for i in range(n):
    if (color[i] == 0 and reachable[i]) or (color[i] == 1 and not reachable[i]):
        answer.append(i + 1)
        if len(answer) == k:
            break

sys.stdout.write("YES\n" + " ".join(map(str, answer)))