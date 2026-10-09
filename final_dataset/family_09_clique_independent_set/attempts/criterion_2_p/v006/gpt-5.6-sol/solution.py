import sys
from collections import deque

sys.setrecursionlimit(300000)
input = sys.stdin.buffer.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# Recover the bipartition.
color = bytearray(b'\xff') * n
left = []

for start in range(n):
    if color[start] != 255:
        continue

    color[start] = 0
    stack = [start]

    while stack:
        u = stack.pop()
        if color[u] == 0:
            left.append(u)

        next_color = color[u] ^ 1
        for v in graph[u]:
            if color[v] == 255:
                color[v] = next_color
                stack.append(v)

# Hopcroft-Karp maximum matching.
match = [-1] * n
INF = n + 1
matching_size = 0

while True:
    dist = [INF] * n
    queue = deque()

    for u in left:
        if match[u] == -1:
            dist[u] = 0
            queue.append(u)

    shortest = INF

    while queue:
        u = queue.popleft()
        if dist[u] >= shortest:
            continue

        for v in graph[u]:
            paired = match[v]
            if paired == -1:
                shortest = dist[u] + 1
            elif dist[paired] == INF:
                dist[paired] = dist[u] + 1
                queue.append(paired)

    if shortest == INF:
        break

    edge_pos = [0] * n

    def augment(u):
        neighbors = graph[u]

        while edge_pos[u] < len(neighbors):
            v = neighbors[edge_pos[u]]
            edge_pos[u] += 1
            paired = match[v]

            if paired == -1:
                if dist[u] + 1 != shortest:
                    continue
            elif dist[paired] != dist[u] + 1 or not augment(paired):
                continue

            match[u] = v
            match[v] = u
            return True

        dist[u] = INF
        return False

    added = 0
    for u in left:
        if match[u] == -1 and augment(u):
            added += 1

    if added == 0:
        break
    matching_size += added

if n - matching_size < k:
    print("NO")
    sys.exit()

# Find vertices reachable from unmatched left vertices by alternating paths.
reachable_left = bytearray(n)
reachable_right = bytearray(n)
queue = deque()

for u in left:
    if match[u] == -1:
        reachable_left[u] = 1
        queue.append(u)

while queue:
    u = queue.popleft()
    matched_v = match[u]

    for v in graph[u]:
        if v == matched_v or reachable_right[v]:
            continue

        reachable_right[v] = 1
        paired = match[v]

        if paired != -1 and not reachable_left[paired]:
            reachable_left[paired] = 1
            queue.append(paired)

# Complement of the minimum vertex cover is a maximum independent set.
answer = []

for u in range(n):
    if color[u] == 0:
        if reachable_left[u]:
            answer.append(u + 1)
    elif not reachable_right[u]:
        answer.append(u + 1)

    if len(answer) == k:
        break

print("YES")
print(*answer)