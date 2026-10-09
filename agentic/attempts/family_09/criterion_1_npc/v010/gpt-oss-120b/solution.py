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

    ALL = (1 << n) - 1
    answer = []

    # recursive search for independent set of size k
    def dfs(cand_mask: int, cur: list):
        nonlocal answer
        if answer:  # already found
            return
        if len(cur) == k:
            answer = cur[:]
            return
        # pruning: not enough vertices left
        if len(cur) + cand_mask.bit_count() < k:
            return
        # choose a vertex (heuristic: smallest degree in candidates)
        # extract candidates list
        # pick first vertex
        v = (cand_mask & -cand_mask).bit_length() - 1  # lowest set bit
        # branch: include v
        new_cand = cand_mask & ~adj[v] & ~(1 << v)
        dfs(new_cand, cur + [v])
        if answer:
            return
        # branch: exclude v
        dfs(cand_mask & ~(1 << v), cur)

    dfs(ALL, [])
    if answer:
        print("YES")
        print(' '.join(str(x + 1) for x in answer))
    else:
        print("NO")

if __name__ == "__main__":
    solve()