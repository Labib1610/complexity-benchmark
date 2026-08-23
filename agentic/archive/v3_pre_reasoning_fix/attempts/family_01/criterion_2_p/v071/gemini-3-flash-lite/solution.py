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
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    color = [0] * (n + 1)
    
    # Lexicographically smallest means we prefer 1 over 2.
    # For each connected component, we try to assign 1 to the first node encountered.
    # Since we want the lexicographically smallest sequence, we iterate 1 to n.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS for this component
            # To ensure lexicographical order, we greedily assign 1 to the 
            # smallest uncolored node in the component.
            stack = [i]
            color[i] = 1
            component = []
            
            # Using a stack to traverse the component
            q = [i]
            while q:
                u = q.pop()
                component.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
                        
    print("YES")
    print(*(color[1:]))

if __name__ == '__main__':
    solve()