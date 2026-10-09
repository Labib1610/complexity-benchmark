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
    
    edges = []
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        edges.append((l1, l2))
        index += 2

    # Create implication graph for 2-SAT
    # Variables: 0 to n-1 (for x0 to xn-1), n to 2n-1 (for not x0 to not xn-1)
    # But we'll use 0 to n-1 for x_i = 0 (OFF), n to 2n-1 for x_i = 1 (ON)
    # Actually, let's think differently.
    # For each variable x_i, we have two nodes: 2*i (x_i = False) and 2*i+1 (x_i = True)
    # But in our case, x_i is 1-based index from 1 to n.
    # Let's map x_i (1-based) to node 2*(i-1) (x_i = False) and 2*(i-1)+1 (x_i = True)
    
    # Each constraint l1 l2 means:
    # V(|l1|)*sgn(l1) + V(|l2|)*sgn(l2) >= 0
    # Where V(i) = 1 if x_i is True (ON), -1 if x_i is False (OFF)
    # So: (1 if x_|l1| else -1)*sgn(l1) + (1 if x_|l2| else -1)*sgn(l2) >= 0
    
    # Let's enumerate all 4 cases for the two variables:
    # x_|l1| = 0, x_|l2| = 0: (-1)*sgn(l1) + (-1)*sgn(l2) = -sgn(l1) - sgn(l2) >= 0 ?
    # x_|l1| = 0, x_|l2| = 1: (-1)*sgn(l1) + (1)*sgn(l2) = -sgn(l1) + sgn(l2) >= 0 ?
    # x_|l1| = 1, x_|l2| = 0: (1)*sgn(l1) + (-1)*sgn(l2) = sgn(l1) - sgn(l2) >= 0 ?
    # x_|l1| = 1, x_|l2| = 1: (1)*sgn(l1) + (1)*sgn(l2) = sgn(l1) + sgn(l2) >= 0 ?
    
    # The forbidden assignments are those where the inequality is false.
    # We'll build a 2-SAT instance: for each forbidden assignment, we add a clause that prevents it.
    
    # Let's map variable i (1-based) to index i-1 in 0-based arrays.
    # For variable i (1-based), node 2*(i-1) represents (x_i = False) and 2*(i-1)+1 represents (x_i = True)
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    def add_clause(a, b):
        # This means (a OR b). We add edges (~a -> b) and (~b -> a)
        # Node a is a literal. If a = 2k, it's (x_{k+1} = False). If a = 2k+1, it's (x_{k+1} = True)
        # ~a = a^1
        adj[a^1].append(b)
        adj[b^1].append(a)
        rev_adj[b].append(a^1)
        rev_adj[a].append(b^1)
    
    for l1, l2 in edges:
        i1 = abs(l1)
        i2 = abs(l2)
        s1 = 1 if l1 > 0 else -1
        s2 = 1 if l2 > 0 else -1
        
        # Check all 4 assignments
        # x_i1 = 0 (OFF), x_i2 = 0 (OFF)
        val = -s1 - s2
        if val < 0:
            # This assignment is forbidden: x_i1=False AND x_i2=False
            # We need to add clause: NOT(x_i1=False) OR NOT(x_i2=False)
            # Which is: (x_i1=True) OR (x_i2=True)
            # Node for x_i1=True is 2*(i1-1)+1
            # Node for x_i2=True is 2*(i2-1)+1
            add_clause(2*(i1-1)+1, 2*(i2-1)+1)
        
        # x_i1 = 0 (OFF), x_i2 = 1 (ON)
        val = -s1 + s2
        if val < 0:
            # This assignment is forbidden: x_i1=False AND x_i2=True
            # Clause: (x_i1=True) OR (x_i2=False)
            # Node for x_i1=True is 2*(i1-1)+1
            # Node for x_i2=False is 2*(i2-1)
            add_clause(2*(i1-1)+1, 2*(i2-1))
            
        # x_i1 = 1 (ON), x_i2 = 0 (OFF)
        val = s1 - s2
        if val < 0:
            # This assignment is forbidden: x_i1=True AND x_i2=False
            # Clause: (x_i1=False) OR (x_i2=True)
            # Node for x_i1=False is 2*(i1-1)
            # Node for x_i2=True is 2*(i2-1)+1
            add_clause(2*(i1-1), 2*(i2-1)+1)
            
        # x_i1 = 1 (ON), x_i2 = 1 (ON)
        val = s1 + s2
        if val < 0:
            # This assignment is forbidden: x_i1=True AND x_i2=True
            # Clause: (x_i1=False) OR (x_i2=False)
            # Node for x_i1=False is 2*(i1-1)
            # Node for x_i2=False is 2*(i2-1)
            add_clause(2*(i1-1), 2*(i2-1))
    
    # Now we do Kosaraju's algorithm to check for contradictions
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
    
    # Second DFS on reverse graph
    visited = [False] * (2 * n)
    components = [-1] * (2 * n)
    comp_num = 0
    
    def dfs2(u):
        visited[u] = True
        components[u] = comp_num
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            comp_num += 1
    
    # Check for contradictions
    for i in range(n):
        if components[2*i] == components[2*i+1]:
            print("NO")
            return
    
    # Assign values
    assignment = [-1] * n
    comp_to_value = [-1] * comp_num
    
    # Process components in reverse topological order
    # We can process them in the order of component numbers (since Kosaraju gives reverse topological)
    for i in range(2*n):
        c = components[i]
        if comp_to_value[c] == -1:
            # If not set yet
            var_index = i // 2
            is_true = i % 2
            # The component containing the positive literal should be assigned True
            # if there's no conflict. But we need to be more careful.
            # Actually, in Kosaraju, later components in the order are "earlier" in the toposort.
            # So if we process in order of component number, and assign the first literal we see
            # in a component to False, and its negation to True, we might get conflicts.
            # Better approach: for each variable, if comp(x_i=False) > comp(x_i=True) in toposort,
            # then x_i=False is reachable after x_i=True, so we should set x_i=True.
            # Since components are numbered in reverse topological order by Kosaraju,
            # higher component number means earlier in the original graph's topological order.
            # So if components[2*i] > components[2*i+1], we set x_i = False.
            # Wait, let's think again.
            # components list gives the component number for each node.
            # Kosaraju's second pass visits in reverse post-order of the first DFS.
            # So the component numbers are assigned in a way that if there's an edge from
            # component A to component B, then A's number < B's number.
            # So if components[2*i] < components[2*i+1], it means x_i=False is in a component
            # that can reach x_i=True's component, so we should set x_i=True.
            # Actually, the standard way:
            # If comp(x_i) appears later in the topo order than comp(not x_i), set x_i = True.
            # In Kosaraju, components are numbered in the order they finish in the second DFS,
            # which is reverse topological order.
            # So if components[2*i] < components[2*i+1], then not x_i is processed before x_i,
            # meaning x_i should be True.
            pass
    
    # Simpler: for each variable, check which of its literals is in a later component
    for i in range(n):
        if components[2*i] > components[2*i+1]:
            assignment[i] = 0  # x_i = False (OFF)
        else:
            assignment[i] = 1  # x_i = True (ON)
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()