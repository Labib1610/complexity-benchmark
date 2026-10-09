import sys
from collections import deque

def find_valid_intervention():
    # Read input
    n, m, s, t, B = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))
    
    # Try all possible subsets of edges to suppress (2^m possibilities)
    # But we'll do something more efficient
    
    # We want to find a subset of edges to suppress such that:
    # 1. Total cost <= B
    # 2. s and t are disconnected in the remaining graph
    
    # Let's use a BFS approach with bitmasks for efficiency
    # But since m can be up to 20, we can't check all 2^m subsets
    # However, n is up to 100, so let's think differently
    
    # We can model this as finding a cut between s and t
    # We want to remove a set of edges with total weight <= B such that s and t are disconnected
    
    # This is essentially finding a minimum s-t cut and checking if its weight <= B
    # But we also need to enumerate a solution if it exists
    
    # Let's try a different approach: iterate through all possible subsets
    # Since m <= 20, 2^20 is about 1 million, which should be manageable
    
    best_subset = None
    min_cost = float('inf')
    
    # Check if s and t are already disconnected
    if s == t:
        print("NO")
        return
    
    # For small m, we can enumerate all subsets
    if m <= 20:
        for mask in range(1 << m):
            cost = 0
            suppressed = []
            for i in range(m):
                if mask & (1 << i):
                    cost += edges[i][2]
                    suppressed.append(i)
            
            if cost > B:
                continue
                
            # Check if s and t are disconnected in the remaining graph
            # Build graph without suppressed edges
            adj = [[] for _ in range(n + 1)]
            for i in range(m):
                if not (mask & (1 << i)):  # Not suppressed
                    u, v, _ = edges[i]
                    adj[u].append(v)
                    adj[v].append(u)
            
            # BFS to check connectivity
            visited = [False] * (n + 1)
            queue = deque([s])
            visited[s] = True
            
            while queue:
                node = queue.popleft()
                if node == t:
                    # s and t are still connected, this is not a valid solution
                    break
                    
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            else:
                # s and t are disconnected
                if cost <= B:
                    if best_subset is None or len(suppressed) < len(best_subset):
                        best_subset = suppressed[:]
                    elif len(suppressed) == len(best_subset) and cost < min_cost:
                        best_subset = suppressed[:]
                        min_cost = cost
    
    if best_subset is not None:
        print("YES")
        print(len(best_subset))
        for idx in best_subset:
            u, v, _ = edges[idx]
            print(u, v)
    else:
        print("NO")

# Optimization for larger cases - let's implement a better approach
def solve():
    # Read input
    n, m, s, t, B = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))
    
    # Special case when s == t
    if s == t:
        print("NO")
        return
    
    # For small m, we can enumerate all subsets
    if m <= 20:
        for mask in range(1 << m):
            cost = 0
            for i in range(m):
                if mask & (1 << i):
                    cost += edges[i][2]
            
            if cost > B:
                continue
                
            # Check if s and t are disconnected in the remaining graph
            # Build graph without suppressed edges
            adj = [[] for _ in range(n + 1)]
            for i in range(m):
                if not (mask & (1 << i)):  # Not suppressed
                    u, v, _ = edges[i]
                    adj[u].append(v)
                    adj[v].append(u)
            
            # BFS to check connectivity
            visited = [False] * (n + 1)
            queue = deque([s])
            visited[s] = True
            connected = False
            
            while queue:
                node = queue.popleft()
                if node == t:
                    connected = True
                    break
                    
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            # If s and t are NOT connected, this is a valid solution
            if not connected:
                print("YES")
                count = bin(mask).count('1')
                print(count)
                for i in range(m):
                    if mask & (1 << i):
                        u, v, _ = edges[i]
                        print(u, v)
                return
        
        print("NO")
        return
    
    # For larger m, we might need a different approach
    # But according to constraints, m <= 20, so above approach works
    print("NO")

solve()