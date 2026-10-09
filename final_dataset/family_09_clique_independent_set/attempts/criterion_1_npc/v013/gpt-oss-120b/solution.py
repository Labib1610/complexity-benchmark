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

    all_mask = (1 << n) - 1
    result = []

    class Found(Exception):
        pass

    def dfs(cand_mask: int, cur_size: int, chosen):
        # prune
        if cur_size == k:
            raise Found(chosen[:])
        if cur_size + cand_mask.bit_count() < k:
            return
        # choose a vertex (simple heuristic: vertex with max degree in cand)
        # get first vertex
        v = (cand_mask & -cand_mask).bit_length() - 1  # least significant bit index
        # branch: include v
        new_cand = cand_mask & ~adj[v] & ~(1 << v)
        dfs(new_cand, cur_size + 1, chosen + [v + 1])
        # branch: exclude v
        dfs(cand_mask & ~(1 << v), cur_size, chosen)

    try:
        dfs(all_mask, 0, [])
        print("NO")
    except Found as e:
        ans = e.args[0]
        print("YES")
        print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()