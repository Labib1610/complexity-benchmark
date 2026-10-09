import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each variable x_i, we create two nodes: i (for x_i = True) and -i (for x_i = False)
    # Each clause (a OR b) translates to implications: NOT a => b and NOT b => a
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # Clause: (l1 OR l2)
        # This is equivalent to: (NOT l1 => l2) AND (NOT l2 => l1)
        # In terms of graph edges: (-l1 -> l2) and (-l2 -> l1)
        adj[-l1].append(l2)
        adj[-l2].append(l1)
        rev_adj[l2].append(-l1)
        rev_adj[l1].append(-l2)
    
    # Kosaraju's algorithm for SCC
    visited = set()
    order = []
    
    def dfs1(u):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs1(v)
        order.append(u)
    
    # First DFS on original graph
    all_nodes = set(adj.keys()) | set(rev_adj.keys())
    for node in all_nodes:
        if node not in visited:
            dfs1(node)
    
    visited.clear()
    scc_map = {}
    scc_id = 0
    
    def dfs2(u):
        visited.add(u)
        scc_map[u] = scc_id
        for v in rev_adj[u]:
            if v not in visited:
                dfs2(v)
    
    # Second DFS on transpose graph in reverse finish order
    for node in reversed(order):
        if node not in visited:
            dfs2(node)
            scc_id += 1
    
    # Check for contradiction: for any variable x_i, i and -i must be in different SCCs
    for i in range(1, n+1):
        if scc_map.get(i, -1) == scc_map.get(-i, -2):
            print("NO")
            return
    
    # Assign values based on SCC topological order
    # Variables in later finishing SCCs should be assigned True
    assignment = {}
    for i in range(1, n+1):
        pos_scc = scc_map.get(i, -1)
        neg_scc = scc_map.get(-i, -2)
        if pos_scc == -1 and neg_scc == -2:
            # Variable doesn't appear in any clause, assign True (1)
            assignment[i] = 1
        elif pos_scc > neg_scc:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    result = [str(assignment[i]) for i in range(1, n+1)]
    print(' '.join(result))

if __name__ == "__main__":
    main()