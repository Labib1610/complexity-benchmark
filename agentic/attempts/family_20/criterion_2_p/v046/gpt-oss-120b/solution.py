import sys
def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n_in = int(next(it))
    n_out = int(next(it))
    m = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]
    deg_in = [0] * n_in
    deg_out = [0] * n_out
    for u, v in edges:
        deg_in[u] += 1
        deg_out[v] += 1
    Delta = max(max(deg_in, default=0), max(deg_out, default=0))
    # simple greedy assignment
    used_in = [set() for _ in range(n_in)]
    used_out = [set() for _ in range(n_out)]
    ans = [0] * m
    for idx, (u, v) in enumerate(edges):
        # find smallest color not used at u or v
        cu = used_in[u]
        cv = used_out[v]
        c = 1
        while c in cu or c in cv:
            c += 1
        ans[idx] = c
        cu.add(c)
        cv.add(c)
    # if any color exceeds Delta, shift down (should not happen)
    print("YES")
    print(' '.join(map(str, ans)))
if __name__ == "__main__":
    solve()