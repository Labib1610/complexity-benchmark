import sys
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    zones = [0] * n  # 0 means unassigned, 1-3 means zone
    
    def get_valid_zones(node):
        used = set()
        for neighbor in adj[node]:
            if zones[neighbor] != 0:
                used.add(zones[neighbor])
        return [z for z in [1, 2, 3] if z not in used]
    
    def backtrack(node):
        if node == n:
            return True
        
        valid_zones = get_valid_zones(node)
        for z in valid_zones:
            zones[node] = z
            # Forward check: check unassigned neighbors
            ok = True
            for neighbor in adj[node]:
                if zones[neighbor] == 0 and len(get_valid_zones(neighbor)) == 0:
                    ok = False
                    break
            if ok and backtrack(node + 1):
                return True
            zones[node] = 0
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, zones)))
    else:
        print("NO")

solve()