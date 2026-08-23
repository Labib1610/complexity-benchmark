import sys

def solve():
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().split()
    
    if not data:
        return
    
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
    
    color = [0] * n
    forbidden = [0] * n  # Bitmask of forbidden colors for each vertex
    
    def backtrack(v):
        if v == n:
            return True
        
        for c in range(1, 4):
            bit = 1 << (c - 1)
            if forbidden[v] & bit:
                continue
            
            color[v] = c
            
            # Forward checking: update forbidden colors for uncolored neighbors
            updates = []
            valid = True
            for neighbor in adj[v]:
                if color[neighbor] == 0 and not (forbidden[neighbor] & bit):
                    forbidden[neighbor] |= bit
                    updates.append(neighbor)
                    if forbidden[neighbor] == 7:  # All colors forbidden
                        valid = False
                        break
            
            if valid and backtrack(v + 1):
                return True
            
            # Restore state
            for neighbor in updates:
                forbidden[neighbor] &= ~bit
            color[v] = 0
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

solve()