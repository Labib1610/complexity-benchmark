import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        edges.append((u, v))
        index += 2
    
    # Build adjacency set for O(1) lookup
    adj = [set() for _ in range(n+1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # We want to find a triangle (a 3-clique) with the smallest lexicographical order
    # Enumerate all triplets (i,j,k) with i<j<k and check if they form a triangle
    # Since we want the lexicographically smallest, we iterate in increasing order
    
    for i in range(1, n-1):
        for j in range(i+1, n):
            if j not in adj[i]:
                continue
            for k in range(j+1, n+1):
                if k not in adj[i] or k not in adj[j]:
                    continue
                # Found a triangle: i-j-k
                print(i, j, k)
                return

if __name__ == "__main__":
    main()