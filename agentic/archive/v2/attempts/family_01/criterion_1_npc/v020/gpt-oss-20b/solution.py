import sys
sys.setrecursionlimit(10000)

def main():
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
        if v not in adj[u]:
            adj[u].append(v)
            adj[v].append(u)

    colors = [0] * n          # 0 = uncolored, else 1..3
    forb_mask = [0] * n       # bitmask of forbidden colors for each vertex

    def dfs(idx):
        if idx == n:
            return True
        v = idx
        mask = forb_mask[v]
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if mask & bit:
                continue
            colors[v] = c
            changed = []
            for u in adj[v]:
                if colors[u] == 0 and not (forb_mask[u] & bit):
                    forb_mask[u] |= bit
                    changed.append(u)
            # early pruning
            bad = False
            for u in range(idx + 1, n):
                if colors[u] == 0 and forb_mask[u] == 7:
                    bad = True
                    break
            if not bad and dfs(idx + 1):
                return True
            # backtrack
            for u in changed:
                forb_mask[u] &= ~bit
            colors[v] = 0
        return False

    if dfs(0):
        out = ['YES', '\n', ' '.join(str(c) for c in colors)]
        sys.stdout.write(''.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    main()