import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    # Build adjacency list and set for fast lookup
    adj = defaultdict(set)
    
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].add(v)
        adj[v].add(u)
    
    # For lexicographically smallest, iterate a from 1 to n
    for a in range(1, n + 1):
        # For each neighbor b of a where b > a (sorted to find smallest b first)
        neighbors_a = sorted(adj[a])
        for b in neighbors_a:
            if b <= a:
                continue
            # For each neighbor c of b where c > b (sorted to find smallest c first)
            neighbors_b = sorted(adj[b])
            for c in neighbors_b:
                if c <= b:
                    continue
                # Check if a and c are connected
                if c in adj[a]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()