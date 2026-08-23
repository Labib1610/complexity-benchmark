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
    valid_colors = [7] * n  # bitmask 0b111 = all colors valid
    
    def backtrack(node):
        if node == n:
            return True
        
        for color in [1, 2, 3]:
            bit = 1 << (color - 1)
            if valid_colors[node] & bit:
                colors[node] = color
                
                saved = []
                for neighbor in adj[node]:
                    if colors[neighbor] == 0 and (valid_colors[neighbor] & bit):
                        saved.append((neighbor, valid_colors[neighbor]))
                        valid_colors[neighbor] &= ~bit
                
                valid = True
                for neighbor in adj[node]:
                    if colors[neighbor] == 0 and valid_colors[neighbor] == 0:
                        valid = False
                        break
                
                if valid and backtrack(node + 1):
                    return True
                
                for neighbor, vc in saved:
                    valid_colors[neighbor] = vc
                colors[node] = 0
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

solve()