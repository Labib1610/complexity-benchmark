import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        neighbors[u].append(v)
        neighbors[v].append(u)

    color = [0] * (n + 1)          # assigned color, 0 means unassigned
    avail = [7] * (n + 1)          # bitmask of available colors (bits 0,1,2 for colors 1,2,3)
    solution = None

    def dfs(idx: int) -> bool:
        nonlocal solution
        if idx > n:
            solution = color[1:]
            return True
        v = idx
        if avail[v] == 0:
            return False
        for col in (1, 2, 3):
            bit = 1 << (col - 1)
            if avail[v] & bit:
                color[v] = col
                changes = []
                conflict = False
                # propagate to unassigned neighbors
                for u in neighbors[v]:
                    if color[u] == 0:
                        prev = avail[u]
                        new = prev & ~bit
                        if new == 0:
                            conflict = True
                            break
                        if new != prev:
                            changes.append((u, prev))
                            avail[u] = new
                if not conflict:
                    if dfs(idx + 1):
                        return True
                # backtrack
                for u, old in changes:
                    avail[u] = old
                color[v] = 0
        return False

    if dfs(1):
        out = ['YES', ' '.join(str(c) for c in solution)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()