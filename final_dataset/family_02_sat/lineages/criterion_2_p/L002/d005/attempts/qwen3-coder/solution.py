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
    
    constraints = []
    idx = 2
    for _ in range(m):
        c1 = int(data[idx])
        c2 = int(data[idx+1])
        idx += 2
        constraints.append((c1, c2))
    
    # For each constraint c1, c2:
    # c1 * p[|c1|] + c2 * p[|c2|] > -(|c1| + |c2|)
    # Since p[i] = 2*s[i] - 1, we have p[i] in {-1, 1}
    # Let's rewrite the constraint in terms of p values
    # c1 * p[|c1|] + c2 * p[|c2|] > -(|c1| + |c2|)
    # This is a linear constraint on p[|c1|] and p[|c2|]
    
    # We can model this as a 2-SAT problem
    # Each machine i has two variables: p[i] = 1 (s[i]=1) or p[i] = -1 (s[i]=0)
    # For each constraint, we determine which combinations of p[|c1|], p[|c2|] satisfy it
    # Then we build implication graph for 2-SAT
    
    # Let's define variables:
    # For machine i (1-based), 
    # var i represents p[i] = 1 (i.e., s[i] = 1)
    # var -i represents p[i] = -1 (i.e., s[i] = 0)
    
    # To make indexing easier, we'll map variable (1 to n and -1 to -n) to 0 to 2n-1
    def var_to_index(v):
        # v is from -n to n, excluding 0
        # map 1..n to 0..n-1 and -1..-n to n..2n-1
        if v > 0:
            return v - 1
        else:
            return (-v - 1) + n
    
    # For each constraint c1, c2, we enumerate all 4 combinations of p[|c1|], p[|c2|]
    # and see which ones satisfy the constraint
    # The constraint is: c1 * p[|c1|] + c2 * p[|c2|] > -(|c1| + |c2|)
    
    from collections import defaultdict
    
    # Build implication graph
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for c1, c2 in constraints:
        m1 = abs(c1)
        m2 = abs(c2)
        
        # Check all 4 combinations
        valid = []
        for p1 in [-1, 1]:
            for p2 in [-1, 1]:
                if c1 * p1 + c2 * p2 > -(abs(c1) + abs(c2)):
                    valid.append((p1, p2))
        
        # For each invalid combination, we add implications
        # If (p1, p2) is invalid, then we must have !p1 OR !p2
        # Which means if p1 is true, then !p2 must be true, and if p2 is true, then !p1 must be true
        for p1 in [-1, 1]:
            for p2 in [-1, 1]:
                if (p1, p2) not in valid:
                    # This combination is not allowed
                    # If p[|c1|] = p1, then p[|c2|] != p2
                    # If p[|c2|] = p2, then p[|c1|] != p1
                    
                    # p[|c1|] = p1 is represented by variable (p1*m1)
                    # p[|c2|] = p2 is represented by variable (p2*m2)
                    # !p[|c1|] = p1 is represented by variable (-(p1*m1))
                    # !p[|c2|] = p2 is represented by variable (-(p2*m2))
                    
                    v1 = p1 * m1
                    v2 = p2 * m2
                    
                    # If v1 is true, then v2 must be false => !v1 OR !v2
                    # This is equivalent to v1 => !v2 and v2 => !v1
                    graph[var_to_index(v1)].append(var_to_index(-v2))
                    graph[var_to_index(v2)].append(var_to_index(-v1))
                    
                    reverse_graph[var_to_index(-v2)].append(var_to_index(v1))
                    reverse_graph[var_to_index(-v1)].append(var_to_index(v2))
    
    # Now we do strongly connected components to check 2-SAT satisfiability
    # Kosaraju's algorithm
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
    
    # Second DFS on reverse graph
    visited = [False] * (2 * n)
    scc_id = [-1] * (2 * n)
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in reverse_graph[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
    
    # Check if for each variable, variable and its negation are in different SCCs
    for i in range(n):
        if scc_id[i] == scc_id[i + n]:
            print("NO")
            return
    
    # Assign values
    # Variables in later SCCs in topological order are assigned True
    # For each variable, if its SCC comes after the SCC of its negation, assign True
    assignment = [False] * n
    for i in range(n):
        if scc_id[i] > scc_id[i + n]:
            assignment[i] = True  # p[i+1] = 1 => s[i+1] = 1
        else:
            assignment[i] = False # p[i+1] = -1 => s[i+1] = 0
    
    print("YES")
    print(" ".join(str(int(b)) for b in assignment))

if __name__ == "__main__":
    main()