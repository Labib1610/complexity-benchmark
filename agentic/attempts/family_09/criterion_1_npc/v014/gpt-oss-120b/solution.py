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

    all_vertices = (1 << n) - 1
    solution = []

    def dfs(cand_mask: int, cur):
        nonlocal solution
        if solution:   # already found
            return True
        cur_len = len(cur)
        if cur_len == k:
            solution = cur[:]
            return True
        # prune
        if cur_len + cand_mask.bit_count() < k:
            return False
        # choose a vertex (heuristic: vertex with max degree in cand)
        # simple: take lowest set bit
        v = (cand_mask & -cand_mask).bit_length() - 1

        # branch: include v
        new_cand = cand_mask & ~adj[v] & ~(1 << v)
        if dfs(new_cand, cur + [v + 1]):
            return True

        # branch: exclude v
        cand_mask_without_v = cand_mask & ~(1 << v)
        if dfs(cand_mask_without_v, cur):
            return True

        return False

    dfs(all_vertices, [])
    out = sys.stdout
    if solution:
        out.write("YES\n")
        out.write(" ".join(map(str, solution)) + "\n")
    else:
        out.write("NO\n")

if __name__ == "__main__":
    solve()