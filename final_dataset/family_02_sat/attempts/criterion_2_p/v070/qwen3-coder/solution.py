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
        print(" ".join(["1"] * n))
        return
    
    clauses = []
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        clauses.append((l1, l2))
        index += 2
    
    # Create implication graph for 2-SAT
    # Variables: for each channel i (1-based), 
    # var i represents high-gain (value 1)
    # var -i represents low-gain (value 0)
    # We'll use 0-based indexing internally for variables
    # var i (0-based) corresponds to channel i+1 high-gain
    # var i+n (0-based) corresponds to channel i+1 low-gain
    
    # But actually, let's think differently.
    # For each channel i (1-based):
    # variable i-1 represents high-gain (True) 
    # variable (i-1)+n represents low-gain (True)
    # But this is getting confusing.
    
    # Let's use a clearer approach:
    # For channel i (1-based):
    # variable i-1 (0-based index) = True means high-gain
    # variable (i-1)+n = True means low-gain
    # But we need to ensure exactly one is true per channel.
    # This makes it more complex than standard 2-SAT.
    
    # Let's reconsider the problem.
    # Each protocol says: if not A then B, and if not B then A
    # Which is equivalent to: A OR B
    # So each clause is a disjunction.
    
    # For a clause (a b):
    # if a>0: a means channel |a| is high-gain
    # if a<0: -a means channel |a| is low-gain
    # Same for b
    
    # So the clause means: (channel |a| in mode a>0 ? high : low) OR (channel |b| in mode b>0 ? high : low)
    
    # This is a 2-SAT problem.
    # Variables: x_i for i=1..n meaning channel i is high-gain
    # Not x_i means channel i is low-gain
    
    # For each clause (a b):
    # If a>0 and b>0: x_a OR x_b
    # If a>0 and b<0: x_a OR (not x_|b|)
    # If a<0 and b>0: (not x_|a|) OR x_b
    # If a<0 and b<0: (not x_|a|) OR (not x_|b|)
    
    # In implication form (for 2-SAT solver):
    # (not a) => b  and (not b) => a
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for l1, l2 in clauses:
        # Convert to 0-based variable indices
        # var i (0..n-1) represents channel i+1 is high-gain
        # var i+n (n..2n-1) represents channel i+1 is low-gain
        
        # But we don't need both. We can work with just x_i and not x_i
        # Let's use standard 2-SAT notation:
        # Variable i (0-based) corresponds to channel i+1 being high-gain
        # not i corresponds to channel i+1 being low-gain
        
        # Given clause (l1 l2), which means "mode of l1 OR mode of l2"
        # In terms of boolean variables:
        v1 = abs(l1) - 1  # 0-based index
        neg1 = l1 < 0     # True if we're talking about low-gain
        
        v2 = abs(l2) - 1
        neg2 = l2 < 0
        
        # The clause is: (neg1 ? not x[v1] : x[v1]) OR (neg2 ? not x[v2] : x[v2])
        # Which is equivalent to: (not (neg1 ? not x[v1] : x[v1])) => (neg2 ? not x[v2] : x[v2])
        # Simplifying:
        # If neg1=True (low-gain for channel v1+1), then clause is (not x[v1]) OR (...)
        # Which gives us: x[v1] => (...)
        # If neg1=False (high-gain for channel v1+1), then clause is x[v1] OR (...)
        # Which gives us: (not x[v1]) => (...)
        
        # Similarly for v2.
        
        # So we get two implications:
        # not (neg1 ? not x[v1] : x[v1]) => (neg2 ? not x[v2] : x[v2])
        # not (neg2 ? not x[v2] : x[v2]) => (neg1 ? not x[v1] : x[v1])
        
        # Let's compute what these mean:
        # First implication:
        # LHS: not (neg1 ? not x[v1] : x[v1]) = (neg1 ? x[v1] : not x[v1]) = (neg1 == False ? not x[v1] : x[v1])
        # RHS: (neg2 ? not x[v2] : x[v2])
        # So if neg1==False: not x[v1] => (neg2 ? not x[v2] : x[v2])
        #    if neg1==True:  x[v1] => (neg2 ? not x[v2] : x[v2])
        
        # Second implication:
        # LHS: not (neg2 ? not x[v2] : x[v2]) = (neg2 ? x[v2] : not x[v2]) = (neg2 == False ? not x[v2] : x[v2])
        # RHS: (neg1 ? not x[v1] : x[v1])
        # So if neg2==False: not x[v2] => (neg1 ? not x[v1] : x[v1])
        #    if neg2==True:  x[v2] => (neg1 ? not x[v1] : x[v1])
        
        # Adding edges to implication graph:
        if not neg1:  # l1 represents high-gain for channel v1+1, so x[v1]
            # not x[v1] => (neg2 ? not x[v2] : x[v2])
            # This is: not x[v1] => x[v2] if not neg2, else not x[v1] => not x[v2]
            if not neg2:
                adj[v1 + n].append(v2)      # not x[v1] => x[v2]
                rev_adj[v2].append(v1 + n)
            else:
                adj[v1 + n].append(v2 + n)  # not x[v1] => not x[v2]
                rev_adj[v2 + n].append(v1 + n)
        else:  # l1 represents low-gain for channel v1+1, so not x[v1]
            # x[v1] => (neg2 ? not x[v2] : x[v2])
            if not neg2:
                adj[v1].append(v2)          # x[v1] => x[v2]
                rev_adj[v2].append(v1)
            else:
                adj[v1].append(v2 + n)      # x[v1] => not x[v2]
                rev_adj[v2 + n].append(v1)
                
        if not neg2:  # l2 represents high-gain for channel v2+1, so x[v2]
            # not x[v2] => (neg1 ? not x[v1] : x[v1])
            if not neg1:
                adj[v2 + n].append(v1)      # not x[v2] => x[v1]
                rev_adj[v1].append(v2 + n)
            else:
                adj[v2 + n].append(v1 + n)  # not x[v2] => not x[v1]
                rev_adj[v1 + n].append(v2 + n)
        else:  # l2 represents low-gain for channel v2+1, so not x[v2]
            # x[v2] => (neg1 ? not x[v1] : x[v1])
            if not neg1:
                adj[v2].append(v1)          # x[v2] => x[v1]
                rev_adj[v1].append(v2)
            else:
                adj[v2].append(v1 + n)      # x[v2] => not x[v1]
                rev_adj[v1 + n].append(v2)
    
    # Now run Kosaraju's algorithm for 2-SAT
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    # Build SCCs
    visited = [False] * (2 * n)
    scc_id = [-1] * (2 * n)
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
    
    # Check if satisfiable
    for i in range(n):
        if scc_id[i] == scc_id[i + n]:
            print("NO")
            return
    
    # Assign values
    assignment = [False] * n
    # Process SCCs in reverse topological order
    scc_order = [[] for _ in range(scc_count)]
    for i in range(2 * n):
        scc_order[scc_id[i]].append(i)
    
    assigned = [False] * n
    
    # Go through SCCs in reverse order
    for component in reversed(scc_order):
        for node in component:
            if node < n:  # x_i variable
                if not assigned[node]:
                    assignment[node] = False  # Since we're setting false literals first
            else:  # not x_i variable (node = i + n)
                idx = node - n
                if not assigned[idx]:
                    assignment[idx] = True
    
    print("YES")
    print(" ".join("1" if assignment[i] else "0" for i in range(n)))

if __name__ == "__main__":
    main()