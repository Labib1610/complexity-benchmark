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
    for i in range(n):
        adj[i] = 1 << i  # self-loop to simplify exclusion

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    all_vertices = (1 << n) - 1
    solution = []

    # depth‑first search with pruning
    def dfs(cur_mask: int, cand_mask: int, size: int):
        nonlocal solution
        if size == k:
            # extract vertices from cur_mask
            sol = []
            cm = cur_mask
            while cm:
                v = (cm & -cm).bit_length() - 1
                sol.append(v + 1)
                cm &= cm - 1
            solution = sol
            return True
        # not enough vertices left
        if size + cand_mask.bit_count() < k:
            return False
        # choose a vertex (least significant bit)
        v = (cand_mask & -cand_mask).bit_length() - 1

        # branch: include v
        if dfs(cur_mask | (1 << v), cand_mask & ~adj[v], size + 1):
            return True
        # branch: exclude v
        if dfs(cur_mask, cand_mask & ~(1 << v), size):
            return True
        return False

    dfs(0, all_vertices, 0)

    if solution:
        print("YES")
        print(" ".join(map(str, solution)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()