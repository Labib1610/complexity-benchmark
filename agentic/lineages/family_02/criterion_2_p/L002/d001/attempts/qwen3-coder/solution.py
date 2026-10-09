import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # If no interlocks, any configuration works
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build implication graph for 2-SAT
    # Variables: 0..n-1 for mode 1, n..2n-1 for mode 0
    # var[i] = i (mode 1), var[i+n] = i (mode 0)
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    def add_implication(x, y):
        adj[x].append(y)
        rev_adj[y].append(x)
    
    def negate(x):
        if x < n:
            return x + n
        else:
            return x - n
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # l1 and l2 are literals
        # An interlock triggers if BOTH literals are FALSE
        # So we need at least one of them to be TRUE
        # This is equivalent to (l1 OR l2)
        # Which translates to (~l1 -> l2) and (~l2 -> l1)
        
        # Convert to variable indices
        if l1 > 0:
            var1 = l1 - 1  # machine l1 in mode 1
        else:
            var1 = (abs(l1) - 1) + n  # machine |l1| in mode 0
            
        if l2 > 0:
            var2 = l2 - 1  # machine l2 in mode 1
        else:
            var2 = (abs(l2) - 1) + n  # machine |l2| in mode 0
            
        # Add clauses: (~var1 -> var2) and (~var2 -> var1)
        add_implication(negate(var1), var2)
        add_implication(negate(var2), var1)
    
    # Kosaraju's algorithm for SCC
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
    
    # Reverse graph DFS
    visited = [False] * (2 * n)
    components = [-1] * (2 * n)
    component_id = 0
    
    def dfs2(u):
        visited[u] = True
        components[u] = component_id
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    for u in reversed(order):
        if not visited[u]:
            dfs2(u)
            component_id += 1
    
    # Check satisfiability
    for i in range(n):
        if components[i] == components[i + n]:
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    assignment = [False] * n
    comp_order = [(components[i], i) for i in range(2 * n)]
    comp_order.sort(reverse=True)
    
    assigned = [False] * n
    
    for _, var in comp_order:
        idx = var % n
        if not assigned[idx]:
            if var < n:  # mode 1
                assignment[idx] = False  # mode 0
            else:  # mode 0
                assignment[idx] = True   # mode 1
            assigned[idx] = True
    
    print("YES")
    result = []
    for i in range(n):
        if assignment[i]:
            result.append("1")
        else:
            result.append("0")
    print(" ".join(result))

if __name__ == "__main__":
    main()