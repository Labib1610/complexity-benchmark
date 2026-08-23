from collections import defaultdict, deque
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Build adjacency list for constraints: u < v means u must be less than v in tier
    # For each edge (u,v), we need u < v or v < u, i.e., tiers differ and one is strictly less
    # This is a 3-coloring problem with ordering: colors 1 < 2 < 3
    # We can model this as a 2-SAT or try all assignments, but with n<=40 and only 3 colors,
    # and we need lex smallest, so we can try backtracking with early pruning
    
    # But since n<=40 and we have constraints, let's think differently.
    # Each edge (u,v) means tier[u] != tier[v], and tier[u] < tier[v] or tier[v] < tier[u]
    # So for each edge, there are 6 possible ordered pairs out of 9 total pairs:
    # (1,2), (1,3), (2,3), (2,1), (3,1), (3,2)
    # Invalid pairs: (1,1), (2,2), (3,3)
    
    # We can model this as a graph where each node can be 1,2,3 and edges enforce constraints
    # This is a special case of graph coloring with order constraints
    # Since we have only 3 colors and total order, we can try all 3^n assignments for small n
    # But n=40 is too large for that.
    
    # Actually, let's think of it as a directed graph:
    # For each edge (u,v), we have either u < v or v < u
    # So we can try to orient each edge and check for consistency (no cycles)
    # But we also want the lex smallest assignment
    
    # Let's use backtracking with constraint propagation:
    # Try assigning tiers 1,2,3 to each node in order, and propagate constraints
    
    # Let's model it as a CSP:
    # Variables: nodes 0 to n-1
    # Domains: {1,2,3}
    # Constraints: for each edge (u,v), tier[u] != tier[v]
    
    # But we also need to ensure that for every edge, one is strictly less than the other
    # So tier[u] != tier[v] and (tier[u] < tier[v] or tier[v] < tier[u])
    # Which is just tier[u] != tier[v]
    
    # Wait, no. The constraint is that in the overlapping region, signals must be asymmetric
    # So one tower must operate at a strictly higher tier than the other
    # That means tier[u] != tier[v] is required, and one must be < the other
    # But since we only have 3 tiers, tier[u] != tier[v] already implies one is < the other
    # So the constraint is just tier[u] != tier[v]
    
    # This is a graph 3-coloring problem!
    # But we also want the lexicographically smallest solution
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to 3-color the graph with colors 1,2,3, minimizing lex order
    # Use backtracking
    color = [0] * n  # 0 means unassigned
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        for c in [1, 2, 3]:
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    main()