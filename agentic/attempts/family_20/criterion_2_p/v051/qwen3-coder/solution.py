import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N_S = int(data[idx])
    idx += 1
    N_G = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    transfers = []
    sat_deg = [0] * (N_S + 1)
    gs_deg = [0] * (N_G + 1)
    
    for _ in range(M):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        transfers.append((u, v))
        sat_deg[u] += 1
        gs_deg[v] += 1
    
    D = max(max(sat_deg), max(gs_deg))
    
    # Build adjacency list for bipartite graph
    adj = defaultdict(list)
    for i, (u, v) in enumerate(transfers):
        adj[u].append((v, i))  # satellite u connects to ground station v with transfer index i
        adj[v + N_S].append((u, i))  # ground station v connects to satellite u with transfer index i
    
    # Color the edges using D colors
    result = [0] * M
    sat_edge_color = defaultdict(int)  # (sat, gs) -> color
    gs_edge_color = defaultdict(int)  # (gs, sat) -> color
    
    # For each satellite, assign colors to its edges
    for u in range(1, N_S + 1):
        used_colors = set()
        edges_from_u = []
        for v, i in adj[u]:
            edges_from_u.append((v, i))
        
        # Assign colors
        for v, i in edges_from_u:
            # Find a color not used by u or v
            color = 1
            while color in used_colors or color <= gs_edge_color[(v, u)]:
                color += 1
            result[i] = color
            sat_edge_color[(u, v)] = color
            gs_edge_color[(v, u)] = color
            used_colors.add(color)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()