import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * n
    for i in range(m):
        u = int(input_data[2 + 2 * i]) - 1
        v = int(input_data[3 + 2 * i]) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        
    assignment = [0] * n
    
    def dfs(u):
        if u == n:
            return True
        
        used = 0
        for v in range(u):
            if (adj[u] >> v) & 1:
                used |= 1 << assignment[v]
                
        for color in range(3):
            if not (used & (1 << color)):
                assignment[u] = color
                if dfs(u + 1):
                    return True
                    
        assignment[u] = 0
        return False

    if dfs(0):
        print("YES")
        print(" ".join(str(x + 1) for x in assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()