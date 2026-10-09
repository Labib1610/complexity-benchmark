import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        v = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        edges.append((u, v))
    
    # If no edges, any permutation works
    if m == 0:
        print("YES")
        print(" ".join(str(i+1) for i in range(n)))
        return
    
    # For small n, try all permutations
    if n <= 8:
        for perm in permutations(range(n)):
            total = 0
            pos = [0] * n
            for i in range(n):
                pos[perm[i]] = i
            for u, v in edges:
                total += abs(pos[u] - pos[v])
                if total > B:
                    break
            if total <= B:
                print("YES")
                result = [0] * n
                for i in range(n):
                    result[perm[i]] = i + 1
                print(" ".join(map(str, result)))
                return
        print("NO")
        return
    
    # For larger n, use a heuristic: place nodes greedily to minimize total distance
    # Start with placing first two connected nodes at ends
    if m > 0:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Find the node with maximum degree to place at center
        max_deg = max(degree)
        center_node = degree.index(max_deg)
        
        # Assign positions: place center_node at middle, others around it
        pos = [-1] * n
        order = [center_node]
        visited = [False] * n
        visited[center_node] = True
        
        # BFS to get an ordering
        queue = [center_node]
        while queue:
            curr = queue.pop(0)
            neighbors = adj[curr]
            for nei in neighbors:
                if not visited[nei]:
                    visited[nei] = True
                    order.append(nei)
                    queue.append(nei)
        
        # Place nodes in order along the line
        for i in range(n):
            pos[order[i]] = i
        
        # Calculate total distance
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
        
        if total <= B:
            result = [0] * n
            for i in range(n):
                result[pos[i]] = i + 1
            # Create the inverse mapping
            final_pos = [0] * n
            for i in range(n):
                final_pos[order[i]] = i + 1
            print("YES")
            print(" ".join(map(str, final_pos)))
            return
    
    # Try a few random permutations for larger graphs
    import random
    random.seed(42)
    for _ in range(1000):
        perm = list(range(n))
        random.shuffle(perm)
        pos = [0] * n
        for i in range(n):
            pos[perm[i]] = i
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            if total > B:
                break
        if total <= B:
            result = [0] * n
            for i in range(n):
                result[perm[i]] = i + 1
            print("YES")
            print(" ".join(map(str, result)))
            return
            
    print("NO")

if __name__ == "__main__":
    main()