import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # order vertices by degree descending
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    pos_in_order = [0] * n
    for idx, v in enumerate(order):
        pos_in_order[v] = idx

    colors = [-1] * n
    found = False

    sys.setrecursionlimit(10000)

    def dfs(idx: int):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        v = order[idx]
        # try colors 0,1,2
        neighbor_mask = adj[v]
        for c in range(3):
            conflict = False
            # check neighbors already colored
            nb = neighbor_mask
            while nb:
                u = (nb & -nb).bit_length() - 1
                nb &= nb - 1
                if colors[u] == c:
                    conflict = True
                    break
            if not conflict:
                colors[v] = c
                dfs(idx + 1)
                if found:
                    return
                colors[v] = -1

    dfs(0)

    if not found:
        print("NO")
    else:
        print("YES")
        # output in original order, convert to 1..3
        print(' '.join(str(colors[i] + 1) for i in range(n)))

if __name__ == "__main__":
    solve()