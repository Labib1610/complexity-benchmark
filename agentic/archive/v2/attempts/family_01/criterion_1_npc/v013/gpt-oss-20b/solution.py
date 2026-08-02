import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Quick check for K4
    for a in range(n):
        for b in range(a + 1, n):
            if not (adj[a] >> b) & 1:
                continue
            for c in range(b + 1, n):
                if not ((adj[a] >> c) & 1 and (adj[b] >> c) & 1):
                    continue
                for d in range(c + 1, n):
                    if not ((adj[a] >> d) & 1 and (adj[b] >> d) & 1 and (adj[c] >> d) & 1):
                        continue
                    print("NO")
                    return

    color = [0] * n  # 0 uncolored, 1-3 colors

    sys.setrecursionlimit(10000)

    def dfs(i):
        if i == n:
            return True
        v = i
        for c in (1, 2, 3):
            conflict = False
            neigh = adj[v]
            # iterate over neighbors
            while neigh:
                u = (neigh & -neigh).bit_length() - 1
                neigh &= neigh - 1
                if color[u] == c:
                    conflict = True
                    break
            if conflict:
                continue
            color[v] = c
            if dfs(i + 1):
                return True
            color[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()