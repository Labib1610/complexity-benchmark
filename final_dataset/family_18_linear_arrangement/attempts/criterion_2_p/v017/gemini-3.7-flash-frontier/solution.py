import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])

    if n == 1:
        print("YES")
        print("1")
        return

    adj = [[] for _ in range(n + 1)]
    edges = []
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        idx += 2

    # Find centroids
    sz = [0] * (n + 1)

    def get_sizes(u, p):
        sz[u] = 1
        for v in adj[u]:
            if v != p:
                get_sizes(v, u)
                sz[u] += sz[v]

    get_sizes(1, 0)

    centroids = []

    def get_centroids(u, p):
        is_centroid = True
        for v in adj[u]:
            if v != p:
                get_centroids(v, u)
                if sz[v] > n // 2:
                    is_centroid = False
        if n - sz[u] > n // 2:
            is_centroid = False
        if is_centroid:
            centroids.append(u)

    get_centroids(1, 0)

    # Select candidates to test as root
    if n <= 2000:
        candidates = list(range(1, n + 1))
    else:
        # For large N, test centroids and their immediate neighbors
        cand_set = set(centroids)
        for c in centroids:
            for v in adj[c]:
                cand_set.add(v)
                for w in adj[v]:
                    cand_set.add(w)
        candidates = list(cand_set)

    def get_subtree_size(u, p, tree_sz):
        s = 1
        for v in adj[u]:
            if v != p:
                s += get_subtree_size(v, u, tree_sz)
        tree_sz[u] = s
        return s

    def build_layout_rooted(u, p, tree_sz):
        # Sort children by subtree size ascending
        children = [v for v in adj[u] if v != p]
        children.sort(key=lambda v: tree_sz[v])
        res = [u]
        for v in children:
            res.extend(build_layout_rooted(v, u, tree_sz))
        return res

    best_cost = float("inf")
    best_layout = None

    for r in candidates:
        tree_sz = [0] * (n + 1)
        get_subtree_size(r, 0, tree_sz)

        # Children of root r
        children = adj[r][:]
        # Sort by size descending to alternate to L and R
        children.sort(key=lambda v: tree_sz[v], reverse=True)

        L_children = []
        R_children = []
        for i, v in enumerate(children):
            if i % 2 == 0:
                R_children.append(v)
            else:
                L_children.append(v)

        # L_children sorted ascending by size (closest to r to farthest)
        L_children.sort(key=lambda v: tree_sz[v])
        R_children.sort(key=lambda v: tree_sz[v])

        # Construct layout:
        # L subtrees placed in reverse from closest to farthest
        left_part = []
        for v in L_children:
            sub = build_layout_rooted(v, r, tree_sz)
            sub.reverse()
            left_part = sub + left_part

        right_part = []
        for v in R_children:
            sub = build_layout_rooted(v, r, tree_sz)
            right_part.extend(sub)

        layout = left_part + [r] + right_part

        # Compute actual cost
        pos = [0] * (n + 1)
        for p_idx, u in enumerate(layout):
            pos[u] = p_idx + 1

        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])

        if cost < best_cost:
            best_cost = cost
            best_layout = layout
            if best_cost <= B and n > 2000:
                break

    if best_cost <= B:
        print("YES")
        pos = [0] * (n + 1)
        for p_idx, u in enumerate(best_layout):
            pos[u] = p_idx + 1
        print(*(pos[i] for i in range(1, n + 1)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()