import sys
from collections import deque

sys.setrecursionlimit(300000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, k = data[0], data[1], data[2]
    adj = [[] for _ in range(n)]

    pos = 3
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        adj[u].append(v)
        adj[v].append(u)

    del data

    color = bytearray([255]) * n
    left = []

    for start in range(n):
        if color[start] != 255:
            continue

        color[start] = 0
        stack = [start]
        side0 = []
        side1 = []

        while stack:
            u = stack.pop()
            if color[u] == 0:
                side0.append(u)
            else:
                side1.append(u)

            nc = color[u] ^ 1
            for v in adj[u]:
                if color[v] == 255:
                    color[v] = nc
                    stack.append(v)

        if len(side1) > len(side0):
            for u in side0:
                color[u] = 1
            for u in side1:
                color[u] = 0
            left.extend(side1)
        else:
            left.extend(side0)

    if len(left) >= k:
        ans = left[:k]
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(str(x + 1) for x in ans))
        return

    active_left = [u for u in left if adj[u]]
    pair = [-1] * n
    dist = [0] * n
    inf = n + 1
    matching = 0

    while True:
        q = deque()
        for u in active_left:
            if pair[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = inf

        shortest = inf

        while q:
            u = q.popleft()
            du = dist[u]
            if du >= shortest:
                continue

            nd = du + 1
            for v in adj[u]:
                p = pair[v]
                if p == -1:
                    if nd < shortest:
                        shortest = nd
                elif dist[p] == inf:
                    dist[p] = nd
                    q.append(p)

        if shortest == inf:
            break

        def dfs(u):
            du = dist[u]
            nd = du + 1

            for v in adj[u]:
                p = pair[v]
                if p == -1:
                    if nd == shortest:
                        pair[u] = v
                        pair[v] = u
                        return True
                elif dist[p] == nd and dfs(p):
                    pair[u] = v
                    pair[v] = u
                    return True

            dist[u] = inf
            return False

        augmented = 0
        for u in active_left:
            if pair[u] == -1 and dfs(u):
                augmented += 1

        if augmented == 0:
            break
        matching += augmented

    if n - matching < k:
        sys.stdout.write("NO")
        return

    reachable = bytearray(n)
    q = deque()

    for u in left:
        if pair[u] == -1:
            reachable[u] = 1
            q.append(u)

    while q:
        u = q.popleft()
        matched_v = pair[u]

        for v in adj[u]:
            if v == matched_v:
                continue
            if not reachable[v]:
                reachable[v] = 1
                p = pair[v]
                if p != -1 and not reachable[p]:
                    reachable[p] = 1
                    q.append(p)

    ans = []
    for u in range(n):
        if (color[u] == 0 and reachable[u]) or (color[u] == 1 and not reachable[u]):
            ans.append(u + 1)
            if len(ans) == k:
                break

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()