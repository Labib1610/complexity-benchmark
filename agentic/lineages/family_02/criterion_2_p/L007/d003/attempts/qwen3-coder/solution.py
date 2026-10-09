import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # If no protocols, any configuration works
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each protocol (l1, l2), we must NOT have both yields negative
    # Let's think in terms of boolean satisfiability
    # Each zone i has a boolean variable x_i (True = state 1, False = state 0)
    
    # For a zone i:
    # If l = +i, yield = +i if x_i else -i
    # If l = -i, yield = -i if x_i else +i
    
    # So for a literal l:
    # yield(l) < 0 iff (l > 0 and not x_{|l|}) or (l < 0 and x_{|l|})
    
    # For a protocol (l1, l2), we must avoid:
    # yield(l1) < 0 AND yield(l2) < 0
    
    # This is equivalent to:
    # NOT(yield(l1) < 0) OR NOT(yield(l2) < 0)
    
    # Let's define for each literal l, when yield(l) < 0:
    # neg(l) = (l > 0 and not x_{|l|}) or (l < 0 and x_{|l|})
    # So NOT neg(l) = (l > 0 and x_{|l|}) or (l < 0 and not x_{|l|})
    
    # The constraint for protocol (l1,l2):
    # NOT neg(l1) OR NOT neg(l2)
    # Which is:
    # [(l1>0 and x_{|l1|}) or (l1<0 and not x_{|l1|})] OR 
    # [(l2>0 and x_{|l2|}) or (l2<0 and not x_{|l2|})]
    
    # This is a 2-CNF clause. We can build implication graph and check 2-SAT
    
    # Let's define variables:
    # For zone i (1-based), variable index is i-1 (0-based)
    # x[i] corresponds to zone i+1 being in state 1
    # not x[i] corresponds to zone i+1 being in state 0
    
    # In implication graph:
    # node 2*i represents x[i] (zone i+1 is state 1)
    # node 2*i+1 represents not x[i] (zone i+1 is state 0)
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    def add_clause(a, nota, b, notb):
        # Add clause (a or b) where:
        # a = x[var_a] if not nota else not x[var_a]
        # b = x[var_b] if not notb else not x[var_b]
        # This is equivalent to:
        # (not a) => b  and (not b) => a
        
        node_not_a = 2 * abs(a) - 2 + (1 if (a > 0) ^ (not nota) else 0)
        node_b = 2 * abs(b) - 2 + (1 if b < 0 else 0)
        
        node_not_b = 2 * abs(b) - 2 + (1 if (b > 0) ^ (notb) else 0)
        node_a = 2 * abs(a) - 2 + (1 if a < 0 else 0)
        
        adj[node_not_a].append(node_b)
        adj[node_not_b].append(node_a)
        rev_adj[node_b].append(node_not_a)
        rev_adj[node_a].append(node_not_b)
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # We want NOT (yield(l1) < 0 AND yield(l2) < 0)
        # Which is: NOT(yield(l1) < 0) OR NOT(yield(l2) < 0)
        
        # yield(l) < 0 is:
        # (l > 0 and not x_{|l|}) or (l < 0 and x_{|l|})
        
        # So NOT(yield(l) < 0) is:
        # (l > 0 and x_{|l|}) or (l < 0 and not x_{|l|})
        
        # The clause is:
        # [(l1>0 and x_{|l1|}) or (l1<0 and not x_{|l1|})] OR
        # [(l2>0 and x_{|l2|}) or (l2<0 and not x_{|l2|})]
        
        # This expands to 4 cases:
        # (l1>0 and x_{|l1|}) OR (l2>0 and x_{|l2|})
        # (l1>0 and x_{|l1|}) OR (l2<0 and not x_{|l2|})
        # (l1<0 and not x_{|l1|}) OR (l2>0 and x_{|l2|})
        # (l1<0 and not x_{|l1|}) OR (l2<0 and not x_{|l2|})
        
        # But it's easier to think as:
        # NOT [ (yield(l1) < 0) AND (yield(l2) < 0) ]
        # yield(l1) < 0 -> node1
        # yield(l2) < 0 -> node2
        # We add clause (NOT node1 OR NOT node2)
        # Which means: if node1 then NOT node2, and if node2 then NOT node1
        
        # Determine nodes for yield(l1) < 0 and yield(l2) < 0
        # For l: yield(l) < 0 iff:
        # if l > 0: not x_{|l|}
        # if l < 0: x_{|l|}
        
        var1 = abs(l1) - 1  # 0-based
        var2 = abs(l2) - 1  # 0-based
        
        # Node for yield(l1) < 0
        if l1 > 0:
            node1 = 2 * var1 + 1  # not x_{var1}
        else:
            node1 = 2 * var1      # x_{var1}
            
        # Node for yield(l2) < 0
        if l2 > 0:
            node2 = 2 * var2 + 1  # not x_{var2}
        else:
            node2 = 2 * var2      # x_{var2}
            
        # Add clause: NOT(node1 AND node2)
        # Which is: (NOT node1) OR (NOT node2)
        # Implications: node1 -> NOT node2, node2 -> NOT node1
        
        not_node1 = node1 ^ 1
        not_node2 = node2 ^ 1
        
        adj[node1].append(not_node2)
        adj[node2].append(not_node1)
        rev_adj[not_node2].append(node1)
        rev_adj[not_node1].append(node2)
    
    # Now run 2-SAT using Kosaraju's algorithm
    # First DFS on original graph to get finishing times
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
    
    # Second DFS on transpose graph in reverse order
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
    
    # Check if satisfiable
    for i in range(n):
        if components[2*i] == components[2*i + 1]:
            print("NO")
            return
    
    # Satisfiable, reconstruct solution
    assignment = [0] * n
    # Process components in reverse topological order
    # A variable is true if its positive node's component has higher number than negative node's
    
    for i in range(n):
        if components[2*i] > components[2*i + 1]:
            assignment[i] = 1
        else:
            assignment[i] = 0
            
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()