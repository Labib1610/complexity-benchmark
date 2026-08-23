import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(300000)

def solve():
    # Read n and m
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
        
    # color[i] will be 0 (unvisited), 1 (Mode 1), or 2 (Mode 2)
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, we iterate through modules 1 to n.
    # For each connected component, the first unvisited node 'i' should be assigned 
    # the smallest possible value (1) if it doesn't lead to a contradiction.
    # However, since it's a bipartite graph, if we assign color[i] = 1, 
    # the colors of all other nodes in the component are fixed.
    # If we assign color[i] = 2, they are also fixed (flipped).
    # To minimize lexicographically, we must check if assigning 1 to the smallest index
    # in the component is possible. Since the component is bipartite, 
    # assigning 1 to the root is always as good as or better than assigning 2, 
    # PROVIDED we only care about the root. 
    # Wait, the lexicographical smallest means we want s_1 to be 1 if possible, 
    # then s_2 to be 1 if possible, and so on.
    # For a connected component, once the color of one node is fixed, all others are fixed.
    # Let the smallest index in a component be 'root'. 
    # We want s_{root} = 1. Then we check if this is valid (bipartite).
    # If the component is bipartite, assigning s_{root} = 1 will always yield a 
    # lexicographically smaller sequence than s_{root} = 2 because 
    # the sequence starts with a smaller value at the first differing position.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS to color the component
            stack = [(i, 1)]
            color[i] = 1
            component = [i]
            
            # Standard BFS to find all nodes in component and check bipartiteness
            q = [i]
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
    print("YES")
    print(*(color[1:]))

if __name__ == "__main__":
    solve()