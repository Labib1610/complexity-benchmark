import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if v not in neighbors[u]:
            neighbors[u].append(v)
        if u not in neighbors[v]:
            neighbors[v].append(u)

    color = [0] * n          # 0 unassigned, 1-3 assigned
    avail = [0b111] * n      # available colors bitmask for each vertex

    def dfs(i: int) -> bool:
        if i == n:
            return True
        # iterate colors 1..3
        for c in (1, 2, 3):
            # check conflict with already assigned neighbors
            conflict = False
            for nb in neighbors[i]:
                if nb < i and color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            # assign color
            color[i] = c
            changed = []
            ok = True
            for nb in neighbors[i]:
                if nb > i and (avail[nb] >> (c - 1)) & 1:
                    avail[nb] &= ~(1 << (c - 1))
                    changed.append(nb)
                    if avail[nb] == 0:
                        ok = False
                        break
            if ok and dfs(i + 1):
                return True
            # backtrack
            for nb in changed:
                avail[nb] |= (1 << (c - 1))
            color[i] = 0
        return False

    if dfs(0):
        out = ["YES"]
        out.append(" ".join(str(color[i]) for i in range(n)))
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()