import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    FULL = (1 << (n + 1)) - 1
    adj_mask = [0] * (n + 1)
    for i in range(1, n + 1):
        adj_mask[i] = adj[i] & FULL
    
    memo = {}
    
    def can_complete(pos, used1, used2):
        if pos > n:
            return True
        key = (pos, used1, used2)
        if key in memo:
            return memo[key]
        
        forbidden = used1 | used2 | adj_mask[pos]
        avail = FULL & ~forbidden
        
        if (avail >> pos) & 1:
            if can_complete(pos + 1, used1 | (1 << pos), used2):
                memo[key] = True
                return True
        
        if (avail >> (pos + n + 1)) & 1:
            if can_complete(pos + 1, used1, used2 | (1 << pos)):
                memo[key] = True
                return True
        
        memo[key] = False
        return False
    
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        color[i] = 3
        used1 = 0
        used2 = 0
        for j in range(1, i):
            if color[j] == 1:
                used1 |= (1 << j)
            elif color[j] == 2:
                used2 |= (1 << j)
        
        forbidden = used1 | used2 | adj_mask[i]
        if not ((forbidden >> i) & 1):
            if can_complete(i + 1, used1 | (1 << i), used2):
                color[i] = 1
                continue
        
        if not ((forbidden >> (i + n + 1)) & 1):
            if can_complete(i + 1, used1, used2 | (1 << i)):
                color[i] = 2
                continue
        
        print("NO")
        return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()