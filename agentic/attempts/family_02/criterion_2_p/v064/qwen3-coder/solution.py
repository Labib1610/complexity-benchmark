import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    clauses = []
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        clauses.append((l1, l2))
        index += 2
    
    # Create implication graph for 2-SAT
    # Variables: 1 to n (positive), -1 to -n (negative)
    # We'll use node ids: for variable x (1-based), 
    # node 2*x represents x=True, node 2*x+1 represents x=False
    # But let's use a clearer mapping:
    # For variable i (1-based):
    # node 2*i -> x_i = True
    # node 2*i+1 -> x_i = False
    # But to make it easier, let's map:
    # var i (1..n) true: node i*2
    # var i (1..n) false: node i*2 + 1
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    # For each clause (l1 OR l2), we add edges:
    # (~l1 -> l2) and (~l2 -> l1)
    for l1, l2 in clauses:
        # Convert to node numbers
        # l1 positive: l1, negative: -l1
        # Node for var v being true: v*2
        # Node for var v being false: v*2 + 1
        # ~l1: if l1>0 then node for not l1 is l1*2+1, else it's (-l1)*2
        # Similarly for l2
        
        # (~l1 -> l2)
        if l1 > 0:
            # ~l1 is "l1 is false" which is node l1*2+1
            # l2: if l2>0 then "l2 is true" which is l2*2
            #     if l2<0 then "l2 is false" which is (-l2)*2+1
            from_node = l1 * 2 + 1
            to_node = l2 * 2 if l2 > 0 else (-l2) * 2 + 1
        else:
            # ~l1 is "l1 is true" which is (-l1)*2
            from_node = (-l1) * 2
            to_node = l2 * 2 if l2 > 0 else (-l2) * 2 + 1
        adj[from_node].append(to_node)
        rev_adj[to_node].append(from_node)
        
        # (~l2 -> l1)
        if l2 > 0:
            from_node = l2 * 2 + 1
            to_node = l1 * 2 if l1 > 0 else (-l1) * 2 + 1
        else:
            from_node = (-l2) * 2
            to_node = l1 * 2 if l1 > 0 else (-l1) * 2 + 1
        adj[from_node].append(to_node)
        rev_adj[to_node].append(from_node)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n + 2)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    # Run DFS1 on all nodes
    for i in range(2, 2*n + 2):  # nodes 2 to 2*n+1
        if not visited[i]:
            dfs1(i)
    
    # Transpose graph and run DFS in reverse order
    visited = [False] * (2 * n + 2)
    components = {}
    comp_num = 0
    
    def dfs2(u):
        visited[u] = True
        components[u] = comp_num
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            comp_num += 1
    
    # Check if satisfiable
    for i in range(1, n+1):
        node_true = i * 2
        node_false = i * 2 + 1
        if components[node_true] == components[node_false]:
            print("NO")
            return
    
    # Assign values
    assignment = [0] * (n + 1)
    # Sort components by their topological order
    # In Kosaraju, later finishing times in first DFS correspond to later components in topological sort
    # So components with higher numbers come later
    # We want to assign values based on reverse topological order of SCCs
    for i in range(1, n+1):
        node_true = i * 2
        node_false = i * 2 + 1
        if components[node_true] > components[node_false]:
            assignment[i] = 1
        else:
            assignment[i] = 0
            
    print("YES")
    print(' '.join(map(str, assignment[1:])))

if __name__ == "__main__":
    main()