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

    # popcount using builtin
    popcnt = int.bit_count

    # get lowest set bit index
    def lowbit(x: int) -> int:
        return (x & -x).bit_length() - 1

    def dfs(cand: int, cur_size: int, chosen: list) -> bool:
        nonlocal answer
        if cur_size == k:
            answer = chosen[:]
            return True
        if cur_size + popcnt(cand) < k:
            return False
        v = lowbit(cand)
        # include v
        new_cand = cand & ~ (adj[v] | (1 << v))
        if dfs(new_cand, cur_size + 1, chosen + [v]):
            return True
        # exclude v
        cand2 = cand & ~ (1 << v)
        if dfs(cand2, cur_size, chosen):
            return True
        return False

    if dfs(all_vertices, 0, []):
        # convert to 1‑based output
        ans1 = [str(x + 1) for x in answer]
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(ans1) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()