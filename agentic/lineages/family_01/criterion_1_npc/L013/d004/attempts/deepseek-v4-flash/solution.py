import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m = int(input_data[0]), int(input_data[1])
    edges = []
    idx = 2
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)

    colors = [0] * n  # 0 = uncolored, 1,2,3 = values

    # Pre-check: if any vertex has degree > 2? Not needed, but we can still use backtracking.

    # Sort vertices by degree for better pruning
    order = sorted(range(n), key=lambda x: len(adj[x]), reverse=True)
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i

    # Build adjacency in order indices
    adj_ordered = [[] for _ in range(n)]
    for u, v in edges:
        adj_ordered[pos[u]].append(pos[v])
        adj_ordered[pos[v]].append(pos[u])

    assignment = [0] * n

    def backtrack(i):
        if i == n:
            return True
        v = order[i]
        used = [False] * 4
        for nb in adj_ordered[i]:
            if assignment[nb] != 0:
                used[assignment[nb]] = True
        for c in range(1, 4):
            if not used[c]:
                assignment[i] = c
                if backtrack(i + 1):
                    return True
                assignment[i] = 0
        return False

    if backtrack(0):
        # Map back to original order
        result = [0] * n
        for i, v in enumerate(order):
            result[v] = assignment[i]
        print("YES")
        print(" ".join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()