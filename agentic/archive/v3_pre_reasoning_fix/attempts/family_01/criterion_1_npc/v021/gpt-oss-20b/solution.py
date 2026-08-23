import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)          # 1-indexed
    usedMask = [0] * (n + 1)       # bitmask of colors used by colored neighbors

    def dfs(pos):
        if pos > n:
            return True
        for c in (1, 2, 3):
            # check conflict with already colored neighbors
            conflict = False
            for nb in adj[pos]:
                if nb < pos and color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            # assign color
            color[pos] = c
            changes = []
            mask_bit = 1 << (c - 1)
            for nb in adj[pos]:
                if nb > pos:
                    prev = usedMask[nb]
                    usedMask[nb] |= mask_bit
                    changes.append((nb, prev))
            # forward checking
            feasible = True
            for j in range(pos + 1, n + 1):
                if usedMask[j] == 0b111:
                    feasible = False
                    break
            if feasible and dfs(pos + 1):
                return True
            # revert
            for nb, prev in changes:
                usedMask[nb] = prev
            color[pos] = 0
        return False

    if dfs(1):
        out = ['YES', ' '.join(str(color[i]) for i in range(1, n + 1))]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()