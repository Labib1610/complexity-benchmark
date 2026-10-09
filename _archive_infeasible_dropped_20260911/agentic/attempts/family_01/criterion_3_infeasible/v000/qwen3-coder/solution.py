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
    
    # Build adjacency list using sets for fast lookup
    adj = [set() for _ in range(n + 1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle: three nodes a, b, c such that
    # a-b, a-c, and b-c are all edges.
    # To get lexicographically smallest, we iterate a from 1 to n,
    # for each a, iterate b from a+1 to n, and for each b,
    # iterate c from b+1 to n, checking if all three edges exist.
    
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            # If a and b are not connected, skip
            if b not in adj[a]:
                continue
            for c in range(b + 1, n + 1):
                # Check if a-c and b-c exist
                if c in adj[a] and c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()