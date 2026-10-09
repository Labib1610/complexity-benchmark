import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n  # bitmask of neighbors
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # order vertices by degree descending
    order = sorted(range(n), key=lambda x: adj[x].bit_count(), reverse=True)
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1] * n
    found = False

    def dfs(idx: int) -> bool:
        nonlocal found
        if idx == n:
            return True
        v = order[idx]
        # try colors 0,1,2
        neighbor_mask = adj[v]
        for c in range(3):
            conflict = False
            # iterate over already colored neighbors
            nb = neighbor_mask
            while nb:
                u = (nb & -nb).bit_length() - 1
                nb &= nb - 1
                if colors[u] == c:
                    conflict = True
                    break
            if not conflict:
                colors[v] = c
                if dfs(idx + 1):
                    return True
                colors[v] = -1
        return False

    if dfs(0):
        print("YES")
        # output in original order, convert to 1..3
        print(' '.join(str(colors[i] + 1) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()