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
    
    # For each variable, we'll have implications
    # We'll use 2-SAT approach
    # Variables: 1 to n (positive) and -1 to -n (negative)
    # We'll build implication graph and use Kosaraju's algorithm for SCC
    
    # But since each clause has exactly 2 literals, we can model as 2-SAT
    # For clause (a OR b), we add edges: (~a -> b) and (~b -> a)
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        index += 2
        
        # Clause is (l1 OR l2)
        # This is equivalent to (~l1 -> l2) AND (~l2 -> l1)
        # In terms of our notation:
        # not l1 implies l2
        # not l2 implies l1
        
        # Node representation: 
        # For variable x (1-based): 
        #    x represents x=True (switch x is 1)
        #   -x represents x=False (switch x is 0)
        
        # (~l1 -> l2) : not l1 implies l2
        if l1 > 0:
            # not (x is 1) => x is 0, so -l1 -> l2
            adj[-l1].append(l2)
            rev_adj[l2].append(-l1)
        else:
            # l1 is negative, so l1 = -|l1|
            # not (x is 0) => x is 1, so -l1(=|l1|) -> l2
            adj[-l1].append(l2)
            rev_adj[l2].append(-l1)
            
        # (~l2 -> l1) : not l2 implies l1  
        if l2 > 0:
            # not (x is 1) => x is 0, so -l2 -> l1
            adj[-l2].append(l1)
            rev_adj[l1].append(-l2)
        else:
            # l2 is negative, so l2 = -|l2|
            # not (x is 0) => x is 1, so -l2(=|l2|) -> l1
            adj[-l2].append(l1)
            rev_adj[l1].append(-l2)
    
    # Now perform Kosaraju's algorithm to find strongly connected components
    visited = set()
    order = []
    
    def dfs1(u):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs1(v)
        order.append(u)
    
    # First DFS on original graph
    nodes = set(adj.keys()) | set(rev_adj.keys())
    for u in nodes:
        if u not in visited:
            dfs1(u)
    
    # Second DFS on transpose graph in reverse finish order
    visited.clear()
    scc = {}
    scc_id = [0]
    
    def dfs2(u, root):
        visited.add(u)
        scc[u] = root
        for v in rev_adj[u]:
            if v not in visited:
                dfs2(v, root)
    
    while order:
        u = order.pop()
        if u not in visited:
            dfs2(u, scc_id[0])
            scc_id[0] += 1
    
    # Check for contradiction: variable and its negation in same SCC
    for i in range(1, n+1):
        if i in scc and -i in scc and scc[i] == scc[-i]:
            print("NO")
            return
    
    # Assign values based on SCC topological order
    # Variables in later finishing SCCs should be true
    assignment = {}
    
    # Process SCCs in reverse topological order (by finish time in second DFS)
    # But we already have the component IDs from dfs2
    
    # Actually, let's reorganize: we want to process in topological order of SCC DAG
    # SCC with higher ID was finished later in the second DFS, so should be processed first
    
    # Let's just go through all variables and assign values
    for i in range(1, n+1):
        if i not in scc:
            # Not involved in any constraints, can be False
            assignment[i] = 0
        elif -i not in scc:
            # Only positive form appears, can be True
            assignment[i] = 1
        elif scc[i] > scc[-i]:
            # Positive literal's SCC finishes later, so make it True
            assignment[i] = 1
        else:
            # Negative literal's SCC finishes later or equal, make it False
            assignment[i] = 0
    
    print("YES")
    result = []
    for i in range(1, n+1):
        result.append(str(assignment[i]))
    print(" ".join(result))

if __name__ == "__main__":
    main()