import sys

sys.setrecursionlimit(10000)

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

    # order vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1] * n
    found = False

    def dfs(idx: int):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        v = order[idx]
        # try each color
        for c in range(3):
            conflict = False
            neigh_mask = adj[v]
            while neigh_mask:
                u = (neigh_mask & -neigh_mask).bit_length() - 1
                neigh_mask &= neigh_mask - 1
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
        # output in original order, convert 0/1/2 to 1/2/3
        print(' '.join(str(colors[i] + 1) for i in range(n)))

if __name__ == "__main__":
    solve()