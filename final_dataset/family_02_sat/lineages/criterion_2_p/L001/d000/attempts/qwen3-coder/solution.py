import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each constraint (a or b), we create implications
    # If a is false, then b must be true: -a => b
    # If b is false, then a must be true: -b => a
    
    # Build implication graph
    # Nodes: 1..n for ACTIVE, -(1..n) for DORMANT
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # l1 or l2 must be true
        # If -l1 is true, then l2 must be true
        # If -l2 is true, then l1 must be true
        graph[-l1].append(l2)
        graph[-l2].append(l1)
        reverse_graph[l2].append(-l1)
        reverse_graph[l1].append(-l2)
    
    # Kosaraju's algorithm for finding strongly connected components
    visited = set()
    order = []
    
    def dfs1(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs1(neighbor)
        order.append(node)
    
    # Run DFS1 on all nodes
    for i in range(1, n + 1):
        if i not in visited:
            dfs1(i)
        if -i not in visited:
            dfs1(-i)
    
    # Reverse the order
    order.reverse()
    
    # DFS2 on reversed graph to find SCCs
    visited = set()
    scc = {}
    scc_id = 0
    
    def dfs2(node):
        if node in visited:
            return
        visited.add(node)
        scc[node] = scc_id
        for neighbor in reverse_graph[node]:
            dfs2(neighbor)
    
    for node in order:
        if node not in visited:
            dfs2(node)
            scc_id += 1
    
    # Check if for each variable, x and -x are in different SCCs
    for i in range(1, n + 1):
        if scc[i] == scc[-i]:
            print("NO")
            return
    
    # Assign values based on SCC topological order
    # SCC with higher id comes first in topological order
    assignment = {}
    
    # Process SCCs in reverse topological order
    for node in order:
        if node not in assignment:
            # If node is unassigned, assign it true
            assignment[node] = 1
            # Assign its negation false
            assignment[-node] = 0
    
    print("YES")
    result = []
    for i in range(1, n + 1):
        result.append(str(assignment[i]))
    print(" ".join(result))

solve()