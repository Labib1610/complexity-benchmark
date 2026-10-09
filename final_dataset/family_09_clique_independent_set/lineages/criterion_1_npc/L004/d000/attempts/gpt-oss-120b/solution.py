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

    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # complement graph (edges where there is NO friendship)
    comp = [0] * n
    full = (1 << n) - 1
    for i in range(n):
        comp[i] = full ^ adj[i] ^ (1 << i)   # remove self and friends

    target = k
    answer = []

    # Bron–Kerbosch style search for a clique of size k in the complement graph
    def dfs(R_mask: int, R_list: list, P_mask: int):
        nonlocal answer
        if answer:   # already found
            return
        rsize = len(R_list)
        if rsize == target:
            answer = R_list[:]
            return
        # prune if even taking all remaining vertices cannot reach k
        if rsize + P_mask.bit_count() < target:
            return

        # choose pivot u with max degree in P (heuristic)
        # we can just pick any vertex from P
        # to improve, pick vertex with max neighbors in P
        # compute candidates for iteration: vertices in P not adjacent to pivot
        # pivot selection
        u = -1
        max_deg = -1
        temp = P_mask
        while temp:
            v = (temp & -temp).bit_length() - 1
            deg = (P_mask & comp[v]).bit_count()
            if deg > max_deg:
                max_deg = deg
                u = v
            temp &= temp - 1
        # vertices to try: P \ N(u)
        candidates = P_mask & ~comp[u] if u != -1 else P_mask

        while candidates:
            v = (candidates & -candidates).bit_length() - 1
            candidates &= candidates - 1

            new_R_list = R_list + [v + 1]          # store 1‑based
            new_P_mask = P_mask & comp[v]          # keep only vertices adjacent to v in complement
            dfs(R_mask | (1 << v), new_R_list, new_P_mask)
            if answer:
                return
            # remove v from P
            P_mask &= ~(1 << v)

    all_vertices_mask = (1 << n) - 1
    dfs(0, [], all_vertices_mask)

    if answer:
        print("YES")
        print(" ".join(map(str, answer[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()