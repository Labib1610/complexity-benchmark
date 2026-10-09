import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    # 2*n nodes: node 2*i = x_i (switch i is ON), node 2*i+1 = ~x_i (switch i is OFF)
    # Actually let's use: node 2*i = x_i is True, node 2*i+1 = x_i is False
    # x_i = "switch i is ON"
    
    adj = [[] for _ in range(2 * n)]
    radj = [[] for _ in range(2 * n)]
    
    def add_imp(u, v):
        adj[u].append(v)
        radj[v].append(u)
    
    def add_clause(u, v):
        # u OR v => ~u -> v, ~v -> u
        add_imp(u ^ 1, v)
        add_imp(v ^ 1, u)
    
    for _ in range(m):
        l1 = int(input_data[idx]); idx += 1
        l2 = int(input_data[idx]); idx += 1
        
        a = abs(l1) - 1  # 0-indexed
        b = abs(l2) - 1
        
        e_a = 1 if l1 > 0 else 0
        e_b = 1 if l2 > 0 else 0
        
        # x_a == e_a: if e_a=1 then x_a, else ~x_a
        # node for "s_a == e_a": 2*a if e_a=1, 2*a+1 if e_a=0
        u = 2 * a if e_a == 1 else 2 * a + 1
        v = 2 * b if e_b == 1 else 2 * b + 1
        
        add_clause(u, v)
    
    # Kosaraju's SCC
    visited = [False] * (2 * n)
    order = []
    
    sys.setrecursionlimit(300000)
    
    def dfs1(v):
        stack = [(v, 0)]
        visited[v] = True
        while stack:
            node, i = stack[-1]
            if i < len(adj[node]):
                stack[-1] = (node, i + 1)
                nxt = adj[node][i]
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, 0))
            else:
                order.append(node)
                stack.pop()
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1] * (2 * n)
    
    def dfs2(v, c):
        stack = [v]
        comp[v] = c
        while stack:
            node = stack.pop()
            for nxt in radj[node]:
                if comp[nxt] == -1:
                    comp[nxt] = c
                    stack.append(nxt)
    
    c = 0
    for i in reversed(order):
        if comp[i] == -1:
            dfs2(i, c)
            c += 1
    
    # Check satisfiability
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
    
    # Assign values: x_i = True if comp[2*i] > comp[2*i+1] (later in topological order)
    result = []
    for i in range(n):
        if comp[2 * i] > comp[2 * i + 1]:
            result.append(1)
        else:
            result.append(0)
    
    print("YES")
    print(" ".join(map(str, result)))

solve()