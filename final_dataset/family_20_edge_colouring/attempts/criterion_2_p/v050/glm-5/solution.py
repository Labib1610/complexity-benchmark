import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    try:
        NT = int(next(iterator))
        NR = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    edges = []
    adj_T = [[] for _ in range(NT)]
    adj_R = [[] for _ in range(NR)]
    
    for i in range(M):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        edges.append((u, v))
        adj_T[u].append(i)
        adj_R[v].append(i)
    
    K = 0
    for i in range(NT):
        if len(adj_T[i]) > K:
            K = len(adj_T[i])
    for i in range(NR):
        if len(adj_R[i]) > K:
            K = len(adj_R[i])
    
    if M == 0:
        print("YES")
        print("")
        return

    # Build adjacency list for the line graph
    # Nodes are edge indices 0..M-1
    # Two edges are adjacent if they share a transmitter or receiver
    # We need to find a K-coloring of this line graph
    
    # To avoid O(M*K) memory, we iterate over shared devices to find neighbors
    # We need to store the current color of each edge
    colors = [0] * M
    
    # We process edges in some order, assigning the smallest available color
    # To find available color, we check colors of adjacent edges
    
    # For faster lookup of available color, we can use a boolean array of size K+1
    # But we need to know which edges are adjacent
    
    # Let's build adjacency lists for the line graph, but only for edges that share a device
    # However, total degree can be large: sum of (deg^2) over all devices
    # In worst case, K ~ 400000, M ~ 400000, deg ~ 400000 -> deg^2 is too large
    
    # Alternative: greedy coloring with efficient neighbor checking
    # For each edge, we check all edges sharing its transmitter and receiver
    # Mark their colors as used, then pick the smallest unused color
    
    # To optimize, we can process edges in order of decreasing degree? 
    # Or just process in input order.
    
    # Since K is the max degree in the line graph, greedy will use at most K colors
    
    # We need to efficiently find the set of colors used by neighbors
    # We can iterate through all neighbors and collect their colors
    
    # Let's precompute for each device, the list of edges connected to it
    # adj_T and adj_R are already computed
    
    # For each edge (u, v), its neighbors are:
    # all edges in adj_T[u] and all edges in adj_R[v], excluding itself
    
    # We'll use a boolean array to mark used colors for each edge
    # Since K can be up to 400000, we need to reset this array efficiently
    # We can use a timestamp array instead of resetting
    
    used_color = [0] * (K + 2)  # 1-indexed colors, K+1 for safety
    timestamp = 0
    
    for i in range(M):
        u, v = edges[i]
        
        # Mark colors of adjacent edges as used
        timestamp += 1
        
        # Check edges sharing transmitter u
        for neighbor_idx in adj_T[u]:
            if neighbor_idx != i:
                c = colors[neighbor_idx]
                if c != 0:
                    used_color[c] = timestamp
        
        # Check edges sharing receiver v
        for neighbor_idx in adj_R[v]:
            if neighbor_idx != i:
                c = colors[neighbor_idx]
                if c != 0:
                    used_color[c] = timestamp
        
        # Find smallest available color
        color = 1
        while used_color[color] == timestamp:
            color += 1
        
        colors[i] = color
    
    print("YES")
    print(" ".join(map(str, colors)))

if __name__ == "__main__":
    solve()