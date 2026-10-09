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
    
    clauses = []
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        clauses.append((l1, l2))
        index += 2
    
    # For each gate, we'll track implications
    # We'll use 2-SAT approach
    # Variables: 1 to n (positive = open, negative = closed)
    # For each clause (a or b), we add edges: not a -> b and not b -> a
    
    # Build implication graph
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for a, b in clauses:
        # not a -> b  which is  -a -> b
        # not b -> a  which is  -b -> a
        graph[-a].append(b)
        graph[-b].append(a)
        reverse_graph[b].append(-a)
        reverse_graph[a].append(-b)
    
    # Kosaraju's algorithm for SCC
    visited = set()
    order = []
    
    def dfs1(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs1(neighbor)
        order.append(node)
    
    # First DFS on original graph
    all_nodes = set()
    for a, b in clauses:
        all_nodes.add(a)
        all_nodes.add(b)
        all_nodes.add(-a)
        all_nodes.add(-b)
    
    for node in all_nodes:
        dfs1(node)
    
    # Second DFS on reverse graph
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
    
    # Process in reverse order
    while order:
        node = order.pop()
        if node not in visited:
            dfs2(node)
            scc_id += 1
    
    # Check if any variable and its negation are in the same SCC
    for i in range(1, n+1):
        if i in scc and -i in scc and scc[i] == scc[-i]:
            print("NO")
            return
    
    # Assign values based on SCC topological order
    # Variables in later SCCs should be assigned TRUE
    assignment = {}
    
    # Create a mapping from SCC id to nodes
    scc_nodes = defaultdict(list)
    for node, sid in scc.items():
        scc_nodes[sid].append(node)
    
    # Process SCCs in topological order (reverse of finishing times)
    # We can process them in order of scc_id since Kosaraju gives us that
    for sid in range(scc_id):
        for node in scc_nodes[sid]:
            var = abs(node)
            if var not in assignment:
                # If node is positive literal, set to 0 (since we process in order)
                # If node is negative literal, set to 1
                if node > 0:
                    assignment[var] = 0
                else:
                    assignment[var] = 1
    
    # For variables not in any clause, assign 0
    for i in range(1, n+1):
        if i not in assignment:
            assignment[i] = 0
    
    print("YES")
    result = []
    for i in range(1, n+1):
        result.append(str(assignment[i]))
    print(" ".join(result))

if __name__ == "__main__":
    main()