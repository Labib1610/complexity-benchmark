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

    # depth‑first search with pruning
    def dfs(cur_mask: int, cand_mask: int):
        cur_sz = cur_mask.bit_count()
        if cur_sz == k:
            return cur_mask
        # not enough vertices left
        if cur_sz + cand_mask.bit_count() < k:
            return None
        # pick a vertex v (lowest set bit)
        v_bit = cand_mask & -cand_mask
        v = (v_bit.bit_length() - 1)

        # try to take v
        new_cand = cand_mask & ~adj[v]          # remove neighbours
        new_cand &= ~v_bit                      # also remove v itself
        res = dfs(cur_mask | v_bit, new_cand)
        if res is not None:
            return res

        # skip v
        return dfs(cur_mask, cand_mask & ~v_bit)

    ans_mask = dfs(0, all_vertices)

    out = []
    if ans_mask is None:
        out.append("NO")
    else:
        out.append("YES")
        vertices = [str(i + 1) for i in range(n) if (ans_mask >> i) & 1]
        out.append(" ".join(vertices))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()