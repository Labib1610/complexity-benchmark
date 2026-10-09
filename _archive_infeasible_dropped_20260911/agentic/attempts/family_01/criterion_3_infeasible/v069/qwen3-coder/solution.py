import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list (incompatibility graph)
    adj = [set() for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].add(v)
        adj[v].add(u)
        index += 2
    
    # We need to find the lexicographically smallest triangle (a triple where each pair is connected)
    # That means we're looking for a triangle in the complement graph
    # So for any three nodes a<b<c, if none of (a,b), (a,c), (b,c) are in the edge set, then it's a valid triple
    
    # Let's iterate through all combinations a < b < c and check if they form a triangle in the complement
    # i.e., check if there are NO edges between a,b,c in the original graph
    
    # To make it faster, for each node, store its neighbors in a set
    # Then for each pair (a,b), find common non-neighbors
    
    # But since n <= 2000, O(n^3) might be too slow. Let's think differently.
    
    # For each node a, look at all pairs (b,c) where a < b < c
    # Check if there's no edge between a-b, a-c, b-c
    
    # Let's try a different approach:
    # For each node a from 1 to n-2:
    #   For each node b from a+1 to n-1:
    #       For each node c from b+1 to n:
    #           Check if none of (a,b), (a,c), (b,c) exist in adj
    #           If so, we found our triple
    
    # This is O(n^3) but with pruning might work
    
    # Actually, let's just do brute force with early termination
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            # If a and b are compatible (i.e., NOT in adj), proceed
            if b not in adj[a]:
                for c in range(b + 1, n + 1):
                    # Check if a,c and b,c are also compatible
                    if c not in adj[a] and c not in adj[b]:
                        print(a, b, c)
                        return

if __name__ == "__main__":
    main()