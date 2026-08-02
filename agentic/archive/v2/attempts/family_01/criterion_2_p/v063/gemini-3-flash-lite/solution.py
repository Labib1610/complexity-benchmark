import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
        
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # We want to pick the smallest color (1) first to be lexicographically smallest
            # For each connected component, we try assigning color 1 to the first uncolored node
            stack = [(i, 1)]
            color[i] = 1
            
            # Use a list to store nodes in current component to verify consistency
            component = []
            
            while stack:
                u, c = stack.pop()
                component.append(u)
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - c
                        stack.append((v, 3 - c))
                    elif color[v] == c:
                        print("NO")
                        return
                        
    print("YES")
    print(*(color[1:]))

if __name__ == '__main__':
    solve()