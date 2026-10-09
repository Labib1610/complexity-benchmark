import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    # Build adjacency list
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate through all possible trios in lexicographical order
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            for c in range(b + 1, n + 1):
                # Check if all three edges exist (triangle)
                if b in adj[a] and c in adj[a] and c in adj[b]:
                    # Get internal conflict sets (intersection of adjacencies with {a,b,c})
                    S_a = set()
                    S_b = set()
                    S_c = set()
                    
                    for x in [b, c]:
                        if x in adj[a]:
                            S_a.add(x)
                    for x in [a, c]:
                        if x in adj[b]:
                            S_b.add(x)
                    for x in [a, b]:
                        if x in adj[c]:
                            S_c.add(x)
                    
                    # Check condition 1: all non-empty
                    if len(S_a) > 0 and len(S_b) > 0 and len(S_c) > 0:
                        # Check condition 2: all different
                        if S_a != S_b and S_b != S_c and S_a != S_c:
                            print(a, b, c)
                            return

if __name__ == "__main__":
    main()