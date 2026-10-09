import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    required_nodes = set()
    for _ in range(t):
        try:
            required_nodes.add(int(next(iterator)))
        except StopIteration:
            break
            
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            adj[v].append((u, w))
        except StopIteration:
            break

    # If t <= 1, no cabling is needed
    if t <= 1:
        print(0)
        return

    # We perform a post-order traversal (DFS) to compute the minimum cost
    # to connect required nodes within each subtree.
    # dp[u] = minimum cost to connect all required nodes in the subtree of u.
    # If a subtree has 0 or 1 required node, dp[u] = 0.
    # If a subtree has >= 2 required nodes, we must connect them.
    
    # We need to track the parent to avoid going back up the tree
    # Using an explicit stack to avoid recursion depth issues for n=200000
    
    # Stack elements: (u, parent, state)
    # state 0: entering the node (pre-processing)
    # state 1: exiting the node (post-processing)
    
    stack = [(1, 0, 0)]
    # We will store results in a list or dictionary
    # dp_values[u] will store the result for node u
    dp_values = [0] * (n + 1)
    # count_required[u] will store the count of required nodes in subtree u
    count_required = [0] * (n + 1)
    
    while stack:
        u, parent, state = stack.pop()
        
        if state == 0:
            # Entering node u
            stack.append((u, parent, 1))
            # Push children to stack
            for v, w in adj[u]:
                if v != parent:
                    stack.append((v, u, 0))
        else:
            # Exiting node u, children have been processed
            # Calculate count of required nodes in subtree u
            current_count = 1 if u in required_nodes else 0
            current_cost = 0
            
            for v, w in adj[u]:
                if v != parent:
                    # v is a child
                    child_count = count_required[v]
                    child_cost = dp_values[v]
                    
                    current_count += child_count
                    
                    if child_count >= 1:
                        # If the child's subtree has required nodes, we must connect
                        # the child's subtree to u.
                        # The cost is the cost to connect within the child's subtree (child_cost)
                        # plus the cost of the edge (u, v) to bring that connection to u.
                        current_cost += child_cost + w
            
            count_required[u] = current_count
            dp_values[u] = current_cost
            
    print(dp_values[1])

if __name__ == '__main__':
    solve()