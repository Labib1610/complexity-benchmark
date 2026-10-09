import sys
from collections import defaultdict, deque

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
    graph = defaultdict(list)
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based indexing
        v = int(data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # Since the graph is a tree (n nodes, n-1 edges, connected), we can use DFS/BFS to generate permutations smartly
    # But with n up to 8, we can try all permutations
    
    if n > 8:
        # For larger n, we might need a smarter approach, but according to constraints, it's likely small
        pass
    
    # Generate all permutations and check
    from itertools import permutations
    
    for perm in permutations(range(n)):
        total_length = 0
        pos = [0] * n  # position of module i in the permutation
        for i in range(n):
            pos[perm[i]] = i
        
        for u, v in edges:
            total_length += abs(pos[u] - pos[v])
            if total_length > B:
                break
        
        if total_length <= B:
            # Found a valid permutation
            result = [str(p + 1) for p in perm]  # Convert back to 1-based indexing
            print("YES")
            print(" ".join(result))
            return
    
    print("NO")

if __name__ == "__main__":
    main()