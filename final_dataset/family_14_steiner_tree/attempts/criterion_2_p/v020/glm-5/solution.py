import sys

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    # Read the t special fragments
    special_nodes = [int(x) for x in input_data[3:3+t]]
    
    # Build the adjacency list for the tree
    adj = [[] for _ in range(n + 1)]
    idx = 3 + t
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3
        
    # If there is 1 or fewer special fragments, no resin is needed
    if t <= 1:
        print(0)
        return
        
    # Keep track of which nodes are special
    is_special = [False] * (n + 1)
    for node in special_nodes:
        is_special[node] = True
        
    total_resin = 0
    
    # Iterative DFS to avoid recursion depth limits and function call overhead
    # State: (node, parent, edge_weight, state)
    # state 0 means entering the node, state 1 means exiting
    stack = [(1, 0, 0, 0)]
    count = [0] * (n + 1)
    
    while stack:
        u, p, w, state = stack.pop()
        
        if state == 0:
            # Entering node u
            stack.append((u, p, w, 1))
            # Push children to stack
            for v, weight in adj[u]:
                if v != p:
                    stack.append((v, u, weight, 0))
        else:
            # Exiting node u
            if is_special[u]:
                count[u] += 1
                
            # If the subtree rooted at u contains at least one special node,
            # and the rest of the tree also contains at least one special node,
            # then the edge connecting u to its parent must be in the Steiner Tree.
            if count[u] > 0 and count[u] < t:
                total_resin += w
                
            # Propagate the count of special nodes up to the parent
            if p != 0:
                count[p] += count[u]
                
    print(total_resin)

if __name__ == '__main__':
    solve()