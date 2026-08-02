import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    adj = [[] for _ in range(N + 1)]
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # To get the lexicographically smallest assignment, we prefer channel 1
    # for lower-indexed nodes whenever possible.
    # We process nodes 1 to N. If a node is not colored, we color it 1
    # and use DFS to color its connected component.
    
    color = [0] * (N + 1)
    
    for i in range(1, N + 1):
        if color[i] == 0:
            # Start coloring this component. 
            # We must assign color[i] = 1 to be lexicographically smallest.
            stack = [(i, 1)]
            color[i] = 1
            
            while stack:
                u, c = stack.pop()
                
                # Sort neighbors to ensure deterministic behavior if needed,
                # though here we just need to traverse the component.
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - c
                        stack.append((v, color[v]))
                    elif color[v] == c:
                        print("NO")
                        return
                        
    print("YES")
    print(*(color[1:]))

if __name__ == '__main__':
    solve()