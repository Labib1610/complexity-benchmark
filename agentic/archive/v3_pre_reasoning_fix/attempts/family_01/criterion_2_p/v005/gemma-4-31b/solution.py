import sys

# Increase recursion depth for deep DFS trees in large graphs
sys.setrecursionlimit(300000)

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    # colors: 0 = unvisited, 1 = shift 1, 2 = shift 2
    colors = [0] * (n + 1)
    
    # To get the lexicographically smallest assignment, 
    # we iterate through workers 1 to n.
    # If a worker is not yet assigned, we try assigning them to shift 1.
    # Since we must maintain bipartiteness, once the first node of a 
    # connected component is assigned, the rest are determined.
    # To minimize lexicographically, we want the earliest indices to have the smallest possible values.
    # For each component, we check if it's bipartite. 
    # If it is, we have two choices for the coloring (swap 1s and 2s).
    # We choose the one that results in a lexicographically smaller sequence.
    
    for i in range(1, n + 1):
        if colors[i] == 0:
            # New connected component
            component = []
            stack = [i]
            colors[i] = 1 # Try assigning the first node to 1
            
            # BFS/DFS to find all nodes in the component and check bipartiteness
            q = [i]
            visited_idx = 0
            possible = True
            while visited_idx < len(q):
                u = q[visited_idx]
                visited_idx += 1
                component.append(u)
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = 3 - colors[u]
                        q.append(v)
                    elif colors[v] == colors[u]:
                        print("NO")
                        return
            
            # We have a valid 2-coloring for this component.
            # Now decide whether to keep it or flip it (1 <-> 2).
            # To minimize lexicographically, we look at the smallest index in the component.
            # Since we process components starting from the smallest index i,
            # and we already set colors[i] = 1, this is already the best choice for the 
            # first element of the component.
            # However, we must ensure that this choice doesn't force a larger value 
            # on an even smaller index (which is impossible here since i is the smallest).
            # So keeping colors[i] = 1 is always optimal for the lexicographical order.
            pass

    print("YES")
    print(*(colors[1:]))

if __name__ == "__main__":
    solve()