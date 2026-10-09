import sys
from collections import defaultdict, deque

# Increase recursion depth just in case for DFS
sys.setrecursionlimit(500000)

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # Adjacency list: adj[u] contains list of (v, type_constraint)
    # Constraint type t:
    # t = 0: u and v must be different
    # t = 1: u and v must be same
    adj = [[] for _ in range(n + 1)]

    # Parse filters
    for _ in range(m):
        raw_a = int(next(it))
        raw_b = int(next(it))
        
        u = abs(raw_a)
        v = abs(raw_b)
        
        # Determine targets
        # target = 1 if positive, 0 if negative
        # Filter condition: |freq_u - target_u| + |freq_v - target_v| < 2
        # This is equivalent to: NOT(|freq_u - target_u| == 1 AND |freq_v - target_v| == 1)
        # Which simplifies to:
        # If target_u == target_v:
        #   NOT(freq_u != target_u AND freq_v != target_v) => NOT(freq_u == freq_v_inv AND freq_v == freq_u_inv)
        #   => freq_u == freq_v
        # If target_u != target_v:
        #   NOT(freq_u != target_u AND freq_v == target_u) => NOT(freq_u == freq_v_inv AND freq_v == freq_u)
        #   => freq_u != freq_v
        
        target_u = 1 if raw_a > 0 else 0
        target_v = 1 if raw_b > 0 else 0
        
        constraint_type = 1 if target_u == target_v else 0
        
        adj[u].append((v, constraint_type))
        adj[v].append((u, constraint_type))

    # Variables for 2-SAT
    # Graph has 2*n nodes: 1..n (false), n+1..2n (true)
    # For node u: False/u -> u, True/u -> u + n
    N_total = 2 * n
    
    adj_sat = [[] for _ in range(N_total + 1)]
    rev_adj_sat = [[] for _ in range(N_total + 1)]
    
    for u in range(1, n + 1):
        for v, typ in adj[u]:
            # typ 1: same, typ 0: diff
            # u -> v false
            # v -> u false
            # u+n -> v+n
            # v+n -> u+n
            
            if typ == 1: # u == v
                # u -> v, v -> u, ~u -> ~v, ~v -> ~u
                adj_sat[u].append(v)
                rev_adj_sat[v].append(u)
                adj_sat[v].append(u)
                rev_adj_sat[u].append(v)
                
                adj_sat[u + n].append(v + n)
                rev_adj_sat[v + n].append(u + n)
                adj_sat[v + n].append(u + n)
                rev_adj_sat[u + n].append(v + n)
            else: # u != v
                # u -> ~v, v -> ~u, ~u -> v, ~v -> u
                adj_sat[u].append(v + n)
                rev_adj_sat[v + n].append(u)
                adj_sat[v].append(u + n)
                rev_adj_sat[u + n].append(v)
                
                adj_sat[u + n].append(v)
                rev_adj_sat[v].append(u + n)
                adj_sat[v + n].append(u)
                rev_adj_sat[u].append(v + n)

    # Kosaraju's Algorithm
    visited = [False] * (N_total + 1)
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == 0:
                if visited[node]:
                    continue
                visited[node] = True
            
            pushed = False
            while idx < len(adj_sat[node]):
                neighbor = adj_sat[node][idx]
                idx += 1
                if not visited[neighbor]:
                    stack.append((node, idx))
                    stack.append((neighbor, 0))
                    pushed = True
                    break
            if not pushed:
                order.append(node)

    for i in range(1, N_total + 1):
        if not visited[i]:
            dfs1(i)

    comp_id = [-1] * (N_total + 1)
    current_comp = 0
    
    # We iterate in reverse order of finishing times
    for u in reversed(order):
        if comp_id[u] != -1:
            continue
        # DFS on reversed graph
        current_comp += 1
        stack = [u]
        comp_id[u] = current_comp
        while stack:
            node = stack.pop()
            for neighbor in rev_adj_sat[node]:
                if comp_id[neighbor] == -1:
                    comp_id[neighbor] = current_comp
                    stack.append(neighbor)

    # Check satisfiability and assign values
    # If comp_id[u] == comp_id[u+n], then contradiction (u and ~u in same SCC)
    # Value is True if comp_id[u+n] > comp_id[u] (topologically later SCC means true in assignment)
    
    result = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if comp_id[i] == comp_id[i + n]:
            possible = False
            break
        if comp_id[i + n] > comp_id[i]:
            result[i] = 1
        else:
            result[i] = 0
            
    if not possible:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, result[1:])) + "\n")

solve()