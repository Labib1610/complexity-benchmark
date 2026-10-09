import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    adj = [0] * n  # original graph adjacency bitmask
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # complement graph (edges where no dangerous reaction)
    comp = [0] * n
    full = (1 << n) - 1
    for i in range(n):
        comp[i] = (~adj[i]) & (full ^ (1 << i))  # exclude self

    target = k
    answer = []

    # popcount
    def popcnt(x: int) -> int:
        return x.bit_count()

    found = False

    # recursive search for clique of size k in complement graph
    def expand(R_mask: int, R_list: list, P: int, X: int):
        nonlocal found, answer
        if found:
            return
        rsize = len(R_list)
        if rsize == target:
            answer = R_list[:]
            found = True
            return
        # prune if even taking all candidates cannot reach target
        if rsize + popcnt(P) < target:
            return
        # choose pivot u from P|X with max degree in P
        union = P | X
        # simple heuristic: pick first vertex in union
        # better: max degree
        max_deg = -1
        u = -1
        temp = union
        while temp:
            v = (temp & -temp).bit_length() - 1
            deg = popcnt(P & comp[v])
            if deg > max_deg:
                max_deg = deg
                u = v
            temp &= temp - 1
        # vertices to iterate: P without neighbors of u
        candidates = P & ~comp[u] if u != -1 else P
        while candidates:
            v = (candidates & -candidates).bit_length() - 1
            candidates &= candidates - 1
            new_R_mask = R_mask | (1 << v)
            new_R_list = R_list + [v + 1]  # store 1‑based
            new_P = P & comp[v]
            new_X = X & comp[v]
            expand(new_R_mask, new_R_list, new_P, new_X)
            if found:
                return
            P &= ~(1 << v)
            X |= 1 << v

    all_vertices = (1 << n) - 1
    expand(0, [], all_vertices, 0)

    if found:
        print("YES")
        print(" ".join(map(str, answer)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()