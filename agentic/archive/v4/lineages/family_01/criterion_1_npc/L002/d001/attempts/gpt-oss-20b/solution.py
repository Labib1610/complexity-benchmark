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

    assigned = [0] * (n + 1)          # 0 unassigned, 1..3 colors
    avail = [0b111] * (n + 1)         # available colors bitmask for unassigned nodes

    def dfs(pos: int) -> bool:
        if pos > n:
            return True
        # Try colors 1..3
        for c in range(1, 4):
            # check conflict with already assigned neighbors
            conflict = False
            for nb in adj[pos]:
                if nb < pos and assigned[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            # check if color available
            if not (avail[pos] & (1 << (c - 1))):
                continue
            # assign
            assigned[pos] = c
            # update neighbors > pos
            affected = []
            for nb in adj[pos]:
                if nb > pos and assigned[nb] == 0:
                    old = avail[nb]
                    new = old & ~(1 << (c - 1))
                    if new == 0:
                        # revert
                        assigned[pos] = 0
                        for a, _ in affected:
                            avail[a] = _
                        break
                    if new != old:
                        affected.append((nb, old))
                        avail[nb] = new
            else:
                # no break, proceed
                if dfs(pos + 1):
                    return True
            # backtrack
            assigned[pos] = 0
            for a, old in affected:
                avail[a] = old
        return False

    if dfs(1):
        out = ['YES', ' '.join(str(assigned[i]) for i in range(1, n + 1))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()