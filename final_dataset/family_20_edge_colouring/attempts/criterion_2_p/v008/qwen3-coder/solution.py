import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    nL = int(data[idx])
    idx += 1
    nR = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v + nL].append((u, i))
    
    # Determine the maximum degree (Δ)
    delta = 0
    for u in range(nL):
        delta = max(delta, len(adj[u]))
    for v in range(nL, nL + nR):
        delta = max(delta, len(adj[v]))
    
    if delta == 0:
        print("YES")
        print()
        return
    
    # Color the edges: each edge gets a color from 1 to delta
    result = [0] * m
    used_colors = [set() for _ in range(nL + nR)]
    
    # For each edge, assign the smallest available color
    for u, v in edges:
        v_shifted = v + nL
        color = 1
        while color in used_colors[u] or color in used_colors[v_shifted]:
            color += 1
        result[edges.index((u, v))] = color
        used_colors[u].add(color)
        used_colors[v_shifted].add(color)
    
    # Reorder to match input order
    edge_to_index = {edge: i for i, edge in enumerate(edges)}
    final_result = [0] * m
    for i, (u, v) in enumerate(edges):
        final_result[i] = result[i]
    
    print("YES")
    print(' '.join(map(str, final_result)))

if __name__ == "__main__":
    main()