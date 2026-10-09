import sys
from collections import defaultdict, deque

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
    
    # Build implication graph
    # Each switch i has two nodes: i (UP) and -i (DOWN)
    # For a clause (a or b), we add edges: not a -> b and not b -> a
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    index = 2
    clauses = []
    for _ in range(m):
        a = int(data[index])
        b = int(data[index+1])
        index += 2
        clauses.append((a, b))
        # Add implications: not a -> b and not b -> a
        graph[-a].append(b)
        graph[-b].append(a)
        reverse_graph[b].append(-a)
        reverse_graph[a].append(-b)
    
    # Add all nodes to graphs to avoid missing keys
    for i in range(1, n+1):
        if i not in graph:
            graph[i] = []
        if -i not in graph:
            graph[-i] = []
        if i not in reverse_graph:
            reverse_graph[i] = []
        if -i not in reverse_graph:
            reverse_graph[-i] = []
    
    # Kosaraju's algorithm to find SCCs
    def dfs1(u, visited, stack):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs1(v, visited, stack)
        stack.append(u)
    
    def dfs2(u, visited, component):
        visited.add(u)
        component.append(u)
        for v in reverse_graph[u]:
            if v not in visited:
                dfs2(v, visited, component)
    
    # First DFS to get finishing order
    visited = set()
    stack = []
    nodes = list(graph.keys())
    for u in nodes:
        if u not in visited:
            dfs1(u, visited, stack)
    
    # Second DFS on transpose graph in reverse order
    visited = set()
    sccs = []
    while stack:
        u = stack.pop()
        if u not in visited:
            component = []
            dfs2(u, visited, component)
            sccs.append(component)
    
    # Build SCC mapping
    scc_map = {}
    for idx, component in enumerate(sccs):
        for node in component:
            scc_map[node] = idx
    
    # Check for contradictions
    for i in range(1, n+1):
        if scc_map[i] == scc_map[-i]:
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    assignment = {}
    # Process SCCs in reverse topological order (reverse of finishing order)
    for component in sccs:
        for node in component:
            if node not in assignment:
                # If node is positive literal
                if node > 0:
                    assignment[node] = 1  # UP
                    assignment[-node] = 0 # DOWN
                else:
                    assignment[node] = 1  # DOWN (since node is negative)
                    assignment[-node] = 0 # UP
    
    # Verify the assignment satisfies all clauses
    for a, b in clauses:
        val_a = assignment.get(a, 0) if a > 0 else assignment.get(a, 1)
        val_b = assignment.get(b, 0) if b > 0 else assignment.get(b, 1)
        if val_a == 0 and val_b == 0:
            # This should not happen if SCC check passed
            print("NO")
            return
    
    print("YES")
    result = []
    for i in range(1, n+1):
        result.append(str(assignment[i]))
    print(" ".join(result))

if __name__ == "__main__":
    main()