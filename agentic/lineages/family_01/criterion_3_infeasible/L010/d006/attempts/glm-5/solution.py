import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = True
        adj[v][u] = True
        deg[u] += 1
        deg[v] += 1
    
    # We need to find a triangle or a path of length 2 with missing middle edge.
    # The problem guarantees a solution exists.
    # We iterate vertices in order 1..n to find lexicographically smallest result.
    
    for u in range(1, n + 1):
        # Check for triangle containing u
        # Iterate neighbors v > u to avoid redundant checks and keep order
        neighbors = [v for v in range(1, n + 1) if adj[u][v]]
        k = len(neighbors)
        for i in range(k):
            v = neighbors[i]
            if v < u: continue # ensure v > u to avoid re-checking, but we need to check all pairs
            # Actually, to find the lex smallest triangle, we should check all pairs of neighbors
            # but we can optimize by checking if v > u.
            # However, since we iterate u from 1 to n, the first triangle found with smallest u,
            # and then smallest v, w will be the answer.
            for j in range(i + 1, k):
                w = neighbors[j]
                if adj[v][w]:
                    # Found triangle u, v, w
                    # Since u is smallest possible, and we iterate v, w in increasing order,
                    # this is the lexicographically smallest triangle.
                    print(u, v, w)
                    return
        
        # Check for path u - v - w where u-w is not an edge
        # We need to find v, w such that adj[u][v] and adj[v][w] and not adj[u][w]
        # We iterate v (neighbor of u) then w (neighbor of v).
        # To get lex smallest, we iterate v in increasing order, then w in increasing order.
        for v in neighbors:
            # We want the final set {u, v, w} to be sorted.
            # u is fixed. v is a neighbor.
            # We need w such that adj[v][w] is true and adj[u][w] is false.
            # w can be any node.
            # We iterate w from 1 to n.
            # Optimization: iterate neighbors of v.
            # But we must ensure we find the smallest w.
            for w in range(1, n + 1):
                if adj[v][w] and not adj[u][w]:
                    # Found a valid path
                    # The set is {u, v, w}.
                    # We need to print them sorted.
                    ans = sorted([u, v, w])
                    print(ans[0], ans[1], ans[2])
                    return

if __name__ == '__main__':
    solve()