import sys
sys.setrecursionlimit(100000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    
    # Build adjacency list: for each operator, list of units containing them
    adj = [[] for _ in range(n + 1)]
    units = []
    
    for unit_id in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        units.append((a, b, c))
        adj[a].append(unit_id)
        adj[b].append(unit_id)
        adj[c].append(unit_id)
    
    # Check if each operator has at least one unit
    for i in range(1, n + 1):
        if not adj[i]:
            print("NO")
            return
    
    used = [False] * t
    matched = [False] * (n + 1)
    result = []
    
    def dfs():
        # Find smallest unmatched operator
        start = 1
        while start <= n and matched[start]:
            start += 1
        
        if start > n:
            return True
        
        # Try each unit containing start
        for unit_id in adj[start]:
            if used[unit_id]:
                continue
            
            a, b, c = units[unit_id]
            if matched[a] or matched[b] or matched[c]:
                continue
            
            # Use this unit
            used[unit_id] = True
            matched[a] = matched[b] = matched[c] = True
            result.append((a, b, c))
            
            if dfs():
                return True
            
            # Backtrack
            used[unit_id] = False
            matched[a] = matched[b] = matched[c] = False
            result.pop()
        
        return False
    
    if dfs():
        print("YES")
        for a, b, c in result:
            print(a, b, c)
    else:
        print("NO")

solve()