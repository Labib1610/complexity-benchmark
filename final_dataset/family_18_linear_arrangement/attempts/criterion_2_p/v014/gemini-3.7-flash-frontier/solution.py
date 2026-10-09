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

    adj = [[] for _ in range(n + 1)]
    idx = 3
    edges = []
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        idx += 2

    if n == 1:
        if B >= 0:
            print("YES")
            print("1")
        else:
            print("NO")
        return

    # Helper to find tree centroids
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

    # Function to build layout rooted at R
    def build_layout(R):
        sub_sz = [0] * (n + 1)

        def calc_sz(u, p):
            s = 1
            for v in adj[u]:
                if v != p:
                    s += calc_sz(v, u)
            sub_sz[u] = s
            return s

        calc_sz(R, 0)

        # Returns a list of vertices with u at the beginning (index 0)
        def layout_subtree(u, p):
            children = [v for v in adj[u] if v != p]
            children.sort(key=lambda x: sub_sz[x])
            res = [u]
            for v in children:
                res.extend(layout_subtree(v, u))
            return res

        # For root R, partition its children into Left and Right
        children = [v for v in adj[R] if v != 0]
        children.sort(key=lambda x: sub_sz[x])

        left_groups = []
        right_groups = []

        for i, v in enumerate(children):
            st = layout_subtree(v, R)
            if i % 2 == 0:
                # v is at st[0]. We want v adjacent to R, so reverse st on the left.
                st.reverse()
                left_groups.append(st)
            else:
                # v is at st[0]. On the right, st starts with v, which is adjacent to R.
                right_groups.append(st)

        # left_groups: smaller subtrees should be closer to R.
        # Since smaller was added first (i=0), we reverse left_groups so smaller is at the end (near R).
        left_groups.reverse()

        order = []
        for g in left_groups:
            order.extend(g)
        order.append(R)
        for g in right_groups:
            order.extend(g)

        return order

    def evaluate(order):
        pos = [0] * (n + 1)
        for i, u in enumerate(order):
            pos[u] = i + 1
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
        return cost, pos

    best_cost = float("inf")
    best_pos = None

    # Candidate roots: all centroids + more if n is small
    candidates = list(centroids)
    if n <= 1000:
        candidates = list(range(1, n + 1))
    elif len(candidates) < 5:
        # Add a few other nodes (e.g. high degree nodes)
        degrees = sorted(
            range(1, n + 1), key=lambda x: len(adj[x]), reverse=True
        )
        for d in degrees[:10]:
            if d not in candidates:
                candidates.append(d)

    for cand in candidates:
        order = build_layout(cand)
        cost, pos = evaluate(order)
        if cost < best_cost:
            best_cost = cost
            best_pos = pos
            if best_cost <= B:
                break

    if best_cost <= B:
        print("YES")
        print(*(best_pos[1:]))
    else:
        print("NO")


if __name__ == "__main__":
    solve()