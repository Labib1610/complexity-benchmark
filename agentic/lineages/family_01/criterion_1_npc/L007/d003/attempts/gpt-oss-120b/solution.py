import sys

def solve() -> None:
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

    # mask of possible colors for each vertex, bits 0,1,2 correspond to colors 1,2,3
    poss = [0b111] * n
    color = [0] * n  # 0 means unassigned

    sys.setrecursionlimit(10000)

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        # try colors 1..3
        for c in range(1, 4):
            bit = 1 << (c - 1)
            if not (poss[idx] & bit):
                continue
            # assign
            color[idx] = c
            changed = []  # list of (neighbor, old_mask)
            fail = False
            for nb in adj[idx]:
                if color[nb]:
                    if color[nb] == c:
                        fail = True
                        break
                    continue
                if poss[nb] & bit:
                    old = poss[nb]
                    new = old & ~bit
                    if new == 0:
                        fail = True
                        # restore later
                        changed.append((nb, old))
                        break
                    poss[nb] = new
                    changed.append((nb, old))
            if not fail and dfs(idx + 1):
                return True
            # backtrack
            for nb, old in reversed(changed):
                poss[nb] = old
            color[idx] = 0
        return False

    if dfs(0):
        out = "YES\n" + " ".join(map(str, color))
    else:
        out = "NO"
    sys.stdout.write(out)

if __name__ == "__main__":
    solve()