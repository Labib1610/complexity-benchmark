import sys
sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)

    # simple check with identity permutation
    identity = list(range(1, n + 1))
    total = 0
    for u, v in edges:
        total += abs(u - v)
    if total <= B:
        print("YES")
        print(*identity)
        return

    # backtracking search
    pos = [-1] * n          # position (0‑based) assigned to each crop
    used = [False] * n      # which positions are taken
    answer = None

    # order nodes by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))

    def dfs(idx: int, cur_sum: int):
        nonlocal answer
        if answer is not None:
            return
        if cur_sum > B:
            return
        if idx == n:
            answer = pos.copy()
            return
        node = order[idx]
        # try each free position
        for p in range(n):
            if not used[p]:
                # compute added cost with already placed neighbours
                add = 0
                for nb in adj[node]:
                    if pos[nb] != -1:
                        add += abs(p - pos[nb])
                used[p] = True
                pos[node] = p
                dfs(idx + 1, cur_sum + add)
                used[p] = False
                pos[node] = -1
                if answer is not None:
                    return

    dfs(0, 0)

    if answer is None:
        print("NO")
    else:
        # convert positions to 1‑based zone numbers per crop index (1..n)
        res = [0] * n
        for crop in range(n):
            res[crop] = answer[crop] + 1
        print("YES")
        print(*res)

if __name__ == "__main__":
    solve()