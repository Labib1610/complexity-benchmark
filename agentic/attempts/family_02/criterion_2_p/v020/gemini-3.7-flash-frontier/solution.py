import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    num_nodes = 2 * n
    
    # 2-SAT representation:
    # Drone i (1-indexed):
    # True (Heavy-Lift = 1) -> 2 * (i - 1)
    # False (Long-Range = 0) -> 2 * (i - 1) + 1
    
    # Read edges and build CSR
    head = [0] * num_nodes
    rev_head = [0] * num_nodes
    
    edges_u = []
    edges_v = []
    
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx+1])
        idx += 2
        
        u = 2 * (l1 - 1) if l1 > 0 else 2 * (-l1 - 1) + 1
        v = 2 * (l2 - 1) if l2 > 0 else 2 * (-l2 - 1) + 1
        
        # (~u -> v) and (~v -> u)
        not_u = u ^ 1
        not_v = v ^ 1
        
        edges_u.append(not_u)
        edges_v.append(v)
        edges_u.append(not_v)
        edges_v.append(u)
        
        head[not_u] += 1
        rev_head[v] += 1
        head[not_v] += 1
        rev_head[u] += 1

    num_edges = len(edges_u)
    
    # CSR for forward graph
    for i in range(num_nodes - 1):
        head[i + 1] += head[i]
    to = [0] * num_edges
    for i in range(num_edges - 1, -1, -1):
        u = edges_u[i]
        head[u] -= 1
        to[head[u]] = edges_v[i]
        
    # CSR for reverse graph
    for i in range(num_nodes - 1):
        rev_head[i + 1] += rev_head[i]
    rev_to = [0] * num_edges
    for i in range(num_edges - 1, -1, -1):
        v = edges_v[i]
        rev_head[v] -= 1
        rev_to[rev_head[v]] = edges_u[i]

    # Kosaraju Step 1: Post-order on G
    order = []
    visited = [False] * num_nodes
    stack = []
    edge_idx = [0] * num_nodes
    for start in range(num_nodes):
        if visited[start]:
            continue
        visited[start] = True
        stack.append(start)
        edge_idx[start] = head[start]
        while stack:
            u = stack[-1]
            e_end = head[u + 1] if u + 1 < num_nodes else num_edges
            e = edge_idx[u]
            if e < e_end:
                edge_idx[u] += 1
                v = to[e]
                if not visited[v]:
                    visited[v] = True
                    edge_idx[v] = head[v]
                    stack.append(v)
            else:
                order.append(stack.pop())

    # Kosaraju Step 2: DFS on G_rev
    scc = [-1] * num_nodes
    scc_count = 0
    stack = []
    for start in reversed(order):
        if scc[start] != -1:
            continue
        scc[start] = scc_count
        stack.append(start)
        while stack:
            u = stack.pop()
            e_start = rev_head[u]
            e_end = rev_head[u + 1] if u + 1 < num_nodes else num_edges
            for e in range(e_start, e_end):
                v = rev_to[e]
                if scc[v] == -1:
                    scc[v] = scc_count
                    stack.append(v)
        scc_count += 1

    # Check satisfiability and determine solution
    ans = []
    for i in range(n):
        pos = 2 * i
        neg = 2 * i + 1
        if scc[pos] == scc[neg]:
            print("NO")
            return
        # In Kosaraju, topological order of SCCs is descending by scc ID.
        # If scc[pos] < scc[neg], pos is topologically after neg, so pos is True.
        if scc[pos] < scc[neg]:
            ans.append(1)
        else:
            ans.append(0)

    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()