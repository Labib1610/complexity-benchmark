import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    heights = [0] * (n + 1)
    
    def backtrack(pillar):
        if pillar > n:
            return True
        
        used = set(heights[neighbor] for neighbor in adj[pillar] if heights[neighbor] != 0)
        
        for h in [1, 2, 3]:
            if h not in used:
                heights[pillar] = h
                if backtrack(pillar + 1):
                    return True
                heights[pillar] = 0
        
        return False
    
    if backtrack(1):
        print("YES")
        print(" ".join(map(str, heights[1:])))
    else:
        print("NO")

solve()