import sys
from collections import defaultdict
import heapq

def solve():
    nA, nB, m = map(int, sys.stdin.readline().split())
    
    # Store edges by index
    edges = []
    # Degree count for each port
    deg_A = [0] * (nA + 1)
    deg_B = [0] * (nB + 1)
    # Adjacency list storing (neighbor, edge_index)
    adj_A = defaultdict(list)
    adj_B = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        deg_A[u] += 1
        deg_B[v] += 1
        adj_A[u].append((v, i))
        adj_B[v].append((u, i))
    
    # Calculate maximum degree
    delta = max(max(deg_A), max(deg_B))
    
    # Initialize result array
    result = [0] * m
    
    # For each primary port, we need to assign colors (windows) to its edges
    # such that no two edges sharing a secondary port have the same color
    
    # For each secondary port, track which windows are used by its neighbors
    used_B = defaultdict(set)
    
    # Process each primary port
    for u in range(1, nA + 1):
        if not adj_A[u]:
            continue
            
        # Available windows for this primary port
        available = list(range(1, delta + 1))
        # Mark windows used by neighbors of connected secondary ports
        used_windows = set()
        
        # Check what windows are already used by neighbors of our secondary ports
        for v, edge_idx in adj_A[u]:
            used_windows.update(used_B[v])
        
        # Assign windows to edges from this primary port
        for v, edge_idx in adj_A[u]:
            # Find first available window not used by this secondary port's neighbors
            for window in available:
                if window not in used_B[v]:
                    result[edge_idx] = window
                    used_B[v].add(window)
                    break
    
    print("YES")
    print(*result)

solve()