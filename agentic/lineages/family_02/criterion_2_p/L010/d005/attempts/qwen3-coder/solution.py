import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each variable (transmitter), we'll have two nodes: x and ~x (x and not x)
    # We'll build a graph for 2-SAT
    # Variables: for transmitter i (1-based), we use:
    # node i*2 for frequency 0
    # node i*2+1 for frequency 1
    # But in 2-SAT solver, we usually use i*2 for variable i being False, i*2+1 for True
    # Let's map transmitter i (1-based) to variable i-1 (0-based)
    # var i-1 = False means freq 0, True means freq 1
    
    # We need to build implication graph for 2-SAT
    # Each clause (filter) is of form (a or b) where a and b are literals
    # Literal: +i means variable i-1 is True, -i means variable i-1 is False
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # Transmitter |l1|, sign indicates target freq
        # Positive: target 1, Negative: target 0
        # Deviation for a connection = |actual_freq - target_freq|
        # For filter to be stable: sum of two deviations < 2
        # Each deviation is 0 or 1, so sum < 2 means sum is 0 or 1
        # Sum = 0: both connections have 0 deviation
        # Sum = 1: one connection has 0 deviation, other has 1
        
        # Let's think in terms of forbidden assignments:
        # Sum >= 2 means both deviations are 1
        # For l1: if l1>0, target=1, so deviation=1 if actual=0
        #         if l1<0, target=0, so deviation=1 if actual=1
        # For l2: if l2>0, target=1, so deviation=1 if actual=0
        #         if l2<0, target=0, so deviation=1 if actual=1
        
        # So forbidden case is:
        # (actual[|l1|] = 0 if l1>0 else 1) AND (actual[|l2|] = 0 if l2>0 else 1)
        # Which is a forbidden assignment to the pair of variables
        
        # Let v1 = |l1|-1, v2 = |l2|-1 (0-based indices)
        # f1 = 0 if l1>0 else 1  (forbidden value for v1)
        # f2 = 0 if l2>0 else 1  (forbidden value for v2)
        
        v1 = abs(l1) - 1
        v2 = abs(l2) - 1
        f1 = 0 if l1 > 0 else 1
        f2 = 0 if l2 > 0 else 1
        
        # Forbidden assignment: v1=f1 AND v2=f2
        # This corresponds to clause: (v1 != f1 OR v2 != f2)
        # Which is: (v1 = not f1 OR v2 = not f2)
        
        # In 2-SAT, we add implications:
        # If v1=f1 AND v2=f2 is forbidden, then:
        # v1=f1 -> v2 != f2
        # v2=f2 -> v1 != f1
        
        # Node IDs: for variable i: node 2*i is (i=False), node 2*i+1 is (i=True)
        # v1=f1 is node 2*v1 + f1
        # v1!=f1 is node 2*v1 + (1-f1)
        # v2=f2 is node 2*v2 + f2
        # v2!=f2 is node 2*v2 + (1-f2)
        
        # Implication: v1=f1 -> v2!=f2  means  add edge from (2*v1+f1) to (2*v2+(1-f2))
        # Implication: v2=f2 -> v1!=f1  means  add edge from (2*v2+f2) to (2*v1+(1-f1))
        
        adj[2*v1 + f1].append(2*v2 + (1 - f2))
        adj[2*v2 + f2].append(2*v1 + (1 - f1))
        rev_adj[2*v2 + (1 - f2)].append(2*v1 + f1)
        rev_adj[2*v1 + (1 - f1)].append(2*v2 + f2)
    
    # Now we do 2-SAT using Kosaraju's algorithm
    # 1. Get finishing order from DFS on original graph
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
    
    # 2. Transpose graph and do DFS in reverse order
    visited = [False] * (2 * n)
    components = [-1] * (2 * n)
    comp_id = 0
    
    def dfs2(u):
        visited[u] = True
        components[u] = comp_id
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            comp_id += 1
    
    # 3. Check if for every variable, false and true are in different SCCs
    for i in range(n):
        if components[2*i] == components[2*i + 1]:
            print("NO")
            return
    
    # 4. Assign values: if component of True node is later than False node, set to True
    assignment = [0] * n
    for i in range(n):
        if components[2*i] < components[2*i + 1]:
            assignment[i] = 1
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()