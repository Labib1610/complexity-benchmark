import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    total_edges = m
    pos = [0] * (n + 1)          # position of each node (0 = unassigned)
    used = [False] * (n + 1)     # positions used
    best_perm = None

    # order nodes by degree descending for better pruning
    order = sorted(range(1, n + 1), key=lambda x: -len(adj[x]))

    # mapping from order index to node id
    order_nodes = order

    # precompute minimal possible remaining contribution = 1 per edge
    min_per_edge = 1

    found = False

    def dfs(idx: int, cur_sum: int, counted_edges: int):
        nonlocal found, best_perm
        if found:
            return
        if idx == n:
            if cur_sum <= B:
                best_perm = pos[1:].copy()
                found = True
            return
        # lower bound
        lower = cur_sum + (total_edges - counted_edges) * min_per_edge
        if lower > B:
            return

        node = order_nodes[idx]
        # try each free position
        for p in range(1, n + 1):
            if used[p]:
                continue
            add = 0
            new_cnt = counted_edges
            for nb in adj[node]:
                if pos[nb]:
                    add += abs(p - pos[nb])
                    new_cnt += 1
            new_sum = cur_sum + add
            # prune with lower bound after this assignment
            lower2 = new_sum + (total_edges - new_cnt) * min_per_edge
            if lower2 > B:
                continue
            pos[node] = p
            used[p] = True
            dfs(idx + 1, new_sum, new_cnt)
            used[p] = False
            pos[node] = 0
            if found:
                return

    dfs(0, 0, 0)

    if not found:
        print("NO")
    else:
        # need output permutation: for each unit i, its slot position
        print("YES")
        print(' '.join(map(str, best_perm)))

if __name__ == "__main__":
    solve()