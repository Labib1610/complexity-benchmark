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
    answer = []

    # simple recursive backtracking with pruning
    def dfs(cand_mask: int, cur_size: int, chosen):
        nonlocal answer
        if answer:          # already found
            return True
        if cur_size == k:
            answer = chosen[:]
            return True
        # not enough vertices left
        if cur_size + cand_mask.bit_count() < k:
            return False
        # pick a vertex (heuristic: vertex with maximum degree in cand)
        # compute degrees within cand
        v = -1
        max_deg = -1
        cm = cand_mask
        while cm:
            lsb = cm & -cm
            idx = (lsb.bit_length() - 1)
            deg = (adj[idx] & cand_mask).bit_count()
            if deg > max_deg:
                max_deg = deg
                v = idx
            cm ^= lsb
        if v == -1:
            return False

        # branch: include v
        new_cand = cand_mask & ~ (adj[v] | (1 << v))
        if dfs(new_cand, cur_size + 1, chosen + [v]):
            return True
        # branch: exclude v
        cand_mask &= ~(1 << v)
        return dfs(cand_mask, cur_size, chosen)

    dfs(all_vertices, 0, [])

    if answer:
        print("YES")
        print(' '.join(str(x + 1) for x in answer))
    else:
        print("NO")

if __name__ == "__main__":
    solve()