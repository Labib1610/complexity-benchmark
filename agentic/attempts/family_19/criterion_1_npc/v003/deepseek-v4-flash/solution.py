import sys
from collections import defaultdict, deque

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    products = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        products.append((s, t, d))

    edges = []
    adj = [[] for _ in range(n)]
    for j in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append((v, j))

    # Enumerate all simple paths for each product
    all_paths = []
    for s, t, d in products:
        paths = []
        # DFS to find all simple paths from s to t
        stack = [(s, [s], [])]  # node, visited nodes, edge indices used
        while stack:
            u, visited, edge_path = stack.pop()
            if u == t:
                paths.append(edge_path)
                continue
            for v, eidx in adj[u]:
                if v not in visited:
                    stack.append((v, visited + [v], edge_path + [eidx]))
        all_paths.append(paths)

    # Backtracking to assign flows
    flow_on_path = [[] for _ in range(k)]
    edge_usage = [0] * m

    def dfs(prod_idx):
        if prod_idx == k:
            return True
        s, t, d = products[prod_idx]
        paths = all_paths[prod_idx]
        # Try to assign d units among paths
        # We'll do recursive assignment per unit (or per path with amount)
        # Use recursion over paths with remaining demand
        def assign_paths(path_idx, remaining, chosen):
            if remaining == 0:
                # Save chosen flows
                flow_on_path[prod_idx] = chosen[:]
                return True
            if path_idx == len(paths):
                return False
            path = paths[path_idx]
            # Try sending x units on this path
            max_possible = min(remaining, min(edges[e][2] - edge_usage[e] for e in path))
            for x in range(max_possible, -1, -1):
                # Temporarily add
                for e in path:
                    edge_usage[e] += x
                chosen.append(x)
                if assign_paths(path_idx + 1, remaining - x, chosen):
                    return True
                chosen.pop()
                for e in path:
                    edge_usage[e] -= x
            return False

        if assign_paths(0, d, []):
            return dfs(prod_idx + 1)
        return False

    if dfs(0):
        # Build output
        out = ["YES"]
        for i in range(k):
            # flow per edge for product i
            edge_flow = [0] * m
            for path_idx, amount in enumerate(flow_on_path[i]):
                if amount > 0:
                    for e in all_paths[i][path_idx]:
                        edge_flow[e] += amount
            out.append(" ".join(str(x) for x in edge_flow))
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    main()