import sys
from collections import deque

sys.setrecursionlimit(300000)
input = sys.stdin.buffer.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = bytearray([255]) * n
is_left = bytearray(n)

for start in range(n):
    if color[start] != 255:
        continue

    color[start] = 0
    q = deque([start])
    component = []
    count0 = 0

    while q:
        u = q.popleft()
        component.append(u)
        if color[u] == 0:
            count0 += 1

        next_color = color[u] ^ 1
        for v in adj[u]:
            if color[v] == 255:
                color[v] = next_color
                q.append(v)

    count1 = len(component) - count0
    chosen_color = 0 if count0 <= count1 else 1
    for u in component:
        if color[u] == chosen_color:
            is_left[u] = 1

left = [u for u in range(n) if is_left[u]]

mate = [-1] * n
dist = [-1] * n
INF = n + 1
shortest = INF

def bfs():
    global shortest
    q = deque()
    for u in left:
        if mate[u] == -1:
            dist[u] = 0
            q.append(u)
        else:
            dist[u] = -1

    shortest = INF
    while q:
        u = q.popleft()
        if dist[u] + 1 > shortest:
            continue

        for v in adj[u]:
            w = mate[v]
            if w == -1:
                if dist[u] + 1 < shortest:
                    shortest = dist[u] + 1
            elif dist[w] == -1:
                dist[w] = dist[u] + 1
                q.append(w)

    return shortest != INF

def dfs(u):
    for v in adj[u]:
        w = mate[v]
        if w == -1:
            if dist[u] + 1 != shortest:
                continue
            mate[u] = v
            mate[v] = u
            return True

        if dist[w] == dist[u] + 1 and dfs(w):
            mate[u] = v
            mate[v] = u
            return True

    dist[u] = -1
    return False

matching_size = 0
while bfs():
    for u in left:
        if mate[u] == -1 and dfs(u):
            matching_size += 1

if n - matching_size < k:
    print("NO")
    sys.exit()

reachable_left = bytearray(n)
reachable_right = bytearray(n)
q = deque()

for u in left:
    if mate[u] == -1:
        reachable_left[u] = 1
        q.append(u)

while q:
    u = q.popleft()
    for v in adj[u]:
        if mate[u] == v:
            continue
        if not reachable_right[v]:
            reachable_right[v] = 1
            w = mate[v]
            if w != -1 and not reachable_left[w]:
                reachable_left[w] = 1
                q.append(w)

answer = []

for u in left:
    if reachable_left[u]:
        answer.append(u + 1)
        if len(answer) == k:
            break

if len(answer) < k:
    for v in range(n):
        if not is_left[v] and not reachable_right[v]:
            answer.append(v + 1)
            if len(answer) == k:
                break

print("YES")
print(*answer)