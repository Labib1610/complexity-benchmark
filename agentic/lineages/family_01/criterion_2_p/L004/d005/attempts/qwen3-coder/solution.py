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
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        adj[u].append(len(edges) - 1)
        adj[v].append(len(edges) - 1)
        index += 2

    # For each edge (u,v), the product of their values must be 2.
    # So we can model this as a 2-SAT problem.
    # Each variable x_i represents whether service i has value 2 (True) or 1 (False).
    # For each edge (u,v): (x_u OR x_v) AND (NOT x_u OR NOT x_v)
    # This is equivalent to: (x_u OR x_v) AND (NOT x_u -> NOT x_v) AND (NOT x_v -> NOT x_u)

    # But let's think simpler:
    # If we assign each node a boolean variable indicating whether it's assigned value 2,
    # then for each edge (u,v), we want: (val_u * val_v = 2)
    # Since val_u, val_v ∈ {1,2}, the products are:
    # 1*1=1, 1*2=2, 2*1=2, 2*2=4
    # So we want exactly one of them to be 2.
    # That means: (x_u XOR x_v) must be true.
    # Which is equivalent to: (x_u OR x_v) AND (NOT x_u OR NOT x_v)
    # This is exactly what was written above.

    # Let's build implication graph for 2-SAT
    # Variables: 0..n-1 for x_i (node i+1 has value 2), n..2n-1 for NOT x_i
    # We'll use 0-based indexing for variables: var[i] = i (means x_{i+1} is True)
    #                                           var[i+n] = i+n (means x_{i+1} is False)
    
    def var(i):
        return i
    
    def neg_var(i):
        return i + n

    # Clauses from edges: for each (u,v), we need (x_u OR x_v) AND (NOT x_u OR NOT x_v)
    # (x_u OR x_v) => add (~x_u -> x_v) and (~x_v -> x_u)
    # (NOT x_u OR NOT x_v) => add (x_u -> ~x_v) and (x_v -> ~x_u)
    
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for u, v in edges:
        u -= 1
        v -= 1
        # (~x_u -> x_v)
        graph[neg_var(u)].append(var(v))
        reverse_graph[var(v)].append(neg_var(u))
        
        # (~x_v -> x_u)
        graph[neg_var(v)].append(var(u))
        reverse_graph[var(u)].append(neg_var(v))
        
        # (x_u -> ~x_v)
        graph[var(u)].append(neg_var(v))
        reverse_graph[neg_var(v)].append(var(u))
        
        # (x_v -> ~x_u)
        graph[var(v)].append(neg_var(u))
        reverse_graph[neg_var(u)].append(var(v))

    # Now run Kosaraju's algorithm to check if there's a solution
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    visited = [False] * (2 * n)
    components = [-1] * (2 * n)
    comp_id = 0
    
    def dfs2(u):
        visited[u] = True
        components[u] = comp_id
        for v in reverse_graph[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            comp_id += 1
            
    # Check if any variable and its negation are in the same SCC
    for i in range(n):
        if components[var(i)] == components[neg_var(i)]:
            print("NO")
            return
    
    # Assign values based on component numbers
    assignment = [False] * n
    # In Kosaraju, later finishing times in first DFS correspond to sink SCCs
    # For 2-SAT, if comp[x] > comp[~x], then x should be True
    for i in range(n):
        if components[var(i)] > components[neg_var(i)]:
            assignment[i] = True
        else:
            assignment[i] = False
    
    # To get lexicographically smallest, we prefer False (value 1) when possible
    # But we already have a satisfying assignment. 
    # Actually, the above gives a valid assignment. 
    # To make it lex smallest, among valid ones, we can try to set early variables to False if possible.
    # But since we just need one valid assignment, and our method already ensures satisfiability,
    # we can proceed with the current assignment.
    
    result = []
    for b in assignment:
        if b:
            result.append('2')
        else:
            result.append('1')
            
    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    main()