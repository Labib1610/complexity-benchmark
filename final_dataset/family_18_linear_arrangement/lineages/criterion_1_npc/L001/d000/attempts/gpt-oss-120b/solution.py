import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    K = int(next(it))

    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)

    # order vertices by degree descending for better branching
    vertices = list(range(n))
    vertices.sort(key=lambda x: -len(adj[x]))

    placed = [False] * n
    pos = [0] * n          # station number (1‑based)
    order = [0] * (n + 1)  # order[idx] = vertex at station idx
    answer = None

    # pre‑compute total edges for bound
    total_edges = m

    def dfs(idx: int, cur_sum: int, placed_edges: int):
        nonlocal answer
        if answer is not None:
            return
        if idx > n:
            if cur_sum <= K:
                # build answer in required format (stations for component 1..n)
                ans = [0] * n
                for v in range(n):
                    ans[v] = pos[v]
                answer = ans
            return

        # try every not yet placed vertex, in the order defined above
        for v in vertices:
            if placed[v]:
                continue
            added = 0
            newly = 0
            for u in adj[v]:
                if placed[u]:
                    added += idx - pos[u]
                    newly += 1
            new_sum = cur_sum + added
            new_placed_edges = placed_edges + newly

            # lower bound: each remaining edge needs at least length 1
            min_possible = new_sum + (total_edges - new_placed_edges)
            if min_possible > K:
                continue

            placed[v] = True
            pos[v] = idx
            order[idx] = v
            dfs(idx + 1, new_sum, new_placed_edges)
            if answer is not None:
                return
            placed[v] = False

    dfs(1, 0, 0)

    out = []
    if answer is None:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(x) for x in answer))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()