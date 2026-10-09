import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # Build implication graph
    # For each variable x, we have nodes x (true) and -x (false)
    # Each clause (a OR b) is equivalent to (~a -> b) AND (~b -> a)
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        # Add implications: ~a -> b and ~b -> a
        graph[-a].append(b)
        graph[-b].append(a)
        reverse_graph[b].append(-a)
        reverse_graph[a].append(-b)
    
    # Add all variables to graphs to ensure all nodes are present
    for i in range(1, n+1):
        if i not in graph:
            graph[i] = []
        if -i not in graph:
            graph[-i] = []
        if i not in reverse_graph:
            reverse_graph[i] = []
        if -i not in reverse_graph:
            reverse_graph[-i] = []
    
    # Kosaraju's algorithm for finding strongly connected components
    def dfs1(node, visited, stack):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs1(neighbor, visited, stack)
        stack.append(node)
    
    def dfs2(node, visited, component):
        visited.add(node)
        component.append(node)
        for neighbor in reverse_graph[node]:
            if neighbor not in visited:
                dfs2(neighbor, visited, component)
    
    # First DFS to get finishing order
    visited = set()
    stack = []
    nodes = list(graph.keys())
    for node in nodes:
        if node not in visited:
            dfs1(node, visited, stack)
    
    # Second DFS on transpose graph in reverse order
    visited = set()
    sccs = []
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs2(node, visited, component)
            sccs.append(component)
    
    # Check if any SCC contains both a variable and its negation
    assignment = {}
    for component in sccs:
        component_set = set(component)
        for node in component:
            if -node in component_set:
                print("NO")
                return
            if abs(node) not in assignment:
                # Assign values: nodes in later SCCs are assigned True
                assignment[abs(node)] = 1 if node > 0 else 0
    
    # Construct result
    result = []
    for i in range(1, n+1):
        if i in assignment:
            result.append(str(assignment[i]))
        else:
            # If variable doesn't appear in any constraint, assign 0
            result.append("0")
    
    print("YES")
    print(" ".join(result))

solve()