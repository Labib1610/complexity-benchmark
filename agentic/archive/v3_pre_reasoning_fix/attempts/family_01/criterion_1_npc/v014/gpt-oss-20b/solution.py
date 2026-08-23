import sys
sys.setrecursionlimit(10000)

def solve():
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

    colors = [0] * n          # 0 unassigned, 1-3 assigned
    avail = [0b111] * n       # bitmask of available colors for each node

    def dfs(idx):
        if idx == n:
            return True
        u = idx
        mask = avail[u]
        # try colors 1..3 in order
        for color in (1, 2, 3):
            bit = 1 << (color - 1)
            if not (mask & bit):
                continue
            changes = []
            ok = True
            for v in adj[u]:
                if colors[v] == 0:
                    new_mask = avail[v] & ~bit
                    if new_mask == 0:
                        ok = False
                        break
                    changes.append((v, avail[v]))
                    avail[v] = new_mask
            if not ok:
                for v, old in changes:
                    avail[v] = old
                continue
            colors[u] = color
            if dfs(idx + 1):
                return True
            colors[u] = 0
            for v, old in changes:
                avail[v] = old
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c) for c in colors))
    else:
        print("NO")

if __name__ == "__main__":
    solve()