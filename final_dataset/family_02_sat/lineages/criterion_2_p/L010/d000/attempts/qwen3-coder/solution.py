import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each clause (l1 l2), we need at least one of them to be true
    # This is a 2-SAT problem
    
    # We'll use implication graph and strongly connected components
    # Variables: 1..n (positive), -1..-n (negative)
    # Nodes: 0..2n-1 representing variables and their negations
    # node_id(x) = 2*(x-1) if x > 0, 2*(-x-1)+1 if x < 0
    
    def node_id(x):
        if x > 0:
            return 2 * (x - 1)
        else:
            return 2 * (-x - 1) + 1
    
    def var_from_node(u):
        if u % 2 == 0:
            return (u // 2) + 1
        else:
            return -((u - 1) // 2 + 1)
    
    # Build implication graph
    # For clause (l1 or l2), we add edges (!l1 -> l2) and (!l2 -> l1)
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    index = 2
    for i in range(m):
        l1 = int(data[index])
        l2 = int(data[index + 1])
        index += 2
        
        # Add implications: !l1 => l2, !l2 => l1
        adj[node_id(-l1)].append(node_id(l2))
        adj[node_id(-l2)].append(node_id(l1))
        rev_adj[node_id(l2)].append(node_id(-l1))
        rev_adj[node_id(l1)].append(node_id(-l2))
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    def dfs2(u, component):
        visited[u] = True
        component.append(u)
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, component)
    
    # First DFS pass
    for u in range(2 * n):
        if not visited[u]:
            dfs1(u)
    
    # Second DFS pass on reversed graph
    visited = [False] * (2 * n)
    components = []
    comp_id = [0] * (2 * n)
    
    while order:
        u = order.pop()
        if not visited[u]:
            component = []
            dfs2(u, component)
            components.append(component)
            cid = len(components) - 1
            for node in component:
                comp_id[node] = cid
    
    # Check if any variable and its negation are in the same SCC
    for i in range(n):
        pos = node_id(i + 1)
        neg = node_id(-(i + 1))
        if comp_id[pos] == comp_id[neg]:
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    assignment = [0] * n
    
    # Process components in reverse topological order
    for component in components:
        for node in component:
            var = var_from_node(node)
            idx = abs(var) - 1
            if assignment[idx] == 0:
                if var > 0:
                    assignment[idx] = 1
                else:
                    assignment[idx] = 0
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()