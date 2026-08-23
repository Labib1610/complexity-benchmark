def solve():
    import sys
    sys.setrecursionlimit(10000)
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
    
    assignment = [0] * n
    available = [7] * n  # bitmask: 7 = 0b111 means all 3 colors available
    
    def backtrack(node):
        if node == n:
            return True
        
        for color in range(1, 4):
            bit = 1 << (color - 1)
            if available[node] & bit:
                assignment[node] = color
                
                removed = []
                for neighbor in adj[node]:
                    if assignment[neighbor] == 0 and (available[neighbor] & bit):
                        available[neighbor] &= ~bit
                        removed.append(neighbor)
                
                if all(available[neighbor] for neighbor in removed):
                    if backtrack(node + 1):
                        return True
                
                for neighbor in removed:
                    available[neighbor] |= bit
                assignment[node] = 0
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()