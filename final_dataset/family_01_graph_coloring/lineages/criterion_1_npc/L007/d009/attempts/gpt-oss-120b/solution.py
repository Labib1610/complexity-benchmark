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
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        edges.append((u, v))

    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return

    # order vertices by degree descending for heuristic
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1] * n
    found = False

    def backtrack(idx: int):
        nonlocal found
        if found:
            return
        if idx == n:
            # all colored, check all edges different (guaranteed by checks)
            found = True
            return
        v = order[idx]
        # try colors 0,1,2
        neighbor_mask = adj[v]
        for c in range(3):
            conflict = False
            # iterate over neighbors already colored
            nb = neighbor_mask
            while nb:
                u = (nb & -nb).bit_length() - 1
                nb &= nb - 1
                if colors[u] == c:
                    conflict = True
                    break
            if not conflict:
                colors[v] = c
                backtrack(idx + 1)
                if found:
                    return
                colors[v] = -1

    backtrack(0)

    if not found:
        print("NO")
    else:
        # map 0,1,2 to 1,2,3
        ans = [str(c + 1) for c in colors]
        print("YES")
        print(" ".join(ans))

if __name__ == "__main__":
    solve()