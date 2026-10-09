import sys
import itertools

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    # Pre‑compute adjacency for quick degree ordering (optional)
    # Try permutations in order of increasing sum using heuristic: start from identity
    # but we will just brute‑force; n is expected to be small for this NP‑hard problem.
    vars_range = list(range(n))
    best_perm = None

    # Simple pruning: if current partial sum already exceeds B, skip further extensions.
    # We'll generate permutations recursively with backtracking.
    pos = [-1] * n          # position assigned to each variable (0‑based stage)
    used = [False] * n

    # For fast edge contribution calculation, store edges per variable
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # order variables for assignment: maybe by degree descending
    order = sorted(range(n), key=lambda x: -len(adj[x]))

    sys.setrecursionlimit(10000)
    found = False
    result = None

    def dfs(idx, cur_sum):
        nonlocal found, result
        if found:
            return
        if cur_sum > B:
            return
        if idx == n:
            # all assigned
            found = True
            # convert positions to 1‑based stages per variable index order
            ans = [pos[i] + 1 for i in range(n)]
            result = ans
            return
        var = order[idx]
        # try each free stage
        for stage in range(n):
            if not used[stage]:
                # compute added sum for edges where neighbor already placed
                add = 0
                for nb in adj[var]:
                    if pos[nb] != -1:
                        add += abs(stage - pos[nb])
                used[stage] = True
                pos[var] = stage
                dfs(idx + 1, cur_sum + add)
                used[stage] = False
                pos[var] = -1
                if found:
                    return

    dfs(0, 0)

    out = []
    if found:
        out.append("YES")
        out.append(" ".join(map(str, result)))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()