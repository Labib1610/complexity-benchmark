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

    colors = [0] * n          # 0 uncolored, 1/2/3 colored
    forb_mask = [0] * n       # bitmask of forbidden colors (bits 0..2)

    ALL_FORBIDDEN = 0b111

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = pos
        for c in (1, 2, 3):
            mask = 1 << (c - 1)
            if forb_mask[v] & mask:
                continue  # color not allowed
            # assign
            colors[v] = c
            affected = []
            for nb in adj[v]:
                if colors[nb] == 0:
                    if not (forb_mask[nb] & mask):
                        forb_mask[nb] |= mask
                        affected.append(nb)
                    else:
                        # already forbidden, just record to revert
                        affected.append(nb)
            # check feasibility
            feasible = True
            for nb in affected:
                if forb_mask[nb] == ALL_FORBIDDEN:
                    feasible = False
                    break
            if feasible:
                # also check any other uncolored vertex that might have become impossible
                for i in range(n):
                    if colors[i] == 0 and forb_mask[i] == ALL_FORBIDDEN:
                        feasible = False
                        break
            if feasible and dfs(pos + 1):
                return True
            # backtrack
            for nb in affected:
                forb_mask[nb] &= ~mask
            colors[v] = 0
        return False

    if dfs(0):
        out = ["YES", "\n".join(str(c) for c in colors)]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()