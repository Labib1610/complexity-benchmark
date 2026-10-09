import sys

sys.setrecursionlimit(5000)


def integers(data):
    num = -1
    for c in data:
        if 48 <= c <= 57:
            if num < 0:
                num = c - 48
            else:
                num = num * 10 + c - 48
        elif num >= 0:
            yield num
            num = -1
    if num >= 0:
        yield num


data = sys.stdin.buffer.read()
it = integers(data)

try:
    k = next(it)
    t = next(it)
except StopIteration:
    sys.exit()

adj = [[] for _ in range(k + 1)]
machine = [0] * (k + 1)
machine_owner = [0] * (k + 1)

pair_u = [0] * (k + 1)
pair_v = [0] * (k + 1)
matching = 0
valid = True

for _ in range(t):
    x = next(it)
    y = next(it)
    z = next(it)

    if machine[x] == 0:
        machine[x] = y
        if machine_owner[y] not in (0, x):
            valid = False
        machine_owner[y] = x
    elif machine[x] != y:
        valid = False

    adj[x].append(z)

    if pair_u[x] == 0 and pair_v[z] == 0:
        pair_u[x] = z
        pair_v[z] = x
        matching += 1

del it
del data

if valid and matching < k:
    INF = k + 1
    dist = [INF] * (k + 1)

    def bfs():
        queue = []
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF

        dist[0] = INF

        for u in queue:
            if dist[u] >= dist[0]:
                continue
            next_dist = dist[u] + 1
            for v in adj[u]:
                paired_u = pair_v[v]
                if dist[paired_u] == INF:
                    dist[paired_u] = next_dist
                    if paired_u != 0:
                        queue.append(paired_u)

        return dist[0] != INF

    def dfs(u):
        if u == 0:
            return True

        next_dist = dist[u] + 1
        for v in adj[u]:
            paired_u = pair_v[v]
            if dist[paired_u] == next_dist and dfs(paired_u):
                pair_u[u] = v
                pair_v[v] = u
                return True

        dist[u] = INF
        return False

    while matching < k and bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

if not valid or matching != k:
    sys.stdout.write("NO\n")
else:
    output = ["YES"]
    for x in range(1, k + 1):
        output.append(f"{x} {machine[x]} {pair_u[x]}")
    sys.stdout.write("\n".join(output))