import sys
from collections import deque

input = sys.stdin.buffer.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n
left = []
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
        next_color = color[u] ^ 1
        for v in adj[u]:
            if color[v] == -1:
                color[v] = next_color
                q.append(v)

if len(left) >= k:
    answer = left[:k]
    sys.stdout.write("YES\n" + " ".join(str(x + 1) for x in answer))
    sys.exit()

right_count = n - len(left)
if right_count >= k:
    answer = []
    for i in range(n):
        if color[i] == 1:
            answer.append(i)
            if len(answer) == k:
                break
    sys.stdout.write("YES\n" + " ".join(str(x + 1) for x in answer))
    sys.exit()

pair_left = [-1] * n
pair_right = [-1] * n
dist = [-1] * n
ptr = [0] * n
matching = 0

while True:
    q.clear()
    shortest = n + 1

    for u in left:
        ptr[u] = 0
        if pair_left[u] == -1:
            dist[u] = 0
            q.append(u)
        else:
            dist[u] = -1

    while q:
        u = q.popleft()
        du = dist[u]
        if du >= shortest:
            continue

        nd = du + 1
        for v in adj[u]:
            matched_left = pair_right[v]
            if matched_left == -1:
                if nd < shortest:
                    shortest = nd
            elif nd < shortest and dist[matched_left] == -1:
                dist[matched_left] = nd
                q.append(matched_left)

    if shortest == n + 1:
        break

    augmented_this_phase = 0

    for root in left:
        if pair_left[root] != -1 or dist[root] != 0:
            continue

        stack_left = [root]
        stack_edge = []
        augmented = False

        while stack_left:
            u = stack_left[-1]
            found_next = False
            neighbors = adj[u]

            while ptr[u] < len(neighbors):
                v = neighbors[ptr[u]]
                ptr[u] += 1
                matched_left = pair_right[v]

                if matched_left == -1:
                    if dist[u] + 1 == shortest:
                        pair_left[u] = v
                        pair_right[v] = u

                        for i in range(len(stack_edge) - 1, -1, -1):
                            parent = stack_left[i]
                            edge = stack_edge[i]
                            pair_left[parent] = edge
                            pair_right[edge] = parent

                        augmented = True
                        found_next = True
                        break
                elif dist[matched_left] == dist[u] + 1:
                    stack_edge.append(v)
                    stack_left.append(matched_left)
                    found_next = True
                    break

            if augmented:
                break

            if not found_next:
                dist[u] = -1
                stack_left.pop()
                if stack_edge:
                    stack_edge.pop()

        if augmented:
            augmented_this_phase += 1

    if augmented_this_phase == 0:
        break
    matching += augmented_this_phase

if n - matching < k:
    sys.stdout.write("NO")
    sys.exit()

reachable_left = bytearray(n)
reachable_right = bytearray(n)
q.clear()

for u in left:
    if pair_left[u] == -1:
        reachable_left[u] = 1
        q.append(u)

while q:
    u = q.popleft()
    matched_edge = pair_left[u]

    for v in adj[u]:
        if v == matched_edge:
            continue
        if not reachable_right[v]:
            reachable_right[v] = 1
            matched_left = pair_right[v]
            if matched_left != -1 and not reachable_left[matched_left]:
                reachable_left[matched_left] = 1
                q.append(matched_left)

answer = []
for i in range(n):
    if (color[i] == 0 and reachable_left[i]) or (
        color[i] == 1 and not reachable_right[i]
    ):
        answer.append(i)
        if len(answer) == k:
            break

sys.stdout.write("YES\n" + " ".join(str(x + 1) for x in answer))