import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [[] for _ in range(n+1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Define matrices
    M1 = [[0, 1], [0, 0]]
    M2 = [[0, 0], [1, 0]]
    Z = [[0, 0], [0, 0]]
    
    def mat_mult(A, B):
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]
    
    def is_zero_matrix(mat):
        return mat == Z
    
    # Check if assignment is valid
    def check_valid(s):
        for u, v in edges:
            if s[u-1] == 1:
                Mu = M1
            else:
                Mu = M2
            if s[v-1] == 1:
                Mv = M1
            else:
                Mv = M2
            prod1 = mat_mult(Mu, Mv)
            prod2 = mat_mult(Mv, Mu)
            if is_zero_matrix(prod1) and is_zero_matrix(prod2):
                return False
        return True
    
    # Precompute forbidden pairs
    forbidden = set()
    for u, v in edges:
        for mode_u in [1, 2]:
            for mode_v in [1, 2]:
                if mode_u == 1:
                    Mu = M1
                else:
                    Mu = M2
                if mode_v == 1:
                    Mv = M1
                else:
                    Mv = M2
                prod1 = mat_mult(Mu, Mv)
                prod2 = mat_mult(Mv, Mu)
                if is_zero_matrix(prod1) and is_zero_matrix(prod2):
                    forbidden.add((u, mode_u, v, mode_v))
                    forbidden.add((v, mode_v, u, mode_u))
    
    # Build implication graph for 2-SAT
    # Variables: var i (0-based) represents node i+1 mode 1, var i+n represents node i+1 mode 2
    # Literals: 2*i for mode 1, 2*i+1 for mode 2
    def var_mode1(i):
        return 2 * i
    def var_mode2(i):
        return 2 * i + 1
    def negate(lit):
        if lit % 2 == 0:
            return lit + 1
        else:
            return lit - 1
    
    # Number of variables
    num_vars = 2 * n
    # Adjacency list for implication graph
    imp_graph = [[] for _ in range(2 * num_vars)]
    
    # Add constraints: each node must have exactly one mode
    for i in range(n):
        # (mode1 OR mode2) AND (NOT mode1 OR NOT mode2)
        # This is equivalent to (NOT mode1 -> mode2) AND (NOT mode2 -> mode1)
        imp_graph[negate(var_mode1(i))].append(var_mode2(i))
        imp_graph[negate(var_mode2(i))].append(var_mode1(i))
    
    # Add constraints from forbidden pairs
    for u, v in edges:
        u_idx = u - 1
        v_idx = v - 1
        # Check all combinations
        for mode_u in [1, 2]:
            for mode_v in [1, 2]:
                if (u, mode_u, v, mode_v) in forbidden:
                    # NOT (mode_u for u AND mode_v for v)
                    # Equivalent to (NOT mode_u for u OR NOT mode_v for v)
                    if mode_u == 1:
                        lit_u = var_mode1(u_idx)
                    else:
                        lit_u = var_mode2(u_idx)
                    if mode_v == 1:
                        lit_v = var_mode1(v_idx)
                    else:
                        lit_v = var_mode2(v_idx)
                    imp_graph[lit_u].append(negate(lit_v))
                    imp_graph[lit_v].append(negate(lit_u))
    
    # Kosaraju's algorithm for SCC
    def kosaraju(graph):
        n_nodes = len(graph)
        visited = [False] * n_nodes
        order = []
        
        def dfs1(u):
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    dfs1(v)
            order.append(u)
        
        for i in range(n_nodes):
            if not visited[i]:
                dfs1(i)
        
        # Transpose graph
        transposed = [[] for _ in range(n_nodes)]
        for u in range(n_nodes):
            for v in graph[u]:
                transposed[v].append(u)
        
        visited = [False] * n_nodes
        scc_id = [-1] * n_nodes
        scc_count = 0
        
        def dfs2(u, cid):
            visited[u] = True
            scc_id[u] = cid
            for v in transposed[u]:
                if not visited[v]:
                    dfs2(v, cid)
        
        while order:
            u = order.pop()
            if not visited[u]:
                dfs2(u, scc_count)
                scc_count += 1
        
        return scc_id
    
    scc_ids = kosaraju(imp_graph)
    
    # Check for conflicts
    for i in range(n):
        if scc_ids[var_mode1(i)] == scc_ids[var_mode2(i)]:
            print("NO")
            return
    
    # Assign values: prefer mode 1 (lexicographically smallest)
    # Process SCCs in reverse topological order
    # We can just process variables in the order where we assign the earliest possible value
    
    assignment = [-1] * n
    # For each variable, if not assigned yet, assign based on SCC ids
    # In 2-SAT, if SCC_id[lit] > SCC_id[negate(lit)], then lit is true
    for i in range(n):
        id1 = scc_ids[var_mode1(i)]
        id2 = scc_ids[var_mode2(i)]
        if id1 > id2:
            assignment[i] = 1
        else:
            assignment[i] = 2
    
    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    main()