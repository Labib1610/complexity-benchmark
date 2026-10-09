import sys

def int_stream(data):
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

data = sys.stdin.buffer.read()
it = iter(int_stream(data))

n = next(it)
m = next(it)
k = next(it)

adj = [[] for _ in range(n)]
for _ in range(m):
    u = next(it) - 1
    v = next(it) - 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n
left = []
right = []

for start in range(n):
    if color[start] != -1:
        continue
    color[start] = 0
    stack = [start]
    while stack:
        u = stack.pop()
        if color[u] == 0:
            left.append(u)
        else:
            right.append(u)
        nc = color[u] ^ 1
        for v in adj[u]:
            if color[v] == -1:
                color[v] = nc
                stack.append(v)

if len(left) >= k:
    ans = left[:k]
    sys.stdout.write("YES\n" + " ".join(str(x + 1) for x in ans))
    sys.exit()

if len(right) >= k:
    ans = right[:k]
    sys.stdout.write("YES\n" + " ".join(str(x + 1) for x in ans))
    sys.exit()

match_l = [-1] * n
match_r = [-1] * n
matching = 0
limit = n - k

# Initial greedy matching
for u in left:
    for v in adj[u]:
        if match_r[v] == -1:
            match_l[u] = v
            match_r[v] = u
            matching += 1
            break
    if matching > limit:
        sys.stdout.write("NO")
        sys.exit()

while True:
    dist = [-1] * n
    queue = []
    for u in left:
        if match_l[u] == -1:
            dist[u] = 0
            queue.append(u)

    head = 0
    best = n + 1
    while head < len(queue):
        u = queue[head]
        head += 1
        du = dist[u]
        if du + 1 > best:
            continue
        for v in adj[u]:
            p = match_r[v]
            if p == -1:
                if du + 1 < best:
                    best = du + 1
            elif dist[p] == -1 and du + 1 < best:
                dist[p] = du + 1
                queue.append(p)

    if best == n + 1:
        break

    edge_pos = [0] * n
    augmented_this_phase = 0

    for root in left:
        if match_l[root] != -1 or dist[root] != 0:
            continue

        stack_u = [root]
        stack_v = []
        augmented = False

        while stack_u:
            u = stack_u[-1]
            neighbors = adj[u]
            advanced = False

            while edge_pos[u] < len(neighbors):
                v = neighbors[edge_pos[u]]
                edge_pos[u] += 1
                p = match_r[v]

                if p == -1:
                    if dist[u] + 1 == best:
                        match_l[u] = v
                        match_r[v] = u
                        for j in range(len(stack_v) - 1, -1, -1):
                            pu = stack_u[j]
                            pv = stack_v[j]
                            match_l[pu] = pv
                            match_r[pv] = pu
                        augmented = True
                        break
                elif dist[p] == dist[u] + 1:
                    stack_v.append(v)
                    stack_u.append(p)
                    advanced = True
                    break

            if augmented:
                break
            if advanced:
                continue

            dist[u] = -1
            stack_u.pop()
            if stack_v:
                stack_v.pop()

        if augmented:
            matching += 1
            augmented_this_phase += 1
            if matching > limit:
                sys.stdout.write("NO")
                sys.exit()

    if augmented_this_phase == 0:
        break

# Construct a maximum independent set from the complement of a minimum vertex cover.
reachable_l = bytearray(n)
reachable_r = bytearray(n)
queue = []

for u in left:
    if match_l[u] == -1:
        reachable_l[u] = 1
        queue.append(u)

head = 0
while head < len(queue):
    u = queue[head]
    head += 1
    matched_v = match_l[u]

    for v in adj[u]:
        if v == matched_v or reachable_r[v]:
            continue
        reachable_r[v] = 1
        p = match_r[v]
        if p != -1 and not reachable_l[p]:
            reachable_l[p] = 1
            queue.append(p)

independent = []
for u in left:
    if reachable_l[u]:
        independent.append(u)
for v in right:
    if not reachable_r[v]:
        independent.append(v)

if len(independent) < k:
    sys.stdout.write("NO")
else:
    ans = independent[:k]
    sys.stdout.write("YES\n" + " ".join(str(x + 1) for x in ans))