import sys

sys.setrecursionlimit(1_000_000)

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

# Bipartition the graph, orienting each component so its smaller side is left.
color = [-1] * n
for start in range(n):
    if color[start] != -1:
        continue

    color[start] = 0
    component = [start]
    head = 0
    count0 = 1
    count1 = 0

    while head < len(component):
        u = component[head]
        head += 1
        next_color = color[u] ^ 1
        for v in adj[u]:
            if color[v] == -1:
                color[v] = next_color
                if next_color == 0:
                    count0 += 1
                else:
                    count1 += 1
                component.append(v)

    if count0 > count1:
        for u in component:
            color[u] ^= 1

left = [u for u in range(n) if color[u] == 0]

# Hopcroft-Karp maximum matching.
mate = [-1] * n
dist = [-1] * n
INF = n + 1

def dfs(u):
    du = dist[u]
    for v in adj[u]:
        w = mate[v]
        if w == -1:
            if du + 1 == shortest:
                mate[u] = v
                mate[v] = u
                return True
        elif dist[w] == du + 1 and dfs(w):
            mate[u] = v
            mate[v] = u
            return True
    dist[u] = -1
    return False

matching = 0

while True:
    queue = []
    for u in left:
        if mate[u] == -1:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = -1

    shortest = INF
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        du = dist[u]

        if du + 1 > shortest:
            continue

        for v in adj[u]:
            w = mate[v]
            if w == -1:
                if du + 1 < shortest:
                    shortest = du + 1
            elif dist[w] == -1:
                dist[w] = du + 1
                queue.append(w)

    if shortest == INF:
        break

    for u in left:
        if mate[u] == -1 and dist[u] == 0 and dfs(u):
            matching += 1

if n - matching < k:
    sys.stdout.write("NO\n")
    sys.exit()

# Alternating reachability from unmatched left vertices.
reach_left = bytearray(n)
reach_right = bytearray(n)
queue = []

for u in left:
    if mate[u] == -1:
        reach_left[u] = 1
        queue.append(u)

head = 0
while head < len(queue):
    u = queue[head]
    head += 1
    matched_v = mate[u]

    for v in adj[u]:
        if v == matched_v or reach_right[v]:
            continue

        reach_right[v] = 1
        w = mate[v]
        if w != -1 and not reach_left[w]:
            reach_left[w] = 1
            queue.append(w)

# Complement of the minimum vertex cover is a maximum independent set.
answer = []
for u in range(n):
    if (color[u] == 0 and reach_left[u]) or (color[u] == 1 and not reach_right[u]):
        answer.append(u + 1)
        if len(answer) == k:
            break

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)) + "\n")