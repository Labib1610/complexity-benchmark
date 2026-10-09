import sys
from collections import defaultdict
import heapq

def solve():
    n_L, n_R, m = map(int, input().split())
    
    # Read edges and build adjacency lists
    edges = []
    adj_L = defaultdict(list)  # adj_L[u] = list of (v, edge_index)
    adj_R = defaultdict(list)  # adj_R[v] = list of (u, edge_index)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj_L[u].append((v, i))
        adj_R[v].append((u, i))
    
    # Find maximum degree K
    K = 0
    for u in range(1, n_L + 1):
        K = max(K, len(adj_L[u]))
    for v in range(1, n_R + 1):
        K = max(K, len(adj_R[v]))
    
    # Assign colors (maintenance cycles) to edges
    result = [0] * m  # result[i] = cycle for edge i
    
    # For each left node, assign colors to its edges
    for u in range(1, n_L + 1):
        deg = len(adj_L[u])
        if deg == 0:
            continue
            
        # Get available colors (cycles)
        used_on_right = {}  # For each right neighbor, what color is used on edge to it
        for v, edge_idx in adj_L[u]:
            if result[edge_idx] != 0:
                used_on_right[v] = result[edge_idx]
        
        # Available colors
        available_colors = set(range(1, K + 1))
        # Remove colors used by neighbors
        for v in used_on_right:
            if used_on_right[v] in available_colors:
                available_colors.remove(used_on_right[v])
        
        # Assign remaining edges
        available_list = list(available_colors)
        color_idx = 0
        for v, edge_idx in adj_L[u]:
            if result[edge_idx] == 0:  # Not yet assigned
                if color_idx < len(available_list):
                    result[edge_idx] = available_list[color_idx]
                    color_idx += 1
                else:
                    # Need to find any valid color not used by right side
                    used_by_right = set()
                    for w, e_idx in adj_R[v]:
                        if result[e_idx] != 0:
                            used_by_right.add(result[e_idx])
                    
                    for c in range(1, K + 1):
                        if c not in used_by_right:
                            result[edge_idx] = c
                            break
    
    print("YES")
    print(' '.join(map(str, result)))

solve()