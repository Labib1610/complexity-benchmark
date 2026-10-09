import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, m, k = data[0], data[1], data[2]

adj = [[] for _ in range(n + 1)]
pos = 3
for _ in range(m):
    u = data[pos]
    v = data[pos + 1]
    pos += 2
    adj[u].append(v)
    adj[v].append(u)
del data

# Recover a bipartition.
color = bytearray([255]) * (n + 1)
left = []

for start in range(1, n + 1):
    if color[start] != 255:
        continue
    color[start] = 0
    stack = [start]
    while stack:
        u = stack.pop()
        if color[u] == 0:
            left.append(u)
        next_color = color[u] ^ 1
        for v in adj[u]:
            if color[v] == 255:
                color[v] = next_color
                stack.append(v)

# Hopcroft-Karp maximum matching.
pair = [0] * (n + 1)
dist = [-1] * (n + 1)
matching = 0
limit = n - k

while True:
    queue = []
    for u in left:
        if pair[u] == 0:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = -1

    head = 0
    shortest = n + 1

    while head < len(queue):
        u = queue[head]
        head += 1
        nd = dist[u] + 1
        if nd > shortest:
            continue

        for v in adj[u]:
            p = pair[v]
            if p == 0:
                if nd < shortest:
                    shortest = nd
            elif nd < shortest and dist[p] == -1:
                dist[p] = nd
                queue.append(p)

    if shortest == n + 1:
        break

    edge_pos = [0] * (n + 1)
    augmented = 0

    for root in left:
        if pair[root] != 0 or dist[root] != 0:
            continue

        path_left = [root]
        path_right = []
        success = False

        while path_left:
            u = path_left[-1]
            neighbors = adj[u]
            descended = False

            while edge_pos[u] < len(neighbors):
                v = neighbors[edge_pos[u]]
                edge_pos[u] += 1
                p = pair[v]

                if p == 0:
                    if dist[u] + 1 != shortest:
                        continue

                    current_v = v
                    for i in range(len(path_left) - 1, -1, -1):
                        current_u = path_left[i]
                        pair[current_u] = current_v
                        pair[current_v] = current_u
                        if i > 0:
                            current_v = path_right[i - 1]

                    success = True
                    break

                if dist[p] == dist[u] + 1:
                    path_right.append(v)
                    path_left.append(p)
                    descended = True
                    break

            if success:
                break

            if descended:
                continue

            dist[u] = -1
            path_left.pop()
            if path_right:
                path_right.pop()

        if success:
            augmented += 1
            matching += 1
            if matching > limit:
                sys.stdout.write("NO\n")
                sys.exit(0)

    if augmented == 0:
        break

# Find the complement of a minimum vertex cover:
# vertices reachable from unmatched left vertices by alternating paths,
# plus unreachable right vertices.
reachable = bytearray(n + 1)
queue = []

for u in left:
    if pair[u] == 0:
        reachable[u] = 1
        queue.append(u)

head = 0
while head < len(queue):
    u = queue[head]
    head += 1
    matched_v = pair[u]

    for v in adj[u]:
        if v == matched_v or reachable[v]:
            continue
        reachable[v] = 1
        p = pair[v]
        if p != 0 and not reachable[p]:
            reachable[p] = 1
            queue.append(p)

answer = []
for u in range(1, n + 1):
    if (color[u] == 0 and reachable[u]) or (color[u] == 1 and not reachable[u]):
        answer.append(u)
        if len(answer) == k:
            break

if len(answer) < k:
    sys.stdout.write("NO\n")
else:
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, answer)) + "\n")