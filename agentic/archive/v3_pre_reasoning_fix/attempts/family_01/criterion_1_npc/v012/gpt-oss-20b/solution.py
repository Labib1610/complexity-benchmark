import sys

def main():
    sys.setrecursionlimit(1000000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n          # 0 = uncolored, 1/2/3 assigned
    forb = [0] * n           # bitmask of forbidden colors for each vertex

    def dfs(idx):
        if idx == n:
            return True
        v = idx
        for col in (1, 2, 3):
            mask = 1 << (col - 1)
            if forb[v] & mask:
                continue
            color[v] = col
            changes = []
            ok = True
            for u in adj[v]:
                if color[u] == 0:
                    old = forb[u]
                    new = old | mask
                    if new == 7:
                        ok = False
                    forb[u] = new
                    changes.append((u, old))
            if ok and dfs(idx + 1):
                return True
            for u, old in changes:
                forb[u] = old
            color[v] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(str(c) for c in color)]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    main()