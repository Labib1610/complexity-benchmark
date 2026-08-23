import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)          # 0 uncolored, 1..3 colored
    avail = [0b111] * (n + 1)      # bitmask of available colors for each vertex

    def dfs(pos: int) -> bool:
        if pos > n:
            return True
        # Try colors 1..3 in order
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (avail[pos] & bit):
                continue  # color not available for this vertex
            color[pos] = c
            changes = []
            ok = True
            for nb in adj[pos]:
                if color[nb] == 0:
                    prev = avail[nb]
                    newmask = prev & ~bit
                    if newmask == 0:
                        ok = False
                        break
                    if newmask != prev:
                        avail[nb] = newmask
                        changes.append((nb, prev))
            if ok and dfs(pos + 1):
                return True
            # backtrack
            color[pos] = 0
            for nb, pm in changes:
                avail[nb] = pm
        return False

    if dfs(1):
        out = ["YES"]
        out.append(" ".join(str(color[i]) for i in range(1, n + 1)))
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()