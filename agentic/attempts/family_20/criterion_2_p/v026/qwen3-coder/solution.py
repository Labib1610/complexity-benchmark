import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N_emp = int(data[idx])
    idx += 1
    N_ven = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    transfers = []
    emp_deg = [0] * (N_emp + 1)
    ven_deg = [0] * (N_ven + 1)
    
    for _ in range(M):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        transfers.append((u, v))
        emp_deg[u] += 1
        ven_deg[v] += 1
    
    F = 0
    if M > 0:
        F = max(max(emp_deg[1:]), max(ven_deg[1:]))
    
    # Build adjacency list for bipartite graph
    # Employees: 1 to N_emp
    # Vendors: N_emp+1 to N_emp+N_ven
    adj = defaultdict(list)
    for u, v in transfers:
        vendor_node = N_emp + v
        adj[u].append(vendor_node)
        adj[vendor_node].append(u)
    
    # Color the bipartite graph with F colors
    # We'll use a greedy edge coloring approach
    # For each node, we'll keep track of which colors are used on its edges
    batch_assignment = [0] * M
    edge_colors = {}
    
    # For each employee, assign colors to its edges
    for u in range(1, N_emp + 1):
        if not adj[u]:
            continue
        # Available colors from 1 to F
        used_colors = [False] * (F + 1)  # index 0 unused
        # Mark colors used by adjacent edges
        for vendor_node in adj[u]:
            v = vendor_node - N_emp
            if (u, v) in edge_colors:
                color = edge_colors[(u, v)]
                used_colors[color] = True
        
        # Assign colors to uncolored edges
        color_ptr = 1
        for vendor_node in adj[u]:
            v = vendor_node - N_emp
            if (u, v) not in edge_colors:
                # Find next available color
                while used_colors[color_ptr]:
                    color_ptr += 1
                edge_colors[(u, v)] = color_ptr
                used_colors[color_ptr] = True
                color_ptr += 1
                if color_ptr > F:
                    color_ptr = 1
    
    # Map back to transfer indices
    transfer_index = {}
    for i, (u, v) in enumerate(transfers):
        transfer_index[(u, v)] = i
    
    for i, (u, v) in enumerate(transfers):
        batch_assignment[i] = edge_colors[(u, v)]
    
    print("YES")
    print(' '.join(map(str, batch_assignment)))

if __name__ == "__main__":
    main()