import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # For each edge (u, v), we need (c_u + 2*c_v) % 3 != 0
    # This means c_u != (-2*c_v) % 3 = c_v (since -2 ≡ 1 mod 3)
    # So c_u != c_v for every edge
    
    # We need to find lexicographically smallest assignment from {1,2,3}
    # such that no two adjacent vertices have the same value
    
    # Greedy approach: assign smallest valid value to each vertex
    assignment = [0] * n
    
    for u in range(n):
        forbidden = set()
        for v in adj[u]:
            if v < u:  # neighbor already assigned
                forbidden.add(assignment[v])
        for val in [1, 2, 3]:
            if val not in forbidden:
                assignment[u] = val
                break
        if assignment[u] == 0:  # no valid value found
            print("NO")
            return
    
    # Verify the solution
    for u in range(n):
        for v in adj[u]:
            if assignment[u] == assignment[v]:
                print("NO")
                return
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()