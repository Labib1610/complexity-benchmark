import sys
sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    neigh = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    color = [0] * n  # 0 unassigned, 1..3 assigned
    color_mask = [0, 0, 0]  # masks for colors 1,2,3
    possible = [0b111] * n  # available colors for each node

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        for c in range(1, 4):
            if (adj[idx] & color_mask[c-1]) != 0:
                continue  # conflict with already colored neighbors
            # assign
            color[idx] = c
            color_mask[c-1] |= 1 << idx
            changes = []
            conflict = False
            for nb in neigh[idx]:
                if color[nb] == 0:
                    if (possible[nb] >> (c-1)) & 1:
                        changes.append((nb, possible[nb]))
                        possible[nb] &= ~(1 << (c-1))
                        if possible[nb] == 0:
                            conflict = True
                            break
            if not conflict:
                if dfs(idx + 1):
                    return True
            # revert
            for nb, old in changes:
                possible[nb] = old
            color[idx] = 0
            color_mask[c-1] ^= 1 << idx
        return False

    if dfs(0):
        out = ["YES", " ".join(str(col) for col in color)]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()