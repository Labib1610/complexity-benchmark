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
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    # color[i] = 0: unvisited, 1: slot 1, 2: slot 2
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence s_1, s_2, ..., s_n,
    # for each connected component, we want to assign the smallest possible
    # values to the smallest indices.
    # However, for a bipartite component, once the color of one node is fixed,
    # the colors of all other nodes in that component are determined.
    # Let the two possible colorings be C1 and C2.
    # C1: node i gets color x, C2: node i gets color 3-x.
    # We compare C1 and C2 lexicographically and pick the smaller one.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            component = []
            stack = [i]
            color[i] = 1
            component.append(i)
            
            # BFS/DFS to find all nodes in the component and check bipartiteness
            idx = 0
            while idx < len(stack):
                u = stack[idx]
                idx += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                        component.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
            # For this component, we have two choices:
            # Choice A: keep colors as assigned (color[v])
            # Choice B: flip all colors (3 - color[v])
            # We want the lexicographically smallest sequence.
            # The first node in the component that we encounter in index order (1..n)
            # should be assigned '1' if possible. 
            # Since we iterate i from 1 to n, 'i' is the smallest index in this component.
            # To make the sequence lexicographically smallest, we MUST set s_i = 1.
            # If we set s_i = 1, then all other nodes in the component are fixed.
            # Wait, if we set s_i = 1, is that always better than s_i = 2?
            # Yes, because s_i is the first element of the sequence among this component's members.
            # So for each component, we find the smallest index 'min_idx' in that component,
            # and ensure s_{min_idx} = 1.
            
            # In our loop, 'i' is already the smallest index in the current component.
            # We already set color[i] = 1. This is the optimal choice for the 
            # lexicographically smallest sequence.
            
    print("YES")
    print(*(color[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()