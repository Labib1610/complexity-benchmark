import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_mask = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    # Build adjacency lists without duplicates
    neighbors = [[] for _ in range(n)]
    for i in range(n):
        mask = adj_mask[i]
        while mask:
            lsb = mask & -mask
            j = (lsb.bit_length() - 1)
            neighbors[i].append(j)
            mask ^= lsb

    col = [0] * n          # 0 means uncolored, else 1/2/3
    avail = [0b111] * n    # bitmask of available colors for each vertex

    sys.setrecursionlimit(1000000)

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        avail_i = avail[idx]
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not avail_i & bit:
                continue
            col[idx] = c
            changes = []
            conflict = False
            for u in neighbors[idx]:
                if col[u] == 0:
                    prev = avail[u]
                    new = prev & ~bit
                    if new == 0:
                        conflict = True
                        break
                    avail[u] = new
                    changes.append((u, prev))
            if not conflict:
                if dfs(idx + 1):
                    return True
            # revert changes
            for u, prev in changes:
                avail[u] = prev
            col[idx] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(col[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()