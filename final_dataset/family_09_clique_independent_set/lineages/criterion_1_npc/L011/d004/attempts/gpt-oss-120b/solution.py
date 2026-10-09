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

    # include self in adjacency mask for easy removal when vertex is taken
    for i in range(n):
        adj[i] |= 1 << i

    full_mask = (1 << n) - 1
    answer = None

    # choose vertex with smallest degree among candidates (heuristic)
    degree = [bin(adj[i]).count("1") - 1 for i in range(n)]

    def dfs(chosen, cand_mask):
        nonlocal answer
        if answer is not None:
            return
        if len(chosen) == k:
            answer = chosen[:]
            return
        # pruning
        if len(chosen) + cand_mask.bit_count() < k:
            return
        # pick a vertex: smallest degree heuristic
        # extract candidates list
        # find first candidate
        v = (cand_mask & -cand_mask).bit_length() - 1  # any candidate
        # try include
        new_cand = cand_mask & ~adj[v]
        chosen.append(v)
        dfs(chosen, new_cand)
        chosen.pop()
        # try exclude
        dfs(chosen, cand_mask & ~(1 << v))

    dfs([], full_mask)

    if answer is None:
        print("NO")
    else:
        # convert to 1‑based indices
        print("YES")
        print(" ".join(str(v + 1) for v in answer))

if __name__ == "__main__":
    solve()