import sys

def solve():
    data = sys.stdin.read().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    tiers = [0] * n
    
    def get_valid_tiers(node):
        used = set(tiers[neighbor] for neighbor in adj[node] if tiers[neighbor] != 0)
        return [t for t in [1, 2, 3] if t not in used]
    
    def forward_check(node):
        for neighbor in adj[node]:
            if tiers[neighbor] == 0 and not get_valid_tiers(neighbor):
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        
        for tier in get_valid_tiers(node):
            tiers[node] = tier
            if forward_check(node) and backtrack(node + 1):
                return True
            tiers[node] = 0
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, tiers)))
    else:
        print("NO")

solve()