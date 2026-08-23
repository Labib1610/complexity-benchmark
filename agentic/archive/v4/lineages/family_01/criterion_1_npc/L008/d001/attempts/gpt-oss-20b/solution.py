import sys

def main():
    sys.setrecursionlimit(10000)
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

    color = [0] * n  # 0 means uncolored, otherwise 1..3
    allowed = [0b111] * n  # bitmask of allowed colors

    def dfs(v):
        if v == n:
            return True
        if allowed[v] == 0:
            return False
        for c in range(3):  # colors 1..3
            if not (allowed[v] & (1 << c)):
                continue
            color[v] = c + 1
            changes = []
            ok = True
            for u in adj[v]:
                if color[u] == 0:
                    old = allowed[u]
                    new = old & ~(1 << c)
                    changes.append((u, old))
                    allowed[u] = new
                    if new == 0:
                        ok = False
            if ok and dfs(v + 1):
                return True
            for u, old in changes:
                allowed[u] = old
            color[v] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(str(col) for col in color)]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    main()