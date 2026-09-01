import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Find lexicographically smallest locked triple
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            # Check if a-b is a link
            ab = b in adj[a]
            for c in range(b + 1, n + 1):
                # Check links for triple (a, b, c)
                ac = c in adj[a]
                bc = c in adj[b]
                
                # Count links in the triple
                cnt = ab + ac + bc
                
                # If cnt >= 2, triple is locked
                if cnt >= 2:
                    print(a, b, c)
                    return
                
                # If cnt == 1, need to check if locked
                # Locked if the two non-linked pairs are both non-links
                if cnt == 1:
                    # The two non-linked pairs must both be non-links
                    # This is equivalent to: exactly one link among the three pairs
                    # and the other two pairs are non-links (which they are by cnt=1)
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()