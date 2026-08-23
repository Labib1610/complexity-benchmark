def solve():
    import sys
    data = sys.stdin.read().split()
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    colors = [0] * n
    forbidden = [0] * n  # bitmask: bit i set means color i+1 forbidden
    
    def backtrack(node):
        if node == n:
            return True
        
        for color in [1, 2, 3]:
            bit = color - 1
            if not (forbidden[node] & (1 << bit)):
                colors[node] = color
                
                changes = []
                for neighbor in adj[node]:
                    if colors[neighbor] == 0 and not (forbidden[neighbor] & (1 << bit)):
                        forbidden[neighbor] |= (1 << bit)
                        changes.append(neighbor)
                
                valid = True
                for neighbor in changes:
                    if forbidden[neighbor] == 7:  # all colors forbidden
                        valid = False
                        break
                
                if valid and backtrack(node + 1):
                    return True
                
                for neighbor in changes:
                    forbidden[neighbor] &= ~(1 << bit)
                colors[node] = 0
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

solve()