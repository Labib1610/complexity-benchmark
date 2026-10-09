import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each toggle, we'll create two nodes: x and -x
    # We'll build a graph where an edge from a to b means if a is true, then b must be true
    # This is for 2-SAT
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # The rule says at least one of l1 or l2 must be true
        # So if l1 is false, then l2 must be true
        # And if l2 is false, then l1 must be true
        # In terms of implications:
        # NOT l1 -> l2  which is equivalent to (-l1) -> l2
        # NOT l2 -> l1  which is equivalent to (-l2) -> l1
        
        # In implication graph:
        # -l1 -> l2
        # -l2 -> l1
        
        adj[-l1].append(l2)
        adj[-l2].append(l1)
        rev_adj[l2].append(-l1)
        rev_adj[l1].append(-l2)
    
    # Now we need to do Kosaraju's algorithm to check if this 2-SAT instance is satisfiable
    
    # First DFS to get finishing times
    visited = set()
    finish_stack = []
    
    def dfs1(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in adj[node]:
            dfs1(neighbor)
        finish_stack.append(node)
    
    # We need to consider all variables that appear
    all_nodes = set(adj.keys()) | set(rev_adj.keys())
    for node in all_nodes:
        if node not in visited:
            dfs1(node)
    
    # Second DFS on transpose graph to find SCCs
    visited.clear()
    scc_map = {}
    scc_id = 0
    
    def dfs2(node):
        if node in visited:
            return
        visited.add(node)
        scc_map[node] = scc_id
        for neighbor in rev_adj[node]:
            dfs2(neighbor)
    
    # Process in reverse order of finishing times
    while finish_stack:
        node = finish_stack.pop()
        if node not in visited:
            dfs2(node)
            scc_id += 1
    
    # Check for contradiction: for each variable x, x and -x must be in different SCCs
    for i in range(1, n+1):
        if scc_map.get(i, -1) == scc_map.get(-i, -2):
            print("NO")
            return
    
    # If satisfiable, reconstruct a solution
    # Assign values based on topological order of SCCs
    # Variables in later finishing SCCs should be assigned TRUE
    
    # We can use the fact that in the first DFS, the order gives us a reverse topological sort of the SCC DAG
    # But we already have the SCC ids. Let's just assign based on which SCC finishes later.
    
    # Actually, let's think differently. 
    # In the implication graph, if SCC of x comes after SCC of not x in topological order,
    # then we should set x to True.
    
    # To get the topological order, we can process the SCCs in the order they were discovered in the second DFS
    # But since we're doing DFS in the reverse graph, the order of scc_id assignment corresponds to reverse topological order
    
    # Better approach: collect all nodes in each SCC, and for each variable decide based on which copy (x or -x) is in a "later" SCC
    
    scc_nodes = defaultdict(list)
    for node, sid in scc_map.items():
        scc_nodes[sid].append(node)
    
    # The SCC ids are assigned in reverse topological order because of how Kosaraju works
    # So higher scc_id means earlier in topological order of the condensation
    # Wait, no. Let me retrace.
    
    # In Kosaraju:
    # 1. Do DFS on original graph, push to stack by finish time
    # 2. Do DFS on transpose graph in order of stack (reverse of finish time)
    #    This visits SCCs in topological order.
    # So the first SCC visited in step 2 is the first in topological order.
    
    # Therefore, lower scc_id means earlier in topological order.
    # If scc_id of x < scc_id of not x, then x should be FALSE.
    # If scc_id of x > scc_id of not x, then x should be TRUE.
    
    result = [0] * (n + 1)  # 1-indexed
    
    for i in range(1, n + 1):
        sid_i = scc_map.get(i, -1)
        sid_not_i = scc_map.get(-i, -2)
        if sid_i > sid_not_i:
            result[i] = 1
        else:
            result[i] = 0
            
    print("YES")
    print(' '.join(map(str, result[1:])))

if __name__ == "__main__":
    main()