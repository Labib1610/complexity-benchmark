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

    # conflict adjacency
    conflict = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        conflict[u] |= 1 << v
        conflict[v] |= 1 << u

    # complement adjacency (non‑conflict, excluding self)
    full = (1 << n) - 1
    comp_adj = [0] * n
    for i in range(n):
        comp_adj[i] = full ^ conflict[i] ^ (1 << i)

    target = k
    answer = None

    # Bron–Kerbosch style search for a clique of size k in the complement graph
    def dfs(R_mask: int, P_mask: int, size: int):
        nonlocal answer
        if answer is not None:
            return
        # pruning: even if we take all remaining vertices we cannot reach k
        if size + P_mask.bit_count() < target:
            return
        if size == target:
            # extract vertices from R_mask
            ans = []
            for v in range(n):
                if (R_mask >> v) & 1:
                    ans.append(v + 1)
            answer = ans
            return
        # choose a pivot to reduce branching (optional)
        # simple heuristic: pick vertex with max degree in P
        # here we just pick first vertex
        while P_mask:
            v = (P_mask & -P_mask).bit_length() - 1  # least significant bit index
            P_mask ^= 1 << v
            dfs(R_mask | (1 << v), P_mask & comp_adj[v], size + 1)
            if answer is not None:
                return

    all_vertices = (1 << n) - 1
    dfs(0, all_vertices, 0)

    out = []
    if answer is None:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(map(str, answer)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()