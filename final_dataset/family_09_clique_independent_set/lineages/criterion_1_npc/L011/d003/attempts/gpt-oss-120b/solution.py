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

    adj = [0] * n          # bitmask of neighbours (including itself)
    for i in range(n):
        adj[i] = 1 << i    # include itself for easy removal

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    all_vertices = (1 << n) - 1
    answer_mask = 0
    found = False

    # pre‑compute degree inside a mask (used for heuristic)
    degree = [bin(adj[i]).count('1') - 1 for i in range(n)]

    # choose vertex with maximal degree inside current mask
    def choose_vertex(mask: int) -> int:
        # simple linear scan – n ≤ 46
        best = -1
        best_deg = -1
        m = mask
        while m:
            v = (m & -m).bit_length() - 1
            d = degree[v]
            if d > best_deg:
                best_deg = d
                best = v
            m &= m - 1
        return best

    def dfs(cand: int, cur_mask: int, cur_sz: int) -> bool:
        nonlocal answer_mask, found
        if cur_sz == k:
            answer_mask = cur_mask
            return True
        # not enough vertices left
        if cur_sz + cand.bit_count() < k:
            return False

        v = choose_vertex(cand)
        # branch 1: include v
        new_cand = cand & ~adj[v]
        if dfs(new_cand, cur_mask | (1 << v), cur_sz + 1):
            return True
        # branch 2: exclude v
        cand_without_v = cand & ~(1 << v)
        if dfs(cand_without_v, cur_mask, cur_sz):
            return True
        return False

    if dfs(all_vertices, 0, 0):
        # output answer
        res = [str(i + 1) for i in range(n) if (answer_mask >> i) & 1]
        print("YES")
        print(" ".join(res))
    else:
        print("NO")

if __name__ == "__main__":
    solve()