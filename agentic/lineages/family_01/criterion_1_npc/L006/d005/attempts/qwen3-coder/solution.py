import sys
from itertools import product

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, m, edges

def forms_cycle(assignments, edges):
    # Create adjacency list based on the assignment
    adj = [[] for _ in range(len(assignments))]
    for u, v in edges:
        cu, cv = assignments[u], assignments[v]
        # Check if cu divides cv
        if cv % cu == 0:
            adj[u].append(v)
        # Check if cv divides cu
        if cu % cv == 0:
            adj[v].append(u)
    
    # Detect cycle with DFS
    visited = [0] * len(assignments)  # 0 = unvisited, 1 = in progress, 2 = finished
    stack = []  # For iterative DFS to avoid recursion limit issues
    
    def has_cycle_dfs(start):
        stack.clear()
        stack.append((start, None))  # node, parent_in_stack
        path = set()  # Nodes in current path
        
        while stack:
            node, parent = stack.pop()
            
            if visited[node] == 2:
                if node in path:
                    path.remove(node)
                continue
                
            if visited[node] == 1:
                visited[node] = 2
                if node in path:
                    path.remove(node)
                continue
                
            visited[node] = 1
            path.add(node)
            stack.append((node, parent))
            
            for neighbor in adj[node]:
                if neighbor in path:
                    return True
                if visited[neighbor] == 0:
                    stack.append((neighbor, node))
                    
        return False
    
    for i in range(len(assignments)):
        if visited[i] == 0:
            if has_cycle_dfs(i):
                return True
    return False

def solve():
    n, m, edges = read_input()
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Try all 3^n combinations
    for combo in product([1, 2, 3], repeat=n):
        if not forms_cycle(combo, edges):
            print("YES")
            print(" ".join(map(str, combo)))
            return
            
    print("NO")

if __name__ == "__main__":
    solve()