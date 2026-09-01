import sys

sys.setrecursionlimit(10000)

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

    colors = [0] * n               # 0 = uncolored, else 1..3
    allowed = [0b111] * n           # bitmask of possible colors for each vertex

    # Precompute neighbor list for speed
    neighbors = adj

    def dfs(v: int) -> bool:
        if v == n:
            return True  # all vertices colored
        # try colors 1..3 in order for lexicographic minimality
        for col in (1, 2, 3):
            if not (allowed[v] & (1 << (col - 1))):
                continue
            # check against already colored neighbors
            conflict = False
            for nb in neighbors[v]:
                if colors[nb] == col:
                    conflict = True
                    break
            if conflict:
                continue

            # assign
            colors[v] = col
            # update allowed masks of uncolored neighbors
            changed = []  # list of (neighbor, previous_mask)
            mask_to_remove = 1 << (col - 1)
            for nb in neighbors[v]:
                if colors[nb] == 0:
                    prev = allowed[nb]
                    new = prev & ~mask_to_remove
                    if new != prev:
                        changed.append((nb, prev))
                        allowed[nb] = new
                        if new == 0:
                            break
            else:
                # no neighbor ran out of colors
                if dfs(v + 1):
                    return True
            # revert changes
            for nb, prev in changed:
                allowed[nb] = prev
            colors[v] = 0
        return False

    possible = dfs(0)
    out = []
    if possible:
        out.append("YES")
        out.append(" ".join(str(c) for c in colors))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()