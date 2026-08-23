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
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n          # 0 unassigned, 1-3 colored
    prohibited = [0] * n    # bitmask of colors forbidden due to assigned neighbors

    def dfs(pos):
        if pos == n:
            return True
        # try colors 1..3
        for c in (1, 2, 3):
            # check neighbor conflict
            conflict = False
            for nb in adj[pos]:
                if color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            # assign
            color[pos] = c
            changes = []
            fail = False
            bit = 1 << (c - 1)
            for nb in adj[pos]:
                if color[nb] == 0:
                    old = prohibited[nb]
                    new = old | bit
                    if new == 7:  # 0b111
                        fail = True
                        # no need to record this change since we will revert all
                        changes.append((nb, old))
                        break
                    prohibited[nb] = new
                    changes.append((nb, old))
            if not fail:
                if dfs(pos + 1):
                    return True
            # revert changes
            for nb, old in changes:
                prohibited[nb] = old
            color[pos] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()