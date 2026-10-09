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

    # original adjacency as bitsets
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full = (1 << n) - 1
    # complement adjacency (edges where original graph has none)
    adjc = [0] * n
    for v in range(n):
        adjc[v] = full ^ (1 << v) ^ adj[v]   # all except self and original neighbours

    answer = None          # will hold list of vertices (0‑based) when found
    target = k

    # ordering vertices by degree in complement (optional heuristic)
    order = sorted(range(n), key=lambda x: adjc[x].bit_count(), reverse=True)

    # map from original index to position in ordered list and back
    pos2orig = order
    orig2pos = [0] * n
    for i, v in enumerate(order):
        orig2pos[v] = i

    # rebuild adjacency according to ordering to improve pruning
    adjc_ord = [0] * n
    for i, v in enumerate(order):
        mask = 0
        for u in range(n):
            if adjc[v] >> u & 1:
                mask |= 1 << orig2pos[u]
        adjc_ord[i] = mask

    all_vertices = (1 << n) - 1

    # recursive search
    def dfs(R_mask: int, R_list: list, P_mask: int):
        nonlocal answer
        if answer is not None:
            return
        if len(R_list) == target:
            answer = R_list[:]
            return
        # pruning
        if len(R_list) + P_mask.bit_count() < target:
            return

        # choose pivot u with max degree in P
        # simple heuristic: first vertex in P
        # better: vertex with max |P ∩ N(u)|
        u = -1
        max_deg = -1
        tmp = P_mask
        while tmp:
            v = (tmp & -tmp).bit_length() - 1
            deg = (P_mask & adjc_ord[v]).bit_count()
            if deg > max_deg:
                max_deg = deg
                u = v
            tmp &= tmp - 1

        # candidates = P \ N(u)
        cand = P_mask & ~adjc_ord[u]

        while cand:
            v = (cand & -cand).bit_length() - 1
            cand &= cand - 1

            R_list.append(pos2orig[v])
            dfs(R_mask | (1 << v), R_list, P_mask & adjc_ord[v])
            R_list.pop()
            if answer is not None:
                return
            P_mask &= ~(1 << v)   # remove v from P

    dfs(0, [], all_vertices)

    out = sys.stdout
    if answer is None:
        out.write("NO\n")
    else:
        # convert back to 1‑based numbers
        ans_one = [str(v + 1) for v in answer]
        out.write("YES\n")
        out.write(" ".join(ans_one) + "\n")

if __name__ == "__main__":
    solve()