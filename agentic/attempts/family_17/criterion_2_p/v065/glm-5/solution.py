import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    # Build adjacency list: for each transmitter, list of receivers
    adj = defaultdict(list)
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
    
    # Sort adjacency lists for deterministic matching
    for a in adj:
        adj[a].sort()
    
    match_r = {}  # receiver -> transmitter
    match_t = {}  # transmitter -> receiver
    
    def dfs(u, visited):
        for v in adj[u]:
            if v in visited:
                continue
            visited.add(v)
            if v not in match_r or dfs(match_r[v], visited):
                match_r[v] = u
                match_t[u] = v
                return True
        return False
    
    # Find maximum matching
    for u in range(1, q + 1):
        if u not in match_t:
            dfs(u, set())
    
    # Check if we have a perfect matching
    if len(match_t) != q:
        print("NO")
        return
    
    # Verify the sum constraint
    total = sum(u + match_t[u] for u in match_t)
    if total != q * (2 * q + 1):
        print("NO")
        return
    
    print("YES")
    for u in range(1, q + 1):
        print(u, match_t[u])

if __name__ == "__main__":
    solve()