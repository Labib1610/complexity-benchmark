import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(300000)

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # colors[i] will be 0 (unvisited), 1, or 2
    colors = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, we process 
    # components in order of their smallest node index.
    # For each component, we try to assign frequency 1 to the smallest node.
    # Since the graph is bipartite, assigning the smallest node in a component 
    # to 1 will always be lexicographically smaller than assigning it to 2, 
    # provided the coloring is consistent.
    
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start a BFS/DFS to color the component
            # We use a stack for iterative DFS to avoid recursion limits
            stack = [(i, 1)]
            colors[i] = 1
            component = []
            
            # Use a temporary list to keep track of nodes in the current component
            # to ensure we can check for bipartiteness.
            q = [i]
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = 3 - colors[u]
                        q.append(v)
                    elif colors[v] == colors[u]:
                        print("NO")
                        return
            
    print("YES")
    print(*(colors[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()