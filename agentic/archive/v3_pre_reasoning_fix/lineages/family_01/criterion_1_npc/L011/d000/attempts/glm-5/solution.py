import sys
sys.setrecursionlimit(100000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    forbidden = [0] * n  # bitmask: bit i set means color i+1 is forbidden
    
    def has_valid_color(node):
        return forbidden[node] != 7  # 7 = 0b111, all colors forbidden
    
    def forward_check(node):
        for neighbor in adj[node]:
            if color[neighbor] == 0 and not has_valid_color(neighbor):
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        
        for c in range(1, 4):
            if not (forbidden[node] & (1 << (c - 1))):
                color[node] = c
                for neighbor in adj[node]:
                    forbidden[neighbor] |= (1 << (c - 1))
                if forward_check(node) and backtrack(node + 1):
                    return True
                for neighbor in adj[node]:
                    forbidden[neighbor] &= ~(1 << (c - 1))
                color[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

solve()