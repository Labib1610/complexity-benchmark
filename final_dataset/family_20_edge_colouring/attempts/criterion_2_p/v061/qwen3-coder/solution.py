import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N_in = int(data[idx])
    idx += 1
    N_out = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    edges = []
    degree = defaultdict(int)
    adj = defaultdict(list)
    
    for i in range(M):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        edges.append((u, v))
        degree[u] += 1
        degree[v + N_in] += 1  # Offset receivers to distinguish from transmitters
        adj[u].append((v + N_in, i))  # (receiver_node, edge_index)
        adj[v + N_in].append((u, i))  # (transmitter_node, edge_index)
    
    D = max(degree.values()) if degree else 0
    
    result = [0] * M
    used_colors = defaultdict(set)
    
    # For each node, maintain a set of available colors
    for u in adj:
        # We'll color the edges of each node one by one
        for v, edge_idx in adj[u]:
            # Find the first color not used by either endpoint
            color = 1
            while color in used_colors[u] or color in used_colors[v]:
                color += 1
            result[edge_idx] = color
            used_colors[u].add(color)
            used_colors[v].add(color)
    
    print("YES")
    if M > 0:
        print(' '.join(map(str, result)))
    else:
        print()

if __name__ == "__main__":
    main()