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
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # We need the lexicographically smallest assignment.
            # When starting a new component, we must try assigning 1 to the smallest node.
            stack = [(i, 1)]
            color[i] = 1
            
            while stack:
                u, c = stack.pop()
                
                # To ensure lexicographical smallest, sort neighbors
                # But we must process them such that we explore nodes in order.
                # Actually, standard bipartite coloring works if we always 
                # try to assign 1 to the smallest uncolored node.
                
                neighbors = sorted(adj[u])
                for v in neighbors:
                    if color[v] == 0:
                        color[v] = 3 - c
                        stack.append((v, 3 - c))
                    elif color[v] == c:
                        print("NO")
                        return

    # Check if this greedy approach yields the lexicographically smallest.
    # The requirement is that we want s1, s2, ..., sn to be lexicographically smallest.
    # This means for each component, we choose the coloring that makes the smallest 
    # index node 1.
    
    print("YES")
    print(*(color[1:]))

solve()