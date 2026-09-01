import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # ---------- 1. compute weights w[i] ----------
    # symbolic simulation: start with A[i] = x_i (different symbols)
    # we only need the total contribution of each x_i to the final sum.
    # Use integer arithmetic: treat each x_i as 1 and later multiply by its
    # coefficient.
    # Simpler: run the process with concrete numbers 1..n and then solve a
    # linear system? Not needed – we can compute contributions directly.
    # We'll simulate with an array coeff[i] = contribution of b[i] to current A[i].
    # Initially coeff[i] = 1 (A_i = 1 * b_i).
    coeff = [1] * n          # coefficient of b[i] inside A_i at current step
    # after each step k, we add 3 * A_k to later A_j, i.e. their coefficients
    # increase by 3 * coeff[k].
    for k in range(n - 1):
        inc = 3 * coeff[k]
        for j in range(k + 1, n):
            coeff[j] += inc
    # final metric M = sum_i coeff[i] * b_i
    w = coeff                # already the needed weights

    # ---------- 2. backtracking search ----------
    colour = [0] * n          # 0 = unassigned, otherwise 1..3
    found = False

    # order of processing: natural order 0..n-1 (weights decreasing)
    def dfs(v: int) -> bool:
        nonlocal found
        if v == n:
            return True
        # try colours 1,2,3 in order
        for c in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if nb < v and colour[nb] == c:   # only already coloured neighbours
                    ok = False
                    break
            if not ok:
                continue
            colour[v] = c
            if dfs(v + 1):
                return True
            colour[v] = 0
        return False

    if dfs(0):
        # we have the lexicographically smallest proper colouring
        print("YES")
        print(' '.join(map(str, colour)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()