import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No constraints, choose all 1s for minimal energy
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build graph
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For each edge (u,v), W_u and W_v must form a basis.
    # W_i = [s_i, 3-s_i]^T
    # Matrix [W_u W_v] = [[s_u, s_v], [3-s_u, 3-s_v]]
    # Determinant = s_u*(3-s_v) - s_v*(3-s_u) = 3*s_u - s_u*s_v - 3*s_v + s_u*s_v = 3*(s_u - s_v)
    # For invertible, det != 0 => s_u != s_v
    # So for every edge, endpoints must have different values (1 or 2).
    # This is a 2-coloring (bipartite check) problem.
    
    color = [-1] * n  # -1 unvisited, 0 or 1 are colors (we'll map to 1 or 2 later)
    
    # Check if graph is bipartite
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    # Check all components
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return
    
    # If bipartite, we have a valid assignment.
    # We need to choose which color gets 1 and which gets 2 to minimize E = sum(s_i * 2^(n-1-i))
    # Try both assignments and pick the one with smaller E
    
    def compute_energy(assign):
        E = 0
        for i in range(n):
            E += assign[i] * (1 << (n - 1 - i))  # 2**(n-1-i)
        return E
    
    # Two possible assignments
    assign0 = [0] * n
    assign1 = [0] * n
    for i in range(n):
        if color[i] == 0:
            assign0[i] = 1
            assign1[i] = 2
        else:
            assign0[i] = 2
            assign1[i] = 1
    
    E0 = compute_energy(assign0)
    E1 = compute_energy(assign1)
    
    chosen_assign = assign0 if E0 <= E1 else assign1
    
    print("YES")
    print(" ".join(map(str, chosen_assign)))

if __name__ == "__main__":
    main()